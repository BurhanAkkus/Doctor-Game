import random

from scipy.stats import beta
import numpy as np
MAX_BETA_VARIANCE = beta.stats(1, 1, moments='v')

# Util functions
def total_num_of_rounds_played(drug_performance):
    total_rounds_played = 0
    for drug_name in drug_performance:
        drug = drug_performance[drug_name]
        total_rounds_played = total_rounds_played + drug['success_count'] + drug['failure_count']
    return total_rounds_played

def cdf_to_pdf(cdf):
    size = len(cdf)
    pdf = []
    for index,cdf_i in enumerate(cdf[1:]):
        pdf.append(cdf_i - cdf[index])
    pdf.append(1 - np.sum(pdf))
    return pdf

def beta_variance_exploration(drug_performance,num_patients):
    variances = []
    for drug_index,drug_name in enumerate(drug_performance):
        drug = drug_performance[drug_name]
        a = drug['success_count'] + 1
        b = drug['failure_count'] + 1
        variances.append((drug_index,beta.stats(a,b,moments='v')))
    remaining_rounds = num_patients - total_num_of_rounds_played(drug_performance)
    variances.sort(key= lambda d: d[1])
    for (drug_index,variance) in variances:
        if(random.random() < (variance / MAX_BETA_VARIANCE * remaining_rounds / num_patients)):
            return drug_index
    return -1

def beta_variance_squared_exploration(drug_performance,num_patients):
    variances = []
    for drug_index, drug_name in enumerate(drug_performance):
        drug = drug_performance[drug_name]
        a = drug['success_count'] + 1
        b = drug['failure_count'] + 1
        variances.append((drug_index, beta.stats(a, b, moments='v')))
    remaining_rounds = num_patients - total_num_of_rounds_played(drug_performance)
    variances.sort(key=lambda d: d[1])
    for (drug_index, variance) in variances:
        if (random.random() < ( (variance / MAX_BETA_VARIANCE) ** 2 * remaining_rounds / num_patients)):
            return drug_index
    return -1


# Example script function to decide the drug choice based on all previous round info and drug performance
def greedy_number_of_success(drug_performance,num_patients):
    """
    This function receives the history of all previous rounds and returns the choice for the next round.
    It also receives the success and failure counts for each drug.
    """
    # Example logic: Prefer the drug with the highest success count, but try all drugs once before repeating
    for i, drug_name in enumerate(drug_performance, 1):
        drug = drug_performance[drug_name]
        if drug['success_count'] == 0 and drug['failure_count'] == 0:
            return i  # Choose an untried drug

    # If all drugs have been tried, choose the one with the highest success count
    best_drug = max(drug_performance, key=lambda d: drug_performance[d]['success_count'])
    return list(drug_performance).index(best_drug) + 1

def greedy_rate_of_success(drug_performance,num_patients):
    """
    This function receives the history of all previous rounds and returns the choice for the next round.
    It also receives the success and failure counts for each drug.
    """
    # Example logic: Prefer the drug with the highest success count, but try all drugs once before repeating
    for i, drug_name in enumerate(drug_performance, 1):
        drug = drug_performance[drug_name]
        if drug['success_count'] == 0 and drug['failure_count'] == 0:
            return i  # Choose an untried drug

    # If all drugs have been tried, choose the one with the highest success count
    best_drug = max(drug_performance, key=lambda d: (drug_performance[d]['success_count']) / (
                drug_performance[d]['success_count'] + drug_performance[d]['failure_count']))
    return list(drug_performance).index(best_drug) + 1

def beta_strategy(drug_performance,num_patients):
    best_beta_params = None
    resolution = 100
    x = np.linspace(0, 1, resolution)
    dx = 1 / resolution
    best_drug_index = -1
    for drug_index,drug_name in enumerate(drug_performance):
        drug = drug_performance[drug_name]
        if(best_beta_params == None):
            best_beta_params = drug['success_count'] + 1, drug['failure_count'] + 1
            best_beta_pdf = cdf_to_pdf(beta.cdf(x,best_beta_params[0],best_beta_params[1]))
        else:
            candidate_beta_params = drug['success_count'] + 1, drug['failure_count'] + 1
            if (candidate_beta_params == best_beta_params):
                continue
            candidate_a = candidate_beta_params[0]
            candidate_b = candidate_beta_params[1]
            probability_sum = 0
            for i,x_i in enumerate(x[:-1]):
                if(x_i < 1):
                    probability_sum = probability_sum + best_beta_pdf[i] * ( 1 - beta.cdf(x[i + 1], candidate_a, candidate_b))
            if(probability_sum > 0.5):
                best_beta_params = candidate_beta_params
                best_beta_pdf = cdf_to_pdf(beta.cdf(x,best_beta_params[0],best_beta_params[1]))
                best_drug_index = drug_index
    return best_drug_index

def beta_strategy_with_naive_exploration(drug_performance,num_patients):
    for i, drug_name in enumerate(drug_performance):
        drug = drug_performance[drug_name]
        if drug['success_count'] == 0 and drug['failure_count'] == 0:
            return i  # Choose an untried drug
    best_beta_params = None
    resolution = 100
    x = np.linspace(0, 1, resolution)
    dx = 1 / resolution
    best_drug_index = -1
    for drug_index,drug_name in enumerate(drug_performance):
        drug = drug_performance[drug_name]
        if(best_beta_params == None):
            best_beta_params = drug['success_count'] + 1, drug['failure_count'] + 1
            best_beta_pdf = cdf_to_pdf(beta.cdf(x,best_beta_params[0],best_beta_params[1]))
            best_drug_index = 0
        else:
            candidate_beta_params = drug['success_count'] + 1, drug['failure_count'] + 1
            if(candidate_beta_params == best_beta_params):
                continue
            candidate_a = candidate_beta_params[0]
            candidate_b = candidate_beta_params[1]
            probability_sum = 0
            for i,x_i in enumerate(x[:-1]):
                if(x_i < 1):
                    probability_sum = probability_sum + best_beta_pdf[i] * ( 1 - beta.cdf(x[i + 1], candidate_a, candidate_b))
            if(probability_sum > 0.5):
                best_beta_params = candidate_beta_params
                best_beta_pdf = cdf_to_pdf(beta.cdf(x,best_beta_params[0],best_beta_params[1]))
                best_drug_index = drug_index
    return best_drug_index

def beta_strategy_with_variance_dependant_exploration(drug_performance, num_patients):
    exploration_result = beta_variance_exploration(drug_performance,num_patients)
    if(exploration_result != - 1):
        return exploration_result
    return beta_strategy(drug_performance,num_patients)

def beta_strategy_with_variance_square_dependant_exploration(drug_performance, num_patients):
    exploration_result = beta_variance_exploration(drug_performance,num_patients)
    if(exploration_result != - 1):
        return exploration_result
    return beta_strategy(drug_performance,num_patients)

def thompson_sampling_one_shot(drug_performance,num_patients):
    beta_predicts = []
    for drug_name in drug_performance:
        drug = drug_performance[drug_name]
        beta_predicts.append(beta.rvs(drug['success_count'] + 1,drug['failure_count'] + 1,size=1)[0])
    return beta_predicts.index(max(beta_predicts))

def thompson_sampling_many_shot(drug_performance,num_patients):
    beta_predicts = []
    sampling_size = 1000
    for drug_name in drug_performance:
        drug = drug_performance[drug_name]
        average = np.sum(beta.rvs(drug['success_count'] + 1,drug['failure_count'] + 1,size=sampling_size))/sampling_size
        beta_predicts.append(average)
    return beta_predicts.index(max(beta_predicts))


strategies = [("greedy_number_of_success",greedy_number_of_success),
              ("greedy_rate_of_success",greedy_rate_of_success),
              ("beta_strategy",beta_strategy),
              ("beta_with_naive_exploration",beta_strategy_with_naive_exploration),
              ("beta_strategy_with_variance_dependant_exploration", beta_strategy_with_variance_dependant_exploration),
              ("beta_strategy_with_variance_square_dependant_exploration", beta_strategy_with_variance_square_dependant_exploration),
              ("thompson_sampling_one_shot", thompson_sampling_one_shot),
              ("thompson_sampling_many_shot", thompson_sampling_many_shot)]


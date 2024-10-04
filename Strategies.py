from scipy.stats import beta
import numpy as np
# Example script function to decide the drug choice based on all previous round info and drug performance
def greedy_number_of_success(drug_performance):
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

def greedy_rate_of_success(drug_performance):
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

def beta_strategy(drug_performance):
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

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
def beta(drug_performance):
    return 0

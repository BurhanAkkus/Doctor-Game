from game_engine import DoctorGame

# Example script function to decide the drug choice based on all previous round info and drug performance
def script_choice_function(drug_performance):
    """
    This function receives the history of all previous rounds and returns the choice for the next round.
    It also receives the success and failure counts for each drug.
    """
    print("\nCurrent Drug Performance:")
    for drug, performance in drug_performance.items():
        print(f"{drug}: {performance['success_count']} successes, {performance['failure_count']} failures")

    # Example logic: Prefer the drug with the highest success count, but try all drugs once before repeating
    for i, drug in enumerate(drug_names, 1):
        if drug_performance[drug]['success_count'] == 0 and drug_performance[drug]['failure_count'] == 0:
            return i  # Choose an untried drug

    # If all drugs have been tried, choose the one with the highest success count
    best_drug = max(drug_performance, key=lambda d: drug_performance[d]['success_count'])
    return list(drug_names).index(best_drug) + 1

# Define a list of drug names
drug_names = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]
# Programmatic play mode
game = DoctorGame(drug_names)

# Play the game programmatically
num_patients = 50
game.play_game_script(num_patients, script_choice_function)

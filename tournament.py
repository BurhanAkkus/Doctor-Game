from random import uniform

from Strategies import strategies
from game_engine import DoctorGame
import matplotlib.pyplot as plt
from scipy.stats import uniform


# Function to play the game multiple times for each strategy
def run_tournament(num_games, num_patients,rates):
    results = []

    # Loop through each strategy
    for strategy_name, strategy_function in strategies:
        total_successes = 0
        total_failures = 0

        # Run the game 'num_games' times with the current strategy
        for _ in range(num_games):
            drug_names = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]
            game = DoctorGame(drug_names,rates[_])
            game_result = game.play_game_script(num_patients, strategy_function)
            total_successes += game_result[0]
            total_failures += game_result[1]
            print(f"Strategy: {strategy_name}, Game:{_}, Rates:{rates[_]}")

        # Calculate the average success rate for the strategy
        avg_success_rate = total_successes / (total_successes + total_failures)
        results.append((strategy_name, avg_success_rate, total_successes, total_failures))

    return results


# Function to plot the results of the tournament
def plot_results(results):
    strategy_names = [result[0] for result in results]
    avg_success_rates = [result[1] for result in results]

    plt.figure(figsize=(10, 6))
    plt.bar(strategy_names, avg_success_rates, color='skyblue')
    plt.xlabel('Strategies')
    plt.ylabel('Average Success Rate')
    plt.title('Comparison of Strategies Based on Average Success Rate')
    plt.xticks(rotation=45)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()



num_games = 100
num_patients = 50

rates = []
for i in range(500):
    rates.append(uniform.rvs(size=5))


tournament_results = run_tournament(num_games, num_patients,rates)

# Print the results
for result in tournament_results:
    print(f"Strategy: {result[0]}, Average Success Rate: {result[1] * 100:.2f}%")
    print(f"  Total Successes: {result[2]}, Total Failures: {result[3]}\n")

# Plot the results
plot_results(tournament_results)
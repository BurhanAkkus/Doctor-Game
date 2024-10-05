from random import uniform
from Strategies import strategies
from game_engine import DoctorGame
import matplotlib.pyplot as plt
from scipy.stats import uniform
import time
import numpy as np

# Function to play the game multiple times for each strategy
def run_tournament(num_games, num_patients,rates):
    results = []

    # Loop through each strategy
    for strategy_name, strategy_function in strategies:
        total_successes = 0
        total_failures = 0

        start_time = time.time()

        # Run the game 'num_games' times with the current strategy
        for _ in range(num_games):
            drug_names = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]
            game = DoctorGame(drug_names,rates[_])
            game_result = game.play_game_script(num_patients, strategy_function)
            total_successes += game_result[0]
            total_failures += game_result[1]
            print(f"Strategy: {strategy_name}, Game:{_}, Rates:{rates[_]}")

        # Calculate the average success rate for the strategy

        end_time = time.time()
        avg_success_rate = total_successes / (total_successes + total_failures)
        results.append((strategy_name, avg_success_rate, total_successes, total_failures,end_time - start_time))

    return results


# Function to plot the results of the tournament
def plot_results(results):
    strategy_names = [result[0] for result in results]
    avg_success_rates = [result[1] for result in results]
    runtimes = [result[4] * 1000 for result in results]  # Convert runtimes to milliseconds

    x = np.arange(len(strategy_names))

    # Creating subplots to display both graphs simultaneously
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

    # Plotting average success rates
    bars1 = ax1.bar(x, avg_success_rates, color='skyblue')
    ax1.set_xlabel('Strategies')
    ax1.set_ylabel('Average Success Rate')
    ax1.set_title('Comparison of Strategies Based on Average Success Rate')
    ax1.set_xticks(x)
    ax1.set_xticklabels(strategy_names, rotation=45)
    ax1.set_ylim(0, 1)

    # Adding numeric value labels to average success rates bars
    for bar in bars1:
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.02, f'{bar.get_height():.2f}', ha='center', va='top' if bar.get_height() > 0.05 else 'bottom')

    # Plotting runtimes
    bars2 = ax2.bar(x, runtimes, color='lightcoral')
    ax2.set_xlabel('Strategies')
    ax2.set_ylabel('Runtime (milliseconds)')
    ax2.set_title('Comparison of Strategies Based on Runtime')
    ax2.set_xticks(x)
    ax2.set_xticklabels(strategy_names, rotation=45)

    # Adding numeric value labels to runtime bars
    for bar in bars2:
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.02, f'{bar.get_height():.2f}', ha='center', va='top')

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
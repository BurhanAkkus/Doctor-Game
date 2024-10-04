# Doctor Game: Predictive Treatment Simulator

Welcome to the **Doctor Game**, a simulation game where you play as a doctor choosing from a variety of drugs to treat patients. Each drug has a different probability of success, and your goal is to effectively treat as many patients as possible by making informed decisions. The game is designed to be played interactively via the command line or programmatically using various strategies.

## Features

- **Interactive Gameplay:** Choose drugs to treat patients manually through a command line interface.
- **Scripted Strategies:** Automatically play the game using pre-defined or custom strategies.
- **Track Performance:** Monitor drug performance and success rates throughout gameplay.
- **Tournament Mode:** Compare different strategies in a tournament to find the best treatment approach.

## Files Overview

- **game_engine.py:** Contains the core game logic, including the `DoctorGame` class that handles patient treatment, drug success rates, and gameplay functions.
- **play_from_command_line.py:** Allows for interactive command line gameplay where you manually choose drugs to treat patients.
- **play_from_script.py:** Runs the game programmatically, using different strategies defined in the `Strategies` module to decide on the best drug for each patient.
- **Strategies.py:** Defines multiple strategies for playing the game, such as `greedy_number_of_success`, `greedy_rate_of_success`, `beta_strategy`, and `thompson_sampling`. Each strategy has its own approach to maximize successful treatments.
- **tournament.py:** Facilitates running multiple games using different strategies to compare their effectiveness, and plots the average success rates.
- **beta.py:** Demonstrates the Beta distribution, which can be used to model drug success rates in the game.

## Getting Started

### Requirements

- Python 3.x
- Required libraries: `numpy`, `scipy`, `matplotlib`

Install the required packages using the following command:

```bash
pip install numpy scipy matplotlib
```

### How to Play

#### Command Line Mode
To play the game interactively from the command line:

```bash
python play_from_command_line.py
```
You will be prompted to enter the number of patients to treat and then choose a drug for each patient.

#### Scripted Mode
To play the game using one of the predefined strategies:

```bash
python play_from_script.py
```
You will be asked to select a strategy, and the game will play out using that strategy to decide on treatments.

#### Tournament Mode
To compare all the strategies in a tournament setting:

```bash
python tournament.py
```
The script will simulate multiple games for each strategy and plot their average success rates.

## Strategies Overview

- **Greedy Number of Successes:** Prefers the drug with the highest number of successes so far.
- **Greedy Rate of Success:** Chooses the drug with the highest rate of success based on past performance.
- **Beta Strategy:** Uses the Beta distribution to evaluate and select the best drug.
- **Beta Strategy with Naive Exploration:** Tries each drug at least once before applying the Beta strategy.
- **Thompson Sampling:** Uses Bayesian inference to balance exploration and exploitation for drug selection.

## Example Usage

Here's an example of running the game programmatically with a selected strategy:

```python
from Strategies import strategies
from game_engine import DoctorGame

# Initialize the game
drug_names = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]
game = DoctorGame(drug_names)

# Play with a specific strategy
strategy = strategies[0][1]  # Greedy number of successes
game_result = game.play_game_script(50, strategy)
print(game_result)
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to open issues or submit pull requests to improve the game, add new strategies, or optimize the existing code.

## Contact

For questions or suggestions, please reach out via GitHub or open an issue in the repository.


import random


# Define a class for the game
class DoctorGame:
    def __init__(self, drug_names):
        """
        Initialize the game with a list of drug names and randomly assign success probabilities,
        along with success and failure counters for each drug.
        """
        self.drugs = {
            drug: {
                "success_rate": random.uniform(0.1, 0.9),
                "success_count": 0,
                "failure_count": 0
            }
            for drug in drug_names
        }
        self.total_success_count = 0
        self.total_failure_count = 0

    def treat_patient(self):
        """
        Allow the doctor to treat a patient by selecting a drug, and update the score based on the outcome.
        """
        print("\nWelcome, doctor! You have the following drugs to choose from:")

        # List the drugs with their chances of success
        for i, (drug, stats) in enumerate(self.drugs.items(), 1):
            print(f"{i}. {drug} (Effective treatments: {stats['success_count']}) (Ineffective treatments: {stats['failure_count']})")

        # Get the doctor's choice
        choice = int(input(f"Choose a drug (1-{len(self.drugs)}): "))
        drug_list = list(self.drugs.keys())
        # Get the selected drug and its success chance
        selected_drug = drug_list[choice - 1]
        success_chance = self.drugs[selected_drug]["success_rate"]

        # Determine if the treatment was successful
        if random.random() <= success_chance:
            print(f"Success! The patient was cured using {selected_drug}.")
            self.drugs[selected_drug]["success_count"] += 1
            self.total_success_count += 1
        else:
            print(f"Failure! The patient was not cured using {selected_drug}.")
            self.drugs[selected_drug]["failure_count"] += 1
            self.total_failure_count += 1

        # Display current score
        self.display_score()

    def display_score(self):
        """
        Display the current score of successful and failed treatments for each drug.
        """
        print(f"\nTotal Score: {self.total_success_count} successes, {self.total_failure_count} failures.")
        print("Drug performance:")
        for drug, stats in self.drugs.items():
            print(f"{drug}: {stats['success_count']} successes, {stats['failure_count']} failures.")

    def play_game(self):
        """
        Run the entire game loop for a set number of patients.
        """
        # Ask the player how many patients they want to treat
        num_patients = int(input("How many patients would you like to treat in this playthrough? "))

        # Run the game loop for the specified number of patients
        for _ in range(num_patients):
            self.treat_patient()

        # Display the final score after all patients have been treated
        print(f"\nFinal Score: {self.total_success_count} successes, {self.total_failure_count} failures.")
        print("Goodbye, doctor!")

        # Display the Success rate for each drug
        for i, (drug, stats) in enumerate(self.drugs.items(), 1):
            print(f"{i}. {drug} (Success Rate: {stats['success_rate'] * 100:.2f}%)")



# Define a list of drug names
drug_names = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]

# Create an instance of the game
game = DoctorGame(drug_names)

# Start the game
game.play_game()

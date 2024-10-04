import random

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
        self.round_history = []  # Store the history of all rounds without success rate info

    def treat_patient(self, drug_choice):
        """
        Treat a patient by selecting a drug based on the provided choice, and update the score.
        Return the outcome of the treatment without revealing the success rate.
        """
        selected_drug = list(self.drugs.keys())[drug_choice]
        success_chance = self.drugs[selected_drug]["success_rate"]

        # Determine if the treatment was successful
        if random.random() <= success_chance:
            self.drugs[selected_drug]["success_count"] += 1
            self.total_success_count += 1
            result = True  # Treatment was successful
        else:
            self.drugs[selected_drug]["failure_count"] += 1
            self.total_failure_count += 1
            result = False  # Treatment failed

        # Append round info (drug name and result) without the success rate to the history
        round_info = {'drug': selected_drug, 'result': result}
        self.round_history.append(round_info)

        return round_info

    def get_round_history(self):
        """
        Return the history of all rounds without the success rate.
        """
        return self.round_history

    def get_drug_performance(self):
        """
        Return the success and failure counts for each drug.
        """
        return {drug: {'success_count': stats['success_count'], 'failure_count': stats['failure_count']}
                for drug, stats in self.drugs.items()}

    def display_drug_success_rates(self):
        """
        Display the success rates for each drug.
        """
        print("\nDrug Success Rates:")
        for drug, stats in self.drugs.items():
            total_attempts = stats["success_count"] + stats["failure_count"]
            print(f"{drug}: {stats['success_rate'] * 100:.2f}% success rate ({stats['success_count']} successes, {stats['failure_count']} failures)")


    def play_game_cli(self, num_patients):
        """
        Play the game interactively via command line input.
        """
        for i in range(num_patients):
            print("\nWelcome, doctor! You have the following drugs to choose from:")
            for j, (drug, stats) in enumerate(self.drugs.items(), 1):
                print(f"{j}. {drug} (Effective Treatments: {stats['success_count']}, Ineffective Treatments: {stats['failure_count']})")

            choice = int(input(f"Choose a drug (1-{len(self.drugs)}): "))
            result_info = self.treat_patient(choice)
            print(f"Patient {i+1}: {'Success' if result_info['result'] else 'Failure'} with {result_info['drug']}")

        # Display final score and drug success rates
        print(f"\nFinal Score: {self.total_success_count} successes, {self.total_failure_count} failures.")
        self.display_drug_success_rates()

    def play_game_script(self, num_patients, choice_function):
        """
        Play the game programmatically. For each patient, the script dynamically makes a choice based on
        all previous rounds using the passed 'choice_function'.
        """
        for i in range(num_patients):
            # Let the script decide the drug choice for each patient based on round history and drug performance
            drug_choice = choice_function(self.get_drug_performance())  # Provide round history and drug performance to the script
            result_info = self.treat_patient(drug_choice)
        self.display_drug_success_rates()
        return self.total_success_count, self.total_failure_count, self.total_success_count / (
                    self.total_success_count + self.total_failure_count)


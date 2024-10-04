from game_engine import DoctorGame
# Define a list of drug names
drug_names = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]
# Interactive CLI mode
game = DoctorGame(drug_names)

# Specify the number of patients for the playthrough
num_patients = int(input("How many patients would you like to treat? "))
game.play_game_cli(num_patients)

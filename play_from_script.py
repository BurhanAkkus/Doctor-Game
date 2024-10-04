from game_engine import DoctorGame


def print_result(game_result):
    print(f"Game result: Effective Treatments : {game_result[0]}\n"
          f"Ineffective Treatments: {game_result[1]}\n"
          f"Rate of Success: {game_result[2] * 100:.2f}\n")

def play_the_game(strategy):
    drug_names = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]
    game = DoctorGame(drug_names)
    num_patients = 50
    game_result = game.play_game_script(num_patients, strategy)
    print_result(game_result)

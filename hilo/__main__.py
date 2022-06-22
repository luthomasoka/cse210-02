from game.director import Director


def continue_game(continue_game_input):
    """Determines if game should continue.

    Args:
        continue_game_input (string): A variable with user's reponse.
    """    
    if continue_game_input == "y":
        return True
    elif continue_game_input == "n":
        return False


continue_game_input = ""
game = True

while game:
    director = Director() 
    director.start_game()
    continue_game_input = input("Play again? [y/n]: ")
    game = continue_game(continue_game_input)
print("Thank you for playing.")

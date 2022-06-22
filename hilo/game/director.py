from game.cards import Cards


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        score (int): The score for one round of play.
        user_guess (string): The input of the director.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.score = 300
        self.user_guess = ""

    def start_game(self):
        """Starts the game by running the main  entry point.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.score > 0:
            current_card = self.get_inputs()
            next_card = self.do_updates(current_card)
            self.do_outputs(next_card)

    def get_inputs(self):
        """Ask the user if they want to guess the next card.

        Args:
            self (Director): An instance of Director.
        """    
        card = Cards()
        card.get_current_card()
        print(f"This card is: {card.current_card}")
        self.user_guess = input("Higher or lower? [h/l]: ").lower()
        return card.current_card

    def do_updates(self, current_card):
        """Updates the player's score depending on the guess
        and returns value for the next card.

        Args:
            self (Director): An instance of Director.
            current_card (int): A variable with the value of the current card.
        """       
        card = Cards()
        card.get_next_card()
        if current_card < card.next_card and self.user_guess == "h":
            self.score += 100
        else:
            self.score -= 75 if self.score else self.score == 0
        return card.next_card

    def do_outputs(self, next_card):
        """Displays the next card and the score. 

        Args:
            self (Director): An instance of Director.
            next_card (int): A variable with the value of the current card.
        """        
        print(f"Next card was: {next_card}")
        print(f"Your score is: {self.score}")
        print()
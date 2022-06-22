import random


class Cards:
    """A card possessing different numbers between 1 and 13.
   
    Attributes:
        value (int): The random number on the card.
    """

    def __init__(self):
        """Constructs a new instance of a card.

        Args:
            self (card): An instance of card (Either current or next).
        """
        self.current_card = 0
        self.next_card = 0

    def get_next_card(self):
        """Generates a new random value for the next card.
        
        Args:
            self (card): An instance of card.
        """
        new_card =  random.randint(1, 13)
        self.next_card = new_card

    def get_current_card(self):
        """Generates a new random value for the next card.
        
        Args:
            self (card): An instance of card.
        """
        new_card =  random.randint(1, 13)
        self.current_card = new_card
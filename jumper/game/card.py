import random


class Card:
    """A rectangular piece of cardboard or other material with an identical pattern on one side and 
    different numbers and symbols on the other.

    The responsibility of Card is to keep track of the number of the card and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of the card.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """

        self.value = 0

    def pick(self):
        """Generates a new random value for the card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)

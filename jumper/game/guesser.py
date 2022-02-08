import random, string

class Guesser:
    """The person trying to guess the word before the jumper dies. 
    
    The responsibility of a Guesser is to guess letters in the randomly chosen word without guessing too much.
    
    Attributes:
        guess (str/char): A letter guess (A-Z).
    """

    def __init__(self):
        """Constructs a new Guesser.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self._guess = random.choice(string.ascii_uppercase)
        self._array_guessing = []
       

    def get_guess(self):
        """Gets the current guess.
        
        Returns:
            str/char: The current guess (1 lowercase char, a-z)
        """
        return self._guess.upper()
        

    def change_guess(self, new_guess):
        """Changes to the given guess.

        Args:
            self (Guesser): An instance of Guesser.
            guess (str/char): The new guess (a-z).
        """
        self._guess = new_guess.upper()
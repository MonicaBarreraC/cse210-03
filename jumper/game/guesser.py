import random, string
from wsgiref.util import request_uri

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

    def create_array_word(self, jumper):
        """Takes the jumer secret word and creates a new array but every character is a '_'
        """
        for _ in range(len(jumper.get_secret_word())):
            self._array_guessing.append('_')

    def get_array_word(self):
        return self._array_guessing

    def set_char_word(self, index, new_letter):
        """
        changes the character of the array of an specific index and put the new letter in that place
        """
        self._array_guessing[index] = new_letter
import random, string
from wsgiref.util import request_uri

class Guesser:
    """The person trying to guess the word before the jumper dies. 
    
    The responsibility of a Guesser is to guess letters in the randomly 
    chosen word without guessing too much tries.
    
    Attributes:
        _guess (str/char): A letter (A-Z).
        _array_guessing (array): This would be the jumper's word but in blank ('_')
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
            str/char: The current guess (1 uppercase char, A-Z)
        """
        return self._guess.upper()
        

    def change_guess(self, new_guess):
        """Replace the previous guess for the new guess

        Args:
            self (Guesser): An instance of Guesser.
            new_guess (str/char): The new guess (a-z).
        """
        self._guess = new_guess.upper()

    def create_array_word(self, jumper):
        """Takes the jumper secret word and creates a new array 
           but every character is a '_'

        Args:
            self (Guesser): An instance of Guesser.
            jumper (Jumper): An instance of Jumper.
        """
        for _ in range(len(jumper.get_secret_word())):
            self._array_guessing.append('_')

    def get_array_word(self):
        """Gets the current guess_array.
        
        Returns:
            array: The current array that the guesser is solving
        """
        return self._array_guessing

    def set_char_word(self, index, new_letter):
        """Changes the character in a specific index of the array
        and put the new letter in that index

        """
        self._array_guessing[index] = new_letter
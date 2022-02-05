import random
from pprint import pprint

class Jumper:
    """The person jumping from the sky with a parachute and a word. 
    
    The responsibility of the Jumper is to let the guesser know if its guesses complete a 
    randomly chosen word...before they die!
    
    Attributes:
        _alive (bool): Whether the jumper is alive or dead!
        _word (str): A word that the guesser tries to guess letter-by-letter.
        _word_str_representation (str) : An abstract replacement of _word in '_ _ _ ' form (for 3 characters).
        _response (list): A list of strings representing the hidden word, jumper, and parachute.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._alive = True
        self._word = random.choice(['cat', 'sequence', 'computer', 'github', 
                                    'bathbomb', 'green', 'slack', 'fork', 
                                    'covid', 'python'])
        
        self._word_str_representation = ''
        for i in range(len(self._word)):
            self._word_str_representation += '_ '
        
        self._response = [self._word_str_representation, '', '  ___', ' /___\\', ' \\   /', '  \\ /', '   0', '  /|\\', '  / \\', '', '^^^^^^^']

    
    def get_hint(self):
        """Gets a hint for the seeker.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """
        hint = "(-.-) Nap time."
        if self._distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self._distance[-1] > self._distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self._distance[-1] < self._distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint

    def is_found(self):
        """Whether or not the hider has been found.

        Args:
            self (Hider): An instance of Hider.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        return (self._distance[-1] == 0)
        
    # refactor, as receive_guess
    #def watch_seeker(self, seeker):
        #"""Watches the seeker by keeping track of how far away it is.
        #
        #Args:
        #    self (Hider): An instance of Hider.
        #"""
        #distance = abs(self._location - seeker.get_location())
        #self._distance.append(distance)
    def receive_guess(self, guesser):
        """Listens to the guesser, and adds the letter to the hidden 
        word or loses some of the parachute.

        Args:
            self (Jumper): An instance of Jumper.
        """
        # Fix the respresentation of the hidden word in the response
        short_word_representation = self._response[0].replace(' ', '')
        for i in range(len(list(self._word))):
            if self._word[i] == guesser.get_letter():
                short_word_representation[i] = guesser.get_letter()
        for i in range(len(list(self._word))):
            print(short_word_representation[i])
            #short_word_representation[i] = f"{short_word_representation[i]} "
            #short_word_representation[i] += ' '
        
        self._response[0] = short_word_representation
        
        # Lose the parachute and die if the guesser runs out of guesses
        if guesser.get_letter() not in self._word and self._response[2] != '   0':
            del self._response[2]
        elif guesser.get_letter() not in self._word and self._response == '   0':
            self._response[2] = '   x'
            self._alive = False
    

    def get_response(self):
        """Getter method for the response

        Args:
            self (Jumper): An instance of Jumper.
        
        Returns:
            string: A list of strings for the Jumper.
        """
        return self._response
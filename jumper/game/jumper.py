#import random
#from pprint import pprint
from game.Word import Word

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
        #self._alive = True ###
        self._nlives = 4
        self._word_obj = Word()
        self._word = ""
        self._array_word = []
        
        # self._word_obj._word = self._word_obj.get_word
        # print(self._word_obj.get_word)
        '''
        self._word_str_representation = ''
        for i in range(len(self._word)):
            self._word_str_representation += '_ '
        
        self._response = [self._word_str_representation, '', '  ___', ' /___\\', ' \\   /', '  \\ /', '   0', '  /|\\', '  / \\', '', '^^^^^^^']
        '''
    

    def select_secret_word(self):
        """Set a word, choosing one from the list using the word object

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._word = self._word_obj.get_word()
        

    def get_secret_word(self):
        """Gets the secret word.

        Args:
            self (Jumper): An instance of Jumper.
        """
        return self._word

    def get_array_word(self):
        """Gets the array_word. 

        Args:
            self (Jumper): An instance of Jumper.
        """
        return self._array_word

    def get_nlives(self):
        """Gets the number of lives of the Jumper. 

        Args:
            self (Jumper): An instance of Jumper.
        """
        return self._nlives
    
    def change_lives(self, number):
        """Changes the number of lives to the number given.

        Args:
            self (Jumper): An instance of Jumper.
            number (int): The new number of lives.
        """
        self._nlives = number
        
    # refactor, as receive_guess
    #def watch_seeker(self, seeker):
        #"""Watches the seeker by keeping track of how far away it is.
        #
        #Args:
        #    self (Hider): An instance of Hider.
        #"""
        #distance = abs(self._location - seeker.get_location())
        #self._distance.append(distance)

    # ->
    '''
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
            self._alive = False'''

    def compare_letter(self, guesser):
        """Listens to the guesser, and adds the letter to the secret 
        word or loose part of the parachute.

        Args:
            self (Jumper): An instance of Jumper.
            guesser(Guesser): An instance of Guesser.
        """
        correct = 0
        for i in range(len(self._array_word)):
            if guesser.get_guess() == self._array_word[i]:
                guesser.set_char_word(i, guesser.get_guess())
                correct += 1

        # The correct is to prevent loosing more than one live in only one guess (for loop)
        if correct <= 0:
            self.change_lives(self.get_nlives() - 1)
    
    '''# ->
    def get_response(self):
        """Getter method for the response

        Args:
            self (Jumper): An instance of Jumper.
        
        Returns:
            string: A list of strings for the Jumper.
        """
        return self._response'''

    def draw_status(self):
        """Prints a draw of the status of the jumper depending on the number of lives

        Args:
            self (Jumper): An instance of Jumper.
        """
        drawing = ['  ___', ' /___\\', ' \\   /', '  \\ /']
        for i in range(4-self._nlives, 4):
            print(drawing[i])
        
        if self._nlives == 0:
            print('   x')
        else:
            print('   0')

        print('  /|\\ \n  / \\ \n\n^^^^^^^\n')

    def transform_word(self):
        """Convert a word like 'HELLO' into an array ['H','E','L','L','O']

        Args:
            self (Jumper): An instance of Jumper.
        """
        for i in range(len(self._word)):
            self._array_word.append(self._word[i])
from game.guesser import Guesser
from game.jumper import Jumper
from game.terminal_service import TerminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        jumper (Jumper): The game's jumper.
        guesser (Guesser): The game's guesser.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._jumper = Jumper()
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # Welcome
        print("\nWelcome to the JUMPER - GAME")

        # Select the secret word for the game and transform it into an array
        self._jumper.select_secret_word()
        self._jumper.transform_word()

        # Creates an array filled with '_'
        self._guesser.create_array_word(self._jumper)

        # Initial Jumper Status
        self._terminal_service.write_word(self._guesser.get_array_word())
        self._jumper.draw_status()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """The guesser provides a letter to try on the secret word

        Args:
            self (Director): An instance of Director.
        """
        # Input of a letter to try on the secret word
        new_guess = self._terminal_service.read_letter('Guess a letter (A-Z): ')
        self._guesser.change_guess(new_guess)
        
    def _do_updates(self):
        """Keeps track of the letters provided from the guesser, if the word is correct
           that letter will appear on the guess_array.
           If the word is not in the secret word, the jumper loose one live (part of the parachute)

        Args:
            self (Director): An instance of Director.
        """       
        # This method checks if the letter is on the secret word
        self._jumper.compare_letter(self._guesser)

        # If nlives == 0 -> Game Over
        if self._jumper.get_nlives() == 0:
            self._is_playing = False

            print("\n* * * GAME OVER * * *")
            print(f"The word was {self._jumper.get_secret_word()}")

        # If they guess the word -> Congratulations!
        if self._guesser.get_array_word() == self._jumper.get_array_word():
            self._is_playing = False
            print("\n* * * CONGRATULATIONS! * * *\nYou guessed the word:", end="")

        #self._jumper.receive_guess(self._guesser)
        #self._response = self._jumper.get_response()
        
    def _do_outputs(self):
        """Provides a draw of the jumper and the letters guessed at the moment

        Args:
            self (Director): An instance of Director.
        """

        # Status of the secret word
        self._terminal_service.write_word(self._guesser.get_array_word())

        # Status of the parachute
        self._jumper.draw_status()
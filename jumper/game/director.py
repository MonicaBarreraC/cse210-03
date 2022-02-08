from game.guesser import Guesser
from game.jumper import Jumper
from game.terminal_service import TerminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        guesser (Guesser): The game's guesser.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        #self._hider = Hider()
        #self._is_playing = True
        #self._seeker = Seeker()
        #self._terminal_service = TerminalService()
        self._jumper = Jumper()
        self._is_playing = True
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper.select_secret_word()
        self._jumper.transform_word()
        # ARRAY 'W O R D S' JUMPER
        self._guesser.create_array_word(self._jumper)
        # ARRAY '_ _ _ _ _' GUESSER

        #INITIAL STATUS JUMPER
        self._jumper.draw_status()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        #new_location = self._terminal_service.read_number("\nEnter a location [1-1000]: ")
        #self._seeker.move_location(new_location)
        
        new_guess = self._terminal_service.read_letter('Guess a letter (A-Z): ')
        self._guesser.change_guess(new_guess)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """       
        # If the new_guess is on the word
        self._jumper.compare_letter(self._guesser)

        #If nlives == 0 -> Game Over
        if self._jumper.get_nlives() == 0:
            self._is_playing = False

            print("GAME OVER")
            print(f"The word was {self._jumper.get_secret_word()}")

        # If they guess the word
        if self._guesser.get_array_word() == self._jumper.get_array_word():
            self._is_playing = False
            print("Congratulations!")

        #self._jumper.receive_guess(self._guesser)
        #self._response = self._jumper.get_response()
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        #hint = self._hider.get_hint()
        #self._terminal_service.write_text(hint)
        #if self._hider.is_found():
            #self._is_playing = False

        # Status of the secret word
        self._terminal_service.write_word(self._guesser.get_array_word())

        # Status of the parachute
        self._jumper.draw_status()
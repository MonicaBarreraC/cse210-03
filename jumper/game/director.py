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
        
        self._jumper.get_response()
        new_guess = self._terminal_service.read_letter('\nGuess a letter (a-z): ')
        self._guesser.change_guess(new_guess)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        #self._hider.watch_seeker(self._seeker)
        self._jumper.receive_guess(self._guesser)
        self._response = self._jumper.get_response()
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        #hint = self._hider.get_hint()
        #self._terminal_service.write_text(hint)
        #if self._hider.is_found():
            #self._is_playing = False
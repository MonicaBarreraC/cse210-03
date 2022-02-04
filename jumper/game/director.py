from game.card import Card

CRED = '\033[91m'
CGRN = '\033[92m'
CYEL = '\033[93m'
CBLU = '\033[94m'
CEND = '\033[0m'

class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        previous (int): The value of the previous card.
        current (int): The value of the current card.
        hi_lo (string): The anser of the player to the question High/Low.
        total_score (int): The score for the entire game.
        first_turn (boolean): Wheter or not the first turn is being played.
    """

#Lewis ->
    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.is_playing = True
        self.previous = 0
        self.current = Card()
        self.hi_lo = ""
        self.total_score = 300
        self.first_turn = True


#Don't Change ->
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

        print("\nThanks for playing!\n")


#Lewis ->
    def get_inputs(self):
        """Ask the user if they want to play. Draw a card before the first turn.
           Then ask the user to guess if the next card is higher or lower.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if self.first_turn:
            temp_card = Card()
            temp_card.pick()
            self.previous = temp_card.value
            print(f"\nLet's begin. Your starting score is {CGRN}{self.total_score} {CEND}")
            print(f"\nYour first card is {CBLU}{self.previous}{CEND}")
        else:
            print(f"\nThe card is {CBLU}{self.current.value}{CEND}")
        
        self.hi_lo = input("Higher or lower? [h/l] ").lower()
        #self.is_playing = (self.hi_lo == "h")
        


#Christopher ->       
    def do_updates(self):
        """Updates the player's score and prints the value of the
           second card

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return 

        if self.first_turn:
            self.first_turn = False
        else:
            self.previous = self.current.value
        
        # Add to the total score (100, -75, 0)

        self.current.pick()
        print(f"Next card was {CBLU}{self.current.value}{CEND}")
        
        if self.hi_lo == 'h' and self.current.value > self.previous:
            self.total_score += 100
        elif self.hi_lo == 'h' and self.current.value < self.previous:
            self.total_score += -75
        elif self.hi_lo == 'l' and self.current.value > self.previous:
            self.total_score += -75
        elif self.hi_lo == 'l' and self.current.value < self.previous:
            self.total_score += 100
        else:
            self.total_score += 0


#Christopher ->       
    def do_outputs(self):
        """Displays the score. Also asks the player if they want to draw again. 

        Args:
            self (Dealer): An instance of Dealer.
        """
        if self.total_score <= 0:
            self.is_playing = False
            print(f"You lose. Your score is {CRED}{self.total_score}{CEND}")
        
        else:
            print(f"Your score is: {self.total_score}")
            keep_playing = input("Draw again? [y/n] ")
            self.is_playing = (keep_playing == "y")
from pprint import pprint

class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    # Not used in this case
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    # this should be good
    def read_letter(self, prompt):
        """Gets input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input (as a character).
        """
        return input(prompt).upper()
        
    # Not used in this case
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        pprint(text)

    def write_word(self, array):
        """Displays the given array on the terminal. 
           The entire word would be on the same line

        Args: 
            self (TerminalService): An instance of TerminalService.
            array (array): The array to display.
        """
        print()
        for i in range(len(array)):
            print(f"{array[i]}", end=" ")
        print("\n")
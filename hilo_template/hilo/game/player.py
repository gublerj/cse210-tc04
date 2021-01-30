class player:

    def __init__(self):
        self.keep_play = ''

    def keep_playing(self):
        """
        Asks the user if they want to keep playing and checks to see if they have 0 points.
        """
        self.keep_play = input("Do you want to keep playing? (y/n): ")
        if self.keep_play == 'n':
            return False
        else:
            return True


    def higher_lower(self):
        """
        Asks the user to guess if the next card will be higher or lower.
        """
        self.guess = input("Do you think the next card will be higher or lower? (h/l): ")
        return self.guess

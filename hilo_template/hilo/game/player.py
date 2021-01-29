class player:

    def keep_playing(self):
        """
        Asks the user if they want to keep playing and checks to see if they have 0 points.
        """
        self.keep_playing = input("Do you want to keep playing? (y/n): ")
        if self.points < 1:
            return False
        elif self.keep_playing == n:
            return False
        else:
            return True


    def higher_lower(self):
        """
        Asks the user to guess if the next card will be higher or lower.
        """
        self.guess = input("do you think the next card will be higher or lower? (h/l): ")
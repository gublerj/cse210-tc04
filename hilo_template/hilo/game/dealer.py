import random
from game.player import player
class dealer:
    """
    Dealer generates a random number, sends it to the player.
    Dealer determines whether the guess is a win or lose for that round.
    """
    def __init__(self):
        self.player = player()
        self.keep_playing = True
        self.count = 0
        self.card1 = 0
        self.card2 = 0
        self.points = 300

    def deal_card(self):
        """
        Generates random number between 1 and 13.
        """
        card = random.randint(1, 13)
        if self.count % 2 == 0:
            self.card1 = card
            print("The card is: ", card)
        else:
            self.card2 = card
            print("next card was: ", card)
        self.count = self.count + 1
        return card
    
    def count_points(self):
        """
        Counts points and display total points.
        """
        if self.count == 0:
            return self.points
        higher_lower = self.player.higher_lower()
        self.deal_card()
        if higher_lower == 'h':
            if self.card1 > self.card2:
                self.points = self.points + 100
            else:
                self.points = self.points - 75
        else:
            if self.card1 < self.card2:
                self.points = self.points + 100
            else:
                self.points = self.points - 75
        print("Your score is: ", self.points)
        return self.points

    def play_game(self):
        while self.keep_playing == True:
            self.deal_card()
            self.points = self.count_points()
            if self.points > 1:
                self.keep_playing = self.player.keep_playing()
            else:
                self.keep_playing = False
            

        

            
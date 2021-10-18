import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class Cardboard():
    CARDS = {
    A: "1" or "11",
    2: "2", 
    3: "3",
    4: "4", 
    5: "5", 
    6: "6",
    7: "7", 
    8: "8", 
    9: "9", 
    J: "10",
    K: "10",
    Q: "10"
    }*4
    
    
    def __init__(self):
        random.shuffle(cardboard.CARDS)
        self.cards = cardboard.CARDS
        self.board = []




    def make_card_game(self): 
        game_board=[]
        for index, letter in enumerate(self.letters, start=1):
            pass

    def show_card_game(self):
        self.board=self.make_card_game()

    def buy_in(self):
        response = input("Would you like to pay the buy in? Yes or No? ")
        if response.lower().strip() == "yes":
            credits - 5
            total_pot + 5
            self.deal()
        else:
            return

    def deal(self): 
        pass

    def player_cards(self):
        pass

    def dealer_cards(self):
        if self.dealer_cards() >= self.player_cards():
            self.take_hit()
        else:
            self.take_stand()

    def take_hit(self): 
        self.deal(self.player_cards)

    def take_stand(self):
        pass 
    
    def place_bet(self):
        response = int(input("how much would you like to bet? "))
        total_pot + int(response)
        credits - int(response)
        

    def show_cards(self):
            print(self.player_cards,self.dealer_cards)


    def you_won(self):
        credits + total_pot
    
    def you_lose(self):
        pass
        
class UI(): 
    def __init__(self): 
        self.card_board = Cardboard()

    def play_game(self):
        pass

credits = 1000
total_pot = 0
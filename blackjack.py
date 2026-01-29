import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(suit, value) for suit in suits for value in values]
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            self.build()
            self.shuffle()
            return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.calculate_value()
        
    def calculate_value(self):
        self.value = 0
        aces = 0
        
        for card in self.cards:
            if card.value in ["J", "Q", "K"]:
                self.value += 10
            elif card.value == "A":
                aces += 1
                self.value += 11
            else:
                self.value += int(card.value)
                
        # Adjust for aces
        while self.value > 21 and aces > 0:
            self.value -= 10
            aces -= 1
            
    def display(self, hide_first=False):
        if hide_first:
            print("Hidden Card")
            for card in self.cards[1:]:
                print(card)
        else:
            for card in self.cards:
                print(card)
            print(f"Total value: {self.value}")

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_chips = 100
        self.bet = 0
        
    def place_bet(self):
        while True:
            try:
                bet = int(input(f"You have {self.player_chips} chips. How much would you like to bet? "))
                if bet > self.player_chips:
                    print("You don't have enough chips!")
                elif bet <= 0:
                    print("Bet must be greater than 0!")
                else:
                    self.bet = bet
                    break
            except ValueError:
                print("Please enter a valid number!")
    
    def deal_initial_cards(self):
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        
    def player_turn(self):
        while self.player_hand.value < 21:
            action = input("Would you like to Hit or Stand? ").lower()
            if action in ["hit", "h"]:
                self.player_hand.add_card(self.deck.deal())
                print("\nYour hand:")
                self.player_hand.display()
            elif action in ["stand", "s"]:
                break
            else:
                print("Please enter 'hit' or 'stand'")
                
    def dealer_turn(self):
        print("\nDealer's hand:")
        self.dealer_hand.display()
        while self.dealer_hand.value < 17:
            print("Dealer hits!")
            self.dealer_hand.add_card(self.deck.deal())
            self.dealer_hand.display()
            
    def determine_winner(self):
        player_value = self.player_hand.value
        dealer_value = self.dealer_hand.value
        
        print(f"\nYour hand value: {player_value}")
        print(f"Dealer's hand value: {dealer_value}")
        
        if player_value > 21:
            print("You bust! Dealer wins.")
            self.player_chips -= self.bet
        elif dealer_value > 21:
            print("Dealer busts! You win!")
            self.player_chips += self.bet
        elif player_value > dealer_value:
            print("You win!")
            self.player_chips += self.bet
        elif dealer_value > player_value:
            print("Dealer wins!")
            self.player_chips -= self.bet
        else:
            print("It's a push! Bet returned.")
            
    def play_round(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        self.place_bet()
        self.deal_initial_cards()
        
        print("\nYour hand:")
        self.player_hand.display()
        
        print("\nDealer's hand:")
        self.dealer_hand.display(hide_first=True)
        
        # Check for blackjack
        if self.player_hand.value == 21:
            print("Blackjack! You win!")
            self.player_chips += self.bet * 1.5
            return
            
        self.player_turn()
        
        if self.player_hand.value <= 21:
            self.dealer_turn()
            
        self.determine_winner()
        
    def play_game(self):
        print("Welcome to Blackjack!")
        
        while self.player_chips > 0:
            self.play_round()
            
            if self.player_chips <= 0:
                print("You're out of chips! Game over.")
                break
                
            play_again = input("\nWould you like to play another hand? (y/n) ").lower()
            if play_again not in ["y", "yes"]:
                print(f"Thanks for playing! You leave with {self.player_chips} chips.")
                break
                
        print("Game over!")

# Start the game
if __name__ == "__main__":
    game = Blackjack()
    game.play_game()
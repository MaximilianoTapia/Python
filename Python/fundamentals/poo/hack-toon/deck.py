import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        value = 0
        num_aces = 0
        for card in self.hand:
            if card.rank in ["Jack", "Queen", "King"]:
                value += 10
            elif card.rank == "Ace":
                value += 11
                num_aces += 1
            else:
                value += int(card.rank)
        
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

class BlackjackGame:
    @staticmethod
    def start_game():
        deck = Deck()
        deck.shuffle()

        player = Player("Player")
        dealer = Player("Dealer")

        # Initial deal
        player.add_card(deck.draw_card())
        dealer.add_card(deck.draw_card())
        player.add_card(deck.draw_card())
        dealer.add_card(deck.draw_card())

        print(f"{player.name}'s hand: {', '.join(str(card) for card in player.hand)}")
        print(f"Dealer's face-up card: {dealer.hand[0]}")

        while True:
            choice = input("Do you want to hit or stand? ").strip().lower()
            if choice == "hit":
                player.add_card(deck.draw_card())
                print(f"{player.name}'s hand: {', '.join(str(card) for card in player.hand)}")
                if player.get_hand_value() > 21:
                    print(f"{player.name} busts! Dealer wins.")
                    break
            elif choice == "stand":
                while dealer.get_hand_value() < 17:
                    dealer.add_card(deck.draw_card())
                print(f"Dealer's hand: {', '.join(str(card) for card in dealer.hand)}")
                if dealer.get_hand_value() > 21:
                    print(f"Dealer busts! {player.name} wins.")
                elif dealer.get_hand_value() >= player.get_hand_value():
                    print("Dealer wins.")
                else:
                    print(f"{player.name} wins!")
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")

if __name__ == "__main__":
    BlackjackGame.start_game()

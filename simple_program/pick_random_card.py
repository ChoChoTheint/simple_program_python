import random

cards = ["Diamonds","Spades","Hearts","Clubs"]
ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

def pick_a_card():
    card = random.choice(cards)
    rank = random.choice(ranks)
    return f'The {card} of {rank}'
print(pick_a_card())
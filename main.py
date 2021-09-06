import random
def dealer():
    """returns a random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """takes a list of cards and returns the sum of the list of cards"""
    if sum(cards)==0 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        print("DRAW")
    elif user_score>computer_score and user_score<=21 :
        print("YOU WIN!!!!")

    elif computer_score > user_score and computer_score > 21:
      print("YOU WIN!!!!")
    else:
        print("YOU LOOSE")
    

user_cards=[]
computer_cards=[]
is_game_over=False
# getting two cards from the deck of cards 
for _ in range(2):
    user_cards.append(dealer())
    computer_cards.append(dealer())
# asking the user is he/she wants draw another card rom the deck
while not is_game_over:
    computer_score=calculate_score(computer_cards)
    user_score=calculate_score(user_cards)
    print(f"user's card is:{user_cards} \n user current score is {user_score} \n the computer's first card is {computer_cards[0]} \n computer current score is:{computer_score}")
    
    if user_score==0 or computer_score==0 or user_score>21 or computer_score > 21:
        compare(user_score, computer_score)
        is_game_over=True
    else:
        draw_another_card=input("enter 'y' if you want to draw another card:")
        if draw_another_card=='y':
            user_cards.append(dealer())
        else:
            compare(user_score, computer_score)
            is_game_over=True

    if computer_score != 0 and computer_score<17:
            computer_cards.append(dealer())
            computer_score=calculate_score(computer_cards)

    
    
        
        

import random

# 덱 초기화
deck = []
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
for suit in suits:
    for rank in ranks:
        deck.append(rank + ' of ' + suit)

# 카드 셔플링 함수
def shuffle_deck():
    random.shuffle(deck)

# 카드 한 장 뽑는 함수
def deal_card():
    return deck.pop()

# 점수 계산 함수
def calculate_hand(hand):
    score = 0
    num_aces = 0
    for card in hand:
        rank = card.split()[0]
        if rank == 'Ace':
            num_aces += 1
            score += 11
        elif rank in ['Jack', 'Queen', 'King']:
            score += 10
        else:
            score += int(rank)
    while num_aces > 0 and score > 21:
        score -= 10
        num_aces -= 1
    return score

# 게임 실행 함수
def play_game():
    print('Welcome to Blackjack!')
    shuffle_deck()
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

# 플레이어 턴
    while True:
        print('Player hand:', player_hand)
        player_score = calculate_hand(player_hand)
        print('Player score:', player_score)
        if player_score > 21:
            print('Bust! You lose!')
            return
        elif player_score == 21:
            print('Blackjack! You win!')
            return
        else:
            action = input('Do you want to hit or stand? ')
            if action == 'hit':
                player_hand.append(deal_card())
            elif action == 'stand':
                break

# 딜러 턴
    while True:
        print('Dealer hand:', dealer_hand)
        dealer_score = calculate_hand(dealer_hand)
        print('Dealer score:', dealer_score)
        if dealer_score > 21:
            print('Dealer bust! You win!')
            return
        elif dealer_score >= 17:
            break
        else:
            dealer_hand.append(deal_card())

 # 결과 비교
    if player_score > dealer_score:
        print('You win!')
    elif player_score == dealer_score:
        print('Push!')
    else:
        print('You lose!')

play_game()


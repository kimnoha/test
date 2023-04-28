import random

# 덱 초기화
deck = []
suits = ['하트', '다이아몬드', '클로버', '스페이드']
ranks = ['에이스', '2', '3', '4', '5', '6', '7', '8', '9', '10', '잭', '퀸', '킹']
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
        if rank == '에이스':
            num_aces += 1
            score += 11
        elif rank in ['잭', '퀸', '킹']:
            score += 10
        else:
            score += int(rank)
    while num_aces > 0 and score > 21:
        score -= 10
        num_aces -= 1
    return score

# 게임 실행 함수
def play_game():
    print('블랙잭 게임에 오신걸 환영합니다!')
    shuffle_deck()
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

# 플레이어 턴
    while True:
        print('당신의 카드:', player_hand)
        player_score = calculate_hand(player_hand)
        print('당신의 점수:', player_score)
        if player_score > 21:
            print('Bust! 당신이 패배하셨습니다!')
            return
        elif player_score == 21:
            print('Blackjack! 당신이 승리하셨습니다!')
            return
        else:
            action = input('hit을 하시겠습니까? 아니면 stand를 하시겠습니까? ')
            if action == 'hit':
                player_hand.append(deal_card())
            elif action == 'stand':
                break

# 딜러 턴
    while True:
        print('딜러의 카드:', dealer_hand)
        dealer_score = calculate_hand(dealer_hand)
        print('딜러의 점수:', dealer_score)
        if dealer_score > 21:
            print('딜러의 Bust! 당신이 승리하셨습니다!')
            return
        elif dealer_score >= 17:
            break
        else:
            dealer_hand.append(deal_card())

 # 결과 비교
    if player_score > dealer_score:
        print('당신이 승리하셨습니다!')
    elif player_score == dealer_score:
        print('무승부!')
    else:
        print('당신이 패배하셨습니다!')

play_game()


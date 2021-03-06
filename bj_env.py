import random

# 1 = Ace, 2-10 = Number cards, Jack/Queen/King = 10
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def cmp(a, b):
    # when a > b return 1; when a < b return -1;when a == b return 0
    return int(a>b) - int(a<b)

def draw_card():
    return random.sample(deck, 1)[0]

# return true if the ace is usable
def usable_ace(hand):
    return 1 in hand and sum(hand) + 10 <= 21

def sum_hand(hand):
    if usable_ace(hand):
        return sum(hand) + 10
    return sum(hand)

def is_bust(hand):
    return sum_hand(hand) > 21

def score(hand):
    return 0 if is_bust(hand) else sum_hand(hand)

class PokerAgent:
    ACTION_SPACE_SIZE=3
    def __init__(self,natural=True):
        self.action_size=1
        self.state_size=[1,3]
        self.natural=natural
        self.player=[]
        self.dealer=[]

    def step(self, action):
        # stand
        if action==0:
            done=True
            # dealer's turn
            while sum_hand(self.dealer)<17:
                self.dealer.append(draw_card())
            reward=cmp(score(self.player),score(self.dealer))
        # hit
        elif action==1:
            self.player.append(draw_card())
            if is_bust(self.player):
                done=True
                reward=-1
            else:
                done=False
                reward=0
        # double down
        else:
            self.player.append(draw_card())
            done=True
            if is_bust(self.player):
                reward=-1*2
            # dealer's turn
            else:
                while sum_hand(self.dealer) < 17:
                    self.dealer.append(draw_card())
                reward=cmp(score(self.player),score(self.dealer)) * 2
        return self.get_obs(),reward,done,{}

    def get_obs(self):
        return [sum_hand(self.player), self.dealer[0], usable_ace(self.player)]

    def reset(self):
        self.player = []
        self.dealer = []
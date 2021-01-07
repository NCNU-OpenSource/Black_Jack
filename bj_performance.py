import numpy as np
from train_bj_env import PokerAgent
from bj import DQNAgent
from tqdm import tqdm


def game_loop():
    env=PokerAgent()
    agent=DQNAgent()
    agent.model.load_weights(agent.MODEL_NAME)
    EPISODE=10000
    stand,hit,double,win,loss,double_win,DONE=0,0,0,0,0,0,0
    money = 10000
    cur_money = money
    for episode_i in tqdm(range(EPISODE),ascii=True,unit="episode"):
        cur_state = env.reset()
        action = np.argmax(agent.get_qs(cur_state))
        if action==0:
            stand+=1
        elif action==1:
            hit+=1
        elif action>1:
            double+=1
        observation,reward,done,_=env.step(action)
        observation=np.reshape(observation,[1,3])
        cur_state=observation
        if done:
            if reward>1:
                double_win+=1
            if reward>0:
                win+=1
            elif reward<0:
                loss+=1
            money+=reward
            DONE+=1
        if episode_i%100==0:
            money_change=money-cur_money
            cur_money=money

    print("\n\nstand:",stand,"  hit:",hit,"  double:",double,sep='')
    print(f"\nstand rate:               {round(stand/(stand+hit+double)*100,2)}%")
    print(f"hit rate:                 {round(hit/(stand+hit+double)*100,2)}%")
    print(f"double rate:              {round(double/(stand+hit+double)*100,2)}%")
    print()
    print(f"win rate:                 {round(win/DONE*100,2)}%")
    print(f"    double_and_win rate:  {round(double_win/double*100,2)}%")
    print(f"draw rate:                {round((DONE-win-loss)/DONE*100 ,2)}%")
    print(f"loss rate:                {round(loss/DONE*100,2)}%")
    print()
    print(f"money less:               {money}\n\n")


if __name__ == '__main__':
    game_loop()
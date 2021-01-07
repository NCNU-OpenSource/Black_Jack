import random
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from collections import deque
from train_bj_env import PokerAgent
from tqdm import tqdm

REPLAY_MEMORY_SIZE=50000
MINI_REPLAY_MEMORY_SIZE=1000
MINIBATCH_SIZE=64
DISCOUNT=0.99
UPDATE_TARGET_EVERY=5

MIN_REWARD=-100
MEMORY_FRACTION=0.2

EPISODE=150000

AGGREGATE_STATS_EVERY=50

env=PokerAgent()

class DQNAgent:
    MODEL_NAME="bj_model_150k.fdh5"
    def __init__(self):
        #main model
        self.model=self.create_model()
        
        #target model
        self.target_model=self.create_model()
        self.target_model.set_weights(self.model.get_weights())

        self.replay_memory=deque(maxlen=REPLAY_MEMORY_SIZE)
        self.target_update_counter=0

    def create_model(self):
        model=Sequential()
        model.add(Dense(256,activation='relu',input_shape=(3,)))
        model.add(Dense(128,activation='relu'))
        model.add(Dense(3,activation='linear'))
        model.compile(loss='mse',optimizer=Adam(lr=0.001),metrics=['accuracy'])
        return model

    def update_replay_memory(self,transition):
        self.replay_memory.append(transition)

    def get_qs(self,state):
        return self.model.predict(np.array(state).reshape(-1,*np.array(state).shape))[0]

    def train(self,terminal_state,step):
        if len(self.replay_memory)<MINI_REPLAY_MEMORY_SIZE:
            return
        minibatch=random.sample(self.replay_memory,MINIBATCH_SIZE)

        current_state=np.array([transition[0] for transition in minibatch])
        current_qs_list=self.model.predict(current_state)

        new_current_state=np.array([transition[3] for transition in minibatch])
        future_qs_list=self.target_model.predict(new_current_state)

        X=[]
        y=[]

        for index,(current_state,action,reward,new_current_state,done) in enumerate(minibatch):
            if not done:
                max_future_q=np.max(future_qs_list[index])
                new_q=reward+DISCOUNT*max_future_q
            else:
                new_q=reward

            current_qs=current_qs_list[index]
            current_qs[action]=new_q

            X.append(current_state)
            y.append(current_qs)
        self.model.fit(np.array(X),np.array(y),batch_size=MINIBATCH_SIZE,verbose=0,shuffle=False if terminal_state else None)

        #updating to determine
        if terminal_state:
            self.target_update_counter+=1

        if self.target_update_counter>UPDATE_TARGET_EVERY:
            self.target_model.set_weights(self.model.get_weights())
            self.target_update_counter=0

    def save(self,file):
        self.model.save_weights(file)

    def load(self,file):
        self.model.load_weights(file)
        self.target_model.load_weights(file)

agent=DQNAgent()

def game_loop():
    epsilon=1
    EPSILON_DECAY=0.99975
    MIN_EPSILON=0.001

    ep_rewards=[-1]
    reward_record=[]

    for episode in tqdm(range(1,EPISODE+1),ascii=True,unit="episode"):
        episode_reward=0
        step=1
        current_state=env.reset()

        done=False

        while not done:
            if np.random.random()>epsilon:
                action=np.argmax(agent.get_qs(current_state))
            else:
                action=np.random.randint(0,env.ACTION_SPACE_SIZE)

            new_state,reward,done,_=env.step(action)

            episode_reward+=reward

            agent.update_replay_memory((current_state,action,reward,new_state,done))
            agent.train(done,step)

            current_state=new_state
            step+=1

            ep_rewards.append(episode_reward)
            if not episode % AGGREGATE_STATS_EVERY or episode == 1:
                average_reward = sum(ep_rewards[-AGGREGATE_STATS_EVERY:])/len(ep_rewards[-AGGREGATE_STATS_EVERY:])
                min_reward = min(ep_rewards[-AGGREGATE_STATS_EVERY:])
                max_reward = max(ep_rewards[-AGGREGATE_STATS_EVERY:])

                if average_reward >= MIN_REWARD:
                    agent.save(agent.MODEL_NAME)

            if epsilon>MIN_EPSILON:
                epsilon*=EPSILON_DECAY
                epsilon=max(MIN_EPSILON,epsilon)
        reward_record.append(episode_reward)

    new_reward_record=[]
    reward_sum=0
    for i in range(len(ep_rewards)):
        if i%200!=199:
            reward_sum+=float(ep_rewards[i])
        else:
            new_reward_record.append(reward_sum/200)
            reward_sum=0
    plt.plot(new_reward_record)
    plt.show()

if __name__ == '__main__':
    game_loop()
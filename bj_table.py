import numpy as np
from bj import DQNAgent


def game_loop():
    agent = DQNAgent()
    agent.model.load_weights(agent.MODEL_NAME)

    table_index=[]
    for i in range(4,22):
        for j in range(2,12):
            for k in range(2):
                if i==21:
                    table_index.append([i,j,True])
                    break
                if i<13 and k==1:
                    break
                if k:
                    table_index.append([i,j,True])
                else:table_index.append([i,j,False])

    action_table=[]
    for i in range(len(table_index)-1):
        if(table_index[i][2]==True and i<249):
            continue
        action=np.argmax(agent.get_qs(table_index[i]))
        if table_index[i+1][2]==True:
            action=np.argmax(agent.get_qs(table_index[i+1]))
        action_table.append(action)

    print("\n\n     2 3 4 5 6 7 8 9 10 11")
    for i in range(len(action_table)):
        if i%10 ==0:
            print()
            if 4+int(i/10)<10:
                print(4+int(i/10),end='    ')
            else:
                print(4+int(i/10),end='   ')
        if action_table[i]==0:
            print("S",end=' ')
        elif action_table[i]==1:
            print("H",end=' ')
        else:
            print("D",end=' ')
    print("\n")


if __name__ == '__main__':
    game_loop()
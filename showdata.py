import pickle
from matplotlib.pyplot import figure, show
import sys

if(__name__ == '__main__'):
    sumdata=[]
    for i in range(8):
        with open('text'+str(i), 'rb') as f:
            sumdata.append(pickle.load(f))
    while 1 :
        inputtext= raw_input("""
            please input like:
            ls -a   :   see all data
            ls -r (int)num1 (int)num2  : see range num1 to num2 (num1<num2<%d)
            exit    : exit
        """%len(sumdata[0]))
        command=inputtext.split(' ')
        if len(command) < 1:
            continue;
        if (command[0]=='exit'):
            exit(0)
        elif (command[0]=='ls'):
            if len(command) == 2:
                fig = figure(1)
                for i in range(8):
                    ax=fig.add_subplot(810+i+1,xticks=[], yticks=[],ylabel=str(i+1))
                    ax.plot(sumdata[i])
                    ax.grid(True)
                show()
            if len(command) == 4:
                try:
                    num1=int(command[2])
                    num2=int(command[3])
                    if(num1>=num2 or num1>len(sumdata[0])):
                        continue
                    fig = figure(1)
                    for i in range(8):
                        ax=fig.add_subplot(810+i+1,xticks=[], yticks=[],ylabel=str(i+1))
                        ax.plot(sumdata[i][num1:num2])
                        ax.grid(True)
                    show()
                except:
                    continue

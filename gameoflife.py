
"""
Created on Mon Oct 10 18:19:36

@author: tyler nelson
"""

import numpy as np
import random as ran

dead = 0
alive = 1


GB = np.zeros((20,20)) #tuple array

def startmap():
    for i in range(20):
        for j in range(20):
            r = ran.uniform(0, 1)
            if r<.1:
                GB[i,j]=1
startmap()##########################################################

def live_neighbors(i,j,GB,status): #add the status perameter so that it can know which rules to use
    neighborhood = GB[i-1:i+1,j-1:j+1]
    count = np.count_nonzero(neighborhood==1)
    if liveordie(count,status)==0:
        tempGB[i,j]=0
    elif liveordie(count,status)==1:
        tempGB[i,j]=1


def liveordie(count,status): #rules depend on wether its alive or dead so check and add that 
    '''
    Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by overpopulation.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

    Any live cell with two or three live neighbors survives.
    Any dead cell with three live neighbors becomes a live cell.
    All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    '''
    if status is alive:
        if count < 2:
            return 0
        if count == 3 or count == 2:
            return 1
        if count > 3:
            return 0
    if status is dead:
        if count == 3:
            return 1

print(GB)############################################################
tempGB =GB

def ghosttown(GB):# check if the entire board is dead
    peeps = 0
    for i in range(1,19):
        for j in range (1,19):
            if GB[i][j]==alive:
                peeps+=1
    if peeps > 1:
        return 1
    else:
        return 0;
    
def rungame():
    while ghosttown(GB)==1:
        for i in range(1,19):
            for j in range (1,19):
                live_neighbors(i,j,GB,GB[i,j])
    print("printing new board")
    printboard()

def printboard(GB):
    for i in range(1,19):
        for j in range (1,19):
            if GB[i][j]==alive:
                print("#")
            else:
                print(" ")
rungame()



        
#add a fuction for those on the edge and corners since they have specific rules





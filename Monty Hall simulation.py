# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 15:25:40 2018

@author: Wen Jie
"""

import numpy as np

# This functions hide the car behind 1 of the 3 doors
def hidecar():
    doors = np.zeros(3)
    for i in range(3):
        temp = np.random.randint(2)
        if (temp == 1 or i == 2):
            doors[i] = 1    
            return doors    
    
# This function simulates the contestant picking 1 of the 3 doors
def pick():
    choice = np.random.randint(3)
    return choice


# This function returns the numbers of the empty doors in a list and the door with a car
def emptydoors(doors):
    idx = np.argmax(doors)
    if idx == 0:
        empty1,empty2 = 1,2
    elif idx == 1 :
        empty1,empty2 = 0,2
    else:
        empty1,empty2 = 0,1
     
    return [empty1,empty2],idx

# emptydoors is a list
def opendoor(choice,emptydoors):
    if (choice!=emptydoors[0] and choice!=emptydoors[1]):
        openeddoor = emptydoors[np.random.randint(2)]
    else:
        if choice == emptydoors[0]:
            openeddoor = emptydoors[1]
        else:
            openeddoor = emptydoors[0]
    return openeddoor

def main(N):
    counter=0
    changecounter = 0
    while True:
          doors = hidecar()
          choice = pick()
          emptydoorslist,car = emptydoors(doors)
          openneddoor = opendoor(choice,emptydoorslist)
          # Changing the choice.
          change  = 3 - choice - openneddoor
          if change == car:
              changecounter+=1

          counter += 1
          
          if counter == N-1:
              return changecounter
              break

N = 50000
x = main(N)
print('The probability to get a car when you switch your choice is {}.'.format(x/N))
print('Out of {} simulations, {} scenarios gave a positive outcome when you switch.'.format(N,x))
        
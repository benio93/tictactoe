#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:13:48 2018

@author: beniamin
"""

from IPython.display import clear_output
ticArr = ['','-','-','-','-','-','-','-','-','-']
print(ticArr[0])
print(len(ticArr))
    

def printArr(arr):
    print(arr[7] + ' | ' + arr[8] + ' | ' + arr[9])
    print('---------')
    print(arr[4] + ' | ' + arr[5] + ' | ' + arr[6])
    print('---------')
    print(arr[1] + ' | ' + arr[2] + ' | ' + arr[3])

printArr(ticArr)

def checkIfWin(arr):
    marker = 'O' or 'X' 
    if(arr[1]==arr[2]==arr[3] == marker):
        return True
    if(arr[4]==arr[5]==arr[6] == marker):
        return True
    if(arr[7]==arr[8]==arr[9] == marker):
        return True
    if(arr[7]==arr[4]==arr[1] == marker):
        return True
    if(arr[8]==arr[5]==arr[2] == marker):
        return True
    if(arr[9]==arr[6]==arr[3] == marker):
        return True
    if(arr[1]==arr[5]==arr[9] == marker):
        return True
    if(arr[7]==arr[5]==arr[3] == marker):
        return True

numArr = [1,2,3,4,5,6,7,8,9] 

while '-' in ticArr:
    while True:
        try:
            player1 = int(input('Player1 '))
            if player1 in numArr:
                break;
            else:
                player1 = int(input('Player1 '))
        except:
            print('Number between 1-9 required')
        
    while ticArr[player1] == 'X' or ticArr[player1] == 'O':
        player1 = int(input('Player1 '))
    
        
    ticArr[player1] = 'X'
    printArr(ticArr)
    
    if checkIfWin(ticArr) == True:
        print(' Player1 Won!')
        break;


    while True:
        try:
            player2 = int(input('Player2 '))
            if player2 in numArr:
                break;
            else:
                player2 = int(input('Player2 '))
        except:
            print('Number between 1-9 required')
    while ticArr[player2] =='X' or ticArr[player2] == 'O':
        player2 = int(input('Player2 '))
    
    ticArr[player2] = 'O' 
    printArr(ticArr)
    
    if checkIfWin(ticArr) == True:
        print('Player2 Won!')
        break;
        
    if(ticArr.count('-') == 1):
        print('No player won')
        break;
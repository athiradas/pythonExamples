# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 19:44:32 2017

@author: athir
"""

def max_profit(houses):
    no_h = len(houses)
    dp = list()
    pos = list()
    dp.append(0)
    pos.append(-1)
    dp.append(houses[0])
    pos.append(0)
    pos_dict = dict.fromkeys(range(no_h))
    for i in range(2, no_h+1):
        dp.append(max(dp[i-1], dp[i-2]+houses[i-1]))
        if (dp[i-1] < (dp[i-2]+houses[i-1])):
            pos.append((i-1, i-3))
            pos_dict[i] = 'Yes'  
            pos_dict[i-2] = 'Yes'
            pos_dict[i-1] = 'No' 
            print (houses[i-1], houses[i-3])
        else:
            pos.append((i-2, i-4))
            pos_dict[i] = 'No'  
            pos_dict[i-2] = 'No'
            pos_dict[i-1] = 'Yes'
            print (houses[i-1], houses[i-3])
        flat_list = list()
        for sublist in pos:
            for item in sublist:
                flat_list.append(item)
        
    return dp, pos_dict, flat_list



print (max_profit([1,25,50,100,20,40 ]))
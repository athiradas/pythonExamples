# -*- coding: utf-8 -*-
"""
Created on Mon Sep 04 20:07:48 2017

@author: athir
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in range(len(s)):            
            if s[i] in valid.values():
                    stack.append(s[i])
            elif s[i] in valid.keys():
                if stack == [] or stack.pop() != valid[s[i]]: 
                    return False 
            else:
                print 'in', s[i]
                return False  
        return stack == []
                

            
                 
sol = Solution()
print sol.isValid('(){}[][]{}')


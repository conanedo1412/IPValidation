# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:54:13 2020

@author: akhil
"""

def IPv4_check(string):
    elements = string.split('.')
    if len(elements)!=4:
        return "Not IPv4"
    for elem in elements:
        b = list(elem)
        if len(elem)!=1 and len(b) !=0 and b[0] =='0':
            return "Not IPv4"
        try:
            int(elem)
        except:
            return "Not IPv4"
        if int(elem)> 255 or int(elem)<0:
            return "Not IPv4"
    return "IPv4"
def IPv6_check(string):
    elements = string.split(':')
    if len(elements)!=8:
        return "Not IPv6"
    for elem in elements:
        if len(elem)>4 and elem!='0':
            return "Not IPv6"
        try: 
            int(elem,16)
        except:
            return "Not IPv6"
    return "IPv6"
    
class Solution:
    def validIPAddress(self, IP: str) -> str:
        result = IPv4_check(IP)
        if result =="IPv4":
            return result
        else: 
            result = IPv6_check(IP)
            if result == "IPv6":
                return result
        return "Neither"
            
        

test = "2001:0db8:85a3:033:0:8A2E:0370:7334"
test2 = "1.0.1."
trial = IPv6_check(test)

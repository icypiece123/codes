#!/usr/bin/env python
# coding: utf-8

# In[6]:


def error(l):
    print ("Error occurred!")
    l[1] = 1
    return l

def E(Str, l):
    l = T(Str, l)
    l = Ed(Str, l)
    return l

def T(Str, l):
    l = F(Str, l)
    l = Td(Str, l)
    return l

def Ed(Str, l):
    if Str[l[0]] == "+":
        l[0] += 1
        l = T(Str, l)
        l = Ed(Str, l)
    return l

def F(Str, l): 
    if Str[l[0]] == "(":
        l[0] += 1
        l = E(Str, l)
        if Str[l[0]] == ")":
            l[0] += 1
        else:
            l = error(l)
    elif Str[l[0]] == "d":
        l[0] += 1
    else:
        l = error(l)
    return l

def Td(Str, l):
    if Str[l[0]] == "*":
        l[0] += 1
        l = F(Str, l)
        l = Td(Str, l)
    return l

user_input = input("Enter : ") + "$"
l = [0, 0]
l = E(user_input, l)

if l[1] == 0:
    print ("String is Valid")
else: 
    print ("String is invalid")


# In[ ]:





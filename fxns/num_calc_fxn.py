#!/usr/bin/env python
# coding: utf-8

# In[17]:


def numerology(name, dob):

    def name_nos(name):

        #reference dictionaries
        vowels = {'a': 1, 'e': 5, 'i': 9, 'o': 6, 'u': 3}
        cons = {1 : ['j', 's'], 2 : ['b', 'k', 't'], 3 : ['c', 'l'],
              4 : ['d', 'm', 'v'], 5 : ['n', 'w'], 6 : ['f', 'x'],
              7 : ['g', 'p', 'y'], 8 : ['h', 'q', 'z'], 9 : ['r']}

        #letter value counters
        soul = 0
        personality = 0

        #name alpha string list
        name_lst = [x.lower() for x in name if x != " "]

        #vowel letter digit sum
        for x in name_lst:
            for i, (k, v) in enumerate(vowels.items()):
                if x == k:
                    soul += v

        #consanant letter digit sum
        for h in name_lst:
            for i, (k, v) in enumerate(cons.items()):
                for j in v:
                    if h == j:
                        personality += k

        #alpha single digit reduction
        while len(str(soul)) > 1:
            soul = sum([int(i) for i in str(soul)])

        while len(str(personality)) > 1:
            personality = sum([int(i) for i in str(personality)])

        #influence number calculation
        influence = soul + personality

        while len(str(personality)) > 1:
            influence = sum([int(i) for i in str(influence)])

        return [soul, personality, influence]    

    def dob_nos(dob):
        
        dob_lst = [int(x) for x in dob]

        #define digits from input string
        life_path = sum(dob_lst)
        impression = sum([dob_lst[d] for d in range(2, 4)])
        attitude = sum([dob_lst[d] for d in range(0, 4)])

        #single digit reduction
        while len(str(life_path)) > 1:
            life_path = sum([int(i) for i in str(life_path)])

        while len(str(impression)) > 1:
            first_imp = sum([int(i) for i in str(impression)])

        while len(str(attitude)) > 1:
            attitude = sum([int(i) for i in str(attitude)])

        return [life_path, impression, attitude]


    
    #list of calculated numbers
    nombre = name_nos(name)
    fecha = dob_nos(dob)

    for i in fecha:
        nombre.append(i)
        
    return nombre


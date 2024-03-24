#!/usr/bin/env python
# coding: utf-8

# In[8]:


def name_no_calc(name):
      vowels = {'a': 1, 'e': 5, 'i': 9, 'o': 6, 'u': 3}
      cons = {1 : ['j', 's'], 2 : ['b', 'k', 't'], 3 : ['c', 'l'], 4 : ['d', 'm', 'v'], 5 : ['n', 'w'], 
              6 : ['f', 'x'], 7 : ['g', 'p', 'y'], 8 : ['h', 'q', 'z'], 9 : ['r']}
     
    #instanciate counters
      vl_no = 0 #vowels
      cn_no = 0 #consinants
       
      name_lst = [x.lower() for x in name if x != " "]
      
      #alpha name vowel calculator
      for x in name_lst:
        for i, (k, v) in enumerate(vowels.items()):
          if x == k:
            vl_no += v
      while len(str(vl_no)) > 1:
        vl_no = sum([int(i) for i in str(vl_no)])
      
      #alpha name consinant calculator
      for h in name_lst:
        for i, (k, v) in enumerate(cons.items()):
          for j in v:
            if h == j:
              cn_no += k

      #final consinant and name power calculation
      while len(str(cn_no)) > 1:
        cn_no = sum([int(i) for i in str(cn_no)])
     
      #nP is name power
      nP_no = cn_no + vl_no
      
      while len(str(nP_no)) > 1:
        nP_no = sum([int(i) for i in str(nP_no)])
      
      return [vl_no, cn_no, nP_no]


# In[9]:


def dob_no_calc(dob):
        
        dob_lst = [int(x) for x in str(dob)]

        #define digits from input string
        lP_no = sum(dob_lst)
        imp_no = sum([dob_lst[d] for d in range(2, 4)])
        att_no = sum([dob_lst[d] for d in range(0, 4)])

        #single digit reductions
        while len(str(lP_no)) > 1:
            lP_no = sum([int(i) for i in str(lP_no)])

        while len(str(imp_no)) > 1:
            imp_no = sum([int(i) for i in str(imp_no)])

        while len(str(att_no)) > 1:
            att_no = sum([int(i) for i in str(att_no)])

        return [lP_no, imp_no, att_no]


# In[10]:


def single_person_spread(name, dob):
      imp_no, lP_no, att_no = dob_no_calc(dob)
      vl_no, cn_no, nP_no = name_no_calc(name)
      print(f'{vl_no}{cn_no}{nP_no}{imp_no}[{lP_no}]/{att_no}*'),
      print(f'Soul: {vl_no}'),
      print(f'Personality: {cn_no}'),
      print(f'Name Power: {nP_no}'),
      print(f'First Impression: {imp_no}'),
      print(f'Life Path: {lP_no}'),
      print(f'Attitude: {att_no}')


# In[1]:


def two_person_match_spread (name_p1, dob_p1, name_p2, dob_p2):
    first_imp_p1, life_path_p1, att_p1 = dob_no_calc(dob_p1)
    vowel_no_p1, cons_no_p1, nP_no_p1 = name_no_calc(name_p1)
    first_imp_p2, life_path_p2, att_p2 = dob_no_calc(dob_p2)
    vowel_no_p2, cons_no_p2, nP_no_p2 = name_no_calc(name_p2)
    print(f'{name_p1}: {vowel_no_p1}{cons_no_p1}{nP_no_p1}{first_imp_p1}[{life_path_p1}]/{att_p1}*')
    print(f'{name_p2}: {vowel_no_p2}{cons_no_p2}{nP_no_p2}{first_imp_p2}[{life_path_p2}]/{att_p2}*')


# In[16]:


def two_person_match_reductions(name_p1, dob_p1, name_p2, dob_p2):
        first_imp_p1, life_path_p1, att_p1 = dob_no_calc(dob_p1)
        vowel_no_p1, cons_no_p1, nP_no_p1 = name_no_calc(name_p1)
        first_imp_p2, life_path_p2, att_p2 = dob_no_calc(dob_p2)
        vowel_no_p2, cons_no_p2, nP_no_p2 = name_no_calc(name_p2)
        p1 = f'{vowel_no_p1}{cons_no_p1}{nP_no_p1}{first_imp_p1}{life_path_p1}{att_p1}'
        p2 = f'{vowel_no_p2}{cons_no_p2}{nP_no_p2}{first_imp_p2}{life_path_p2}{att_p2}'
        p1_p2 = p1 + p2
        return(p1_p2)


# In[13]:


def evaluate_relationship(name_p1, dob_p1, name_p2, dob_p2):
    # Assume two_person_match_reductions, name_no_calc, dob_no_calc are defined elsewhere

    spreads_lst = [i for i in two_person_match_reductions(name_p1, dob_p1, name_p2, dob_p2)]

    match_dict = {
        1: {1: 'Natural Match', 2: 'Challenge', 3: 'Compatible', 4: 'Challenge', 5: 'Natural Match', 6: 'Challenge', 7: 'Natural Match', 8: 'Neutral', 9: 'Compatible'},
        2: {1: 'Challenge', 2: 'Natural Match', 3: 'Compatible', 4: 'Natural Match', 5: 'Challenge', 6: 'Compatible', 7: 'Challenge', 8: 'Natural Match', 9: 'Neutral'},
        3: {1: 'Compatible', 2: 'Compatible', 3: 'Natural Match', 4: 'Challenge', 5: 'Compatible', 6: 'Natural Match', 7: 'Challenge', 8: 'Challenge', 9: 'Natural Match'},
        4: {1: 'Challenge', 2: 'Natural Match', 3: 'Challenge', 4: 'Natural Match', 5: 'Challenge', 6: 'Compatible', 7: 'Compatible', 8: 'Natural Match', 9: 'Challenge'},
        5: {1: 'Natural Match', 2: 'Challenge', 3: 'Compatible', 4: 'Challenge', 5: 'Natural Match', 6: 'Challenge', 7: 'Natural Match', 8: 'Neutral', 9: 'Compatible'},
        6: {1: 'Challenge', 2: 'Compatible', 3: 'Natural Match', 4: 'Compatible', 5: 'Challenge', 6: 'Natural Match', 7: 'Challenge', 8: 'Compatible', 9: 'Natural Match'},
        7: {1: 'Natural Match', 2: 'Challenge', 3: 'Challenge', 4: 'Compatible', 5: 'Natural Match', 6: 'Challenge', 7: 'Natural Match', 8: 'Challenge', 9: 'Neutral'},
        8: {1: 'Neutral', 2: 'Natural Match', 3: 'Challenge', 4: 'Natural Match', 5: 'Neutral', 6: 'Compatible', 7: 'Challenge', 8: 'Natural Match', 9: 'Challenge'},
        9: {1: 'Compatible', 2: 'Neutral', 3: 'Natural Match', 4: 'Challenge', 5: 'Compatible', 6: 'Natural Match', 7: 'Neutral', 8: 'Challenge', 9: 'Natural Match'}
    }

    # Function to access the match dictionary with a given input list
    def access_dictionary(input_list):
        return match_dict[input_list[0]][input_list[1]]

    # Constructing input lists for different relationship aspects
    soul_lst = [int(spreads_lst[0]), int(spreads_lst[6])]
    personality_lst = [int(spreads_lst[1]), int(spreads_lst[7])]
    name_power_lst = [int(spreads_lst[2]), int(spreads_lst[8])]
    first_impression_lst = [int(spreads_lst[3]), int(spreads_lst[9])]
    life_path_lst = [int(spreads_lst[4]), int(spreads_lst[10])]
    attitude_lst = [int(spreads_lst[5]), int(spreads_lst[11])]

    # Accessing the match dictionary for each list and storing the results
    results = {
        'Soul': access_dictionary(soul_lst),
        'Personality': access_dictionary(personality_lst),
        'Name Power': access_dictionary(name_power_lst),
        'First Impression': access_dictionary(first_impression_lst),
        'Life Path': access_dictionary(life_path_lst),
        'Attitude': access_dictionary(attitude_lst),
    }

    return results


# In[14]:


def calculate_percentage_match(results):
    # Mapping of relationship categories to their percentage values
    category_to_percentage = {
        'Compatible': 75,
        'Neutral': 50,
        'Natural Match': 100,
        'Challenge': 25
    }
    
    # Calculating the average percentage match based on the categories in the results
    total_percentage = 0
    for category in results.values():
        total_percentage += category_to_percentage[category]
    average_percentage = total_percentage / len(results)

    return average_percentage


# In[18]:


def evaluate_relationship(name_p1, dob_p1, name_p2, dob_p2):
    # Assume two_person_match_reductions, name_no_calc, dob_no_calc are defined elsewhere

    spreads_lst = [i for i in two_person_match_reductions(name_p1, dob_p1, name_p2, dob_p2)]

    match_dict = {
        1: {1: 'Natural Match', 2: 'Challenge', 3: 'Compatible', 4: 'Challenge', 5: 'Natural Match', 6: 'Challenge', 7: 'Natural Match', 8: 'Neutral', 9: 'Compatible'},
        2: {1: 'Challenge', 2: 'Natural Match', 3: 'Compatible', 4: 'Natural Match', 5: 'Challenge', 6: 'Compatible', 7: 'Challenge', 8: 'Natural Match', 9: 'Neutral'},
        3: {1: 'Compatible', 2: 'Compatible', 3: 'Natural Match', 4: 'Challenge', 5: 'Compatible', 6: 'Natural Match', 7: 'Challenge', 8: 'Challenge', 9: 'Natural Match'},
        4: {1: 'Challenge', 2: 'Natural Match', 3: 'Challenge', 4: 'Natural Match', 5: 'Challenge', 6: 'Compatible', 7: 'Compatible', 8: 'Natural Match', 9: 'Challenge'},
        5: {1: 'Natural Match', 2: 'Challenge', 3: 'Compatible', 4: 'Challenge', 5: 'Natural Match', 6: 'Challenge', 7: 'Natural Match', 8: 'Neutral', 9: 'Compatible'},
        6: {1: 'Challenge', 2: 'Compatible', 3: 'Natural Match', 4: 'Compatible', 5: 'Challenge', 6: 'Natural Match', 7: 'Challenge', 8: 'Compatible', 9: 'Natural Match'},
        7: {1: 'Natural Match', 2: 'Challenge', 3: 'Challenge', 4: 'Compatible', 5: 'Natural Match', 6: 'Challenge', 7: 'Natural Match', 8: 'Challenge', 9: 'Neutral'},
        8: {1: 'Neutral', 2: 'Natural Match', 3: 'Challenge', 4: 'Natural Match', 5: 'Neutral', 6: 'Compatible', 7: 'Challenge', 8: 'Natural Match', 9: 'Challenge'},
        9: {1: 'Compatible', 2: 'Neutral', 3: 'Natural Match', 4: 'Challenge', 5: 'Compatible', 6: 'Natural Match', 7: 'Neutral', 8: 'Challenge', 9: 'Natural Match'}
    }

    # Function to access the match dictionary with a given input list
    def access_dictionary(input_list):
        return match_dict[input_list[0]][input_list[1]]

    # Constructing input lists for different relationship aspects
    soul_lst = [int(spreads_lst[0]), int(spreads_lst[6])]
    personality_lst = [int(spreads_lst[1]), int(spreads_lst[7])]
    name_power_lst = [int(spreads_lst[2]), int(spreads_lst[8])]
    first_impression_lst = [int(spreads_lst[3]), int(spreads_lst[9])]
    life_path_lst = [int(spreads_lst[4]), int(spreads_lst[10])]
    attitude_lst = [int(spreads_lst[5]), int(spreads_lst[11])]

    # Accessing the match dictionary for each list and storing the results
    results = {
        'Soul': access_dictionary(soul_lst),
        'Personality': access_dictionary(personality_lst),
        'Name Power': access_dictionary(name_power_lst),
        'First Impression': access_dictionary(first_impression_lst),
        'Life Path': access_dictionary(life_path_lst),
        'Attitude': access_dictionary(attitude_lst),
    }

    return results


# In[19]:


def calculate_percentage_match(results):
    # Mapping of relationship categories to their percentage values
    category_to_percentage = {
        'Compatible': 90,
        'Neutral': 70,
        'Natural Match': 100,
        'Challenge': 60
    }
    
    # Calculating the average percentage match based on the categories in the results
    total_percentage = 0
    for category in results.values():
        total_percentage += category_to_percentage[category]
    average_percentage = round((total_percentage / len(results)), 2)

    return average_percentage


# In[20]:


def match_compatibility(name_p1, dob_p1, name_p2, dob_p2):
    def calculate_percentage_match(results):
        category_to_percentage = {
        'Compatible': 80,
        'Neutral': 60,
        'Natural Match': 100,
        'Challenge': 40
    }
        percentages = [category_to_percentage[category] for category in results.values()]
        average_percentage = sum(percentages) / len(percentages)
        return round(average_percentage, 2)

    # Assuming evaluate_relationship is already defined
    results = evaluate_relationship(name_p1, dob_p1, name_p2, dob_p2)
    percentage_match = calculate_percentage_match(results)
    
    return f"Overall Match: {percentage_match}%"


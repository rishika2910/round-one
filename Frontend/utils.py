'''
Created on 
Course work: Cancer prognosis
@author: 
Source:
    
'''
# Import necessary modules
import json






#constants


#getting data from json file



with open('questions.json') as f:
   questions = json.load(f)



round_1q = (questions['Round_1'])
round_2q = (questions['Round_2'])
round_3q = (questions['Round_3'])
round_2q_Liver = (round_2q['Liver'])
round_2q_Pancreas = (round_2q['Pancreas'])
round_2q_Lungs = (round_2q['Lungs'])
round_2q_Skin = (round_2q['Skin'])
round_2q_Leukemia = (round_2q['Leukemia'])
round_3q_Liver = (round_3q['Liver'])
round_3q_Pancreas = (round_3q['Pancreas'])
round_3q_Lungs = (round_3q['Lungs'])
round_3q_Skin = (round_3q['Skin'])
round_3q_Leukemia = (round_3q['Leukemia'])    
               

  
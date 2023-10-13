#https://pdas.samhsa.gov/saes/substate#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob
from sklearn.feature_extraction.text import CountVectorizer
#cd HW-02

#load data from csv file
all_data_frames=glob.glob("./Part2/Data/*.csv")+glob.glob("./Part2/Data/*.xlsx")
for fname_index, fname in enumerate(all_data_frames):
    print(fname_index, fname)

#A.clean the data named mental_health
mental_health = all_data_frames[9]
mental_health_df = pd.read_excel(mental_health)  # Use the 'mental_health' variable
# show all the columns of the dataframe
# mental_health_df.columns
print(mental_health_df.head())
# # drop the columns of the dataframes that do not belong to mental health data
mental_health_df = mental_health_df.drop(columns=['Drug use disorders (%)', 'Alcohol use disorders (%)'])
print(mental_health_df.head())
#save the dataframe to csv file
mental_health_df.to_csv("./Part2/Code/mental_health.csv", index=False)



# #B.clean the data named eating_disorders
# eating_disorder = all_data_frames[3]
# print(eating_disorder)
# eating_disorder_df = pd.read_csv(eating_disorder) # Use the 'eating_disorder' variablev
# # show all the columns of the dataframe
# print(eating_disorder_df.columns)
# print(eating_disorder_df.head())
# # drop the columns Continent
# eating_disorder_df = eating_disorder_df.drop(columns=['Continent','Population (historical estimates)'])
# print(eating_disorder_df.shape)
# # only keep the rows of the dataframe when the column 'Year' is between 1990-2021
# # eating_disorder_df = eating_disorder_df.loc[eating_disorder_df['Year'] == range(1990,2022)]
# eating_disorder_df = eating_disorder_df[eating_disorder_df['Year'].isin(range(1990,2022))]
# print(eating_disorder_df.shape)
# rename_map={
#     'Entity':'Country',
#     'Code':'Country Code',
#     'Year':'Year',
#     'Eating disorders (share of population) - Sex: Male - Age: Age-standardized': 'Male',
#     'Eating disorders (share of population) - Sex: Female - Age: Age-standardized':'Female',
# }
# eating_disorder_df.rename(columns=rename_map, inplace=True)
# print(eating_disorder_df.head())
# #caculate the mean of the column Male and Female of the dataframe and save it to a new column named All_gender
# eating_disorder_df['All_gender'] = eating_disorder_df[['Male', 'Female']].mean(axis=1)
# print(eating_disorder_df.head())
# #save the dataframe to csv file
# eating_disorder_df.to_csv("./Part2/Code/eating_disorder.csv", index=False)

# #C.clean the data named discomfort_speaking_anxiety_depression_2020 and Contries_Continents
# Contries_Continents=all_data_frames[0]
# Contries_Continents_df = pd.read_csv(Contries_Continents) 
# print(Contries_Continents_df.head())
# print(Contries_Continents_df.shape)
# discomfort_speaking_anxiety_depression_2020=all_data_frames[1]
# discomfort_speaking_anxiety_depression_2020_df = pd.read_csv(discomfort_speaking_anxiety_depression_2020)
# print(discomfort_speaking_anxiety_depression_2020_df.head())
# print(discomfort_speaking_anxiety_depression_2020_df.columns)
# print(discomfort_speaking_anxiety_depression_2020_df.shape)
# #rename the column 'Entity' to 'Country' and 'Share - Question: mh5 - Someone local comfortable speaking about anxiety/depression with someone they know - Answer: Not at all comfortable - Gender: all - Age_group: all' to 'Not_Comfortable'
# discomfort_speaking_anxiety_depression_2020_df.rename(columns={'Entity':'Country','Share - Question: mh5 - Someone local comfortable speaking about anxiety/depression with someone they know - Answer: Not at all comfortable - Gender: all - Age_group: all':'Not_Comfortable'}, inplace=True)
# # merge the two dataframes
# discomfort_in_continent= discomfort_speaking_anxiety_depression_2020_df.merge(Contries_Continents_df, how='left', left_on='Country', right_on='Country')
# print(discomfort_in_continent.head())
# ##save the dataframe to csv file
# discomfort_in_continent.to_csv("./Part2/Code/discomfort_in_continent.csv", index=False)



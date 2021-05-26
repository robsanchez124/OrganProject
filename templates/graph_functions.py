'''
functions for line plot of organ donations by year
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Original dataframe 
df = pd.read_csv('/Users/guillermo/Downloads/Donor___Donor_Ethnicity_by_Organ,_Donation_Year.csv')
overallreceived = pd.read_csv('/Users/guillermo/Downloads/Transplant___Recipient_Ethnicity_by_Organ.csv')


# Data clean up!
df.rename(columns={"Unnamed: 1": "Dates", 'Unnamed: 0': 'Organ'}, inplace = True)
df.drop(['Multiracial','Unnamed: 2', 'Unknown', 'American Indian/Alaska Native', 'Pacific Islander'], axis=1, inplace = True)
df = df.fillna("")
df1 = df[0:13]

# Data clean up for overallreceived
overallreceived.drop(['Unnamed: 1', 'Unknown', 'American Indian/Alaska Native', 'Pacific Islander', 'Multiracial'], axis=1, inplace = True)
overallreceived.rename(columns={"Unnamed: 0": "Organ"}, inplace = True)
overallreceived = overallreceived[0:7]



# Function that coverts data from strings to integers
ignored_columns = set(['Organ', 'Dates'])
def change_to_int():
    for column_name in df1.columns:
        if column_name not in ignored_columns: 
            df1[column_name] = df1[column_name].str.replace(',','').astype(int)
change_to_int()


# Function for proportions to 'All Ethnicities'
def proportion_to_allethnicities():
    for column_name in df1.columns:
        if column_name not in ignored_columns:
            df1[column_name] = df1[column_name]/df1['All Ethnicities']
            
proportion_to_allethnicities()

'''
New dataframe that pulls column details from "proportion_to_all_ethnicities" function and adds columns for the mean of each ethnicity
'''
dfproportions = {'Dates': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
                 'White': [9849.0, 9635.0, 9539.0, 9648.0, 9828.0, 10163.0, 10843.0, 11221.0, 11810.0, 
                          13057.0, 12378.0],
                 'Black': [2088.0, 1995.0, 1981.0, 2021.0, 1944.0, 2029.0, 2122.0, 2127.0, 2304.0, 
                          2414.0, 2372.0],
                 'Hispanic': [1961.0, 1892.0, 1836.0, 1942.0, 1947.0, 2084.0, 2204.0, 2275.0, 2538.0,
                             2818.0, 2676.0],
                 'Asian': [405.0, 400.0, 429.0, 416.0, 437.0, 515.0, 500.0, 529.0, 555.0, 632.0, 
                          564.0],
                'White_mean': [0.7593333333333333, 0.7593333333333333, 0.7593333333333333, 0.7593333333333333, 0.7593333333333333, 0.7593333333333333, 
                               0.7593333333333333, 0.7593333333333333, 0.7593333333333333, 0.7593333333333333, 0.7593333333333333],
                 'Black_mean': [0.12333333333333334, 0.12333333333333334, 0.12333333333333334, 0.12333333333333334, 0.12333333333333334, 
                                0.12333333333333334, 0.12333333333333334, 0.12333333333333334, 0.12333333333333334, 0.12333333333333334, 0.12333333333333334],
                 'Hispanic_mean': [0.126, 0.126, 0.126, 0.126, 0.126, 0.126, 0.126, 0.126, 0.126, 0.126, 0.126],
                 'Asian_mean': [0.03866666666666667, 0.03866666666666667, 0.03866666666666667, 0.03866666666666667, 0.03866666666666667,
                                0.03866666666666667, 0.03866666666666667, 0.03866666666666667, 0.03866666666666667, 0.03866666666666667, 0.03866666666666667]
                }

dfproportions = pd.DataFrame(data=dfproportions)
'''
Function that divides the columns by the ethnicity mean to rationalize against ethnicity population'''

def ethnic_mean(dfproportions):
    for column_name in dfproportions.columns:
        dfproportions['White']= dfproportions['White'].div(dfproportions['White_mean'], axis = "index")
        dfproportions['Black']= dfproportions['Black'].div(dfproportions['Black_mean'], axis = 'index')
        dfproportions['Hispanic']= dfproportions['Hispanic'].div(dfproportions['Hispanic_mean'], axis = 'index')
        dfproportions['Asian']= dfproportions['Asian'].div(dfproportions['Asian_mean'], axis = 'index')
#         dfprop[]
        return dfproportions
    
ethnic_mean(dfproportions)


# Function for creating the graph
def donation_rate_by_year(dfproportions):
    dfproportions.drop(['White_mean', 'Black_mean', 'Hispanic_mean', 'Asian_mean'], axis = 1, inplace = True)
    sns.set_theme(style="darkgrid")
    ax = dfproportions.plot(kind = 'line');
    plt.legend(loc='upper right')
    ax.set_xticks(dfproportions.Dates.index)
    ax.set(xlabel = "Years", ylabel = "Transplants Donated", title = 'Overall Donation Rate By Population: 2010 - 2020');
    
donation_rate_by_year(dfproportions)

# changing all string vaues to int in overallreceived
def change_to_int(overallreceived):
    for column_name in overallreceived.columns:
        if column_name not in ignored_columns: 
            overallreceived[column_name] = overallreceived[column_name].str.replace(',','').astype(int)
            
change_to_int(overallreceived)

#Data cleanup for allorgansreceived. Singling out the 'All Organs' row
dfallorgansreceived = overallreceived.copy()
dfallorgansreceived.drop([1,2,3,4,5,6], inplace = True)

# Finding the proportion of ethnicity's transplant rates against the overall 
def proportion_to_allethnicities(dfallorgansreceived):
    proportion_ignore = (['Organ', 'Dates', 'All Ethnicities'])
    for column_name in dfallorgansreceived.columns:
         if column_name not in proportion_ignore:
             dfallorgansreceived[column_name] = dfallorgansreceived[column_name]/dfallorgansreceived['All Ethnicities']
        
            
proportion_to_allethnicities(dfallorgansreceived)  

# New dataset for allorgansreceived using values from "dfallorgansreceived" and adding the mean of each ethnicity
organs_rec_proportioned = pd.DataFrame({'Ethnicity': ['White', 'Black', 'Hispanic', 'Asian'],
                                        'Proportioned Amount': [0.622629, 0.190705, 0.127693, 0.042214],
                                        'Ethnicity Mean': [00.7593333333333333, 0.12333333333333334, 0.126, 0.03866666666666667]
                                         })

# Applying ethnic_mean function to "organs_rec_proportioned"
def ethnic_mean(organs_rec_proportioned):
    ignored = (['Ethnicity'])
    for column_name in organs_rec_proportioned.columns:
        if column_name not in ignored:
            print(column_name)
            organs_rec_proportioned['Proportioned Amount'] = organs_rec_proportioned['Proportioned Amount']/organs_rec_proportioned['Ethnicity Mean']
            return organs_rec_proportioned

ethnic_mean(organs_rec_proportioned)

# Applying proportion to ethnicity function to Df allorgansreceived
def proportion_to_allethnicities(dfallorgansreceived):
    proportion_ignore = (['Organ', 'Dates'])
    for column_name in dfallorgansreceived.columns:
        if column_name not in proportion_ignore:
            dfallorgansreceived[column_name] = dfallorgansreceived[column_name]/dfallorgansreceived['All Ethnicities']
            
# Bar graph showing the rates of transplants by ethnicity population against each other
def overall_transplants_by_ethnicity(organs_rec_proportioned):
    organs_rec_proportioned.drop(['Ethnicity Mean'], axis = 1, inplace = True)
    sns.set_theme(style="darkgrid")
    ax = organs_rec_proportioned.set_index('Ethnicity').plot(kind = 'bar');
    plt.legend(loc='upper right')
    ax.set(xlabel="Ethnicity", 
           ylabel = "Overall Transplants Received", 
           title = 'Overall Transplant Rate Normalized to Ethnicity Population: 2010 - 2020',
           # add color somehow
           #color = {'White':'green', 'Black':'red', 'Hispanic': 'cyan', 'Asian': 'olive'}
          );

# Proportioning 'overallreceived' dataframe to the 'All Ethnicities' column
def proportion_to_allethnicities(overallreceived):
    ignored_columns = set(['Organ', 'All Ethnicities'])
    for column_name in overallreceived.columns:
        if column_name not in ignored_columns:
             overallreceived[column_name] = overallreceived[column_name]/overallreceived['All Ethnicities']
            
proportion_to_allethnicities(overallreceived)

'''
Using proportioned 'overallreceived' dataframe as argument to prove if ethnicities are underrepresented or viceversa based off population. This applies for the next 4 functions
'''
def hispanic_proportioned_transplants(overallreceived):
    sns.set_theme(style="darkgrid")
    #overallreceived.drop(['Organ', 'All Ethnicities'], axis = 1, inplace = True)
    ax = overallreceived['Hispanic'].T.plot(kind = 'line');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(.1260, xmin = 0, xmax = 5, label = 'Population Rate')
    plt.legend(loc='upper right')
    ax.set(xlabel = "Organ Type", ylabel = "Transplants Received", title = 'Transplant Rate Proportioned to Hispanic Population');
    
hispanic_proportioned_transplants(overallreceived)

def black_proportioned_transplants(overallreceived):
    ax = overallreceived['Black'].T.plot(kind = 'line');
#     overallreceived.drop(['Organ', 'All Ethnicities'], axis = 1, inplace = True)
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(0.12333333333333334, xmin = 0, xmax = 5, label = 'Population Rate')
    plt.legend(loc='upper right')
    ax.set(xlabel="Ethnicity", ylabel = "Transplants Received", title = 'Transplant Rate Proportioned to Black Population');

black_proportioned_transplants(overallreceived)

def white_proportioned_transplants(overallreceived):
    ax = overallreceived['White'].T.plot(kind = 'line');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(0.7593333333333333, xmin = 0, xmax = 5, label = 'Population Rate')
    plt.legend(loc='upper right')
    ax.set(xlabel="Ethnicity", ylabel = "Transplants Received", title = 'Transplant Rate Proportioned to White Population');


white_proportioned_transplants(overallreceived)

def asian_proportioned_transplants(overallreceived):
    ax = overallreceived['Asian'].T.plot(kind = 'line');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(0.03866666666666667, xmin = 0, xmax = 5, label = 'Population Rate')
    plt.legend(loc='upper right')
    ax.set(xlabel="Ethnicity", ylabel = "Transplants Received", title = 'Transplant Rate Proportioned to Asian Population');

    
asian_proportioned_transplants(overallreceived)


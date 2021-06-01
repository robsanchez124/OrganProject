'''
Function .py file that houses all of the graph functions for the Organ Project

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# dataframe for donations by ethnicity by year
df = pd.read_csv('/Users/guillermo/Downloads/Donor___Donor_Ethnicity_by_Organ,_Donation_Year.csv')
# df datacleanup
df.rename(columns={"Unnamed: 1": "Dates", 'Unnamed: 0': 'Organ'}, inplace = True)
df.drop(['Multiracial','Unnamed: 2', 'Unknown', 'American Indian/Alaska Native', 'Pacific Islander'], axis=1, inplace = True)
df = df.fillna("")
df1 = df[0:13]

# dataframe for transplants received by ethnicity
overallreceived = pd.read_csv('/Users/guillermo/Downloads/Transplant___Recipient_Ethnicity_by_Organ.csv')

# Data clean up for overallreceived
overallreceived.drop(['Unnamed: 1', 'Unknown', 'American Indian/Alaska Native', 'Pacific Islander', 'Multiracial'], axis=1, inplace = True)
overallreceived.rename(columns={"Unnamed: 0": "Organ"}, inplace = True)
overallreceived = overallreceived[0:7]

# dataframe for overall current waiting list by ethnicity
dfwaitinglist = pd.read_csv('/Users/guillermo/Downloads/Waitlist___Ethnicity_by_Organ (1).csv')

# Data cleanup for dfwaitinglist
dfwaitinglist.drop(['Unnamed: 1', 'American Indian/Alaska Native', 'Pacific Islander', 'Multiracial'], axis = 1, inplace = True)
dfwaitinglist.drop([7,8,9,10,11,12,13,14], inplace = True)
dfwaitinglist.rename(columns={"Unnamed: 0": "Organ"}, inplace = True)

# dataframe for status of donor (either living or deceased)
dfdonorstatus = pd.read_csv('/Users/guillermo/Downloads/Donor___Donor_Ethnicity_by_Donor_Type.csv')

# Dataclean up for dfdonorstatus
dfdonorstatus.drop(['Unnamed: 1', 'American Indian/Alaska Native', 'Pacific Islander', 'Unknown', 'Multiracial'], axis = 1, inplace = True)
dfdonorstatus.rename(columns={'Unnamed: 0': 'Donor Type'}, inplace = True)

# Function that coverts data from strings to integers
ignored_columns = set(['Organ', 'Dates'])
def change_to_int(df1):
    for column_name in df1.columns:
        if column_name not in ignored_columns: 
            df1[column_name] = df1[column_name].str.replace(',','').astype(int)



# Function for proportions to 'All Ethnicities'
def proportion_to_allethnicities(df1):
    for column_name in df1.columns:
        if column_name not in ignored_columns:
            df1[column_name] = df1[column_name]/df1['All Ethnicities']
            


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

# Creating pandas dataframe 
dfproportions = pd.DataFrame(data=dfproportions)

# Function that divides the columns by the ethnicity mean to rationalize against ethnicity population
def ethnic_mean(dfproportions):
    for column_name in dfproportions.columns:
        dfproportions['White']= dfproportions['White'].div(dfproportions['White_mean'], axis = "index")
        dfproportions['Black']= dfproportions['Black'].div(dfproportions['Black_mean'], axis = 'index')
        dfproportions['Hispanic']= dfproportions['Hispanic'].div(dfproportions['Hispanic_mean'], axis = 'index')
        dfproportions['Asian']= dfproportions['Asian'].div(dfproportions['Asian_mean'], axis = 'index')
#         dfprop[]
        return dfproportions
    

# Function for creating the graph
def donation_rate_by_year(dfproportions):
    dfproportions.drop(['White_mean', 'Black_mean', 'Hispanic_mean', 'Asian_mean'], axis = 1, inplace = True)
    sns.set_theme(style="darkgrid")
    ax = dfproportions.plot(kind = 'line');
    plt.legend(loc='upper right')
    ax.set_xticks(dfproportions.Dates.index)
    ax.set(xlabel = "Years", ylabel = "Transplants Donated", title = 'Overall Donation Rate By Population: 2010 - 2020');
    

# changing all string vaues to int in overallreceived
def change_to_int(overallreceived):
    for column_name in overallreceived.columns:
        if column_name not in ignored_columns: 
            overallreceived[column_name] = overallreceived[column_name].str.replace(',','').astype(int)
            

#Data cleanup for allorgansreceived. Singling out the 'All Organs' row
dfallorgansreceived = overallreceived.copy()
dfallorgansreceived.drop([1,2,3,4,5,6], inplace = True)

# Finding the proportion of ethnicity's transplant rates against the overall 
def proportion_to_allethnicities(dfallorgansreceived):
    proportion_ignore = (['Organ', 'Dates', 'All Ethnicities'])
    for column_name in dfallorgansreceived.columns:
         if column_name not in proportion_ignore:
             dfallorgansreceived[column_name] = dfallorgansreceived[column_name]/dfallorgansreceived['All Ethnicities'] 

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
            
'''
Using proportioned 'overallreceived' dataframe as argument to prove if ethnicities are underrepresented or viceversa based off population. This applies for the next 4 functions
'''
def hispanic_proportioned_transplants(overallreceived):
    sns.set_theme(style="darkgrid")
    #overallreceived.drop(['Organ', 'All Ethnicities'], axis = 1, inplace = True)
    ax = overallreceived['Hispanic'].T.plot(kind = 'bar');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(.1260, xmin = 0, xmax = 10, color='green', label = 'Population %')
    plt.legend(loc='upper right')
    ax.set(xlabel = "Organ Type", ylabel = "Rate of Transplants Received", title = 'Transplant Rate Proportioned to Hispanic Population');
    
hispanic_proportioned_transplants(overallreceived)

def black_proportioned_transplants(overallreceived):
    ax = overallreceived['Black'].T.plot(kind = 'bar');
#     overallreceived.drop(['Organ', 'All Ethnicities'], axis = 1, inplace = True)
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(0.12333333333333334, xmin = 0, xmax = 10, color='green', label = 'Population %')
    plt.legend(loc='upper right')
    ax.set(xlabel="Ethnicity", ylabel = "Rate of Transplants Received", title = 'Transplant Rate Proportioned to Black Population');

def white_proportioned_transplants(overallreceived):
    ax = overallreceived['White'].T.plot(kind = 'bar');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(0.7593333333333333, xmin = 0, xmax = 10, color='green', label = 'Population %')
    plt.legend(loc='upper right')
    ax.set(xlabel="Ethnicity", ylabel = "Rate of Transplants Received", title = 'Transplant Rate Proportioned to White Population');


def asian_proportioned_transplants(overallreceived):
    ax = overallreceived['Asian'].T.plot(kind = 'line');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(0.03866666666666667, xmin = 0, xmax = 10, color ='green', label = 'Population %')
    plt.legend(loc='upper right')
    ax.set(xlabel="Ethnicity", ylabel = "Rate of Transplants Received", title = 'Transplant Rate Proportioned to Asian Population');


# applying function to dfwaitinglist
ignored_columns = set(['Organ', 'Dates'])
def change_to_int(dfwaitinglist):
    for column_name in dfwaitinglist.columns:
        if column_name not in ignored_columns: 
            dfwaitinglist[column_name] = dfwaitinglist[column_name].str.replace(',','').astype(int)
            
# Applying function to dfwaitinglist
def proportion_to_allethnicities(dfwaitinglist):
    proportion_ignore = (['Organ', 'Dates', 'All Ethnicities'])
    for column_name in dfwaitinglist.columns:
        if column_name not in proportion_ignore:
                dfwaitinglist[column_name] = dfwaitinglist[column_name]/dfwaitinglist['All Ethnicities']

# This function graphs the Hispanic waiting list for all organs and compares against % of population
def hispanic_proportioned_waitinglist(dfwaitinglist):
    sns.set_theme(style="darkgrid")
    ax = dfwaitinglist['Hispanic'].T.plot(kind = 'bar');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(.1260, xmin = 0, xmax = 10, color='green', label = 'Population %')
    plt.legend(loc='upper right')
    ax.set(xlabel = "Organ Type", ylabel = "Waiting List Rate", title = 'Waiting List Rate Proportioned to Hispanic Population');
    
# This function graphs the Black waiting list for all organs and compares against % of population
def black_proportioned_waitinglist(dfwaitinglist):
    sns.set_theme(style="darkgrid")
    ax = dfwaitinglist['Black'].T.plot(kind = 'bar');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(0.12333333333333334, xmin = 0, xmax = 10, color='green', label = 'Population %')
    plt.legend(loc='upper right')
    ax.set(xlabel = "Organ Type", ylabel = "Waiting List Rate", title = 'Waiting List Rate Proportioned to Black Population');

# This function graphs the Asian waiting list for all organs and compares against % of population
def asian_proportioned_waitinglist(dfwaitinglist):
    sns.set_theme(style="darkgrid")
    ax = dfwaitinglist['Asian'].T.plot(kind = 'bar');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(0.03866666666666667, xmin = 0, xmax = 10, color='green', label = 'Population %')
    plt.legend(loc='upper right')
    ax.set(xlabel = "Organ Type", ylabel = "Waiting List Rate", title = 'Waiting List Rate Proportioned to Asian Population');
    
# This function graphs the White waiting list for all organs and compares against % of population
def white_proportioned_waitinglist(dfwaitinglist):
    sns.set_theme(style="darkgrid")
    ax = dfwaitinglist['White'].T.plot(kind = 'bar');
    positions = (0,1,2,3,4,5,6)
    labels= ('All Organs', 'Kidney', 'Liver', 'Pancreas', 'Kidney/Pancreas', 'Heart', 'Lung')
    plt.xticks(positions, labels, rotation = 'vertical')
    plt.hlines(0.7593333333333333, xmin = 0, xmax = 10, color='green', label = 'Population %')
    plt.legend(loc='upper right')
    ax.set(xlabel = "Organ Type", ylabel = "Waiting List Rate", title = 'Waiting List Rate Proportioned to White Population');

# function that cleans up dfdonorstatus.. drops unnecessary columns & renames others
def dropcolumns(dfdonorstatus):
    dfdonorstatus.drop(['Unnamed: 1', 'American Indian/Alaska Native', 'Pacific Islander', 'Unknown', 'Multiracial'], axis = 1, inplace = True)
    dfdonorstatus.rename(columns={'Unnamed: 0': 'Donor Type'}, inplace = True)
    dfdonorstatus.drop([0], inplace = True)

# Applying function to dfdonorstatus
    def change_to_int(dfdonorstatus):
        ignored = (['Donor Type'])
        for column_name in dfdonorstatus.columns:
            if column_name not in ignored:
                dfdonorstatus[column_name] = dfdonorstatus[column_name].str.replace(',','').astype(int)

# applying function to dfdonorstatus
def proportion_to_allethnicities(dfdonorstatus):
    proportion_ignore = (['Donor Type', 'All Ethnicities'])
    for column_name in dfdonorstatus.columns:
        if column_name not in proportion_ignore:
            dfdonorstatus[column_name] = dfdonorstatus[column_name]/dfdonorstatus['All Ethnicities']

# No longer need 'All Ethnicities' column so I'm dropping it
def dropmorecolumns(dfdonorstatus):
    dfdonorstatus = dfdonorstatus.loc[1:2]
    dfdonorstatus.drop(['All Ethnicities'], axis = 1, inplace = True)

# New Dataframe that will allow the next function to divide the columns by the % of population
dfdonorstatusnew = pd.DataFrame({'Ethnicity': ['White', 'Black', 'Hispanic', 'Asian'],
                                'Deceased Donor': [0.70031, 0.141905, 0.12199, 0.021249],
                                'Living Donor': [0.708681, 0.113484, 0.129131, 0.03164],
                                'Ethnicity mean': [00.7593333333333333, 0.12333333333333334, 0.126, 0.03866666666666667]})

'''Function that divides the new 'Ethnicity mean' column by the others
to get the proportioned rate of donation by % of ethnicity
'''      
def donorstatus_ethnicity_mean(dfdonorstatusnew):
    ignore = (['Ethnicity', 'Ethnicity mean'])
    for column_name in dfdonorstatusnew:
        if column_name not in ignore:
            dfdonorstatusnew[column_name] = dfdonorstatusnew[column_name]/dfdonorstatusnew['Ethnicity mean']

# Bar chart of rate of living/deceased donors by ethnicity population
def donationstatus_by_ethnicity(dfdonorstatus):
    dfdonorstatusnew.drop(['Ethnicity mean'], axis = 1, inplace = True)
    sns.set_theme(style="darkgrid")
    ax = dfdonorstatusnew.plot(kind = 'bar');
    plt.legend(loc='upper right')
    positions = (0,1,2,3)
    labels = ('White', 'Black', 'Hispanic', 'Asian')
    plt.xticks(positions, labels, rotation = 'horizontal')
    ax.set(xlabel="Ethnicity", 
           ylabel = 'Rate of Transplants Donated', 
           title = 'Donor Status Proportioned by Ethnicity Population: 2010 - 2020',
           # add color somehow
           #color = {'White':'green', 'Black':'red', 'Hispanic': 'cyan', 'Asian': 'olive'}
          );



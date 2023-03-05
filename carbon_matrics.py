# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:12:33 2023

@author: SHAHANA SHIRIN
"""

import pandas as pd 
import matplotlib.pyplot as plt

def co2_emission():
    """
    function  for ploting the line plot.
    
    This function reads the Carbon emission from the CSV file and creates a line plot of emission for selected countries 
    """ 
    
    #load the carbon_matrics data from the CSV file
    df_1 = pd.read_csv("carbon_matrics.csv")
    #define the countries to plot
    
    countries = ['United States','India','Georgia']
    
    #plot the data
    
    plt.figure()
    
    plt.plot(df_1["year"], df_1[countries], marker = 'o', label = countries)
    
    #to set the axis and title
    
    plt.xticks(df_1["year"], labels = df_1["year"], rotation = 'vertical')
    
    plt.xlabel("year")
    
    plt.ylabel("co2 emission(matric tons/capita) ")
    
    plt.xlim(2010, 2019)
    
    plt.title('Co2 Emmission from 2010-2019\n')
    
    plt.legend()
    
    #to save the figure
    
    plt.savefig("co2.png")
    
    #show the plot
    
    plt.show()
    
    return
    

def cause_of_death():
    """
    function for plotting a pie chart.
    
    this function reads the cause of death data by non-communicable diseases from the CSV file and 
    creates a pie chart showing the percentage of deaths by non-communicable diseases for each country.
    """
    #load the non_communicable data from the CSV file
    
    df_2 = pd.read_csv("non_communicable.csv")

    #plot the data
    
    plt.figure()
    plt.pie(df_2['2019'], labels = df_2['countries'], shadow=True, startangle = 45)
    
    # set the title and axis labels
    
    plt.title('Cause of Death By Non Communicable Disease in 2019\n')
    plt.axis('equal')
    
    #to save the figure
    
    plt.savefig("cause of death.png")
    
    # show the plot
    plt.show()
    
    return

def inflation():
    """
    function for plotting bar plot.
    
    this function reads the inflation of consmuer data from the CSV file and creates a bar plot showing in pie chart
    
    """
    
    # load the inflation_consumer data from the csv file
    df_3 = pd.read_csv('inflation_consumer.csv', index_col= 'year')
    
    # plot the data
    df_3.plot(kind = 'bar', figsize = (10, 6), width = 1)
    
    # set the title and axis labels
    plt.title('inflation in consumer price')
    
    plt.xlabel('Year')
    
    plt.ylabel('inflation')
    
    # add a legend
    plt.legend(loc='upper left')
    
    # to save the figure
    
    plt.savefig("inflation.png")
    
    # show the plot
    plt.show()



   
if __name__ == '__main__':
    """
    Main function that calls the other functions to create the plots.
    """
    #calling function to visualise line plot
    co2_emission()
    
    ##calling function to visualise pie chart
    cause_of_death()
    
    #calling function to visualise bar plot
    inflation()










    

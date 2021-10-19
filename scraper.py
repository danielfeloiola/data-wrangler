# imports
import requests
import pandas as pd
from bs4 import BeautifulSoup


def main():

    # wikipedia URL
    url = 'https://en.wikipedia.org/wiki/Road_safety_in_Europe'

    # get the webpage
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    # find the table
    table = soup.find('table', class_='wikitable sortable')

    #turn it into a dataframe
    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])

    # edit the table based on the specification : 
    # add a year field
    df['Year'] = 2018

    # drop columns not mentioned on the specification
    final_df = df.drop(['Road Network Length (in km) in 2013[29]', 
                        'Number of People Killed per Billion km[30]', 
                        'Number of Seriously Injured in 2017/2018[30]'],
                        axis=1)

    # rename columns
    final_df = final_df.rename(columns={'Area (thousands of km2)[24]': 'Area',
                                        'Population in 2018[25]': 'Population',
                                        'GDP per capita in 2018[26]': 'GDP per capita',
                                        'Population density (inhabitants per km2) in 2017[27]': 'Population density',
                                        'Vehicle ownership (per thousand inhabitants) in 2016[28]': 'Vehicle ownership',
                                        'Total Road Deaths in 2018[30]': 'Total Road Deaths',
                                        'Road deaths per Million Inhabitants in 2018[30]': 'Road deaths per Million Inhabitants'})

    # rearrange columns
    final_df = final_df[['Country',
                        'Year',
                        'Area', 
                        'Population',
                        'GDP per capita',
                        'Population density',
                        'Vehicle ownership',
                        'Total Road Deaths',
                        'Road deaths per Million Inhabitants']]

    # sort by "Road deaths per Million Inhabitants"
    final_df.sort_values(by=['Road deaths per Million Inhabitants'], inplace=True, ascending=False,)

    # remove unwanted characters on the GDP per capita column and population
    final_df['GDP per capita'] = final_df['GDP per capita'].str.replace('[,†a]', '', regex=True)
    final_df['Population'] = final_df['Population'].str.replace('[.,]', '', regex=True)

    # and turn them back into an integer
    final_df['GDP per capita'] = final_df['GDP per capita'].astype(int)
    final_df['Population'] = final_df['Population'].astype(int)

    # output to a csv file (index=False to remove the id column)
    final_df.to_csv('data/data.csv', index=False)

    # add a return statement so the df can be retrieved on the extra.py file
    return final_df

if __name__ == '__main__':
    main()
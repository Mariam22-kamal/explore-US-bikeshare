import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    Return:
        (str) city 
        (str) month 
        (str) day 
   
    while True:
      city = input("\n Which city would you like to filter by from those cities New York City, Chicago or Washington?\n")
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break



    while True:
      month = input(" Which month would you like to filter by? \n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break

  
    while True:
      day = input(" which day are you looking for, type 'all' if you don't have any\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break

    return city, month, day


def load_data(city, month, day):

    Args:
        (str) city
        (str) month
        (str) day
    Returns:
        df 
   
    df = pd.read_csv(CITY_DATA[city])

   
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    if month != 'all':
   	 	
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	
        df = df[df['month'] == month]

       
    if day != 'all':
      
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
 

    print('\n Calculating the most frequent times of Traveling \n')
    start_time = time.time()

   

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)


  

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)



   

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("this took %s seconds" % (time.time() - start_time))
   


def station_stats(df):
 
    print('\nCalculating the most popular stations and trips...\n')
    start_time = time.time()

  

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


 
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("this took %s seconds" % (time.time() - start_time))


def trip_duration_stats(df):
 

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("this took %s seconds." % (time.time() - start_time))



def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
   
    print('User Types:\n', user_types)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

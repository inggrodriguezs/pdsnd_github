# This is the template project file Provided by Udacity Team
# I´ve developed that project following their instructions 

import time
import pandas as pd
import numpy as np

# This is the dictionary that stores all the files, we can index the dictionary
# using the key file
 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
      try:
        # option 1 with names
        city = str(input("Choose the name of the dataframe you want to process: \n Chicago \n New York City \n Washington\n"))
        city = city.lower()
        cities = ['chicago','new york city', 'washington']
        if city in cities:
            break
        else: 
            print('You must type a correct city, please enter again:')
        
        # Option 2 with numbers:
        # city = int(input("Choose the name of the dataframe you want to process: \n 1 = Chicago \n 2 = New York City \n 3 = Washington\n"))
      except ValueError as ve:
        # some code
        print("Exception occurred, please insert a valid number (integer): {}".format(ve))
      except Exception as e:
        # some code
        print("Exception occurred, please insert a valid number (integer): {}".format(e)) 
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      try:
        month = str(input("Which month do you want to filter: \n Insert the name of the month: \n All\n January\n Febuary\n March\n April\n May\n June\n"))
        month = month.lower()
        months = ['all','january', 'february', 'march', 'april', 'may', 'june']
        if month in months:
            break
        else: 
            print('You must type a correct month, please enter again:')
      except ValueError as ve:
        # some code
        print("Exception occurred, please insert a valid month name: {}".format(ve))
      except Exception as e:
        # some code
        print("Exception occurred, please insert a valid month name: {}".format(e)) 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      try:
        day = str(input("Which day do you want to filter: \n Insert the name of the day: \n All\n Monday\n Tuesday\n Wednesday\n Thursday\n Friday\n Saturday\n Sunday\n"))
        day = day.lower()
        days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        
        if day in days:
            break
        else: 
            print('You must type a correct day, please enter again:')    
      except ValueError as ve:
        # some code
        print("Exception occurred, please insert a valid month name: {}".format(ve))
      except Exception as e:
        # some code
        print("Exception occurred, please insert a valid month name: {}".format(e)) 

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Option 2 with numbers 
    
    # city_idex = {'1':'chicago.csv',
                 # '2':'new_york_city.csv',
                 # '3':'washington.csv'}
    
    # load data file into a dataframe option 2
    # df = pd.read_csv(city_idex.get(city))
    
    # load data file into a dataframe option 1
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns, also the start hour
    
    # df['month'] = df['Start Time'].dt.month_name(locale = 'English')
    # df['month'] = df['Start Time'].dt.month)
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    most_common_month = df['month'].value_counts().sort_index().idxmax()
    n = max(df['month'].value_counts().tolist())
    print('The most common month: {} with {} occurrences'.format(most_common_month, n))
    
    # TO DO: display the most common day of week
    
    most_common_dow = df['day_of_week'].value_counts().sort_index().idxmax()
    n = max(df['day_of_week'].value_counts().tolist())
    print('The most common day of week: {} with {} occurrences'.format(most_common_dow, n))

    # TO DO: display the most common start hour
    
    most_common_start_hour = df['start_hour'].value_counts().sort_index().idxmax()
    n = max(df['start_hour'].value_counts().tolist())
    print('The most common start hour: {} with {} occurrences'.format(most_common_start_hour, n))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().sort_index().idxmax()
    n = max(df['Start Station'].value_counts().tolist())
    print('The most commonly used start station: {} with {} occurrences'.format(most_common_start_station, n))
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().sort_index().idxmax()
    n = max(df['End Station'].value_counts().tolist())
    print('The most commonly used start station: {} with {} occurrences'.format(most_common_end_station, n))

    # TO DO: display most frequent combination of start station and end station trip
    
    # Concat start sation asn end station in order to make some counts
    df['start_end_station'] = df[['Start Station','End Station']].apply(lambda x : 'Start: {} - End: {}'.format(x[0],x[1]), axis=1)
    
    # show the calculations    
    most_common_start_end_station = df['start_end_station'].value_counts().sort_index().idxmax()
    n = max(df['start_end_station'].value_counts().tolist())
    print('The most frequent combination of start station and end station trip: {} with {} occurrences'.format(most_common_start_end_station, n))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time was: {} seconds'.format(total_travel_time))
    
    # Time delta: code used: 
    # https://www.kite.com/python/answers/how-to-convert-seconds-to-days,-hours,-and-minutes-in-python
    seconds = total_travel_time
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    days = seconds // seconds_in_day
    hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
    minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
    
    print('The total travel time was: {} days, {} hours, {} minutes'.format(days, hours, minutes))
        
    # TO DO: display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time was: {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print('The count of user types is:\n {}'.format(user_types))

    # TO DO: Display counts of gender
    
    user_gender = df['Gender'].value_counts()
    print('The count of gender is:\n {}'.format(user_gender))


    # TO DO: Display earliest, most recent, and most common year of birth
    
    # calculations
    earliest_yob = int(df['Birth Year'].max())
    most_recent_yob = int(df['Birth Year'].min())
    most_common_yob = int(df['Birth Year'].value_counts().sort_index().idxmax())
    
    # prints
    print('\n')
    print('-'*40) 
    print('The earliest year of birth is: {}'.format(earliest_yob))
    print('The most recent year of birth is: {}'.format(most_recent_yob))
    print('The most common year of birth is: {}'.format(most_common_yob))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
           
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except Exception as e:
            print('An exception has occurred: {}'.format(e))

if __name__ == "__main__":
	main()

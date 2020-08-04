import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

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
    city = None
    while(city not in CITY_DATA):
        city = input("Please select a city: (chicago, new york city or washington)\n")
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    month = None
    while(month not in months):
        month = input("Please input the month for which you want to investigate: (all or select a month from junuary to june)\n")
        month = month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    while(day not in days):
        day = input("Please input the day for which you want to investigate: (all or select a day of the week)\n")
        day = day.lower()



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
    df = pd.read_csv(CITY_DATA[city])
    
     #convert the Start Time column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #creating month and day_of_week columns from Start Time column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


     # filter by month if applicable
    if month != 'all':
        #filter the data to get the selected month
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #filter by the selected day of week 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\nThe most common month is: ")
    print(months[ (df['month'].mode()[0]) - 1])

    # TO DO: display the most common day of week
    print("\nThe most common day of week is: ")
    print(df['day_of_week'].value_counts().idxmax())


    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('\nThe most common hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\nThe most commonly used start station is: ", df['Start Station'].mode()[0])
    
    # display most commonly used end station
    print("\nThe most commonly used end station is: ", df['End Station'].mode()[0])
    # display most frequent combination of start station and end station trip
    print("\nThe most frequent combination of tart station and end station trip is:" , df.groupby(['Start Station','End Station']).size().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nTotal travel time is: ', df['Trip Duration'].sum())
    
    # display mean travel time
    print('\nMean travel time is :', df['Trip Duration'].mean())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nCounts of user types:\n", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    
    if 'Gender' in df.columns:
        print("\nCounts of gender:\n", df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth in the data is:', int(df['Birth Year'].min()))
        print('the most recent year of birth in the data is:', int(df['Birth Year'].max()))
        print('the most common year of birth in the data is:', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    answer = input('Do you want to see raw data? (yes or no)').lower()
    i = 0
    while(answer == 'yes'):
        print(df.iloc[i:i+5,])
        i = i+5
        answer = input('Do you want to see more 5 lines of raw data? (yes or no)').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

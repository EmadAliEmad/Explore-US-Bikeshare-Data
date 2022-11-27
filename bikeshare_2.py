import time
import numpy as np
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike_share data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Please choose a city from : ( Chicago, New York City, and Washington ) : \n").lower()
        if city not in CITY_DATA:
            print("Invalid input.. Please choose a correct city from : ( Chicago, New York City, and Washington ): \n")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please choose month from ( january, february, march , april, may, june ) or type 'all' to "
                      "select all months   :  \n").lower()
        months = ["january", "february", "march", "april", "may", "june"]
        if month != "all" and month not in months:
            print("Invalid input.. Please enter a valid month name : \n")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter a day of the week from : \n  ( monday - tuesday - "
                    "wednesday - thursday - friday - saturday - sunday ) or type 'all' to display days : \n").lower()
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        if day not in days and day != "all":
            print("Invalid input.. Please enter a valid day name \n")
        else:
            break

    print('-' * 40)
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # common_month = df['month'].mode()[0]
    print('Most Common Month: {}'.format(df['month'].mode()[0]))

    # display the most common day of week

    print('Most Common Day : {}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour

    print('Most Common Start Hour: {}'.format(df['Start Hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    print('Most common used start station : {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station

    print("most common end station : {}".format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['common_start_end'] = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('Most common start and end station: {}'.format(df['common_start_end'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time:', (df['Trip Duration'].sum()).round())

    # display mean travel time
    print('Average Travel Time : ', (df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of users types:\n', df['User Type'].value_counts())

    # Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts().to_frame())

        # Display earliest, most recent, and most common year of birth
        print('the most common year of birth is: ', int(df['Birth Year'].mode()[0]))
        print('the most recent year of birth is: ', int(df['Birth Year'].max()))
        print('the earliest year of birth is: ', int(df['Birth Year'].min()))
    else:
        print('There is no data for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    print('Raw data is available to check...\n')
    i = 0
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    if view_data not in ['yes', 'no']:
        print('Invalid input please type yes or no ')
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    elif view_data != 'yes':
        print('Thank You')

    else:
        while i + 5 < df.shape[0]:
            print(df.iloc[i:i + 5])
            i += 5
            view_data = input("Do you wish to continue?:  ").lower()
            if view_data != 'yes':
                print('Thank You')
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

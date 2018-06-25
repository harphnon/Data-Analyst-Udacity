import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city_input = input("\nWhich city would you like to filter the data by? Chicago, New York, or Washington?\n>>")
        city = city_input.title()
        if city in ['Chicago', 'New York', 'Washington']:
            break
        else:
            print("Please enter the name of a valid city.\ You entered:", city)
        # get user input for month (all, January, February, ... , June)
    while True:
        month_input = input(
            '\nWhich month would you like to filter the data by? January, February ...... or all?\n>> ')
        month = month_input.title()
        if month in ['January', 'February', 'March', 'April', 'May', 'June', "All"]:
            break
        else:
            print("Please enter the name of a valid month. You entered:", month)

        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_input = input('\nFor which day? Monday, Tuesday, Wednesday ..... or all ?\n>> ')
        day = day_input.title()
        if day in ["Monday", "Tuesday", "Wednesday", "Thursday" "Friday", "Saturday", "Sunday", "All"]:
            break
        else:
            print("Please enter the name of a valid day of the week. You entered:", day)

    return city, month, day


def load_data(city, month, day):
    global CITY_DATA

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

    # print(df.head(n=15))

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day'] = df['Start Time'].dt.strftime('%A')

    # print(df.head(n=15))

    # filter

    if month != 'All':
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Len of unique month list

    if len(df.month.unique()) >= 2:
        # maximum frequency
        popular_month = df['month'].mode().iloc[0]
        print("The most common month is: {}".format(popular_month))
    else:
        print("You have to choose all month")

    # Len of unique day list
    if len(df.day.unique()) >= 2:
        popular_day = df["day"].mode().iloc[0]
        print("The most common day is: {}".format(popular_day))
    else:
        print("You have to choose all day")

    # display the most common start hour
    hour = df["Start Time"].dt.strftime('%H')
    popular_hour = hour.mode().iloc[0]
    print("The most common hour is; {}".format(popular_hour))

    print("That took %s seconds." % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    start_station = df["Start Station"].mode().iloc[0]
    print("Most commonly used start station: {}".format(start_station))

    # display most commonly used end station

    end_station = df["End Station"].mode().iloc[0]
    print("Most commonly used end station: {}".format(end_station))

    # display most frequent combination of start station and end station trip

    df['trip'] = df['Start Station'] + ' - ' + df['End Station']
    both_station = df['trip'].mode()[0]
    print("Most commonly combination of start and end station: {}".format(both_station))

    print("That took %s seconds." % (time.time() - start_time))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = np.sum(df["Trip Duration"]) / 3600
    print("Total travel time: {} h".format(total_travel_time))

    # display mean travel time

    mean_travel_time = np.average(df["Trip Duration"]) / 60
    print("Mean travel time: {} min".format(mean_travel_time))

    print("That took %s seconds." % (time.time() - start_time))


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user
    if {"User Type"}.issubset(df.columns):
        user_type = df["User Type"].value_counts()
        print("Counts of user types is : {}".format(user_type))
    else:
        print("No User Type in this City")

    # Display counts of gender
    if {"Gender"}.issubset(df.columns):
        gender = df["Gender"].value_counts()
        print("Counts of gender is : {}".format(gender))
    else:
        print("No gender in this City")

    # Display earliest, most recent, and most common year of birth
    if {"Birth Year"}.issubset(df.columns):
        earliest = df["Birth Year"].min()
        most_recent = df["Birth Year"].max()
        # print(df[df["Birth Year"] == df["Birth Year"].max()])
        common = df["Birth Year"].mode()[0]
        print("Display earliest is {}, most recent {}, and most common year of birth {}".format(earliest, most_recent,
                                                                                                common))
    else:
        print("No Birth Year in this city")

    print("That took %s seconds." % (time.time() - start_time))


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

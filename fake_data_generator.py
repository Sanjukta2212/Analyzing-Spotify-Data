import pandas as pd
import numpy as np
import time
import hashlib
import string
import random
from dateutil.relativedelta import relativedelta

def generate_us_phone_numbers(num, country_code):
    """
    US/Canada : In this format, Example : +1 940-566-4815
    Indian : In this format, Example : +91 73302-89911
    """
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module

    if country_code == "+1": # format of us number have two dashes after 3 3 and 4 
        numbers = np.random.randint(100, 999, size=(num, 2))
        last_chunk = np.random.randint(1000, 9999, size=num) # Generate a 4-digit number
        formatted_numbers = np.column_stack([np.full(num, country_code), numbers, last_chunk])
        phone_numbers = list(map(lambda x: f"{x[0]} {x[1]}-{x[2]}-{x[3]}", formatted_numbers))
        return phone_numbers
    elif country_code == "+91": # Just because format of Indian number only have single dash in the middle
        numbers = np.random.randint(70000, 99999, size=(num, 2))
        formatted_numbers = np.column_stack([np.full(num, country_code), numbers])
        phone_numbers = list(map(lambda x: f"{x[0]} {x[1]}-{x[2]}", formatted_numbers))
        return phone_numbers
    else:
        print("I'm only allowed to handle US/Canada/Indian country codes")


def generate_time(num, duration = False, Podcast = False):
    """
    It will be in this format.
    HH:MM:SS
    Example - 17:03:10
    """

    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    mean_hours = 12
    std_dev_hours = 6
    mean_minutes = 30
    std_dev_minutes = 15
    mean_seconds = 30
    std_dev_seconds = 15


    hours = np.random.normal(mean_hours, std_dev_hours, size=num).astype(int) % 24
    minutes = np.random.normal(mean_minutes, std_dev_minutes, size=num).astype(int) % 60
    seconds = np.random.normal(mean_seconds, std_dev_seconds, size=num).astype(int) % 60
    times = np.array([f"{h:02d}:{m:02d}:{s:02d}" for h, m, s in zip(hours, minutes, seconds)])

    if duration:
        duration_minutes = np.random.normal(3, 0.5, size=num)
        duration_seconds = np.random.normal(0, 30, size=num).astype(int) % 60
        durations = np.array([f"{int(0):02d}:{int(mins):02d}:{int(secs):02d}" for mins, secs in zip(duration_minutes, duration_seconds)])
        return durations
    
    if Podcast:
        duration_minutes = np.random.normal(45, 5, size=num).astype(int) % 60
        duration_seconds = np.random.normal(0, 30, size=num).astype(int) % 60
        durations = np.array([f"{int(0):02d}:{int(mins):02d}:{int(secs):02d}" for mins, secs in zip(duration_minutes, duration_seconds)])
        return durations
        

    return times

def generate_date(num, date_format="DD/MM/YYYY"):
    """
    Generates random dates within a specified range.

    Parameters:
    num (int): Number of dates to generate.
    date_format (str): Format of the date. "DD/MM/YYYY" or "MM/DD/YYYY".

    Returns:
    list: List of formatted dates.
    """

    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    start = pd.to_datetime('2018-01-01')
    end = pd.to_datetime('2023-12-31')

    # album_dates = album_date_worldwide.copy()  # Make a copy of the dates list before shuffling
    date_range = pd.date_range(start, end)
    random_dates = np.random.choice(date_range, num)

    if date_format == "DD/MM/YYYY":
        dates = [pd.to_datetime(date).strftime('%d/%m/%Y') for date in random_dates]
    elif date_format == "MM/DD/YYYY":
        dates = [pd.to_datetime(date).strftime('%m/%d/%Y') for date in random_dates]
    else:
        raise ValueError("Invalid date format. Please use 'DD/MM/YYYY' or 'MM/DD/YYYY'.")

    return dates


def generate_numeric_data(low_limit, high_limit, mean, std_dev, num_rows):
    """
    Generates data for likes, followers, and other similar metrics within specified limits using a normal distribution.

    Parameters:
    low_limit (int): Lower limit for the data.
    high_limit (int): Upper limit for the data.
    num_rows (int): Number of data points to generate.

    Returns:
    numpy.ndarray: Array of generated data.
    """
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    # mean = (low_limit + high_limit) / 2
    # std_dev = (high_limit - low_limit) / 6  # Adjust this standard deviation based on the desired spread
    data = np.random.normal(mean, std_dev, size=(num_rows,))
    data = np.clip(data, low_limit, high_limit)  # Clip the values within the specified limits
    return data.astype(int)


def generate_alphabetical_data(chunk_lengths, num_rows):
    """
    Generates alphabetical data with spaces or without space based on the provided chunk lengths.
    Make sure chunk_lengths is in list type.

    Parameters:
    chunk_lengths (list): List of lengths for each chunk.
    num_rows (int): Number of rows to be generated.

    Returns:
    list: List of strings with alphabetical data separated by spaces.
    """
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module

    data = []
    for _ in range(num_rows):
        chunks = ["".join(np.random.choice(list(string.ascii_lowercase), max(1, int(np.random.normal(length, 1))))).strip() for length in chunk_lengths]
        data.append(" ".join(chunks))
    return data



def generate_email_data(domain, num_rows, numeric_part=False):
    """
    Generates email data with random usernames based on the provided parameters.

    Parameters:
    domain (str): Domain name for the email addresses.
    num_rows (int): Number of email addresses to generate.
    numeric_part (bool): If True, includes a numeric part in the username.

    Returns:
    list: List of strings with email addresses.
    """
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    data = []
    for _ in range(num_rows):
        username_length = int(np.random.normal(8, 2))  # Adjust mean and standard deviation as needed
        if numeric_part:
            letters_length = int(np.random.normal(username_length // 2, 1))
            letters_length = max(1, letters_length)
            numbers_length = max(0, username_length - letters_length)  # Ensure non-negative dimensions
            username = ''.join(np.random.choice(list(string.ascii_lowercase), letters_length))
            username += ''.join(np.random.choice(list(string.digits), numbers_length))
        else:
            username = ''.join(np.random.choice(list(string.ascii_lowercase), username_length))
        data.append(f"{username}@{domain}")
    return data



def generate_encrypted_passwords(chunk_lengths, num_rows):
    """
    Generates passwords and their corresponding MD5 hash.

    Parameters:
    chunk_lengths (list): List of lengths for each chunk.
    num_rows (int): Number of rows to be generated.
    
    Returns:
    dict: Dictionary containing the passwords and their MD5 hash.
    """
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    passwords = generate_alphabetical_data(chunk_lengths, num_rows)
    saved_pass = []
    for password in passwords:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        saved_pass.append(hashed_password)
    return saved_pass



def generate_podcasts_date(start_date, end_date, num):
    """
    Generates random dates within a specified range.

    Parameters:
    start_date (str): Starting date for generating the dates.
    end_date (str): Ending date for generating the dates.
    num (int): Number of dates to generate.

    Returns:
    list: List of formatted dates.
    """
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    start_date = pd.to_datetime(start_date) + pd.DateOffset(days=np.random.randint(0, 1200))
    date_range = pd.date_range(start_date, end_date, freq='W')

    dates = [pd.to_datetime(date).strftime('%d/%m/%Y') for date in date_range]
    return dates



def generate_podcast_data(num_rows, podcast_title, start_date, end_date):
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    podcast_data = []
    prev_title = ""
    prev_host = ""
    podcast_id = 0
    for _ in range(num_rows):
        title = np.random.choice(podcast_title)
        if title != prev_title:
            host = np.random.choice(generate_alphabetical_data([5, 7], 1))  # Change the host only if the title changes
        else:
            host = prev_host
        prev_title = title
        prev_host = host

        episodes = int(np.random.normal(5, 2))
        if episodes < 1:
            episodes = 1

        episode_dates = generate_podcasts_date(start_date, end_date, episodes)
        for i in range(episodes):
            podcast_id += 1
            podcast_data.append({
                "Podcast Id" : podcast_id,
                'Podcast Title': title,
                'Episode Number': i + 1,
                'Episode Date': episode_dates[i],
                'Host Name': host  
            })

    
    return podcast_data


def generate_premium_subscription(num_rows, users_table):
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    min_created_at_date = pd.to_datetime(users_table["Created At"], format='%d/%m/%Y').min().date()
    start_dates = [pd.to_datetime(min_created_at_date) + pd.DateOffset(days=np.random.randint(1, 1200)) for _ in range(num_rows)]
    canceled_or_not = np.random.choice(['renew', 'cancel'], num_rows, p=[0.75, 0.25])
    end_dates = []
    for status, start_date in zip(canceled_or_not, start_dates):
        if status == 'cancel':
            end_date = start_date + pd.DateOffset(days=np.random.randint(1200))
            end_dates.append(end_date.strftime('%d/%m/%Y'))
        else:
            end_dates.append('01/01/2099')

    return pd.DataFrame({
        'Subscriber ID': list(range(1, num_rows + 1)), 
        'Start Date': [date.strftime('%d/%m/%Y') for date in start_dates],
        'End Date': end_dates,
        'Canceled or Not': canceled_or_not
    })



def generate_transaction_dates(premium_subscriptions):
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    transaction_dates = []
    subscriber_ids = []
    today = pd.to_datetime('today')
    for idx, (start, end, subscriber_id) in premium_subscriptions[['Start Date', 'End Date', 'Subscriber ID']].iterrows():
        start_date = pd.to_datetime(start, format='%d/%m/%Y', errors= 'coerce')  # Update the format string here
        end_date = pd.to_datetime(end, format='%d/%m/%Y', errors = 'coerce')
        current_date = start_date
        while current_date < min(end_date, today):
            transaction_dates.append(current_date.strftime('%d/%m/%Y'))
            subscriber_ids.append(subscriber_id)
            current_date += relativedelta(months=1)
    return transaction_dates, subscriber_ids



def generate_subscription_ids(is_subscribed):
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    subscription_ids = []
    current_id = 1
    for status in is_subscribed:
        if status == 'yes':
            subscription_ids.append(current_id)
            current_id += 1
        else:
            subscription_ids.append(np.nan)
    return subscription_ids
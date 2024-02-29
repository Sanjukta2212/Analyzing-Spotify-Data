
from fake_data_generator import *


def User():
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    # Creating user table

    # we'll be creating 50000
    ## Creating user.region
    ## 40 regions
    # user.region we'll have 
    # 20,000 rows with 0 space - 10,000 of 5 letter and 10,000 of 9 letters
    # 15,000 rows with 1 space
    # 15,000 rows with 2 spaces
    user_region_spaces_5 = generate_alphabetical_data([5],10)
    usesr_region_spaces_9 = generate_alphabetical_data([9],10)
    user_region_space_1 = generate_alphabetical_data([10, 7], 10)
    user_region_space_2 = generate_alphabetical_data([10, 7, 9], 10)

    user_region = user_region_spaces_5 + usesr_region_spaces_9 + user_region_space_1 + user_region_space_2

    # now we'll be creating user.email

    # it will have 40000 rows
    # 21000 rows without numeric part and
    ##      This will have @gmail.com, @gmail.co.in, @hotmail.com, @buffalo.edu
    # 19000 rows with numeric part
    ##      This will have @yahoo.com, @yahoo.co.in, @outlook.com, @aol.com

    # these are without numeric part
    mail_gmail_com = generate_email_data("gmail.com", 7000)
    mail_hotmail_com = generate_email_data("hotmail.com", 7000)
    mail_buffalo_edu = generate_email_data("buffalo.edu", 7000)

    # these are with numeric part
    mail_yahoo_com = generate_email_data("yahoo.com", 7000, True)
    mail_outlook_com = generate_email_data("outlook.com", 7000, True)
    mail_aol_com = generate_email_data("aol.com", 5000, True)

    user_mail = (
        mail_gmail_com
        + mail_hotmail_com
        + mail_buffalo_edu
        + mail_yahoo_com
        + mail_outlook_com
        + mail_aol_com
    )

    # now we'll be creating user.password
    # and we'll be using MD5 encryption to save it

    # it will have 
    # 25000 rows without the space and
    ##      12500 with 12 length
    ##      12500 with 8 length
    # 25000 rows with the space
    ##      12500 with [5 ,6] lengths
    ##      12500 with [9, 5] lengths

    # passwords without spaces
    pass_8 = generate_encrypted_passwords([8], 10000)
    pass_12 = generate_encrypted_passwords([12], 10000)

    # passwords with spaces
    pass_5_6 = generate_encrypted_passwords([5, 6], 10000)
    pass_9_5 = generate_encrypted_passwords([9, 5], 10000)
    ## make sure to check it's not in dictionary



    user_password = pass_8 + pass_12 + pass_5_6 + pass_9_5
    is_subscribed = np.random.choice(["yes", "no"], 40000, p=[0.35,0.65])
    user_df = pd.DataFrame({
    "User_Id" : [i+1 for i in range(40000)],
    "User_Email" : user_mail,
    "User_Encrypted_Pass" : user_password,
    "User_Region" : np.random.choice(user_region, 40000),
    "Created At" : generate_date(40000),
    "Is_Subscribed" : is_subscribed,
    "Subscription_id" : generate_subscription_ids(is_subscribed)})

    return user_df


def Album():
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    # now we'll be creating Album
    # 5000 albums
    # First we'll be creating album.title
    # Title will have 
    # title without spaces
    ##      12500 rows with 6 letters
    ##      12500 rows with 14 letters
    album_title_6_letters = generate_alphabetical_data([6], 1250)
    album_title_14_letters = generate_alphabetical_data([14], 1250)
    # album_title_6_letters *= 100
    # album_title_14_letters *= 100
    # title with spaces
    ##      12500 rows with 3, 5 letters
    ##      12500 rows with 8, 6 letters
    album_title_3_5_letters = generate_alphabetical_data([3, 5], 1250)
    album_title_8_6_letters = generate_alphabetical_data([8, 6], 1250)

    # album_title_3_5_letters *= 100
    # album_title_8_6_letters *= 100

    album_titles = album_title_6_letters + \
                    album_title_14_letters + \
                    album_title_3_5_letters + \
                    album_title_8_6_letters
    
    # now we'll be creating album.release_date

    # album date 4000
    ## 40000 rows will be worldwide format
    album_date_worldwide = generate_date(5000)

    ## 10000 rows will have US format
    # album_date_US = generate_date(1500, "MM/DD/YYYY")

    album_dates = album_date_worldwide
    # random.shuffle(album_dates)
    album_df = pd.DataFrame({
    "Album_Id" : [i+1 for i in range(5000)],
    "Album_Title" : album_titles,
    "Album_Release_Date" :  album_dates})

    album_df['Album_Release_Date'] = pd.to_datetime(album_df['Album_Release_Date'], format='%d/%m/%Y', errors='coerce').dt.strftime('%d/%m/%Y')


    return album_df


def tracks():
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    # now we'll be generating track

    # track.title = 50000 rows

    # This will have 
    ##  8 letters with no spaces (5000)
    ##  5 letters with no spaces (5000)
    track_title_8_letters_no_spaces = generate_alphabetical_data([8], 5000)
    track_title_5_letters_no_spaces = generate_alphabetical_data([5], 5000)


    ##  12, 4 letters with one space (10000)
    ##  5, 7 letters with one space (10000)
    track_title_12_4_letters_one_space = generate_alphabetical_data([12, 4], 10000)
    track_title_5_7_letters_one_space = generate_alphabetical_data([5, 7], 10000)

    ##  3, 5, 4 letters with 2 spaces (10000)
    ##  5, 7, 6 letters with 2 spaces (10000)
    track_title_3_5_4_letters_two_spaces = generate_alphabetical_data([3, 5, 4], 10000)
    track_title_5_7_6_letters_two_spaces = generate_alphabetical_data([5, 7, 6], 10000)


    track_titles = track_title_8_letters_no_spaces + \
                    track_title_5_letters_no_spaces + \
                    track_title_12_4_letters_one_space + \
                    track_title_5_7_letters_one_space + \
                    track_title_3_5_4_letters_two_spaces + \
                    track_title_5_7_6_letters_two_spaces

    #track.duration 

    #generally ranges from 3 mins and random seconds
    track_duration = generate_time(50000, duration = True)

    #track.genre

    # track region = 50

    track_genre_with_6 = generate_alphabetical_data([6], 10)
    track_genre_6_and_4 = generate_alphabetical_data([6,4], 10)
    track_genre_with_4 = generate_alphabetical_data([4], 10)
    track_genre_3_7_and_3 = generate_alphabetical_data([3,7,3], 10)
    track_genre_with_8 = generate_alphabetical_data([8], 10)

    # track_genre_with_6 *= 1000
    # track_genre_6_and_4 *= 1000
    # track_genre_with_4 *= 1000
    # track_genre_3_7_and_3 *= 1000
    # track_genre_with_8 *= 1000

    track_genre = track_genre_with_6 + \
                    track_genre_6_and_4 + \
                    track_genre_with_4 + \
                    track_genre_3_7_and_3 + \
                    track_genre_with_8
    
    track_df = pd.DataFrame({
    "Track_Id" : [i+1 for i in range(50000)],
    "Track_Title" : track_titles,
    "Track_Duration" : track_duration,
    "Track_Genre" : np.random.choice(track_genre, 50000)})

    track_df['Track_Duration'] = pd.to_timedelta(track_df['Track_Duration'])
    track_df['Track_Duration_Minutes'] = track_df['Track_Duration'].dt.components['minutes']
    track_df['Track_Duration_Seconds'] = track_df['Track_Duration'].dt.components['seconds']

    # Drop the original timedelta column
    track_df.drop('Track_Duration', axis=1, inplace=True)

    return track_df


def artist():
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    # 500 artist

    artist_with_7_letters = generate_alphabetical_data([7], 110)
    artist_with_5_letters_with_1_space = generate_alphabetical_data([5,11], 110)
    artist_with_5_letters_with_2_spaces = generate_alphabetical_data([4,6,8], 110)
    artist_with_13_letters = generate_alphabetical_data([13], 110)
    artist_with_3 = generate_alphabetical_data([3], 60)



    artists_names = (
        artist_with_7_letters
        + artist_with_5_letters_with_1_space
        + artist_with_5_letters_with_2_spaces
        + artist_with_13_letters
        + artist_with_3
    )

    artist_df = pd.DataFrame({"Artist_Id":[i+1 for i in range(500)], "Artist_Name":artists_names})

    return artist_df


def user_playlist():
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    # user playlist

    # 10000 user playlist among 40000 users

    # user_playlist.title

    user_playlist_title_8 = generate_alphabetical_data([8], 2000)
    user_playlist_5_11 = generate_alphabetical_data([5,11], 2000)
    user_playlist_4_6_8 = generate_alphabetical_data([4,6,8], 2000)
    user_playlist_13 = generate_alphabetical_data([13], 2000)
    user_playlist_3 = generate_alphabetical_data([3], 2000)

    user_playlist = user_playlist_13 + user_playlist_3 + user_playlist_4_6_8 + user_playlist_5_11  + user_playlist_title_8

    user_playlist_public_private = np.random.choice(['public', 'private'], 10000)
    user_playlist_track_podcast = np.random.choice(['track', 'podcast'], 10000)

    user_playlist_df = pd.DataFrame({
            "User_Playlist_Id" : [i+1 for i in range(10000)],
            "Tite": user_playlist,
              "public/private":user_playlist_public_private,
               "track/podcast": user_playlist_track_podcast})
    
    return user_playlist_df


def podcast():
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    #  500 podcast title

    podcast_title_8 = generate_alphabetical_data([8], 100)
    podcast_title_15_11 = generate_alphabetical_data([15,11], 100)
    podcast_title_18_10_3 = generate_alphabetical_data([18,10,3], 100)
    podcast_title_6 = generate_alphabetical_data([6], 100)
    podcast_title_12 = generate_alphabetical_data([12], 100)

    podcast_title = podcast_title_8 + podcast_title_15_11 + podcast_title_18_10_3 + podcast_title_6 + podcast_title_12

    # Adjust the start and end dates for the podcast generation
    start_date = '2018-01-01'
    end_date = '2023-12-31'
    num_rows = 500

    # Generate the podcast data
    podcast_data = generate_podcast_data(num_rows, podcast_title, start_date, end_date)

    # Convert the podcast data to a DataFrame
    podcast_df = pd.DataFrame(podcast_data)
    podcast_df['Episode Date'] = pd.to_datetime(podcast_df['Episode Date'], format='%d/%m/%Y', errors='coerce').dt.strftime('%d/%m/%Y')
    return podcast_df


def premium_subscription_df():
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module
    # premium subscription
    ## 30000 premium subscriber
    ## out of 10000 which we'll give some cancels
    premium_subscription_table = generate_premium_subscription(10000, User())
    premium_subscription_table['Start Date'] = pd.to_datetime(premium_subscription_table['Start Date'], format='%d/%m/%Y', errors='coerce')
    premium_subscription_table['End Date'] = pd.to_datetime(premium_subscription_table['End Date'], format='%d/%m/%Y', errors='coerce')
    return premium_subscription_table



def transaction():
    np.random.seed(50)  # Set the seed for numpy random
    random.seed(50)  # Set the seed for the built-in random module

    # Generate the transaction dates and subscriber IDs
    transaction_dates, subscriber_ids = generate_transaction_dates(premium_subscription_df())

    # Create a new dataframe using payment_method, transaction_date, and subscriber ID
    transaction_data = pd.DataFrame({
        'Subscriber ID': subscriber_ids,
        'Payment Method': np.random.choice(['Credit Card', 'Debit Card', 'Paypal', 'Gift Card'], len(transaction_dates),
                                        p=[0.4, 0.4, 0.18, 0.02]),
        'Transaction Date': transaction_dates
    })
    transaction_data['Transaction Date'] = pd.to_datetime(transaction_data['Transaction Date'], format='%d/%m/%Y')
    return transaction_data



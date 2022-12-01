# Brenda Jonsson 11/18/2022
# Assignment 13

# Choice 2
# Create a Python program that uses a web API of your choice. The program should analyze and manipulate
# the data to create meaningful information for a user.

# This code is mainly based off of two things: a contemporary tutorial for using Python's "Tweepy" at:
# https://datascienceparichay.com/article/get-data-from-twitter-api-in-python-step-by-step-guide/
# ...and chapter 17 of the "Python Crash Course" textbook (with a huge number of other sources contributing ideas).

# Must install "tweepy" package
# Then import tweepy
import tweepy as tw

# your Twitter API key and API secret
my_api_key = "EsF5pBXubQXJfVfGE7IgelZnu"
my_api_secret = "MfbD7ITLMhMRm7fG87UUgEPWIrVubfs4P8XhtjkfBU0EF93QUc"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = {"'seven of nine'"}

# Get tweets from the API
num_tweets = 10
tweets = tw.Cursor(api.search_tweets,
                   q=search_query,
                   lang="en",
                   result_type="mixed").items(num_tweets) # Mixed mixes popularity with recency

# Extracting the data and formatting it in a more useful way.

# For bar chart
favorite_copy = []
text_copy = []
username_copy = []
url_copy = []
links = []

for tweet in tweets:

    # Grabs the actual tweet text
    text = tweet.text

    # the ID of the status
    id = tweet.id

    # fetching the status
    status = api.get_status(id)

    # fetching the favorite_count attribute
    favorite_count = status.favorite_count

    # fetching the username
    username = tweet.user.screen_name

    # fetching the URL and ascribing to links for graph
    url = "https://twitter.com/twitter/statuses/" + str(id)
    link = f"<a href='{url}'>{username}</a>"

    # Lists
    favorite_copy.append(favorite_count + 1)
    text_copy.append(text)
    username_copy.append(username)
    links.append(link)


# Visualizing Tweet popularity using Plotly
from plotly import offline
# A bar chart requires lists.
data = [{
    'type': 'bar',
    'x': links,
    'y': favorite_copy,
    'hovertext': text_copy,
    }]

my_layout = {
    'title': "Trending Tweets About Star Trek's Seven of Nine (Ordered Chronologically)",
    'xaxis': {"title": 'The most current and/or most liked tweets talking about Seven of Nine (click username to view original post on Twitter)'},
    'yaxis': {"title": 'Number of times the tweet was favorited (+1)'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="SevenOfNine.html")


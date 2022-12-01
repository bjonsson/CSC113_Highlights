# Brenda Jonsson 10/22/22
# Lab 6


# 8-5. Cities
print("Exercise 8-5: Cities")

# Write a function called "describe_city()" that accepts the name of a city and its country.
# The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter
# for the country a default value. Call your function for three different cities, at least one of
# which is not in the default country.

def describe_city(city, country = "Slovenia"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("Ljubljana")
describe_city("Beijing", "China")
describe_city("Berlin", "Germany")

print()


# 8-7. Album
print("Exercise 8-7: Album")

# Write a function called "make_album()" that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a dictionary
# containing these two pieces of information. Use the function to make three dictionaries
# representing different albums. Print each return value to show that the dictionaries are storing
# the album information correctly. Use "None" to add an optional parameter to "make_album()"
# that allows you to store the number of songs on an album. If the calling line includes a value
# for the number of songs, add that value to the album's dictionary. Make at least one new function
# call that includes the number of songs on an album."

# Dictionary has to go outside the scope of the functions in order to be used by both functions.

music_dictionary = {"beatles": {"artist": "The Beatles", "album": "Help", "songs": []},
                    "knife party": {"artist": "Knife Party", "album": "Internet Friends", "songs": []},
                    "bass": {"artist": "Charles Berthoud", "album": "Charles Berthoud: The New Age of Solo Bass",
                             "songs": []}}

# I list my two functions first--one for the main problem, one for the optional parameter.
def make_album(artist_name, album_title, song = ''):

    for artist, specifics in music_dictionary.items(): #Accessing "beatles" first as a string, and then artist/album as a dictionary.

        if song: #This first if statement is vital to the functioning of this program.
            if artist_name in specifics.values():
                music_dictionary[str(artist)]["songs"].append(song)
                music_dictionary[artist]["num songs"] = len(music_dictionary[artist]["songs"])

        if artist_name in specifics.values():
            print(specifics.items())

        elif album_title in specifics.values():
            print(specifics.items())

def get_song_num(artist_name, album_title):
    for artist, specifics in music_dictionary.items():
        if artist_name in specifics.values():
            print(music_dictionary[artist]["num songs"])


# Here I make my function calls.

# First function call for the dictionaries of each album. You have the option to add a song.
make_album("The Beatles", "Help", "Yesterday")
make_album("The Beatles", "Help", "It's Only Love")
print() #New lines to make the results look neater in the console.
make_album("Knife Party", "Internet Friends")
print()
make_album("Charles Berthoud", "Charles Berthoud: The New Age of Solo Bass", "Tapping Into the Universe")

# Second function call for the number of songs on an album.
print()
get_song_num("The Beatles", "Help")

print()


# 8-8. User Albums
print("Exercise 8-8: User Albums")

# Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album's
# artist and title. Once you have that information, call "make_album()" with the user's input and
# print the dictionary that's created. Be sure to include a quit value in the while loop.

music_dictionary = {"beatles": {"artist": "The Beatles", "album": "Help", "songs": []},
                    "knife party": {"artist": "Knife Party", "album": "Internet Friends", "songs": []},
                    "bass": {"artist": "Charles Berthoud", "album": "Charles Berthoud: The New Age of Solo Bass",
                             "songs": []}}

# Here's what I need from the old program.
def make_album(artist_name, album_title, song = ''):

    for artist, specifics in music_dictionary.items(): #Accessing "beatles" first as a string, and then artist/album as a dictionary.

        if song: #This first if statement is vital to the functioning of this program.
            if artist_name in specifics.values():
                music_dictionary[str(artist)]["songs"].append(song)
                music_dictionary[artist]["num songs"] = len(music_dictionary[artist]["songs"])

        if artist_name in specifics.values():
            print(specifics.items())

        elif album_title in specifics.values():
            print(specifics.items())

# Here's my new program with the while loop. It brings up a dictionary for an album.
flag = True
while flag == True:

    artist_name = input("Enter an artist's name. ")
    album_title = input("Enter their album title. Press 'q' to quit. ")

    if artist_name == "q" or album_title == "q":
        flag = False
        break

    for artist, specifics in music_dictionary.items():
        if artist_name in specifics.values() and album_title in specifics.values():
            make_album(artist_name, album_title)
            break #The break is important. The else statement runs without it.
        else:
            print("We don't have a dictionary for that item.")
            break

print()


# 8-9. Messages
print("Exercise 8-9: Messages")

# Make a list containing a series of short text messages. Pass the list to a function
# called "show_messages()" which prints each text message.

# Messages from my phone
texts = ["You have 1 new library item(s) for pickup.", "928347 is your Amazon OTP. Do not share it with anyone.",
         "Payment Confirmation 2837238 for $219.34 paid.", "You just earned 2 Points at Third Shot Coffee!",
         "Bank notification for account ending in 58.", "It's time to refill SOD FLUORIDE PST.",
         "Your pet's next appointment is scheduled for 4:00 p.m. on 10/2/2022."]

def show_messages(to_print):
    for each in to_print:
        print(each)

show_messages(texts)

print()

# 8-10. Sending Messages
print("Exercise 8-10: Sending Messages")

# Start with a copy of your program from Exercise 8-9. Call the function "send_messages()"
# with a copy of the list of messages. After calling the function, print both of your lists
# to show that the original list has retained its messages.

# Messages from my phone
texts = ["You have 1 new library item(s) for pickup.", "928347 is your Amazon OTP. Do not share it with anyone.",
         "Payment Confirmation 2837238 for $219.34 paid.", "You just earned 2 Points at Third Shot Coffee!",
         "Bank notification for account ending in 58.", "It's time to refill SOD FLUORIDE PST.",
         "Your pet's next appointment is scheduled for 4:00 p.m. on 10/2/2022."]

def send_messages(to_print):
    for each in to_print:
        test = each.upper()
        print(test)

copied_list = texts[:]

# Calling function with copied list
send_messages(copied_list)

print()

# Proving that neither list is changed
print(texts)
print(copied_list)
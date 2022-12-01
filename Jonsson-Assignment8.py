# Brenda Jonsson 11/5/22
# Assignment 8

# Write a Python program that asks the user for his or her name, and then asks the user to enter
# a sentence that describes himself or herself.

# Ask a few more questions of your own to use as content for the tags below.
# •	html
# •	body
# •	h1, h2, h3
# •	p
# •	A link - <a href…
# •	ol, li
# •	any other tags you would like to try

# Once the user has entered the requested input, the program should create an HTML file, containing
# the input, for a simple Web page. Remember an HTML file has an extension of .html  (Example: “myProgram.html”).

# Make sure your program also includes:
# •	Exception handling (you decide what to check)
# •	Functions – remember all programs must at least have a main function.






# Start of program.

# Getting inputs.
#
# I didn't put these into a function, because I needed the variables to be global,
# and I heard that it's bad programming practice to declare global variables. Also, it would make the
# program longer to declare them outside of a function and then get the values through a function.

# Lots of functions would be a really, really good idea if I was gatekeeping the content (trying to
# make sure it is a certain way, like .char-char-char for the website, or 9 digits for the phone number,
# or a minimum of 3 words per sentence).

name = input("What is your name? ")

first_sentence = input("Write a sentence about what you do for work or school. ")

second_sentence = input("Write a sentence about your personal hobbies. ")

list_0 = input("What is something you want for yourself in five years? ")
list_1 = input("What is another thing you want for yourself in five years? ")
list_2 = input("What is one last thing you want for yourself in five years? ")

future = [list_0, list_1, list_2]

website = str(input("What is your website? (Do not include https://)" ))

flag = True
while flag == True:
    try:
        phone = int(input("What is your phone number? Format: xxxxxxxxxx "))
    except ValueError:
        print("Enter numbers only!")
    else:
        flag = False
        break


# This chunk also doesn't belong in a function, because it will return 'None.'
custom_string = f"""
    <html>
    <body>
    
    <h1>Who am I?</h1>
    
    {first_sentence}
    
    <p>
    
    {second_sentence}
    
    <h2>Three things I want 5 years from now.</h2>
    <ol>
        <li>{future[0]}</li>
        <li>{future[1]}</li>
        <li>{future[2]}</li>
    </ol>
    
    <h3>My website</h3>
    You can see my work <a href="https://{website}">here</a>.
    
    <h3>Call me</h3>
    My phone number is {phone}.
    
    </body>
    </html>
    """


# This is actually a nice place for a function. I would prefer to call it something else, but
# I know Debbie has decades of experience at prestigious coding organizations.
def main(custom_string):

    filename = f"about{name}.html"

    with open(filename, 'w') as f:
        f.write(custom_string)



# Calling the function
main(custom_string)
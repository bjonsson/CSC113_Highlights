# Brenda Jonsson 10/12/22
# Assignment 3

# Choice 1 - Troubleshooting Car Issues
print("Troubleshooting Car Issues")

# Declaring variables:
first_branch = None
second_branch_y = None
second_branch_n = None
third_branch = None
fourth_branch = None
fifth_branch = None

flag1 = True
flag2 = True
flag3 = True
flag4 = True
flag5 = True

#Code begins.
#The flags return people to the question when they enter something other than a properly formatted answer.

while flag1 == True:
    first_branch = input("Is the car silent when you turn the key? Enter y or n. ")

    if first_branch == 'y':
        flag1 = False
        while flag2 == True:
            second_branch_y = input("Are the battery terminals corroded? Enter y or n. ")

            if second_branch_y == 'y':
                    print("Clean terminals and try starting again.")
                    flag2 = False

            if second_branch_y == 'n':
                    print("Replace cables and try again.")
                    flag2 = False

    if first_branch == 'n':
        flag1 = False
        while flag2 == True:
            second_branch_n = input("Does the car make a clicking noise? Enter y or n. ")

            if second_branch_n == 'y':
                print("Replace the battery.")
                flag2 = False

            if second_branch_n == 'n':
                flag2 = False
                while flag3 == True:
                    third_branch = input("Does the car crank up but fail to start? Enter y or n. ")

                    if third_branch == 'y':
                        print("Check spark plug connections.")
                        flag3 = False

                    if third_branch == 'n':
                        flag3 = False
                        while flag4 == True:
                            fourth_branch = input("Does the engine start and then die? Enter y or n. ")

                            if fourth_branch == 'y':
                                flag4 = False
                                while flag5 == True:
                                    fifth_branch = input("Does your car have fuel injection? Enter y or n. ")

                                    if fifth_branch == 'y':
                                        print("Get it in for service.")
                                        flag5 = False

                                    if fifth_branch == 'n':
                                        print("Check to ensure the choke is opening and closing.")
                                        flag5 = False

                            if fourth_branch == 'n':
                                print("Your problem is too complex for this program.")
                                flag4 = False
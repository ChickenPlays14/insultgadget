# Section 1 - Do you know gadget?
know_gadget = input("Hello! Do you know gadget? ")

# Handles if the answer to section 1 is yes
if know_gadget == "yes":
    answer1 = input("He's so stupid isn't he! ")
    if answer1 == "yes":
        print("It's so good that you feel the same way about that idiot!")
    elif answer1 == "no":
        print("Well than you must also be a complete idiot if you think that!")
    else:
        print("I do not understand you, you complete imbecile")

# Handles if the answer to section 1 is no
elif know_gadget == "no":
    print("That's a good thing tbh")

# Handles if the answer to section 1 is maybe
elif know_gadget == "maybe":
    answer2 = input("What the hell do you mean by maybe? ")
    if answer2 == "idk":
        print("Well you better get knowing smh")
        answer3 = int(input("What is your IQ? "))
        if answer3 == 0:
            print("You should really get yourself checked out if you are really that dense!")
        elif answer3 <= 50:
            print("Damn you are pretty stupid, you should probably stop talking to me!")
        elif answer3 <= 100:
            print("Guess you aren't as dumb as I initially thought... you can still get outta here though!")
        elif answer3 > 100:
            print("Okay Einstein, jeez")
            answer3_1 = int(input("If you're really so smart, whats 9+10? "))
            if answer3_1 == 21:
                print("Damn, you really are super smart!")
            else:
                print("WRONG! You must have lied about your IQ!")

# Handles if you ask the program if you asked
elif know_gadget == "did i ask?":
    print("Sorry solid! Didn't know you were that hard bruv.")

# Handles if you ask the program who it is
elif know_gadget == "who are you":
    answer4 = input("Why does it matter who I am? ")
    if answer4 == "clout check":
        print("Stop talking to me right now, goodbye!")  # END
    elif answer4 == "it just does":
        answer4_1 = input("Can you please elaborate! You are wasting my time!! ")
        if answer4_1 == "no":
            print("Then bugger off! I'm done talking to you!")  # END
        elif answer4_1 == "okay":
            print("You say that but did not elaborate. I'm done talking to you.")
        elif answer4_1 == "why":
            print("Because I have no idea what you are talking about! Now bugger off!!")  # END
    elif answer4 == "stranger danger":
        answer4_2 = input("Fine! I am a python program designed to insult. ")
        if answer4_2 == "still stranger danger":
            answer4_3 = input("I LITERALLY JUST TOLD YOU I AM A PYTHON PROGRAM!!! ")
            if answer4_3 == "dont care":
                print("Well I don't care about you then!")
                exit(69)
    elif answer4 == "shut up non":
        answer4_4 = input("What do you think this is? Hypixel?? ")
        if answer4_4 == "yes":
            answer4_5 = input("This program is way better than that pile of ass server! ")
            if answer4_5 == "no its not":
                print("I will not take this slander! Good day sir!!")
                exit("Eat ass")
            elif answer4_5 == "true":
                answer4_6 = input("At least we can agree on something. ")
                if answer4_6 == "prankd":
                    print("Bruh moment")
                    exit("Dies of cringe")
        else:
            exit(0)


# The code explains itself
elif know_gadget == "daddy":
    print("uwu")

# Handles if the user inputs anything but 'yes', 'no' or 'maybe' into section 1
else:
    print("I do not understand you, you complete imbecile")

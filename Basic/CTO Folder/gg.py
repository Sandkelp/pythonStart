word = input("Enter your tweet to see if you are under the char limit: ")
gtr = len(word)
if gtr < 280:
    print("Your tweet is good to go!")
else:
    print("Try getting rid of some words.")


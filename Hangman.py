import random

wordpool = ["welcome","fantasy","noodles","aadvark","unlikely","mississippi"]

#This is a comment

def selectword():

    return wordpool[random.randint(0,5)]

def getemptylist(n):

    my_list = []
    for _ in range(n):
        my_list.append('')
    return my_list
   
def checkposition(letter):
    # Check the position of the guessed letter in word
    for i in range(len(gameletters)):
        if letter == gameletters[i]:
            guessletters[i] = letter


gameletters = list(selectword())
print (gameletters)

guessletters = getemptylist(len(gameletters))
print(guessletters)

while gameletters != guessletters:
    guess = input("Guess a letter: ")
    checkposition(guess)
    print(guessletters)

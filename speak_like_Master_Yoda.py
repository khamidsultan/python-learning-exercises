# Task:
# Master Yoda speaks a sentence in a different order. 
# Let's say you want to convert a sentence to Yoda’s speech.  
# Write a function named master_yoda which will take a string as input and return the output after reversing the words of the sentence.


def master_yoda(sentence):
    ''' This function makes reverse of your sentence'''
  
    sentence=input("Input your sentence: ")
    words = sentence.split()

    # Reverse the list of words
    words.reverse()

    # Join the reversed words back into a sentence
    return print(' '.join(words))

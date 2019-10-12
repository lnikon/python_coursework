
import random

def generate_radom_data():
    ## No need to modify this function.
    ## It will generate random_words.txt 
    print("Genreating Random Data")
    origin = open('words.txt','r')
    res = open('random_words.txt','w')

    words = origin.read().split("\n")
    for i in range(random.randrange(1000,2000):
        temp = random.choice(words)
        res.write(temp+'\n')


def get_data():
    ### TBD
    ### This function should get the data from text. 
    ### Modify the funciton and return the data.

    file_hndl = open('random_words.txt','r')
    array = file_hndl.readlines()  # this will read all the data as array of strings. Each line as a seperate string
    #array = file_hndl.read()  #this will read entire text as one string

    ########################
    ##  add your code here
    ########################

def get_max_val(arg1):
    ### TBD
    ### This function should get the word that apears most and also tell how many times that word apears. 
    ### Modify the funciton and return the data.

	

### This is the code that runs. 
### You need to make this work.

print("Calling Generate data function")
generate_radom_data()
print("Done Generating data. random_words.txt generated")

print(" Getting data from random_words.txt")
data = get_data()
print(" Data is ready")

print("Getting most common word")
get_max_val(data)
print("Done")


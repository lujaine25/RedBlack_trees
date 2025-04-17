
import os
from RedBlackTree import RedBlackTree


def load_dictionary(rbt,filename):
    if not os.path.exists(filename):
        print("Dictionary file not found!")
        return
    with open(filename, 'r') as file:
        for line in file:
            word= line.strip() #removes spaces and /n
            if word:    #if line isnt empty, insert
                rbt.insert(word)

    
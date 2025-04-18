
import os
from RedBlackTree import RedBlackTree


def insert_word(rbt, word, filename):
    if rbt.searchTree(word).item == word:    #checking if word exists
        print("Word already exists in the dictionary!")
        return
    rbt.insert(word)
    print(f'Word "{word}" inserted successfully')
    with open(filename, 'a') as f:
        f.write(word+'\n')
    print("Dictionary Size:", rbt.tree_size() , " words")
    rbt.print_height()
    print("Black Height:", rbt.get_black_height())

                

     

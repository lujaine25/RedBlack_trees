
from RedBlackTree import RedBlackTree
from Load_dictionary import load_dictionary

def main():
 
 dictionary_rbt = RedBlackTree()
 filename='dictionary.txt'
 load_dictionary(dictionary_rbt,filename)

 print("tree size:", dictionary_rbt.tree_size()) 
if __name__ == "__main__":
    main() 


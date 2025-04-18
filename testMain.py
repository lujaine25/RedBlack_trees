
from RedBlackTree import RedBlackTree
from Load_dictionary import load_dictionary

def main():
 
 dictionary_rbt = RedBlackTree()
 filename='Dictionary.txt'
 load_dictionary(dictionary_rbt,filename)

 print("1- Search for a word")
 print("2- Insert a word")
 print("3- Print tree height")
 print("4- Print tree size")
 print("5- Print black height")

 while True:
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        word = input("Enter a word to search: ")
        dictionary_rbt.lookup(word)

    elif choice == '2':
        word = input("Enter a word to insert: ")
        dictionary_rbt.insert(word)
        print(f"{word} has been inserted into the dictionary.")

    elif choice == '3':
        print("Tree height:", dictionary_rbt.get_height(dictionary_rbt.root))

    elif choice == '4':
        print("Tree size:", dictionary_rbt.tree_size())

    elif choice == '5':
        print("Black height:", dictionary_rbt.get_black_height())

    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main() 
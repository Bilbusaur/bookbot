


def main():
    try:
     #opens and reads file, counts and displays words in the documents. 
        with open("books/frankenstein.txt") as f:
            filepath = "books/frankenstein.txt"
            file_contents = f.read()
            print(f"--- Book Report of {filepath} ---")
            print(f"{len(file_contents.split())} words found in the document")
            print(" ")
            return file_contents

    except FileNotFoundError:
        print("This file could not be found. Please check the path and try again. ")

#Counts the letters only if alphabetic. 
def count_characters(character_counts):
    characters_dict = {}
    for letter in character_counts.lower():
        if letter.isalpha():
            if letter in characters_dict:
                characters_dict[letter] += 1
            
            else:
                characters_dict[letter] = 1
    return characters_dict


def display_letters(letter_counts):
        #sort the dictionary by keys.
        sorted_letters = sorted(letter_counts.items())
        for letter, count in sorted_letters:# Grabs key,value from the dictionary.
            print(f"The character '{letter}' appears {count} times.")
    

#Executes only on call, helps with imports I think.
if __name__ == "__main__":
    #calls open and read function.
    contents = main() #defines the document to work with.
    if contents:#Only runs if there is content.
        character_counts = count_characters(contents)
        diction = count_characters(contents)# The dictionary returned from the count function
        display = display_letters(diction)
        
    
    
    
    

 

    



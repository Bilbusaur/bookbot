


def main():
    try:
      
        with open("books/frankenstein.txt") as f:
            filepath = "books/frankenstein.txt"
            file_contents = f.read()
            print(f"--- Book Report of {filepath} ---")
            print(f"{len(file_contents.split())} words found in the document")
            print(" ")
            return file_contents

    except FileNotFoundError:
        print("This file could not be found. Please check the path and try again. ")


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
        for letter, count in sorted_letters:
            print(f"The character '{letter}' appears {count} times.")
    


if __name__ == "__main__":

    contents = main()
    if contents:
        character_counts = count_characters(contents)
        diction = count_characters(contents)
        display = display_letters(diction)
        
    
    
    
    

 

    



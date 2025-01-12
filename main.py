def main():
    try:
        
        


        with open("books/frankenstein.txt") as f:
            content = []
            file_contents = f.read()
            content.append(file_contents)
            content.split()
            print(type(content))
            


            

                
            


            return file_contents
    except FileNotFoundError:
        print("This file could not be found. Please check the path and try again. ")

        
        
if __name__ == "__main__":
    main()

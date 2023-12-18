"""A simple English to Pig Latin translator"""

def main():
    """User enters string and translator converts it to pig latin and prints to screen."""
    while True:
        input_string = input("\nEnter English to translate to Pig Latin: ").split()    
        translator(input_string)
        another_loop = input("\nWould you like to try another? (y/n): ")
        if another_loop.lower() == 'n':
            break


def translator(entered_input):
    """Recieves input from user and converts to pig latin"""
    vowles = ['a', 'e', 'i', 'o', 'u']
    return_string = ""
    for word in entered_input:
        if word[0] in vowles:
            word = word + 'way '
        else:
            word = word[1:] + word[0] + 'ay '
        return_string += word.lower()  
    print(f"\n\n{return_string.capitalize()}")

if __name__ == "__main__":
    main()
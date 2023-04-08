import random

#Wilson Xu, 4/7/23
'''
Now you are going to write an "encoder / decoder" program that makes use of your six cryptographic functions. Begin by writing a program that continually asks the user to enter in an encoding pattern and a word to encode. The user should also be able to end the program using a sentinel value.

If the user chooses to encode a word you should do the following:

Ask the user for an "encoding pattern" string. This string will contain instructions on how to encode / decode a string. The valid commands that this string can contain are the following (case insensitive - either upper or lowercase letters should be accepted):
'A' = add 1 random character after each character (i.e. cat -> cZaZtZ)
'X' = delete 1 character after each character (i.e. cZaZtZ -> cat)
'F' = flip the string
'U' = ASCII shift all characters by +1
'D' = ASCII shift all characters by -1
'L' = Shift all characters to the left by 1
'R' = Shift all characters to the right by 1
Next, ask them to enter in a phrase that they want to encode. Convert this all alphabetic characters in this string to uppercase.
Finally, apply the desired encoding pattern to their string, giving them feedback during the process. Apply the pattern one operation at a time, from left to right. Any invalid or unrecognized commands should be ignored and reported to the user.
Hint: use your functions!
The sentinel value should be case insensitive (i.e. any case variation of 'end' should be accepted)
'''

#function1
def ascii_shift(word, direction):
    shifted_word = ""
    for char in word:
        if char.isupper():
            if direction == "up":
                shifted_word += chr(((ord(char) - 65 + 1) % 26) + 65)
            elif direction == "down":
                shifted_word += chr(((ord(char) - 65 - 1) % 26) + 65)
            else:
                return word
        else:
            shifted_word += char
    return shifted_word

#function2
def shift_right(word):
    return word[-1:] + word[:-1]

#function3
def shift_left(word):
    return word[1:] + word[:1]

#function4
def flip(word):
    mid = len(word) // 2
    if len(word) % 2 == 0:
        return word[mid:] + word[:mid]
    else:
        return word[mid + 1:] + word[mid] + word[:mid]

#function5 needs import random
def add_letters(word, num):
    result = ""
    for char in word:
        result += char
        for _ in range(num):
            result += chr(random.randint(65, 90))
    return result

#function6
def delete_characters(word, num):
    result = ""
    i = 0
    while i < len(word):
        result += word[i]
        i += num + 1
    return result

#Main Function for part 2b
def main():
    while True:
        pattern = input("Enter an encoding pattern, 'end' to end: ")
        if pattern.lower() == "end":
            break

        word = input("Enter a word to encode/decode: ").upper()

        for command in pattern.upper():
            if command == "A":
                word = add_letters(word, 1)
                print("* Adding 1 letter between all characters:", word)
            elif command == "X":
                word = delete_characters(word, 1)
                print("* Deleting 1 character after each character:", word)
            elif command == "F":
                word = flip(word)
                print("* Flipping:", word)
            elif command == "U":
                word = ascii_shift(word, "up")
                print("* ASCII shifting up:", word)
            elif command == "D":
                word = ascii_shift(word, "down")
                print("* ASCII shifting down:", word)
            elif command == "L":
                word = shift_left(word)
                print("* Shifting left:", word)
            elif command == "R":
                word = shift_right(word)
                print("* Shifting right:", word)
            else:
                print(f"{command}", "is an invalid command, ignoring ")

        print("Final encoding / decoding:", word)

if __name__ == "__main__":
    main()

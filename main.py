char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char_dict = {}
total_words = 0
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    split_contents = file_contents.split()
    total_words = len(split_contents)
    
    for word in split_contents:
        for character in word:
            char = character.lower()
            if char in char_dict and char in char_list:
                char_dict[char] += 1
            elif char in char_list:
                char_dict[char] = 1

print(f"{total_words} words were found in the document")
for letter in char_dict:
    print(f"The '{letter}' character was found {char_dict[letter]}  ")

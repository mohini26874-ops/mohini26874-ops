# Q1. Write a Python program to count the number of characters
# (character frequency) in a string.

string = "google.com"
frequency = {}

for character in string:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print(frequency)


# Q2. Write a Python program to get a string made of the first 2
# and last 2 characters of a given string.
# If the string length is less than 2, return the empty string.

string = input("Enter a string: ")

if len(string) < 2:
    print("Empty String")
else:
    print(string[:2] + string[-2:])


# Q3. Write a Python program to get a single string from two given
# strings, separated by a space and swap the first two characters
# of each string.

string1 = "abc"
string2 = "xyz"

new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]

print(new_string1 + " " + new_string2)
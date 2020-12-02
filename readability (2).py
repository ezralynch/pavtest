"""
 * readability.py
 *
 * Introductie Programmeren
 * Ezra Lynch
 *
 * - counts the letters, words and sentences in a body of text
 * - calculates the Coleman-Liau index
"""

from cs50 import get_string

# words start at 1 because the last word isn't counted
text = get_string("Text? ")
letters = 0
words = 1
sentences = 0

# every character in the string given by the user is checked
for c in text:
    # if a character in a string is a alphabetic character a letter is added
    if c.isalpha():
        letters = letters + 1
    # if there's a space another word is added
    elif c == " ":
        words = words + 1
    # if a sentence ends another sentence is added
    elif c == "?" or c == "!" or c == ".":
        sentences = sentences + 1

# calculations for the Coleman-Liau index
l = letters * (100 / words)
s = sentences * (100 / words)
grade = 0.0588 * l - 0.296 * s - 15.8
# the Coleman-Liau index is rounded
roundedgrade = round(grade)

if roundedgrade >= 16:
    print("Grade: 16+")
elif roundedgrade < 2:
    print("Before Grade 1")
else:
    print(f"Grade: {roundedgrade}")

#toevoeging!
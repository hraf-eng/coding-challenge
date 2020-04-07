# 3. Check words with typos:
# There are three types of typos that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to
# check if they are one typo (or zero typos) away.
# Examples:
# pale, ple ­> true
# pales, pale ­> true
# pale, bale ­> true
# pale, bake ­> false

# Function for building a dictionary with the count for each letter in word
def get_letter_count(word):
    letter_count = dict()
    for letter in word:
        # If dictionary has letter, increase count
        if letter_count.get(letter):
            letter_count[letter] += 1
        else: # If not, start count
            letter_count[letter] = 1
    return letter_count

def is_typo(word1, word2):
    letter_count1 = get_letter_count(word1)
    letter_count2 = get_letter_count(word2)

    size1 = len(word1)
    matching_letters = 0

    # Check each letter present on first word
    for key in letter_count1.keys():
        # Verify if it is present on the second dictionary
        if letter_count2.get(key):
            # Increment matching letter count
            matching_letters += 1

    # Calculate the difference in matching letters
    difference = abs(size1 - matching_letters)
    return difference <= 1

print("pale, ple ->", is_typo("pale", "ple"))
print("pales, pale ->", is_typo("pales", "pale"))
print("pale, bale ->", is_typo("pale", "bale"))
print("pale, bake ->", is_typo("pale", "bake"))

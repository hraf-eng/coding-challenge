# 2. Check words with jumbled letters :
# Our brain can read texts even if letters are jumbled, like the following sentence:  “Yuo
# cna porbalby raed tihs esaliy desptie teh msispeillgns.” Given two strings, write a
# method to decide if one is a partial­permutation of the other. Consider a
# partial­permutation only if:
# ­ The first letter hasn’t changed place
# ­ If word has more than 3 letters, up to 2/3 of the letters have changed place
# Examples:
# you, yuo ­> true
# probably, porbalby ­> true
# despite, desptie ­> true
# moon, nmoo ­> false
# misspellings, mpeissngslli ­> false

def is_partial_permutation(str1, str2):
    # Check if the first letter hasn’t changed place
    if str1[0] != str2[0]:
        return False

    size1 = len(str1)
    size2 = len(str2)

    #  Check if word has more than 3 letters
    if size1 > 3:
        shared_letters = 0

        # Count shared letters
        for i in range(min(size1, size2)):
            if str1[i] == str2[i]:
                shared_letters += 1
        
        # Calculate changed letters
        changed_letters = size1 - shared_letters

        # Check is percentage is under 66%
        return changed_letters/size1 < 0.66
    else:
        return True

print("you, yuo -> ", is_partial_permutation("you", "yuo"))
print("probably, porbalby -> ", is_partial_permutation("probably", "porbalby"))
print("despite, desptie -> ", is_partial_permutation("despite", "desptie"))
print("moon, nmoo -> ", is_partial_permutation("moon", "nmoo"))
print("misspellings, mpeissngslli -> ", is_partial_permutation("misspellings", "mpeissngslli"))
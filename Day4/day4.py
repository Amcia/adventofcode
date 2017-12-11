"""
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
"""

# Return each line from the file
def line_by_line(file_name):
    with open(file_name) as fp:
        for line in fp:
            yield line.rstrip()     # Remove last character from the line (\n)


def passphrase_check(file_name):
    for line in line_by_line(file_name):
        words = line.split(' ')     # Split the line to list of the words
        if len(words) == len(set(words)):       # Set() stores only unique values
            yield 1
        else:
            yield 0


"""
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?
"""


def passphrase_check_2(file_name):
    count = 0
    for num, line in enumerate(line_by_line(file_name)):
        is_end = False
        words = line.split(' ')     # Split the line to list of the words
        words_sorted = sorted(words, key=len)
        # Debugging line
        # print(words_sorted)
        for i, word in enumerate(words_sorted):
            # If we are checking the last word, passphrase is good, there are no matched words
            if i+1 == len(words_sorted):
                # Debugging line
                # print('count+1\tword: {}'.format(word))
                count += 1
                break
            else:
                for z in range(i+1, len(words_sorted)):
                    if len(word) == len(words_sorted[z]):
                        # If combination of all letters from two words are matched (passphrase is wrong)
                        # Just sort all letters in the word and compare it with the next sorted one
                        if sorted(tab_char_1 for
                                  tab_char_1 in word) == sorted(tab_char_2 for tab_char_2 in words_sorted[z]):
                            # Debugging line
                            # print('{} == {}\t|\titer: {} --- count: {}'.format(word, words_sorted[z], num+1, count))
                            is_end = True
                            break
                    else:
                        break
                if is_end:
                    break
    return count


if __name__ == '__main__':
    print(sum(i for i in passphrase_check('input')))
    print(passphrase_check_2('input'))




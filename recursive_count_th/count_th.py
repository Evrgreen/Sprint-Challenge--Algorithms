'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # TBC
    num = 1 if word[0:2] == "th" else 0
    if len(word) < 2:
        return 0
    return num+count_th(word[1:])


print(count_th("abcthefthghiththhthhth"))

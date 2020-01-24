'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

    #Check if first two letters are th
    #If so, count += 1
    #re-run count_th for word[1:]
    # TBC

def count_th(word):
    count = 0
    if len(word) < 2:
        return 0
    if word[0:1] == 'th':
        count +=1
    return count_th(word[1:])

print(count_th("IBIKIththibikithth"))
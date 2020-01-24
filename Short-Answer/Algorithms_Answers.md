#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n) - same ammount of calculations regardless of what N is, just increased by the time it takes to multiply bigger numbers

A linear algorithm – O(n)
Runtime grows directly in proportion to n.

b)

O(nlogn) - as n increases, the runtime has to increase as well

A superlinear algorithm – O(nlogn)
Runtime grows in proportion to n.


c)

O(n) - Regardless of n number of bunnies, the function runs subtracting the two ears per each bunnie once

A linear algorithm – O(n)
Runtime grows directly in proportion to n.




## Exercise II


Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


You would go half way up, drop egg, if it breaks, move half way down, if lives, move half way up, untill you hit the sweet spot. 

It would be O(Log n) since its essentially a binary search for the right height.

aka :

    binary search(floorArr, breakFloor):
    low = 0, high = len(floorArr) -1
    mid = (high-low)//2

    if breakFloor == floorArr[mid]:
        Return mid
    elif breakFloor < floorArr[mid]:
        return search(floorArr[:mid])
    else:
        return search(floorArr[mid:])
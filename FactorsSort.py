'''
You are given an array A of N elements. Sort the given array in increasing order of number of distinct factors of each element, i.e., element having the least number of factors should be the first to be displayed and the number having highest number of factors should be the last one. If 2 elements have same number of factors, then number with less value should come first.

Note: You cannot use any extra space

Input 1:
A = [6, 8, 9]
Input 2:
A = [2, 4, 7]


Output 1:
[9, 6, 8]
Output 2:
[2, 7, 4]
'''

def numberOfFactors(number):
    factors, i = 1, 2

    while i * i <= number:
        if number % i == 0:
            if i < number // i:
                factors += 2
            else:
                factors += 1
        i += 1
    return factors


def factorsSort(array):
    array.sort(key=lambda x: (numberOfFactors(x), x))
    return array


array = list(map(int, input().strip().split()))
print(factorsSort(array))
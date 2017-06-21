def bad_fibonaci(n):
    """ This is bad version of calculating fibonaci array
        Because the number of call recursive function is 
        exponential of n.
        """
    if n <= 1:
        return 1
    else:
        return bad_fibonaci(n - 1) + bad_fibonaci(n - 2)
        
        
def good_fibonaci(n):
    """ This is better version of calculating fibonaci array
        Because for each call to function only generate one
        next call
    """
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonaci(n -1)
        return (a + b, a)
        

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
        
def binary_search(data, target, low, high):
    """This is a version of binary search --> tail recursion"""
    if low > high:
        return False
    else:
        mid = (low + high) / 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
            
def binary_search_iterative(data, target):
    """This is a change from recursion to non-recursion by using iterative"""
    low = 0
    high = len(data) - 1
    
    while (low <= high):
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            low =  + 1
        else:
            high = mid - 1
    return False


def reserve_array(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reserve_array(S, start + 1, stop - 1)
        
def reserve_array_iterative(S):
    start = 0
    stop = len(S)
    
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start, stop = start + 1, stop - 1
        
def power(x, n):
    if n == 0:
        return 1
    
    partial = power(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
        result *=x
    return result

def binary_sum(S, start, stop):
    if start == stop - 1:
        return S[start]
    elif start >= stop:
        return 0
    else: 
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
        

def find_min_max(S, index):
    """Find minimum and maximum of array by recursive"""
    if index == (len(S) - 1) :
        return (S[index], S[index])
        
    minimum, maximum = find_min_max(S, index + 1) 
    
    if minimum > S[index]:
        if maximum < S[index]:
            return (S[index], S[index])
        else:
            return (S[index], maximum)
    else:
        if maximum < S[index]:
            return (minimum, S[index])
        else:
            return (minimum, maximum)
        
def find_uniqueness(S):
    """Check array has or not an unique element"""
    if len(S) == 1:
        return True
        
    first_element = S[0]
    remaining = S[1:]
    isUnique = first_element not in remaining
    recur_unique = find_uniqueness(S[1:])
    
    return isUnique and recur_unique
    
def product(a, b):
    if b == 0:
        return 0
    
    result = 0
    result = a + product(a, b - 1)
    return result
    


def list_subset(S):
    if S == []:
        return [[]]
    
    x = list_subset(S[1:])
    return x + [[S[0]] + y for y in x]
        
def check_palindrome(S):
    if len(S) == 2:
        return S[0] == S[1]
    elif len(S) == 1:
        return True
     
    if (S[0] == S[len(S) - 1]):
        return check_palindrome(S[1:(len(S)-1)])

    return False


def vowelvsconsonant(S):
    if not S:
        return 0, 0
        
    vowels, consonants = vowelvsconsonant(S[1:])
    
    if S[0] in "aeiouAEIOU":
        vowels +=1
    else:
        consonants += 1
    return vowels, consonants
    
def rearrange_array(S, start):
    if start == len(S) - 1:
        return S
    
    if (S[start] % 2 == 1):
        nextEven = start + 1
        while S[nextEven] % 2 == 1 and nextEven < len(S) - 1:
            nextEven += 1
        S[start], S[nextEven] = S[nextEven], S[start]
    
    rearrange_array(S, start + 1)
    
    return S
    
def rearrange_k(S, k, start):
    if start == len(S) - 1:
        return S
        
    if S[start] > k:
        nextIndex = start + 1
        while S[nextIndex] > k and nextIndex < len(S) - 1:
            nextIndex += 1
        S[start], S[nextIndex] = S[nextIndex], S[start]
        
        rearrange_k(S, k, start + 1)
    
    return S
    
import os
def list_file(p, filename):
    for file in os.listdir(p):
        if file.find(filename) != -1:
            print file
        
        if os.path.isdir(os.path.join(p, file)):
            list_file(os.path.join(p, file), filename)
    


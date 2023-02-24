from collections import Counter

def arrays_similar(arr1, arr2):
    return Counter(arr1) == Counter(arr2)
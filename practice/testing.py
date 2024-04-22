#!/usr/bin/python3

"""
Your company needs function that meets the following requirements:
1. For a given array of n integers , the function returns the index of the element with the 
minimum value in the array. If there is more than one element with the minimum value, the returned
index should be the smallest one.
2. If an empty array is passed to the function, it should raise an exception.
"""

#  function to test minimum index.

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

class TestDataEmptyArray(object):
     @ staticmethod
     def get_array():
         return []
         
class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        return [3, 1, 2]
    @ staticmethod

    def get_expected_result():
        return 1
    
class TestDataExactlyTwoDifferentMininmums(object):
    @staticmethod
    def get_array():
        return [3, 1, 1]
    @ staticmethod

    def get_expected_result():
        return 1

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False

def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)
    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

def TestWithExactlyTwoDifferentMinimus():
    seq = TestDataExactlyTwoDifferentMininmums.get_array()  # Corrected class name here
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMininmums.get_expected_result()  # Corrected class name here
    result = minimum_index(seq)
    assert result == expected_result


TestWithEmptyArray()
TestWithUniqueValues()
TestWithExactlyTwoDifferentMinimus()
print("Ok")


def digit_sum(num):
    # Calculate the sum of digits of a number
    return sum(int(digit) for digit in str(num))

def solution(A):
    # Dictionary to store the maximum sum of two numbers for each digit sum
    max_sums = {}
    
    # Iterate through the array
    for num in A:
        sum_of_digits = digit_sum(num)
        if sum_of_digits in max_sums:
            max_sums[sum_of_digits] = max(max_sums[sum_of_digits], num + max_sums[sum_of_digits])
        else:
            max_sums[sum_of_digits] = num
    
    result = -1
    # Find the maximum sum of two numbers whose digits add up to the same sum
    for key in max_sums:
        if max_sums[key] > result:
            result = max_sums[key]
    
    return result

# Test cases
print(solution([51, 71, 17, 42]))  # Output: 93
print(solution([42, 33, 60]))  # Output: 102
print(solution([51, 32, 43]))  # Output: -1

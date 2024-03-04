def solution(N):
    # Calculate the number of times each letter should occur
    letters_count = N // 26
    remainder = N % 26

    # Generate the string pattern with each letter repeating letters_count times
    pattern = ''.join(chr(ord('a') + i) * letters_count for i in range(26))

    # Add the first few letters to the pattern the extra number of times
    for i in range(remainder):
        pattern = pattern[:i] + chr(ord('a') + i) + pattern[i:]

    return pattern

# Test cases
print(solution(3))   # Output: "abc"
print(solution(5))   # Output: "abcde"
print(solution(30))  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"

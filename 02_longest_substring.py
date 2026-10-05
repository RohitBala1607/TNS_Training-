# Longest Substring Without Repeating Characters - Sliding Window
s = "abcabcbb"

left = 0
max_length = 0
seen = {}

for right, char in enumerate(s):
    if char in seen and seen[char] >= left:
        left = seen[char] + 1

    seen[char] = right
    max_length = max(max_length, right - left + 1)

print(max_length)

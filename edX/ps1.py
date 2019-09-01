s = 'azcbobobegghakl'
# count = 0
# for char in s:
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#         count += 1
# print("Number of vowels:", str(count))

# total = 0
# for char in range(len(s) - 2):
#     if s[char:char + 3] == 'bob':
#         total += 1
# print("Number of times bob occurs is:", total)

longest = 0
current = 1
currentIndex = 0
longestIndex = 0
for char in range(len(s) - 1):
        curr = s[char]
        nxt = s[char + 1]
        if curr <= nxt:
                current += 1
        else:
                if current > longest:
                        longest = current
                        longestIndex = currentIndex
                current = 1
                currentIndex = char + 1

if current > longest:
        longest = current

print("Longest substring in alphabetical order is:", s[longestIndex: longestIndex + longest])
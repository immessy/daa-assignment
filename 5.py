pattern = "ABCBCABC"
lps = [0]
length = 0

for i in range(1, len(pattern)):
    while length > 0 and pattern[i] != pattern[length]:
        length = lps[length - 1]
    if pattern[i] == pattern[length]:
        length += 1
    lps.append(length)

print("LPS Table:", lps)


s = input("Enter a string: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for ch in s:
    if freq[ch]!=1:
        print("first repeating character is:",ch)
        break
else:
    print("No repeating character found")
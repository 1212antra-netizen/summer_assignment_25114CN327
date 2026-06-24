s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagram")
else:
    freq = {}
    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in s2:
        if ch in freq:
            freq[ch] -= 1
        else:
            freq[ch] = 1
    is_anagram = True
    for key in freq:
        if freq[key] != 0:
            is_anagram = False
            break

    if is_anagram:
        print("Anagram")
    else:
        print("Not Anagram")
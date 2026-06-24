s=input("enter a string:")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
max_ch=""
max_count=0
for key in freq:
    if freq[key]>max_count:
        max_count=freq[key]
        max_ch=key
print("the maximum occuring character is :",max_ch)
print("frequency is:",max_count)

def is_rotation(s1,s2):
    if len(s1)!=len(s2) or len(s1)==0:
        return False
    return s2 in (s1+s1)
s1=input("enter string 1:")
s2=input("enter string 2:")
if is_rotation(s1,s2):
    print("string is rotation")
else:
    print("not rotation")
s1='bac'
s2='abc'
if(s1.len()!=s2.len()):
    print("not anagram")
else:
    if(s1.sorted()==s2.sorted):
        print("anagram")
    else:
        print("not anagram")
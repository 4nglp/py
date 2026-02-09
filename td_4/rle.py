def comp(s):
    sc = ""
    l = []
    curr_char = s[0]
    count = 1
    for i in range(1,len(s)):
        if s[i] == curr_char:
            count+=1
        else:
            l.append(count)
            sc+=curr_char
            curr_char = s[i]
            count = 1
    sc+=curr_char
    l.append(count)
    return s,sc,l
print(comp("AASDDSDNNSSSSWWWWWL"))

def occ(s,sc):
    l=[]
    i=0
    for char in sc:
        count = 0
        while i < len(s) and s[i] == char:
            i+=1
            count+=1
        l.append(count)
    return l

def decomp(sc,l):
    s=""
    for i in range(len(sc)):
        s+=sc[i]*l[i]
    return s
print(decomp("sbwj",[1,2,3,4]))

def comp(s):
    sc = ""
    l = []
    count = 1
    curr_char = s[0]
    for i in range(1,len(s)):
        if s[i]==curr_char:
            count+=1
        else:
            l.append(count)
            sc+=curr_char+str(count)
            curr_char = s[i]
            count = 1
    sc+=curr_char+str(count)
    return sc

def decomp_sc(sc):
    s=""
    for i in range(0,len(sc),2):
        s+= sc[i]*int(sc[i+1])
    return s
print(decomp_sc("M5N4B1"))

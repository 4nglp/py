def is_sorted_desc(l):
    if len(l)<=1:
        return True
    if l[0] < l[1]:
         return False
    return is_sorted_desc(l[1:])

print(is_sorted_desc([8,8,4,2]))

def is_sorted_desc_strict(l):
    if len(l)<=1:
        return True
    if l[0] <= l[1]:
        return False
    return is_sorted_desc_strict(l[1:])
print(is_sorted_desc_strict([8,8,4,2]))

# reverse the condion for the asec version
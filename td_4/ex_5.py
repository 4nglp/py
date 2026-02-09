def est_palindrome_recur(s):
    accents = {"é": "e", "è": "e", "ê": "e", "à": "a", "â": "a", "ç": "c", "î": "i", "ï": "i"}
    s = s.lower().replace(" ", "")
    for char, replacement in accents.items():
        s = s.replace(char, replacement)
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return est_palindrome_recur(s[1:-1])
print(est_palindrome_recur("Ésope reste ici et se repose"))
print(est_palindrome_recur("La mariée ira mal"))             































def is_pal(s):
    accent = {"e":"e"}
    s = s.lower().replace(" ","")
    for char,rep in accent:
        s.replace(char,rep)
    if len(s) <=1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_pal(s[1:-1])
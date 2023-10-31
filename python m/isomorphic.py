def are_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping = {} 
    mapped_chars = set()  
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        if char_s in mapping:
            if mapping[char_s] != char_t:
                return False
        else:
            if char_t in mapped_chars:
                return False
            mapping[char_s] = char_t
            mapped_chars.add(char_t)
    
    return True

s = "egg"
t = "add"
result = are_isomorphic(s, t)

if result:
    print("true")
else:
    print("false")

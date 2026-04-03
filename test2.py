def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True

s1, t1 = "anagram", "nagaram"
s2, t2 = "rat", "car"

print(f"'{s1}' и '{t1}': {isAnagram(s1, t1)}")
print(f"'{s2}' и '{t2}': {isAnagram(s2, t2)}")
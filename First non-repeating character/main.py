def first_non_repeating_letter(s):
    for char in s:
        if char.lower() not in s[s.index(char)+1:].lower():
            return char

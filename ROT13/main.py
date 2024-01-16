dic = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m'}

def rot13(txt):
    res = ''
    for char in txt:
        if char.lower() in dic:
            if char.isupper():
                res += dic[char.lower()].upper()
            else:
                res += dic[char]
        else:
            res += char
    return res

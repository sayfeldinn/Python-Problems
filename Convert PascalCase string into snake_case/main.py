def to_underscore(txt):
    txt = str(txt)
    snake_case = txt[0]
    if len(txt)>1:
        for i in txt[1:]:
            snake_case += '_'+i if i.isupper() else i
    return snake_case.lower()

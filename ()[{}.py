
s = ["(]"]


def isValid(s):
    t = True
    f = False
    storage = []

    n = "("
    m = "["
    d = "{"

    if (len(s) % 2 == 0):
        return t
    storage.append(s[0])
    for x in range(1, len(storage)):
        for y in storage:
            if (s[x] == ")" and (y == "(")):
                storage.remove("(")
            elif (s[x] == "]" and (y == "[")):
                storage.remove("[")
            elif (s[x] == "}" and (y == "{")):
                storage.remove("{")
            else:
                storage.append(s[x])

    if (len(storage) == 0):
        print("True " + storage)
    else:
        print("False " + storage)

isValid(s)
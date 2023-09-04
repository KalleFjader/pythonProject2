#strs = ["flower","flow","flight"]
#strs = ["a"]
strs = ["cir", "car"]
def longestCommonPrefix(strs):
    common = []
    current = "a"
    sep = ""

    shortest = 40

    for y in range(0, (len(strs))):
        if (len(strs[y]) < shortest):
            shortest = len(strs[y])

    for x in range (0,(shortest)):
        current = strs[0][x]
        for ord in range (0,(len(strs))):
            print("testar")
            if(strs[ord][x] == current):
                print("Samma bokstav " + strs[ord][x])
                if(ord == (len(strs)-1)):
                    common.append(strs[ord][x])
                    print("Appended!!")
            elif(strs[ord][x] != current):
                sep = sep.join(common)
                print("Answer2: " + sep)

    print(common)
    sep = sep.join(common)
    print ("Answer: " + sep)

longestCommonPrefix(strs)

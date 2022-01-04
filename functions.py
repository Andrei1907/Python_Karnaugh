

def generate(ultima_col, karnaughPos, karnaughVal, res, inclusion):
    if(ultima_col == 3):
        for i in range(8):
            inclusion.append(0)

        karnaughPos[:] = [[3, 2, 0, 1, 3, 2, 0, 1], [7, 6, 4, 5, 7, 6, 4, 5]]
        karnaughVal[:] = [[0]*8 for i in range(2)]

        for i in range(0, 2):
            for j in range(0, 8):
                if karnaughPos[i][j] in res:
                    karnaughVal[i][j] = 1
    else:
        for i in range(16):
            inclusion.append(0)

        karnaughPos[:] = [[15, 14, 12, 13, 15, 14, 12, 13], [11, 10, 8, 9, 11, 10, 8, 9], [3, 2, 0, 1, 3, 2, 0, 1], [7, 6, 4, 5, 7, 6, 4, 5],
                       [15, 14, 12, 13, 15, 14, 12, 13], [11, 10, 8, 9, 11, 10, 8, 9], [3, 2, 0, 1, 3, 2, 0, 1], [7, 6, 4, 5, 7, 6, 4, 5]]
        karnaughVal[:] = [[0]*8 for i in range(8)]

        for i in range(0, 8):
            for j in range(0, 8):
                if karnaughPos[i][j] in res:
                    karnaughVal[i][j] = 1


def groupComp(groups, gnew):
    for i in range(0, len(groups)):
        if(all(x in gnew for x in groups[i])):
            groups.pop(i)
            if(gnew not in groups):
                groups.append(gnew)
            return 1
    return 0


def validGroup(karnaughPos, karnaughVal, val, x, y, X, Y):
    possible = []
    for i in range(x, X+1):
        for j in range(y, Y+1):
            possible.append(karnaughPos[i][j])
            if(karnaughVal[i][j] != val):
                possible = []
                return possible
    return possible


def generateGroups(karnaughPos, karnaughVal, groups, inclusion, x, y, val):
    gcoord = [[3, 3], [1, 3], [3, 1], [1, 1], [0, 3], [3, 0], [0, 1], [1, 0], [0, 0]]
    for k in range(0, 9):
        if(x + gcoord[k][0] < len(karnaughVal) and y + gcoord[k][1] < len(karnaughVal[0])):
            result = validGroup(karnaughPos, karnaughVal, val, x, y, x + gcoord[k][0], y + gcoord[k][1])
            result.sort()
            if result: #s-a intors un grup posibil
                # OK = 0
                # for t in range(0, len(result)):
                #     if(inclusion[result[t]] == 0):
                #         OK = 1
                if(result not in groups):
                    for t in range(0, len(result)):
                        inclusion[result[t]] = 1
                        #verificare inglobare alte grupuri
                        if((groupComp(groups, result) == 0)):
                            groups.append(result)


def karnaughGroups(karnaughPos, karnaughVal, groups, inclusion, val):
    for i in range(0, len(karnaughVal)):
        for j in range(0, len(karnaughVal[0])):
            if(karnaughVal[i][j] == val):
                generateGroups(karnaughPos, karnaughVal, groups, inclusion, i, j, val)
    #stergere grupuri mici redundante
    popped = 1
    i = 0
    if(len(groups) > 1):
        while(i < len(groups)):
            if(popped == 0):
                i = i + 1
                if(i == len(groups)):
                    return
            disposable = 1
            for j in range(0, len(groups[i])):
                OK = 1
                for k in range(0, len(groups)):
                    if((groups[i][j] in groups[k]) and (k != i) and (len(groups[i]) <= len(groups[k]))):
                        OK = 0
                if(OK == 1):
                    disposable = 0
            if(disposable == 1):
                groups.pop(i)
                popped = 1
            else: popped = 0
    # for i in range(0, len(groups)):
    #     disposable = 1
    #     for j in range(0, len(groups[i])):
    #         OK = 1
    #         for k in range(0, len(groups)):
    #             if((groups[i][j] in groups[k]) and (k != i) and (len(groups[i]) < len(groups[k]))):
    #                 OK = 0
    #         if(OK == 1):
    #             disposable = 0
    #     if(disposable == 1):
    #         groups.pop(i)
    #         i = i - 1


def normalForm(groups, tabela, ultima_col, type):
    afis = ""
    for i in range (0, len(groups)):
        if(type == 0):
            piece = ""
        else: piece = "("
        charact = 'A'
        for j in range(0, ultima_col):
            sum = 0
            for k in range(0, len(groups[i])):
                sum = sum + tabela[groups[i][k]][j]
            if(sum == 0 and type == 0):
                piece = piece + charact + "\'"
            elif(sum == 0 and type == 1 and piece == "("):
                piece = piece + charact
            elif(sum == 0 and type == 1):
                piece = piece + " + " + charact
            elif(sum == len(groups[i]) and type == 0):
                piece = piece + charact
            elif(sum == len(groups[i]) and type == 1 and piece == "("):
                piece = piece + charact + "\'"
            elif (sum == len(groups[i]) and type == 1):
                piece = piece + " + " + charact + "\'"
            charact = chr(ord(charact) + 1)
        if(type == 1):
            piece = piece + ")"
        if(not afis):
            afis = afis + piece
        elif(type == 0): afis = afis + " + " + piece
        else: afis = afis + " * " + piece

    file1 = open("table.txt", "a")
    if(type == 0):
        file1.write("Forma normala disjunctiva: ")
    else: file1.write("Forma normala conjunctiva: ")
    file1.write(afis + "\n")
    file1.close()
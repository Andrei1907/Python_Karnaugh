import re
from functions import generate
from functions import karnaughGroups
from functions import normalForm


if __name__ == '__main__':
    # initializare string => preluare din input dat de utilizator
    sigma_input = input()

    temp = re.findall(r'\d+', sigma_input)
    res = list(map(int, temp))

    #nr virgule
    if(sigma_input.count(',') != len(res) - 1):
        file1 = open("table.txt", "w")
        file1.write("Respectati sintaxa!" + "\n")
        file1.close()
        quit()

    #paranteze corecte
    p_open = 0
    for i in range(0, len(sigma_input)):
        if(sigma_input[i] == '('):
            p_open = p_open + 1
        if(sigma_input[i] == ')'):
            p_open = p_open - 1
        if(p_open < 0):
            file1 = open("table.txt", "w")
            file1.write("Respectati sintaxa!" + "\n")
            file1.close()
            quit()
    if(p_open != 0):
        file1 = open("table.txt", "w")
        file1.write("Respectati sintaxa!" + "\n")
        file1.close()
        quit()

    #identificare maxim
    maxi = max(res)
    if(not(maxi >=4 and maxi <= 15)):
        file1 = open("table.txt", "w")
        file1.write("Valorile sigma nu permit reprezentarea cu 3/4 variabile. Introduceti o varianta corecta!" + "\n")
        file1.close()
        quit()

    #construire tabela adevar
    pow2 = 2
    if(maxi >= 8):
        ultima_col = 4
    else: ultima_col = 3
    lin, col = pow(2, ultima_col), ultima_col
    tabela = [[0 for j in range(col)] for i in range(lin)]

    for j in range(col-1, -1, -1):
        for i in range(0, lin):
            if(i % pow2 < pow2/2):
                tabela[i][j] = 0
            else: tabela[i][j] = 1
        pow2 = pow2 * 2

    if(ultima_col == 3):
        afis = "A B C Output"
    else: afis = "A B C D Output"

    file1 = open("table.txt", "w")
    file1.write(afis + "\n")
    file1.close()

    for i in range(0, lin):
        afis = ""
        for j in range(0, col):
            afis = afis + str(tabela[i][j]) + " "
        if(i in res):
            afis = afis + "1"
        else: afis = afis + "0"

        file1 = open("table.txt", "a")
        file1.write(afis + "\n")
        file1.close()

    #generare matrici Karnaugh
    if(ultima_col == 3):
        karnaughPos = 2 * [8 * [0]]
        karnaughVal = 2 * [8 * [0]]
    else:
        karnaughPos = 8 * [8 * [0]]
        karnaughVal = 8 * [8 * [0]]

    groups = []
    inclusion = []

    generate(ultima_col, karnaughPos, karnaughVal, res, inclusion)
    karnaughGroups(karnaughPos, karnaughVal, groups, inclusion, 1)
    normalForm(groups, tabela, ultima_col, 0)

    print(groups)

    groups = []
    inclusion = []

    generate(ultima_col, karnaughPos, karnaughVal, res, inclusion)
    karnaughGroups(karnaughPos, karnaughVal, groups, inclusion, 0)

    print(groups)

    normalForm(groups, tabela, ultima_col, 1)
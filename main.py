import re


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


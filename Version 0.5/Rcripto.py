def simple_cripto(te,co):
    texto = list(te)
    codigo = list(co)
    pa = len(te)%len(co)
    text = []
    new_text = ""
    for i in range(0,len(te)+pa):
        try:
            text.append(ord(texto[i])+ord(codigo[i%len(co)]))
        except IndexError:
            text.append(00)
    for i in text:
        if i != 0:
            new_text+=chr(i)
    return new_text

def simple_descripto(te,co):
    texto = list(te)
    codigo = list(co)
    text = []
    new_text = ""
    for i in range(0,len(te)):
        try:
            text.append(ord(texto[i])-ord(codigo[i%len(co)]))
        except IndexError:
            text.append(00)
    for i in text:
        if i != 0:
            new_text+=chr(i)
    return new_text

def cripto(te):
    from random import randrange

    def mais(alfabeto,letra,num):
        cont = 0
        for i in alfabeto:
            if letra == i:
                if alfabeto[cont - num[0]] == "w":
                    if num[0] > 0:
                        num[0] -= 1
                    else:
                        num[0] += 1
                return alfabeto[cont - num[0]]
            cont += 1

    def menos(alfabeto,letra,num):
        cont = 0
        for i in alfabeto:
            if letra == i:
                if cont + num[0] > 25:
                    count = cont + num[0] - 26
                else:
                    count = cont + num[0]
                if alfabeto[count] == "w":
                    if num[0] > 0:
                        num[0] -= 1
                    else:
                        num[0] += 1
                if cont + num[0] > 25:
                    return alfabeto[cont + num[0] - 26]
                else:
                    return alfabeto[cont + num[0]]
            cont += 1


    # Entrada de Dados
    texto = te.lower()
    alfabeto = ["a","b","c","d","e","f",
                "g","h","i","j","k","l",
                "m","n","o","p","q","r",
                "s","t","u","v","w","x",
                "y","z"]
    texto = list(texto)
    count = len(texto)
    palavra = ""
    numero = ""
    num = [0]

    # Criptografando
    for i in range(count):
        simbolo = randrange(2)
        if texto[i] != " ":
            if simbolo == 0:
                simbolo = "+"
                num[0] = randrange(10)
                pa = mais(alfabeto,texto[i],num)
                nume = simbolo + str(num[0])
            else:
                simbolo = "-"
                num[0] = randrange(10)
                pa = menos(alfabeto,texto[i],num)
                nume = simbolo + str(num[0])
            numero += nume
        else:
            pa = "w"
        palavra += pa

    # Tratamento de Dados dos numeros
    nume = list(numero)
    count = len(nume)

    i = count-1
    while(i > 0):
        if nume[i] == "+" or nume[i] == "-":
            if nume[i] == nume[i-2]:
                del nume[i]
        i = i-1

    # Juntando os Numeros
    numero = ""
    for i in nume:
        numero += i

    # Resultados
    return palavra,numero

def descripto(te,pa):
    def menos(letra, numero, alfabeto):
        cont = 0
        numero = int(numero)
        for c in alfabeto:
            if letra == c:
                if cont - numero < 0:
                    cont = 26 + (cont - numero)
                    return alfabeto[cont]
                else:
                    return alfabeto[cont - numero]
            cont += 1

    def mais(letra, numero, alfabeto):
        cont = 0
        numero = int(numero)
        for c in alfabeto:
            if letra == c:
                if cont + numero > 25:
                    cont = (cont + numero) - 26
                    return alfabeto[cont]
                else:
                    return alfabeto[cont + numero]
            cont += 1

    # Variaveis Inicializadas
    num = ""
    simbolo = ""
    resto = ""
    palavra = ""
    frase = ""
    cont = 0
    alfabeto = ["a","b","c","d","e","f",
                "g","h","i","j","k","l",
                "m","n","o","p","q","r",
                "s","t","u","v","w","x",
                "y","z"]

    # Pedir Valores e Separa-los em Vetores
    pal = te
    texto = list(pal)
    pal = pal.count("w")
    position = []
    numero = list(pa)

    # Montar a Estrutura da soma e subtração da criptografia
    for c in numero:
        if "-" in c or "+" in c:
            simbolo = c
            resto = simbolo
        else:
            simbolo = ""

        if simbolo == "-" or simbolo == "+":
            num += " " + c
        else:
            num += " " + resto + c + " "

    num = num.split()
    numero = ""

    for c in num:
        if c == "+" or c == "-":
            numero += ""
        else:
            numero += " " + c
    numero = numero.split()

    # Montar a Estrutura do Texto a ser Descriptografado
    for i in texto:
        if i == "w":
            position.append(cont)
            palavra += " "
        else:
            palavra += i
        cont += 1

    palavra = palavra.split()
    texto = ""
    cont = 0
    for i in palavra:
        if i != " ":
            texto += i
    texto = list(texto)

    # Descriptografar o Texto
    for c in numero:
        if "+" in c:
            num = list(c)
            pa = mais(texto[cont], num[1], alfabeto)
            frase += pa
        if "-" in c:
            num = list(c)
            pa = menos(texto[cont], num[1], alfabeto)
            frase += pa
        cont += 1

    # Inserir Espaços
    frase = list(frase)
    for i in range(0, pal):
        frase.insert(position[i]," ")
    frases = ""
    for i in frase:
        frases += i

    # Resultado
    return frases

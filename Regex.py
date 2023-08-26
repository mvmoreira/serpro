import re

frase = "socorram-me subi no onibus em Marrocos"
frase = frase.lower()
fraseNova = re.sub(r'[\W]','',frase)

for i in range(len(fraseNova)//2):
    print(f'Comparando {fraseNova[i]} com {fraseNova[len(fraseNova)-1-i]}')
    if fraseNova[i] != fraseNova[len(fraseNova)-1-i]:
        print("Não é palindromo")
        break


print (fraseNova)
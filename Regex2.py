import re
texto = "AaBb@#$9#_"

textoNovo = re.sub(r'[^A-Za-z0-9_]','',texto)



print (f'Texto antes => {texto}')
print (f'Texto depois => {textoNovo}')
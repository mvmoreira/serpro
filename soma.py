def soma(valor1,valor2):
    if type(valor1) == int and type(valor2) == int:
       return int(valor1 + valor2)
    else: 
       return 0

valor1 = input("informe o valor 1:")
valor2 = input("informe o valor 2:")

# ALTERAÇÃO BRANCH 3

print(f'A soma é {soma(valor1,valor2)}')
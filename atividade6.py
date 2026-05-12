#atividade 1
from math import factorial


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print(f"O maior número é: {num1}")
else:
    print(f"O maior número é: {num2}")

#atividade 2
valor = float(input("Digite um valor: "))
if valor > 0:
    print(f"O valor {valor} é positivo.")
else:
    print(f"O valor {valor} é negativo.")

#atividade 3
letra = input("Digite F ou M: ").upper()

if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")

#atividade 4
letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")

#atividade 5
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7 and media < 10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
        print("Aprovado com Distinção")

#atividade 6
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1
if num2 > maior:
        maior = num2
if num3 > maior:
        maior = num3

print(f"O maior número é: {maior}")

#atividade 7 
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

#atividade 8
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

mais_barato = min(preco1, preco2, preco3)

if mais_barato == preco1:
    print("Você deve comprar o primeiro produto.")
elif mais_barato == preco2:
 print("Você deve comprar o segundo produto.")
elif mais_barato == preco3:
   print("Você deve comprar o terceiro produto.")

#atividade 9
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
numeros = [num1, num2, num3]
numeros.sort(reverse=True)
print("Números em ordem decrescente:")
for numero in numeros:
    print(numero)

#atividade 10
turno = input("Em que turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ").upper()
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
        print("Boa Tarde!")

elif turno == "N":
            print("Boa Noite!")

else:
                print("Valor Inválido!")

#exercicio 11
salario = float(input("Digite o salário do colaborador: "))
if salario <= 280:
    percentual_aumento = 20
elif salario > 280 and salario <= 700:
        percentual_aumento = 15

elif salario > 700 and salario <= 1500:
            percentual_aumento = 10
else:
 percentual_aumento = 5
aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento
print(f"Salário antes do aumento: R${salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário após o aumento: R${novo_salario:.2f}")

#atividade 12
valor_hora = float(input("Digite o valor da hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    percentual_ir = 0
elif salario_bruto <= 1500:
    percentual_ir = 5
elif salario_bruto <= 2500:
    percentual_ir = 10
else:
    percentual_ir = 20

desconto_ir = salario_bruto * (percentual_ir / 100)

desconto_inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({percentual_ir}%)                 : R$ {desconto_ir:.2f}")
print(f"(-) INSS (10%)                : R$ {desconto_inss:.2f}")
print(f"FGTS (11%)                    : R$ {fgts:.2f}")
print(f"Total de descontos            : R$ {total_descontos:.2f}")
print(f"Salário Líquido               : R$ {salario_liquido:.2f}")

#atividade 13
num = int(input("Digite um número de 1 a 7 para saber o dia da semana: "))
if num == 1:
    print("Domingo")
elif num == 2:
              print("Segunda-feira")
elif num == 3:
              print("Terça-feira")
elif num == 4:
              print("Quarta-feira")
elif num == 5:
              print("Quinta-feira")
elif num == 6:
              print("Sexta-feira")
elif num == 7:
              print("Sábado")
else:
              print("Número inválido! Por favor, digite um número de 1 a 7.")

#atividade 14
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    conceito = "S"
elif media >= 7.5:
    conceito = "A"
elif media >= 6:
    conceito = "B"
elif media >= 4:
    conceito = "C"
else:
    conceito = "D"

print(f"\nPrimeira Nota: {nota1}")
print(f"Segunda Nota: {nota2}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")

#atividade 15
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    if lado1 == lado2 == lado3:
        print("O triângulo é Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é Isósceles.")
    else:
        print("O triângulo é Escaleno.")
else:
    print("Os valores não formam um triângulo.")

#atividade 16
import math
a = float(input("Digite o valor de a: "))
if a == 0:
    print("A equação não é do segundo grau.")
else:

        b = float(input("Digite o valor de b: "))

        c = float(input("Digite o valor de c: "))

        delta = b**2 - 4*a*c

if delta < 0:
            print("A equação não possui raízes reais.")
elif delta == 0:
            raiz = -b / (2*a)
            print(f"A equação possui uma raiz real: {raiz:.2f}")
else:
            raiz1 = (-b + math.sqrt(delta)) / (2*a)
            raiz2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")

#atividade 17 
# Entrada do ano
ano = int(input("Digite um ano: "))

# Verificação de ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

    

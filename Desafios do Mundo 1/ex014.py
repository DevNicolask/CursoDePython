# Desafio: Escreva um programa que converta uma temperatura digitada em graus Celsius para graus Fahrenheit.

a = float(input('Temperatura em graus célcius: '))
print(f'Essa temperatura em fahrenheit é igual a {(9*a/5)+32:.2f}°F e em Kelvin é {a+273:.0f} K.')

# Desafio: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
# (Apendi como faz uma biblioteca em Python resolvi usar aqui).

from cores import Cores

nome = input(Cores.ciano2 + 'Qual é o seu nome? ' + Cores.reset)
print(Cores.ciano2 + 'Prazer em te conhecer' + Cores.reset, nome)

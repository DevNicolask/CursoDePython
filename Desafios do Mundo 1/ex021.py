# Desafio: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer, event

mixer.init()
mixer.music.load('Ex.021.mp3')
mixer.music.play(-1)
input()
event.wait()

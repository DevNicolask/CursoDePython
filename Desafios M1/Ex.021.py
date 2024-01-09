# Versão Normal.
from pygame import mixer, event

mixer.init()
mixer.music.load('Ex.021.mp3')
mixer.music.play(-1)
input()
event.wait()

# Esse não tem versão colorida rs

import pygame #Biblioteca para desenvolvimento de jogos    
import os #Biblioteca para integrar o codigo com os arquivos do computador
import random 

#Definir a largura e altura da interface grafica do game(janela)
TELA_LARGURA = 500
TELA_ALTURA = 800

#Definir as imagens do game
    #pygame.transform.scale2x(), serve para aumentar em 2 vezes a escala das imagens
    #pygame.image.load(), serve para carregar a imagem 
    #os.path.join(), faz o python entrar na pasta imgs para assim encontrar o arvivo de imagem, algo como imgs/...
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

#Fonte do Texto de pontuação do game
pygame.font.init()  #Iniciar a fonte
FONTE_PONTOS = pygame.font.SysFont('arial', 50) #Nome e tamanho da fonte respectivamente

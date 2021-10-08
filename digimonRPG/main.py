from Digimon import *

import math
import pygame

# Init Pygame
running = True
pygame.init()
	
# Aliados
Agumon = Digimon("Agumon", 160,80,20,20,20)
Guilmon = Digimon("Guilmon", 150,100,20,20,20)
Gabumon = Digimon("Gabumon", 130,140,20,20,20)

# Clock
mainClock = pygame.time.Clock()
FPS = 60

# Superficie
bg = pygame.Surface((640,480))
bg.fill ((40,40,40))

# In game Windows
janelaX = 70
janelaY = 310
janelaAgumon = pygame.Rect((janelaX,310,160,160))
janelaGuilmon = pygame.Rect((janelaX+170,310,160,160))
janelaGabumon = pygame.Rect((janelaX+340,310,160,160))

screen = pygame.display.set_mode((640,480))

# Text dos aliados
font = pygame.font.SysFont(None,30)

# Agumon
nomeAgumon = font.render(Agumon.nome, True, (200,255,200))

# As funcoes atualizam e imprimem os dados dos digimon
def updateAgumonStatus():
	textoHpAgumon = "HP: " + str(Agumon.status[0])
	hpAgumon = font.render(textoHpAgumon, True, (200,255,200))
	textoMpAgumon = "MP: " + str(Agumon.status[1])
	mpAgumon = font.render(textoMpAgumon, True, (200,255,200))
	screen.blit(hpAgumon,(80,420))
	screen.blit(mpAgumon,(80,440))

# Guilmon
nomeGuilmon = font.render(Guilmon.nome, True, (200,255,200))

def updateGuilmonStatus():
	textoHpGuilmon = "HP: " + str(Guilmon.status[0])
	hpGuilmon = font.render(textoHpGuilmon, True, (200,255,200))
	textoMpGuilmon = "MP: " + str(Guilmon.status[1])
	mpGuilmon = font.render(textoMpGuilmon, True, (200,255,200))
	screen.blit(hpGuilmon,(250,420))
	screen.blit(mpGuilmon,(250,440))

# Gabumon
nomeGabumon = font.render(Gabumon.nome, True, (200,255,200))

def updateGabumonStatus():
	textoHpGabumon = "HP: " + str(Gabumon.status[0])
	hpGabumon = font.render(textoHpGabumon, True, (200,255,200))
	textoMpGabumon = "MP: " + str(Gabumon.status[1])
	mpGabumon = font.render(textoMpGabumon, True, (200,255,200))
	screen.blit(hpGabumon,(420,420))
	screen.blit(mpGabumon,(420,440))


while running:
	
	screen.blit(bg,(0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		# Teste pra verificar atualizaçao do texto
		if event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_a) and Agumon.status[0] > 0:
				Agumon.sofreDano(20)
			if (event.key == pygame.K_s) and Guilmon.status[0] > 0:
				Guilmon.sofreDano(20)
			if (event.key == pygame.K_d) and Gabumon.status[0] > 0:
				Gabumon.sofreDano(20)
	
	# Janela dos aliados
	pygame.draw.rect(bg, (180,150,30), janelaAgumon)
	pygame.draw.rect(bg, (180,30,30), janelaGuilmon)
	pygame.draw.rect(bg, (30,100,180), janelaGabumon)
	
	# Texto do HP E MP dos aliados
	screen.blit(nomeAgumon,(80,320))
	updateAgumonStatus()
	
	screen.blit(nomeGuilmon,(250,320))
	updateGuilmonStatus()
	
	screen.blit(nomeGabumon,(420,320))
	updateGabumonStatus()
	
	mainClock.tick(FPS)
	pygame.display.update()

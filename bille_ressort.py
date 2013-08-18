#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        exemple
# Purpose:      montrer ce que peut faire le moteur physique
#
# Author:      Timosis
#
# Created:     08/04/2013
# Copyright:   (c) Timosis 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import physics,pygame,sys,math
from pygame.locals import *
from funcs import *

#quelques constantes
masse_bille = 10
Lo = 90
k = 10
g = 9.81
pas = 0.1


#creation de l'interface graphique
pygame.init()
fen = pygame.display.set_mode((1024,560))
fen.fill((255,255,255))

#definition des objets
bille = physics.PhysObject(400,250,masse_bille)
point = physics.PhysObject(500,250,1)
bille.ch_pas(pas)

#definition des forces
f_elas = physics.ForceElastique(bille,point,Lo,k)
poids = physics.Force(0,g*masse_bille)
frottements = physics.Frottements(bille,0.01,1)

#application des forces
bille.addforce(poids)
bille.addforce(f_elas,True)
bille.addforce(frottements,True)


#vitesse initiale
#point.vitx = 50


def main():
	boucle = 1
	running = False
	trace = False
	while boucle:
		for event in pygame.event.get():
			if event.type == QUIT:
				boucle = 0
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					running = obool(running)	
				if event.key == K_t:
					trace = obool(trace)
					
		if running: 
			bille.tick()
			point.tick_euler()
			
		if not trace:
			fen.fill((255,255,255))
			
		pygame.draw.circle(fen,(0,0,0),(int(point.posx),int(point.posy)),2)
		pygame.draw.circle(fen,(0,0,0),(int(bille.posx),int(bille.posy)),5)
		pygame.draw.line(fen,(254*(1-math.exp(-bille.distance(point)/160)),0,0),(int(point.posx),int(point.posy)),(int(bille.posx),int(bille.posy)))
		
		pygame.display.flip()
		
if __name__ == '__main__':
	main()

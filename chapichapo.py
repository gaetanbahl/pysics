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
masse_pi = 5
masse_po = 10
Lo = 100
k = 0.5
pas = 0.05

#creation de l'interface graphique
pygame.init()
fen = pygame.display.set_mode((1024,560))
fen.fill((255,255,255))

#definition des objets
pi = physics.PhysObject(600,250,masse_pi)
po = physics.PhysObject(500,250,masse_po)
pi.ch_pas(pas)
po.ch_pas(pas)

#definition des forces
f_elas = physics.ForceElastique(pi,po,Lo,k)
f_elas2 = physics.ForceElastique(po,pi,Lo,k)
#application des forces
pi.addforce(f_elas,True)
po.addforce(f_elas2,True)

#vitesse initiale
pi.posx_ = 601
def main():
	boucle = 1
	running = False
	trace = False
	x,y,m = physics.barycentre([pi,po])
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
			pi.tick()
			po.tick()
			x,y,m = physics.barycentre([pi,po])
		if not trace:
			fen.fill((255,255,255))
		pygame.draw.circle(fen,(0,0,0),(int(po.posx),int(po.posy)),po.mass)
		pygame.draw.circle(fen,(0,0,0),(int(pi.posx),int(pi.posy)),pi.mass)
		pygame.draw.circle(fen,(0,100,0),(int(x),int(y)),2)

		pygame.draw.line(fen,(254*(1-math.exp(-pi.distance(po)/160)),0,0),(int(po.posx),int(po.posy)),(int(pi.posx),int(pi.posy)))
		
		pygame.display.flip()
		
if __name__ == '__main__':
	main()

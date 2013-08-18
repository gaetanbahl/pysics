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
m = 1800
M = 19000
pichenette = 300


#creation de l'interface graphique
pygame.init()
fen = pygame.display.set_mode((1024,560))
#pygame.key.set_repeat(30, 30)
fen.fill((255,255,255))

#definition des objets
planete2 = physics.PhysObject(800,100,m)
planete = physics.PhysObject(800,250,M)
#planete.ch_pas(0.01)
#planete2.ch_pas(0.01)

#definition des forces
attraction_plan = physics.Attraction_grav(planete2,planete)
attraction_tri = physics.Attraction_grav(planete,planete2)
boost = physics.Force(0,0)

#application des forces
planete2.addforce(boost)
planete2.addforce(attraction_plan,True)
planete.addforce(attraction_tri,True)

#vitesse initiale
planete2.vitx = 25
planete2.posx_ = 799.8
planete.posx_ = 800.11
def main():
	boucle = 1
	running = False
	trace = False
	while boucle:
		for event in pygame.event.get():
			if event.type == QUIT:
				boucle = 0
			if event.type == KEYDOWN:
				if event.key == K_UP:
					boost.x, boost.y  = +pichenette*math.sin(rad),-pichenette*math.cos(rad)
				if event.key == K_RIGHT:
					planete2.omega += 2
				if event.key == K_LEFT:
					planete2.omega -= 2
				if event.key == K_DOWN:
					boost.x, boost.y  = -pichenette*math.sin(rad),+pichenette*math.cos(rad)
				if event.key == K_SPACE:
					running = obool(running)	
				if event.key == K_t:
					trace = obool(trace)
			if event.type == KEYUP:
				if event.key == K_UP or event.key == K_DOWN:
					boost.x, boost.y  = 0,0
					
		rad = degtorad(planete2.theta)
		
		if running: 
			planete2.tick()
			planete.tick()
			
		G = physics.barycentre([planete,planete2])
		x,y,m = G
		
		if not trace:
			fen.fill((255,255,255))
		pygame.draw.circle(fen,(0,128,0),(int(x),int(y)),5)
		pygame.draw.circle(fen,(0,0,0),(int(planete.posx),int(planete.posy)),5)
		pygame.draw.circle(fen,(0,0,0),(int(planete2.posx),int(planete2.posy)),2)
		
		pygame.display.flip()
		
if __name__ == '__main__':
	main()

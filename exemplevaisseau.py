#-------------------------------------------------------------------------------
# Name:        exemplevaisseau
# Purpose:      montrer ce que peut faire le moteur physique
#
# Author:      Timosis
#
# Created:     08/04/2013
# Copyright:   (c) Timosis 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import physics,pygame,sys,math
from pygame.locals import *

pygame.init()
g = 9.81
moteur = 2000
fen = pygame.display.set_mode((1024,560))
imgtriangle = pygame.image.load("triangle.png").convert_alpha()
pygame.key.set_repeat(30, 30)
triangle = physics.PhysObject(400,100,600)
planete = physics.PhysObject(400,250,5E3)
attraction_plan = physics.Attraction_grav(triangle,planete)

boost = physics.Force(0,0)
triangle.addforce(boost)
triangle.addforce(attraction_plan,True)
plan = pygame.Surface((1024,560))
triangle.vitx = 10
triangle.vity = 0
triangle.ch_pas(0.1)
def main():
	boucle = 1
	while boucle:
		for event in pygame.event.get():
			if event.type == QUIT:
				boucle = 0
			if event.type == KEYDOWN:
				if event.key == K_UP:
					boost.x, boost.y  = +moteur*math.sin(thetarad),-moteur*math.cos(thetarad)
				if event.key == K_RIGHT:
					triangle.omega += 1
				if event.key == K_LEFT:
					triangle.omega -= 1
				if event.key == K_DOWN:
					boost.x, boost.y  = -moteur*math.sin(thetarad),+moteur*math.cos(thetarad)
			if event.type == KEYUP:
				if event.key == K_UP or event.key == K_DOWN:
					boost.x, boost.y  = 0,0
		thetarad = 3.1415 * triangle.theta / 180
		fen.fill((255,255,255))
		pygame.draw.circle(fen,(0,0,0),(int(planete.posx),int(planete.posy)),10)
		
		triangle.tick_euler()
		
		fen.blit(pygame.transform.rotate(imgtriangle, -triangle.theta), (triangle.posx-25,triangle.posy-25))
		pygame.display.flip()
		
if __name__ == '__main__':
	main()

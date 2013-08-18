#-------------------------------------------------------------------------------
# Name:        exempletroispoints
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
from funcs import *

pygame.init()
fen = pygame.display.set_mode((1024,560))

systeme = physics.System()

systeme.addobject(physics.PhysObject(60,500,190000))
systeme.addobject(physics.PhysObject(700,150,250000))
systeme.addobject(physics.PhysObject(300,250,220000))

systeme.setgravity()
systeme.objectlist[0].posx_ = 60.2 
systeme.objectlist[0].posy_ = 500.4
systeme.objectlist[1].posx_ = 699.9 
systeme.objectlist[1].posy_ = 149.4
systeme.objectlist[2].posx_ = 299.9 
systeme.objectlist[2].posy_ = 250.4
systeme.pas = 0.01
systeme.setpas()
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
			
			
		if not trace:	
			fen.fill((255,255,255))
		for i in systeme.objectlist:
			pygame.draw.circle(fen,(0,0,0),(int(i.posx),int(i.posy)),i.mass/40000)
		
		
		bar = physics.barycentre(systeme.objectlist)
		x,y,m = bar
		pygame.draw.circle(fen,(0,128,0),(int(x),int(y)),5)
		
		if running:
			systeme.update()
			
			
		pygame.display.flip()
		
if __name__ == '__main__':
	main()

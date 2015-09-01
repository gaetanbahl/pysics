#-------------------------------------------------------------------------------
# Name:        4points
# Purpose:      montrer ce que peut faire le moteur physique
#
# Author:      Timosis
#
# Created:     08/04/2013
# Copyright:   (c) Timosis 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
## ??? o_o
import physics,pygame,sys,math,time
from pygame.locals import *
from funcs import *

pygame.init()
fen = pygame.display.set_mode((1024,560))

systeme = physics.System()

systeme.addobject(physics.PhysObject(60,500,15000))
systeme.addobject(physics.PhysObject(600,150,19000))
systeme.addobject(physics.PhysObject(300,250,22000))
systeme.addobject(physics.PhysObject(200,450,19000))
systeme.setgravity()
systeme.collisions = True
for i in systeme.objectlist:
	i.size = 20

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
			pygame.draw.circle(fen,(0,0,0),(int(i.posx),int(i.posy)),i.mass/2000)
		
		
		bar = physics.barycentre(systeme.objectlist)
		x,y,m = bar
		pygame.draw.circle(fen,(0,128,0),(int(x),int(y)),5)
		
		if running:
			start = time.time()
			systeme.update_euler()
			print time.time() - start
			
		pygame.display.flip()
		
if __name__ == '__main__':
	main()

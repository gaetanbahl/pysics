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

import physics,pygame,sys,math,time
from pygame.locals import *
from funcs import *

pygame.init()
fen = pygame.display.set_mode((1024,560))

systeme = physics.System()

systeme.addobject(physics.PhysObject(900,150,15000))
systeme.addobject(physics.PhysObject(600,150,15000))
systeme.pas = 0.1
systeme.setpas()
#systeme.setgravity()
systeme.objectlist[0].vitx = -50
systeme.objectlist[1].vitx = -5
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
		i = systeme.objectlist[0]
		pygame.draw.circle(fen,(128,0,0),(int(i.posx),int(i.posy)),10)
		j = systeme.objectlist[1]
		pygame.draw.circle(fen,(0,0,128),(int(j.posx),int(j.posy)),10)
		
		
		bar = physics.barycentre(systeme.objectlist)
		x,y,m = bar
		pygame.draw.circle(fen,(0,128,0),(int(x),int(y)),5)
		
		if running:
			#start = time.time()
			systeme.update_euler()
			#print time.time() - start
			
		pygame.display.flip()
		
if __name__ == '__main__':
	main()

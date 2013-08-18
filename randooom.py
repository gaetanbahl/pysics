#-------------------------------------------------------------------------------
# Name:        randooomfullgravity
# Purpose:      tester les perfs
#
# Author:      Timosis
#
# Created:     08/04/2013
# Copyright:   (c) Timosis 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import physics,pygame,sys,math,random
from pygame.locals import *
from funcs import *
import time


pygame.init()
fenx,feny = 1024,560
fen = pygame.display.set_mode((fenx,feny))

systeme = physics.System()

for i in range(60):
	systeme.addobject(physics.PhysObject(random.randint(0,fenx),random.randint(0,feny),random.randint(5000,30000)))
systeme.setgravity()

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
		
			pygame.draw.circle(fen,(0,0,0),(int(i.posx),int(i.posy)),1)
		
		
		bar = physics.barycentre(systeme.objectlist)
		x,y,m = bar
		pygame.draw.circle(fen,(0,128,0),(int(x),int(y)),5)
		
		if running:
			start = time.time()
			systeme.update()
			end = time.time()
			print end - start
			
		pygame.display.flip()
		
if __name__ == '__main__':
	main()

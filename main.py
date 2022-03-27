from itertools import count
import pygame
import time
import random 
from pygame import  mixer

pygame.init()
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

car_width = 50
car_height = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Car Racing")


clock = pygame.time.Clock()

carImg = pygame.image.load("car1.png") #load the car image
car2Img = pygame.image.load("car2.png")
bgImg = pygame.image.load("bbg.png")
crash_img = pygame.image.load("crash.png")
bgsImg = pygame.image.load("car.png")



def highscore(count):
	font = pygame.font.SysFont(None,45)
	text = font.render("Score : "+str(count),True,black)
	gameDisplay.blit(text,(30,30))

	
def draw_things(thingx,thingy,thing):
	gameDisplay.blit(thing,(thingx,thingy))

def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
	textSurface = font.render(text,True,blue)
	return textSurface,textSurface.get_rect()

def message_display(text,size,x,y):
	font = pygame.font.Font("freesansbold.ttf",size)
	text_surface , text_rectangle = text_objects(text,font)
	text_rectangle.center =(x,y)
	gameDisplay.blit(text_surface,text_rectangle)

def crash(x,y):
	gameDisplay.blit(crash_img,(x,y))
	message_display("GAME OVER",64,display_width/2,display_height/2)	
	pygame.display.update()
	time.sleep(1)
	gameloop() 

def pause():
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
		message_display("пауза",64,display_width/2,display_height/2)
		pygame.display.update()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			paused = False
	
	pygame.display.update()
	clock.tick(15)
def gameloop():
	bg_x1 = (display_width/2)-(360/2)
	bg_x2 = (display_width/2)-(360/2)
	bg_y1 = 0
	bg_y2 = -600
	bg_speed = 10
	car_x = ((display_width / 2) - (car_width / 2))
	car_y = (display_height - car_height)
	car_x_change = 0
	road_start_x =  (display_width/2)-130
	road_end_x = (display_width/2)+130


	thing_startx = random.randrange(road_start_x,road_end_x-car_width)
	thing_starty = -600
	thingw = 50
	thingh = 100
	thing_speed = 10
	count=0
	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					car_x_change = -10
				elif event.key == pygame.K_RIGHT:
					car_x_change = 10
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				pause()
  

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					car_x_change = 0
			
			
		car_x+=car_x_change
		
		if car_x > road_end_x-car_width:
			crash(car_x,car_y)
		if car_x < road_start_x:
			crash(car_x-car_width,car_y)
		
		
		if car_y < thing_starty + thingh:
			if car_x >= thing_startx and car_x <= thing_startx+thingw:
				crash(car_x-25,car_y-car_height/2)
			if car_x+car_width >= thing_startx and car_x+car_width <= thing_startx+thingw:
				crash(car_x,car_y-car_height/2)
		
			
		
		
		gameDisplay.fill(green) #display white background
		gameDisplay.blit(bgsImg,(0,0))
		gameDisplay.blit(bgsImg,(440,0))

		gameDisplay.blit(bgImg,(bg_x1,bg_y1))
		gameDisplay.blit(bgImg,(bg_x2,bg_y2))
		
		car(car_x,car_y) #display car
		draw_things(thing_startx,thing_starty,car2Img)
		
		highscore(count)
		count+=1
		thing_starty += (thing_speed)+10
		
		if thing_starty > display_height:
			thing_startx = random.randrange(road_start_x,road_end_x-car_width)
			thing_starty = -200
			
		bg_y1 += bg_speed
		bg_y2 += bg_speed
		
		if bg_y1 >= display_height:
			bg_y1 = -600
			
		if bg_y2 >= display_height:
			bg_y2 = -600
			
		
		
		pygame.display.update() # update the screen
		clock.tick(60) # frame per sec
		
gameloop()

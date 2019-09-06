#AADITYA MOHAPATRA
#
#

import pygame
import sys
import random
import time 

pygame.init()

width = 800
height = 700

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
yellow = (255,255,0)
background = (49, 189, 179)

rect_width = 40
rect_height = 40

player_size = 40											#positions on a screen in python start [0,0] at the top left of the screen
player_pos = [width/2,height - 2*player_size]

enemy_size = 40 
enemy_pos = [(random.random()*800)-enemy_size, 0]
enemy_list = [enemy_pos]

speed = 5
screen = pygame.display.set_mode((width,height), pygame.FULLSCREEN)

gameover = False 

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)
myFont2 = pygame.font.SysFont("monospace", 20)

def set_level(score, speed):
	if score < 20:
		speed = 3

	elif score < 40:
		speed = 4

	elif score < 60:
		speed = 5

	elif score < 80: 
		speed = 6

	else:
		speed = 15

	return speed

def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list)<10 and delay < 0.1:

		x_pos = (random.random()*800)-enemy_size
		y_pos = 0

		enemy_list.append([x_pos,y_pos])


def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:

		pygame.draw.rect(screen, blue, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def update_enemy_pos(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):

		if ((enemy_pos[1]>=0) and (enemy_pos[1] < height)):
			enemy_pos[1]+= speed

		else:
			enemy_list.pop(idx)
			score +=1

	return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(player_pos, enemy_pos):
			return True

	return False

def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):

			return True

	return False

while not gameover:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT:
				x-= player_size 

			elif event.key == pygame.K_RIGHT:
				x+=player_size

			player_pos = [x,y]

	screen.fill(background)

	drop_enemies(enemy_list)
	score = update_enemy_pos(enemy_list, score)
	speed = set_level(score,speed)

	text = "Score: " + str(score)
	label = myFont.render(text,1,yellow)
	screen.blit(label, (width-200, height-40))

	text_me = "By Aaditya Mohapatra"
	label_2 = myFont2.render(text_me,1,yellow)
	screen.blit(label_2, (width-250, height-60))
	
	if collision_check(enemy_list, player_pos):
		gameover = True
		break

	draw_enemies(enemy_list)

	pygame.draw.rect(screen, red, (player_pos[0],player_pos[1], player_size, player_size))

	clock.tick(60)
	pygame.display.update()
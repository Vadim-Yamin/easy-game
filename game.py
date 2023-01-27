import pygame as pg
import os
pg.init()

W,H = 720, 1500

Red = (250,0,0)

display = pg.display.set_mode((W,H))

#background = pg.image.load("background.png")

enemy_x = 100
enemy_y = 500
enemy_y2 = 1450
enemy_x = 150
enemy_x2 = 380
enemy_x3 = 665
enemy_speed = 3
enemy_list = []
enemy_timer = pg.USEREVENT + 1
pg.time.set_timer(enemy_timer, 2000)

def push(but):
	keys = pg.mouse.get_pressed()
	mouse = pg.mouse.get_pos()
	if but.x < mouse[0] < but.x+but.w:
		if but.y < mouse[1] < but.y+but.h:
			if keys[0] == 1:
				return True

score = 0

arial_black = pg.font.SysFont("arial black", 64)



def add_score(score):
	score += 1

x = W//2
y = H//2
speed=5
up = pg.Rect((270,1100), (200,100))
down = pg.Rect((270,1250), (200,100))
right = pg.Rect((500,1250), (200,100))
left = pg.Rect((0,1250), (200,100))

run = True

while run:
	display.fill((0,0,255))
	#display.blit(background (0,0))
	
	score_text = arial_black.render(f"Счёт: {score}",1,(255,0,0))
	display.blit(score_text, (275, 100))
	enemy_y += enemy_speed
	enemy_y2 += enemy_speed
	
	enemy2 = pg.draw.circle(display,(255,0,0), (10000,10000), 100)

	enemy3 = pg.draw.circle(display,(255,0,0), (10000,10000), 100)
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			
		
	enemy1 = pg.draw.circle(display,(255,0,0), (enemy_x,enemy_y), 75)
	enemy2 = pg.draw.circle(display,(255,0,0), (enemy_x2, enemy_y2), 75)
	enemy3 = pg.draw.circle(display,(255,0,0), (enemy_x3,enemy_y), 75)
	
	player = pg.draw.circle(display,(0,255,0), (x,y), 50)	
	enemy = pg.draw.circle(display,(255,0,0), (enemy_x,enemy_y), 75)
	enemy1 = pg.draw.circle(display,(255,0,0), (10000,10000), 75)	
    
	if player.colliderect(enemy) or player.colliderect(enemy1) or player.colliderect(enemy2) or player.colliderect(enemy3):
	    exit()

	if push(up):
		y-=speed
	if push(down):
		y+=speed
	if push(left):
		x-=speed
	if push(right):
		x+=speed
	
	if x-50 < 0:
		x = 50
	elif x+50 > 720:
		x =720-50
	elif y-50 < 0:
		y = 50
	elif y+50 > 1500:
		y = 1500-50

	if enemy_y-50 < 0:
		enemy_y = 50
	elif enemy_y+50 > 1500:
		enemy_y -= 1300
		enemy_speed += 0.01
		score += 1
	
	if enemy_y2-50 < 0:
		enemy_y2 = 50
		score += 1
	elif enemy_y2+50 > 1700:
		add_score(score)
		enemy_speed += 0.01
		enemy_y2 -= 1650
    
	display.fill((Red), up)
	display.fill((Red), down)
	display.fill((Red), right)
	display.fill((Red), left)
	pg.display.update()

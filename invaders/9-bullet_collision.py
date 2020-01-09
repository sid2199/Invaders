import pygame as pg
from random import randint as ri
import math as m
pg.init()

score = 0
screen = pg.display.set_mode((800, 600))
logo = pg.image.load("LOGO.png")
pg.display.set_icon(logo)
pg.display.set_caption("Invaders!!")
background = pg.image.load("back.jpg")


player_img = pg.image.load("player.png")
bullet_img = pg.image.load("bullet.png")
enemy_img = pg.image.load("alien.png")


playerX = 360
playerY = 500
playerX_change = 0
playerY_change = 0

enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
	enemy_img.append(pg.image.load("alien.png"))
	enemyX.append(ri(0, 600))
	enemyY.append(ri(10, 400))
	enemyX_change .append(5)
	enemyY_change.append(30)

bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x, y):
	screen.blit(player_img, (x, y))

def enemy(x, y, i):
	screen.blit(enemy_img[i], (x, y))

def fire(x, y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bullet_img, (x+16, y+15))

def hit(enemyX, enemyY, bulletX, bulletY):
	distance = m.sqrt((m.pow(enemyX - bulletX, 2)) + (m.pow(enemyY - bulletY, 2)))
	if distance < 27:
		return True
	else:
		return False

running = True
while running:
	screen.fill((255, 0, 0))
	screen.blit(background, (0, 0))
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_LEFT:
				playerX_change = -5
			if event.key == pg.K_RIGHT:
				playerX_change = 5
			if event.key == pg.K_SPACE:
				if bullet_state == "ready":
					bulletX = playerX
					fire(bulletX, bulletY)
		if event.type == pg.KEYUP:
			if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
				playerX_change = 0
	playerX += playerX_change
	
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	for i in range(number_of_enemies):
		enemyX[i] += enemyX_change[i]
		if enemyX[i] <= 0:
			enemyX_change[i] = 5
			enemyY[i] +=30
		elif enemyX[i] >= 736:
			enemyX_change[i] = -5
			enemyY[i]+=enemyY_change[i]

		collision = hit(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision:
			bulletY = 500
			bullet_state = "ready"
			score += 1
			enemyX[i] = ri(0, 600)
			enemyY[i] = ri(10, 400)
			print(score)
		enemy(enemyX[i], enemyY[i], i)

	if bullet_state == "fire":
		fire(bulletX, bulletY)
		bulletY -= bulletY_change
		if bulletY <= 0:
			bullet_state = "ready"
			bulletY = 500

	if bullet_state == "ready":
		screen.blit(bullet_img, (768, 0))

	collision = hit(enemyX[i], enemyY[i], bulletX, bulletY)
	if collision:
		bulletY = 500
		bullet_state = "ready"
		score += 1
		enemyX = ri(0, 600)
		enemyY = ri(10, 400)
		print(score)
	player(playerX, playerY)
	
	pg.display.update()
"""шаблон Pygame"""
import pygame

#задаем параметры окна экрана
WIDTH = 800
HEIGHT = 800

# можно задать цвета
BLACK = (0,0,0)
WHITE = (255,255,255)

#ФПС
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("name")
clock = pygame.time.Clock()
coordinates = [(100,100),(200,200)]


running = True
while running:
	screen.fill(BLACK)	

	for i in coordinates:
		pygame.draw.rect(screen,
						(0,255,0),
						(i[0],i[1], 20,20))





	for event in pygame.event.get():
# проверяем закрывшееся окно
		if event.type == pygame.QUIT:
		    running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP_ENTER:
				print('ok')
			
	pygame.display.flip()


pygame.quit()

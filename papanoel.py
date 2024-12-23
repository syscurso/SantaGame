import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Papa Noel')

fondo_img = pygame.image.load('background.png')
fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))

santa_img = pygame.image.load("santa.png")
santa_img = pygame.transform.scale(santa_img, (80, 80))
regalo_img = pygame.image.load("gift.png")
regalo_img = pygame.transform.scale(regalo_img, (50, 50))

reloj = pygame.time.Clock()
santa_x, santa_y = ANCHO // 2, ALTO - 100
regalos = [{"x": random.randint(0, ANCHO - 50), "y" : -50}]
puntaje = 0

while True:
    pantalla.blit(fondo_img, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and santa_x > 0:
        santa_x -= 10
    if teclas[pygame.K_RIGHT] and santa_x < ANCHO -80:
        santa_x += 10

    for regalo in regalos[:]:
        regalo["y"] += 5
        if regalo["y"] > ALTO:
            pygame.quit()
            sys.exit()
        if santa_x < regalo["x"] + 50 and santa_x + 80 > regalo["x"] and santa_y < regalo["y"] + 50 and santa_y + 80 > regalo["y"]:
            regalos.remove(regalo)
            puntaje += 1
    
    if random.randint(1,50) == 1:
        regalos.append({"x": random.randint(0, ANCHO - 50), "y" : -50})
        
    pantalla.blit(santa_img, (santa_x, santa_y))
    for regalo in regalos:

        pantalla.blit(regalo_img, (regalo["x"], regalo["y"]))

    texto = pygame.font.SysFont(None, 36).render(f"Puntaje: {puntaje}", True, (0,0,0))
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(30)
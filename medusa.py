import math
import pygame

WIDTH = 800
HEIGHT = 800

# Resolución interna para suavizado (más grande)
SCALE = 2
W2 = WIDTH * SCALE
H2 = HEIGHT * SCALE

t = 0
buffer = pygame.Surface((W2, H2))  # superficie de dibujo grande

def update():
    global t
    t += math.pi / 45

def draw():
    global buffer

    # fondo semitransparente para efecto de desvanecimiento
    fade = pygame.Surface((W2, H2))
    fade.set_alpha(30)
    fade.fill((0, 0, 0))
    buffer.blit(fade, (0, 0))

    for i in range(10000):
        x = i % 200
        y = i / 55

        k = 9 * math.cos(x / 8)
        e = y / 8 - 12.5
        d = (k**2 + e**2)**0.5 / 99 + math.sin(t) / 6 + 0.5

        angle = math.atan2(k, e) * 7
        q = 99 - e * math.sin(angle) / d + k * (3 + math.cos(d * d - t) * 2)
        c = d / 2 + e / 69 - t / 16

        px = q * math.sin(c) * SCALE + W2 // 2
        py = (q + 19 * d) * math.cos(c) * SCALE + H2 // 2

        if 0 <= px < W2 and 0 <= py < H2:
            buffer.set_at((int(px), int(py)), (255, 255, 255))

    # Escalar suavizado hacia la ventana original
    smooth = pygame.transform.smoothscale(buffer, (WIDTH, HEIGHT))
    screen.blit(smooth, (0, 0))

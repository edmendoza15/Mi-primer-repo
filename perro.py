import pygame
import sys

pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configuración de la pantalla
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Definir la velocidad de la serpiente
snake_speed = 15
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = pygame.KEYDOWN

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*snake_speed)) % width), (cur[1] + (y*snake_speed)) % height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = pygame.KEYDOWN

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, WHITE, (p[0], p[1], snake_size, snake_size))
snake = Snake()
snake_size = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.direction = (1, 0)

    snake.update()

    screen.fill(BLACK)
    snake.render(screen)
    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()
sys.exit()

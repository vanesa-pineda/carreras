import pygame

# Configuración de la ventana
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Laberinto Mejorado')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)

# Tamaño de las celdas
CELL_SIZE = 50

# Laberinto: 1 es pared, 0 es camino libre
laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Posiciones del jugador (inicio) y meta (final)
start_pos = [1, 1]  # Posición inicial
end_pos = [8, 8]  # Posición final
player_pos = list(start_pos)

# Reloj para controlar la velocidad
clock = pygame.time.Clock()

# Función para dibujar el laberinto con mejores gráficas
def draw_maze():
    for row in range(len(laberinto)):
        for col in range(len(laberinto[row])):
            color = WHITE if laberinto[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, LIGHT_BLUE, (col * CELL_SIZE + 3, row * CELL_SIZE + 3, CELL_SIZE - 6, CELL_SIZE - 6))  # Sombras ligeras

    # Dibujar el inicio (en verde) con bordes redondeados
    pygame.draw.rect(screen, GREEN, (start_pos[1] * CELL_SIZE, start_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.circle(screen, (0, 200, 0), (start_pos[1] * CELL_SIZE + CELL_SIZE // 2, start_pos[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)

    # Dibujar el final (en rojo) con bordes redondeados
    pygame.draw.rect(screen, RED, (end_pos[1] * CELL_SIZE, end_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.circle(screen, (200, 0, 0), (end_pos[1] * CELL_SIZE + CELL_SIZE // 2, end_pos[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)

    # Dibujar al jugador (círculo azul con sombra)
    pygame.draw.circle(screen, BLUE, (player_pos[1] * CELL_SIZE + CELL_SIZE // 2, player_pos[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
    pygame.draw.circle(screen, (0, 0, 128), (player_pos[1] * CELL_SIZE + CELL_SIZE // 2 + 2, player_pos[0] * CELL_SIZE + CELL_SIZE // 2 + 2), CELL_SIZE // 3)

# Comprobar si el jugador ha llegado a la meta
def check_win():
    return player_pos == end_pos

# Mensaje de fin de juego
def game_over():
    font = pygame.font.SysFont('Arial', 48)
    text = font.render('¡Ganaste!', True, GREEN)
    screen.blit(text, (250, 250))
    pygame.display.flip()

# Bucle principal
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        new_pos = [player_pos[0], player_pos[1] - 1]
        if laberinto[new_pos[0]][new_pos[1]] == 0:
            player_pos = new_pos
    if keys[pygame.K_RIGHT]:
        new_pos = [player_pos[0], player_pos[1] + 1]
        if laberinto[new_pos[0]][new_pos[1]] == 0:
            player_pos = new_pos
    if keys[pygame.K_UP]:
        new_pos = [player_pos[0] - 1, player_pos[1]]
        if laberinto[new_pos[0]][new_pos[1]] == 0:
            player_pos = new_pos
    if keys[pygame.K_DOWN]:
        new_pos = [player_pos[0] + 1, player_pos[1]]
        if laberinto[new_pos[0]][new_pos[1]] == 0:
            player_pos = new_pos

    # Comprobar si se ha ganado
    if check_win():
        game_over()
        pygame.time.delay(2000)  # Espera 2 segundos para que el jugador vea el mensaje antes de cerrar el juego
        running = False
    
    draw_maze()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()

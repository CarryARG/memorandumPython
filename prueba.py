import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Memory Game")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración del juego
FILAS = 4
COLUMNAS = 4
CARTA_ANCHO = 150
CARTA_ALTO = 150
ESPACIO_ENTRE_CARTAS = 10

# Función para crear el tablero
def crear_tablero():
    simbolos = ["imagen1", "imagen2", "imagen3", "imagen4", "imagen5", "imagen6", "imagen7", "imagen8"]  # Lista de nombres de imágenes
    simbolos = simbolos[:FILAS * COLUMNAS // 2]
    cartas = simbolos * 2
    
    random.shuffle(cartas)
    
    tablero = [cartas[i:i+COLUMNAS] for i in range(0, FILAS * COLUMNAS, COLUMNAS)]
    return tablero

# Inicialización del juego
tablero = crear_tablero()
seleccionadas = []
cartas_volteadas = []

# Cargar imágenes de las cartas
imagenes_cartas = {}
for carta in set(sum(tablero, [])):
    imagen = pygame.image.load(f'E:\Todo\Memorandum-Python\{carta}.jpg')  # Reemplaza 'imagenes/' con la ruta a tus imágenes
    imagen = pygame.transform.scale(imagen, (CARTA_ANCHO, CARTA_ALTO))
    imagenes_cartas[carta] = imagen

# Loop del juego
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            fila = mouseY // (CARTA_ALTO + ESPACIO_ENTRE_CARTAS)
            columna = mouseX // (CARTA_ANCHO + ESPACIO_ENTRE_CARTAS)
            
            if len(seleccionadas) < 2 and (fila, columna) not in seleccionadas:
                seleccionadas.append((fila, columna))
                if len(seleccionadas) == 2:
                    carta1 = tablero[seleccionadas[0][0]][seleccionadas[0][1]]
                    carta2 = tablero[seleccionadas[1][0]][seleccionadas[1][1]]
                    
                    if carta1 == carta2:
                        cartas_volteadas.extend(seleccionadas)
                        seleccionadas = []
                    else:
                        pygame.time.wait(100)
                        seleccionadas = []
    
    PANTALLA.fill(BLANCO)
    
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            x = columna * (CARTA_ANCHO + ESPACIO_ENTRE_CARTAS)
            y = fila * (CARTA_ALTO + ESPACIO_ENTRE_CARTAS)
            
            if (fila, columna) in cartas_volteadas:
                carta = tablero[fila][columna]
                PANTALLA.blit(imagenes_cartas[carta], (x, y))
            elif (fila, columna) in seleccionadas:
                carta = tablero[fila][columna]
                PANTALLA.blit(imagenes_cartas[carta], (x, y))
            else:
                pygame.draw.rect(PANTALLA, NEGRO, (x, y, CARTA_ANCHO, CARTA_ALTO))
    
    pygame.display.flip()
    reloj.tick(60)
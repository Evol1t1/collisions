import pygame

# --- Константы ---
WIDTH = 860
HEIGHT = 573
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
RECT_WIDTH = 50
RECT_HEIGHT = 50
IMPULSE = 0.90
BACKGROUND_IMAGE = "image\kai.png"  # Имя файла фонового изображения

# --- Классы ---
class RectangleObject:
    def __init__(self, x, y, color, speed_x, speed_y):
        self.rect = pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT)
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.handle_screen_edge_bounce()  # Обработка отскока от границ

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def handle_screen_edge_bounce(self):
        """Отскок от границ экрана."""
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1

def check_collision(rect1, rect2):
    """Проверяет, пересекаются ли два прямоугольника (pygame.Rect)."""
    return rect1.colliderect(rect2)


# --- Инициализация Pygame ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Collision")

# --- Загрузка изображения фона ---
background = pygame.image.load(BACKGROUND_IMAGE)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# --- Создание объектов ---
rect1 = RectangleObject(100, 100, RED, 5, 3)
rect2 = RectangleObject(400, 400, BLUE, 0, 0)  # Изначально неподвижен

# --- Игровой цикл ---
running = True
while running:
    # --- Обработка событий ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Движение и обработка столкновений ---
    rect1.move()
    rect2.move()

    if check_collision(rect1.rect, rect2.rect):
        # Передача импульса
        temp_speed_x = rect1.speed_x
        temp_speed_y = rect1.speed_y

        rect1.speed_x = rect2.speed_x * IMPULSE
        rect1.speed_y = rect2.speed_y * IMPULSE

        rect2.speed_x = temp_speed_x * IMPULSE
        rect2.speed_y = temp_speed_y * IMPULSE

        # Корректировка позиции (небольшой сдвиг после столкновения)
        rect1.move()
        rect2.move()

    # --- Отрисовка ---
    screen.blit(background, (0, 0))  # Рисуем фон перед всем остальным
    rect1.draw(screen)
    rect2.draw(screen)
    pygame.display.flip()

# --- Завершение Pygame ---
pygame.quit()
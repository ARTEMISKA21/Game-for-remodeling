import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана и карты
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
MAP_WIDTH, MAP_HEIGHT = 1000, 1200

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Загрузка изображений
background = pygame.image.load('background.png').convert()
player_image = pygame.image.load('player.png').convert_alpha()
jump_image = pygame.image.load('jump.png').convert_alpha()
right_image = pygame.image.load('right.png').convert_alpha()
left_image = pygame.image.load('left.png').convert_alpha()
up_image = pygame.image.load('up.png').convert_alpha()
menu_image = pygame.image.load('menu.png').convert_alpha()
menu_image1 = pygame.image.load('menu1.png').convert_alpha()  # Новое изображение меню
change_player_image = pygame.image.load('change_player.png').convert_alpha()  # Новое изображение игрока

# Параметры игрока
player_x, player_y = 400, 300
speed = 5

# Параметры камеры
camera_x, camera_y = 0, 0
camera_speed = 0.1

# Изображение для меню (изначально стандартное)
menu_images = [menu_image, menu_image, menu_image]

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение персонажа
    keys = pygame.key.get_pressed()
    current_image = player_image  # Устанавливаем стандартное изображение

    if keys[pygame.K_w]:  # Вверх
        player_y -= speed
        current_image = up_image
    elif keys[pygame.K_a]:  # Влево
        player_x -= speed
        current_image = left_image
    elif keys[pygame.K_s]:  # Вниз
        player_y += speed
        current_image = player_image
    elif keys[pygame.K_d]:  # Вправо
        player_x += speed
        current_image = right_image
    elif keys[pygame.K_SPACE]:  # Прыжок
        current_image = jump_image

    # Обработка нажатий клавиш для изменения меню и изображений игрока
    if keys[pygame.K_l]:  # Меняем первую картинку меню
        menu_images[0] = menu_image1
    if keys[pygame.K_1]:  # Меняем изображение персонажа
        current_image = change_player_image
    elif keys[pygame.K_2] or keys[pygame.K_3]:  # Оставляем стандартное изображение
        current_image = player_image

    # Ограничение перемещения игрока в пределах карты
    player_x = max(0, min(player_x, MAP_WIDTH - player_image.get_width()))
    player_y = max(0, min(player_y, MAP_HEIGHT - player_image.get_height()))

    # Обновление позиции камеры
    camera_x = player_x - SCREEN_WIDTH // 2 + player_image.get_width() // 2
    camera_y = player_y - SCREEN_HEIGHT // 2 + player_image.get_height() // 2

    # Ограничение камеры в пределах карты
    camera_x = max(0, min(camera_x, MAP_WIDTH - SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, MAP_HEIGHT - SCREEN_HEIGHT))

    # Отображение фонового изображения
    for x in range(-1, (SCREEN_WIDTH // 300) + 2):
        for y in range(-1, (SCREEN_HEIGHT // 300) + 2):
            screen.blit(background, (x * 300 - camera_x, y * 300 - camera_y))
    
    # Отображение игрока
    screen.blit(current_image, (player_x - camera_x, player_y - camera_y))

    # Отображение меню игрока
    menu_pos_x = 20  # X-координата меню
    menu_pos_y = SCREEN_HEIGHT - 100  # Y-координата меню
    spacing = 10  # Промежуток между изображениями
    menu_image_width = menu_images[0].get_width()

    for i in range(3):
        screen.blit(menu_images[i], (menu_pos_x + i * (menu_image_width + spacing), menu_pos_y))

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Ограничение до 60 кадров в секунду

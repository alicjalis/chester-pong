import pygame

pygame.init()
size = (800,600)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Chester-pong")

# obrazki
game_icon = pygame.image.load("images/chester_icon.png")
chips_pizza = pygame.image.load("images/chips_pizza.png")
chip_size = (60, 40)
chips_pizza = pygame.transform.scale(chips_pizza, chip_size)
pygame.display.set_icon(game_icon)

WHITE = (255,255,255)
RED = (255, 0 , 0)
DARK_MODE = "#34495E"
DARK_PADDLE = "#7d7d7d"

# paletka
speed = 7
paddle_width = 200
paddle_height = 40
paddle_x = 300
paddle_y = 500
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# siatka chipsow
chips = []
rows, cols = 6, 15
chip_width, chip_height = chip_size
padding = 1
start_x = (size[0] - (cols * (chip_width + padding) - padding)) // 2
start_y = 10

for row in range(rows):
    for col in range(cols):
        chip_x = start_x + col * (chip_width + padding)
        chip_y = start_y + row * (chip_height + padding)
        chips.append((chip_x, chip_y))


running = True
while running:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= speed

    if keys[pygame.K_RIGHT] and paddle.right < size[0]:
        paddle.x += speed



    window.fill(DARK_MODE)
    for chip_x, chip_y in chips:
        window.blit(chips_pizza, (chip_x, chip_y))

    pygame.draw.rect(window, DARK_PADDLE, paddle)
    pygame.display.update()

pygame.quit()



import colors
import pygame

from random import randint

WINDOW_HEIGHT = 840
WINDOW_WIDTH = 800
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT

SEGMENT_SIZE = 20

KEY_MAP = {
    273: "Up",
    274: "Down",
    275: "Right",
    276: "Left"
}

pygame.init()
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)


def check_collisions(snake_positions):
    head_x_position, head_y_position = snake_positions[0]

    return (
        head_x_position in (-20, WINDOW_WIDTH )
        or head_y_position in (20, WINDOW_HEIGHT)
        or (head_x_position, head_y_position) in snake_positions[1:]
    )


def check_food_collision(snake_positions, food_position):
    if snake_positions[0] == food_position:
        snake_positions.append(snake_positions[-1])

        return True


def draw_objects(snake_positions, food_position):
    pygame.draw.rect(screen, colors.FOOD, [food_position, (SEGMENT_SIZE, SEGMENT_SIZE)])

    for x, y in snake_positions:
        pygame.draw.rect(screen, colors.SNAKE, [x, y, SEGMENT_SIZE, SEGMENT_SIZE])


def move_snake(snake_positions, direction):
    head_x_position, head_y_position = snake_positions[0]

    if direction == "Left":
        new_head_position = (head_x_position - SEGMENT_SIZE, head_y_position)
    elif direction == "Right":
        new_head_position = (head_x_position + SEGMENT_SIZE, head_y_position)
    elif direction == "Down":
        new_head_position = (head_x_position, head_y_position + SEGMENT_SIZE)
    elif direction == "Up":
        new_head_position = (head_x_position, head_y_position - SEGMENT_SIZE)

    snake_positions.insert(0, new_head_position)
    del snake_positions[-1]


def on_key_press(event, current_direction):
    key = event.__dict__["key"]
    new_direction = KEY_MAP.get(key)

    all_directions = ("Up", "Down", "Left", "Right")
    opposites = ({"Up", "Down"}, {"Left", "Right"})

    if (new_direction in all_directions
    and {new_direction, current_direction} not in opposites):
        return new_direction

    return current_direction


def set_new_food_position(snake_positions):
    while True:
        x_position = randint(0, 39) * SEGMENT_SIZE
        y_position = randint(2, 41) * SEGMENT_SIZE
        food_position = (x_position, y_position)

        if food_position not in snake_positions:
            return food_position


def play_game():
    score = 0

    current_direction = "Right"
    snake_positions = [(100, 100), (80, 100), (60, 100)]
    food_position = set_new_food_position(snake_positions)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                current_direction = on_key_press(event, current_direction)

        screen.fill(colors.BACKGROUND)
        draw_objects(snake_positions, food_position)

        font = pygame.font.Font(None, 28)
        text = font.render(f"Score: {score}", True, colors.TEXT)
        screen.blit(text, (10, 10))

        pygame.display.update()

        move_snake(snake_positions, current_direction)

        if check_collisions(snake_positions):
            return

        if check_food_collision(snake_positions, food_position):
            food_position = set_new_food_position(snake_positions)
            score += 1

        clock.tick(30)


play_game()
import pygame
import time
import random
from pygame.locals import *

SIZE = 40


class Apple:
    def __init__(self, surface):
        self.parent_screen = surface
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 25)*SIZE
        self.y = random.randint(1, 12)*SIZE


class Snake:
    def __init__(self, surface, length):
        self.parent_screen = surface
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'

        self.length = length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill((232, 125, 134))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def display_score(self):
        font = pygame.font.SysFont('arial', 20)
        score = font.render(f"Score: {self.snake.length}",True, (0,0,0))
        self.surface.blit(score,(850,5))

    def show_game_over(self):
        self.surface.fill((252, 3, 3))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is Over!!! Your Score is {self.snake.length}", True, (0,0,0))
        self.surface.blit(line1,(200,300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (0,0,0))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        for i in range(2,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise Exception("Collision Occured")

        if self.snake.x[0]> 1000 or self.snake.x[0]<0 or self.snake.y[0]> 800 or self.snake.y[0]> 800:
            raise Exception("Game Over")

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)


if __name__ == '__main__':
    game = Game()
    game.run()

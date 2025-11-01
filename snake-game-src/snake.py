import pygame as pg
from game.settings import *
from game.snake import Snake
from game.apple import spawn

def main():
    screen = pg.display.set_mode(WSIZE)
    clock = pg.time.Clock()

    snake = Snake(start_pos=(MSIZE[0]//2, MSIZE[1]//2))
    apple = spawn(MSIZE, snake.body)
    fps = FPS_START

    running = True
    while running:
        clock.tick(fps)
        screen.fill(COLOR_BG)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if snake.alive:
                    if event.key == pg.K_RIGHT and snake.direction != 2:
                        snake.direction = 0
                    if event.key == pg.K_DOWN and snake.direction != 3:
                        snake.direction = 1
                    if event.key == pg.K_LEFT and snake.direction != 0:
                        snake.direction = 2
                    if event.key == pg.K_UP and snake.direction != 1:
                        snake.direction = 3
                else:
                    if event.key == pg.K_SPACE:
                        snake = Snake(start_pos=(MSIZE[0]//2, MSIZE[1]//2))
                        apple = spawn(MSIZE, snake.body)
                        fps = FPS_START

        snake.move(MSIZE)

        if snake.body[0] == apple:
            snake.grow()
            apple = spawn(MSIZE, snake.body)
            fps += 1

        for x, y in snake.body:
            pg.draw.rect(screen, COLOR_SNAKE, (x*TSIDE, y*TSIDE, TSIDE-1, TSIDE-1))
        pg.draw.rect(screen, COLOR_APPLE, (apple[0]*TSIDE, apple[1]*TSIDE, TSIDE-1, TSIDE-1))

        screen.blit(FONT_SCORE.render(f"Score: {len(snake.body)}", True, COLOR_SCORE),
                    (5, 5))
        if not snake.alive:
            screen.blit(FONT_GAMEOVER.render("GAME OVER", True, COLOR_TEXT),
                        (WSIZE[0]//2 - 100, WSIZE[1]//2 - 50))
            screen.blit(FONT_SPACE.render("Press SPACE to restart", True, COLOR_TEXT),
                        (WSIZE[0]//2 - 100, WSIZE[1]//2 + 10))

        pg.display.flip()

if __name__ == "__main__":
    main()

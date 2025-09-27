# snake.py
import pygame, sys
from snake_logic import SnakeGame, CELL, COLS, ROWS, DIRS

FPS = 10
WIDTH, HEIGHT = COLS*CELL, ROWS*CELL

def draw_rect(screen, color, pos):
    x, y = pos
    pygame.draw.rect(screen, color, (x*CELL, y*CELL, CELL-1, CELL-1), border_radius=4)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake (pygame)")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    big_font = pygame.font.SysFont(None, 56)

    game = SnakeGame()

    while True:
        clock.tick(FPS)

        # --- 입력(GUI 전용) ---
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
                if game.game_over and e.key == pygame.K_r:
                    game.reset(); continue
                if e.key in (pygame.K_UP, pygame.K_w):    game.turn(DIRS["UP"])
                elif e.key in (pygame.K_DOWN, pygame.K_s): game.turn(DIRS["DOWN"])
                elif e.key in (pygame.K_LEFT, pygame.K_a): game.turn(DIRS["LEFT"])
                elif e.key in (pygame.K_RIGHT, pygame.K_d):game.turn(DIRS["RIGHT"])

        # --- 로직 호출(한 줄) ---
        game.step()

        # --- 그리기(GUI 전용) ---
        screen.fill((18, 18, 18))
        draw_rect(screen, (220, 70, 70), game.apple)
        for i, p in enumerate(game.snake):
            color = (60, 200, 120) if i else (100, 255, 160)
            draw_rect(screen, color, p)
        score_surf = font.render(f"Score: {game.score}", True, (240, 240, 240))
        screen.blit(score_surf, (10, 8))

        if game.game_over:
            txt = big_font.render("GAME OVER", True, (255, 220, 220))
            tip = font.render("R: 재시작   ESC: 종료", True, (230, 230, 230))
            screen.blit(txt, txt.get_rect(center=(WIDTH//2, HEIGHT//2 - 20)))
            screen.blit(tip, tip.get_rect(center=(WIDTH//2, HEIGHT//2 + 20)))

        pygame.display.flip()

if __name__ == "__main__":
    main()
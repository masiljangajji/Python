# snake.py
import pygame, random, sys

# ===== 설정 =====
CELL = 20                 # 한 칸 픽셀 크기
COLS, ROWS = 30, 20       # 보드 크기(칸)
WIDTH, HEIGHT = COLS*CELL, ROWS*CELL
FPS = 10                  # 초당 이동(난이도)

# ===== 유틸 =====
def draw_rect(screen, color, pos):
    x, y = pos
    pygame.draw.rect(screen, color, (x*CELL, y*CELL, CELL-1, CELL-1), border_radius=4)

def random_empty_cell(snake):
    while True:
        p = (random.randrange(COLS), random.randrange(ROWS))
        if p not in snake:
            return p

def reset():
    snake = [(COLS//2, ROWS//2)]
    direction = (1, 0)            # 처음엔 오른쪽
    apple = random_empty_cell(snake)
    score = 0
    return snake, direction, apple, score, False  # False = 게임오버 아님

# ===== 메인 =====
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake (pygame)")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    big_font = pygame.font.SysFont(None, 56)

    snake, direction, apple, score, game_over = reset()

    while True:
        clock.tick(FPS)

        # --- 입력 ---
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if game_over:
                    if e.key == pygame.K_r:  # R로 재시작
                        snake, direction, apple, score, game_over = reset()
                    continue

                dx, dy = direction
                if e.key in (pygame.K_UP, pygame.K_w) and dy != 1:
                    direction = (0, -1)
                elif e.key in (pygame.K_DOWN, pygame.K_s) and dy != -1:
                    direction = (0, 1)
                elif e.key in (pygame.K_LEFT, pygame.K_a) and dx != 1:
                    direction = (-1, 0)
                elif e.key in (pygame.K_RIGHT, pygame.K_d) and dx != -1:
                    direction = (1, 0)

        if not game_over:
            # --- 이동 ---
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            # 벽 충돌 체크(랩어라운드 X)
            if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
                game_over = True
            # 몸 충돌 체크
            elif new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)      # 머리 추가
                if new_head == apple:          # 사과 먹음
                    score += 1
                    apple = random_empty_cell(snake)
                else:
                    snake.pop()                # 꼬리 제거(이동)

        # --- 그리기 ---
        screen.fill((18, 18, 18))
        # 사과
        draw_rect(screen, (220, 70, 70), apple)
        # 뱀 (머리 밝게)
        for i, p in enumerate(snake):
            color = (60, 200, 120) if i else (100, 255, 160)
            draw_rect(screen, color, p)

        # 점수
        score_surf = font.render(f"Score: {score}", True, (240, 240, 240))
        screen.blit(score_surf, (10, 8))

        # 게임오버 안내
        if game_over:
            txt = big_font.render("GAME OVER", True, (255, 220, 220))
            tip = font.render("R: 재시작   ESC: 종료", True, (230, 230, 230))
            screen.blit(txt, txt.get_rect(center=(WIDTH//2, HEIGHT//2 - 20)))
            screen.blit(tip, tip.get_rect(center=(WIDTH//2, HEIGHT//2 + 20)))

        pygame.display.flip()

if __name__ == "__main__":
    main()
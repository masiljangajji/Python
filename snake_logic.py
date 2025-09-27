# snake_logic.py  — 학생용 (GUI 건드리지 말고 이 파일만 수정)
import random

# 기준 값( GUI가 import 해 사용 )
CELL = 20
COLS, ROWS = 30, 20

# 키 입력 → 방향으로 매핑할 상수 (GUI에서 사용)
DIRS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
}

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        """게임 상태 초기화"""
        # ✅ 기본은 중앙에서 시작, 오른쪽으로 이동
        self.snake = [(COLS // 2, ROWS // 2)]
        self.direction = DIRS["RIGHT"]
        # ❌ 현재는 사과가 '뱀 몸 위'에 생성될 수 있음 (Stage 4에서 고치기)
        self.apple = self._random_empty_cell_naive()
        self.score = 0
        self.game_over = False

    # ==================== 메인 업데이트: 여기 단계별로 고치기 ====================
    def step(self):
        """한 틱 진행(이동/충돌/먹이 처리). GUI는 매 프레임마다 이걸 호출함."""
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # ---------- Stage 1: 벽 충돌 규칙 만들기 ----------
        # 현재 구현: '랩어라운드(벽을 넘어가면 반대편으로 튐)'가 적용됨 → 게임오버가 절대 안 남
        # 목표: ① 기본 규칙은 "랩어라운드 X" → 벽을 넘으면 game_over = True
        #      ② 선택 과제: 랩어라운드 모드 켜기/끄기 (원한다면 bool 플래그로 확장)
        # TODO: 벽 충돌 로직 추가

        # ---------- Stage 2: 자기 몸 충돌 만들기 ----------
        # 현재 구현: 몸에 부딪혀도 게임오버가 안 됨
        # 목표: new_head가 self.snake 안에 있으면 game_over = True
        # (힌트: if new_head in self.snake: ...)
        # TODO: 자기 몸 충돌 로직 추가

        # ---------- 이동 처리 ----------
        self.snake.insert(0, new_head)

        # ---------- Stage 3: 사과 먹기 & 성장 ----------
        # 현재 구현: 사과를 먹어도 점수/성장/새 사과 생성이 없음 → 항상 꼬리를 pop 해서 길이 고정
        # 목표:
        #   1) new_head == self.apple 이면: score += 1, 사과를 비어있는 칸에 새로 배치(랜덤),
        #      그리고 '성장'을 위해 pop() 하지 않음
        #   2) 아니면 일반 이동: pop() 해서 길이 유지
        if True:  # ❌ 임시: 항상 pop → 수정 대상
            self.snake.pop()

        # ---------- Stage 4: 사과가 뱀 위에 생성되지 않게 만들기 ----------
        # 현재 self._random_empty_cell_naive()는 비어있는 칸을 보장하지 않음
        # 목표: self._random_empty_cell()을 직접 구현하고 reset()과 사과 재배치에서도 그걸 사용
        # (힌트: while True로 랜덤 좌표 뽑고, 뱀 몸에 없으면 반환)

    def turn(self, new_dir):
        """방향 전환 (반대 방향 금지)"""
        ndx, ndy = new_dir
        cdx, cdy = self.direction

        # ---------- Stage 0: 반대 방향 금지 ----------
        # 현재 구현: 바로 반대로 꺾어도 허용됨 → 자기자신과 즉시 충돌하는 버그 발생 가능
        # 목표: 새 방향이 현재 방향의 정반대라면 무시
        # (힌트: if (ndx, ndy) == (-cdx, -cdy): return)
        # TODO: 반대 방향 금지 로직 추가

        self.direction = (ndx, ndy)

    # ============================ 유틸들 ============================
    def _random_empty_cell_naive(self):
        """❌ 잘못된 버전: 뱀 몸을 무시하고 임의 좌표 반환 (Stage 4에서 교체할 것)"""
        return (random.randrange(COLS), random.randrange(ROWS))

    # TODO Stage 4: 이 함수를 직접 구현해서, '뱀 몸과 겹치지 않는' 빈 칸을 보장하자.
    def _random_empty_cell(self):
        """
        목표 구현:
            while True:
                무작위 좌표 p 생성
                p가 self.snake에 없으면 return p
        """
        # pass  # 구현 후 reset()과 사과 재배치에서 이 함수를 쓰도록 바꿔라.
        # 임시로 Naive 반환 (학생이 바꾸기 전까지 돌아는 가도록)
        return self._random_empty_cell_naive()
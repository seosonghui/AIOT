import pygame
import random
import math

# 게임 초기화
pygame.init()

# 상수 정의
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
PINK = (255, 192, 203)

# 게임 설정
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_SPEED = 8

BALL_SIZE = 20
BALL_SPEED = 6

BRICK_WIDTH = 75
BRICK_HEIGHT = 30
BRICK_ROWS = 8
BRICK_COLS = 10
BRICK_PADDING = 5

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BALL_SIZE, BALL_SIZE])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, WHITE, (BALL_SIZE//2, BALL_SIZE//2), BALL_SIZE//2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # 공의 속도 (랜덤한 각도로 시작)
        angle = random.uniform(-math.pi/3, math.pi/3)  # -60도 ~ 60도
        self.speed_x = BALL_SPEED * math.sin(angle)
        self.speed_y = -BALL_SPEED * math.cos(angle)
        
        self.stuck_to_paddle = True
        
    def update(self, paddle):
        if self.stuck_to_paddle:
            # 패들에 붙어있을 때
            self.rect.centerx = paddle.rect.centerx
            self.rect.bottom = paddle.rect.top - 1
        else:
            # 자유롭게 움직일 때
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            
            # 벽과의 충돌 검사
            if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
                self.speed_x = -self.speed_x
                
            if self.rect.top <= 0:
                self.speed_y = -self.speed_y
    
    def launch(self):
        """공을 발사"""
        self.stuck_to_paddle = False
        
    def bounce_off_paddle(self, paddle):
        """패들과의 충돌 처리"""
        # 패들의 어느 부분에 맞았는지에 따라 반사각 조정
        paddle_center = paddle.rect.centerx
        ball_center = self.rect.centerx
        
        # 패들의 중심에서 얼마나 떨어져 있는지 계산 (-1.0 ~ 1.0)
        offset = (ball_center - paddle_center) / (PADDLE_WIDTH / 2)
        
        # 새로운 각도 계산
        angle = offset * math.pi/3  # 최대 60도까지 꺾임
        speed = math.sqrt(self.speed_x**2 + self.speed_y**2)
        
        self.speed_x = speed * math.sin(angle)
        self.speed_y = -abs(speed * math.cos(angle))  # 항상 위쪽으로

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = PADDLE_SPEED
        
    def update(self):
        # 키보드 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
            
    def move_to_mouse(self, mouse_x):
        """마우스 위치로 패들 이동"""
        self.rect.centerx = mouse_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color, points=10):
        super().__init__()
        self.image = pygame.Surface([BRICK_WIDTH, BRICK_HEIGHT])
        self.image.fill(color)
        # 벽돌에 테두리 추가
        pygame.draw.rect(self.image, WHITE, (0, 0, BRICK_WIDTH, BRICK_HEIGHT), 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.points = points

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, power_type):
        super().__init__()
        self.power_type = power_type
        self.image = pygame.Surface([30, 30])
        
        # 파워업 타입별 색상
        colors = {
            'expand_paddle': GREEN,
            'multi_ball': YELLOW,
            'extra_life': RED
        }
        self.image.fill(colors.get(power_type, WHITE))
        
        # 파워업 표시
        font = pygame.font.Font(None, 20)
        text_map = {
            'expand_paddle': 'E',
            'multi_ball': 'M',
            'extra_life': '♥'
        }
        text = font.render(text_map.get(power_type, '?'), True, BLACK)
        text_rect = text.get_rect(center=(15, 15))
        self.image.blit(text, text_rect)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        
    def update(self):
        self.rect.y += self.speed

class BreakoutGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("벽돌깨기 게임")
        self.clock = pygame.time.Clock()
        
        # 게임 상태
        self.game_state = "menu"  # menu, playing, game_over, victory
        self.score = 0
        self.lives = 3
        self.level = 1
        
        # 폰트
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        # 스프라이트 그룹
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        
        # 게임 객체 초기화
        self.paddle = None
        self.reset_game()
        
    def reset_game(self):
        """게임 리셋"""
        self.all_sprites.empty()
        self.balls.empty()
        self.bricks.empty()
        self.powerups.empty()
        
        # 패들 생성
        self.paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, 
                           SCREEN_HEIGHT - 50)
        self.all_sprites.add(self.paddle)
        
        # 공 생성
        ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.balls.add(ball)
        self.all_sprites.add(ball)
        
        # 벽돌 생성
        self.create_bricks()
        
    def create_bricks(self):
        """벽돌 생성"""
        colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]
        
        start_x = (SCREEN_WIDTH - (BRICK_COLS * (BRICK_WIDTH + BRICK_PADDING) - BRICK_PADDING)) // 2
        start_y = 80
        
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = start_x + col * (BRICK_WIDTH + BRICK_PADDING)
                y = start_y + row * (BRICK_HEIGHT + BRICK_PADDING)
                
                color = colors[row % len(colors)]
                points = (BRICK_ROWS - row) * 10  # 위쪽 벽돌일수록 높은 점수
                
                brick = Brick(x, y, color, points)
                self.bricks.add(brick)
                self.all_sprites.add(brick)
    
    def handle_events(self):
        """이벤트 처리"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            elif event.type == pygame.KEYDOWN:
                if self.game_state == "menu":
                    if event.key == pygame.K_SPACE:
                        self.game_state = "playing"
                        
                elif self.game_state == "playing":
                    if event.key == pygame.K_SPACE:
                        # 공 발사
                        for ball in self.balls:
                            if ball.stuck_to_paddle:
                                ball.launch()
                                
                elif self.game_state == "game_over" or self.game_state == "victory":
                    if event.key == pygame.K_r:
                        self.restart_game()
                        
            elif event.type == pygame.MOUSEMOTION:
                if self.game_state == "playing":
                    self.paddle.move_to_mouse(event.pos[0])
                    
        return True
    
    def update(self):
        """게임 업데이트"""
        if self.game_state != "playing":
            return
            
        # 스프라이트 업데이트
        self.paddle.update()
        
        for ball in self.balls:
            ball.update(self.paddle)
            
        self.powerups.update()
        
        # 충돌 검사
        self.check_collisions()
        
        # 공이 바닥에 떨어졌는지 검사
        for ball in self.balls.copy():
            if ball.rect.top > SCREEN_HEIGHT:
                self.balls.remove(ball)
                self.all_sprites.remove(ball)
                
        # 모든 공이 사라졌는지 검사
        if len(self.balls) == 0:
            self.lives -= 1
            if self.lives <= 0:
                self.game_state = "game_over"
            else:
                # 새 공 생성
                ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
                self.balls.add(ball)
                self.all_sprites.add(ball)
                
        # 모든 벽돌이 파괴되었는지 검사
        if len(self.bricks) == 0:
            self.game_state = "victory"
            
        # 파워업이 화면 밖으로 나갔는지 검사
        for powerup in self.powerups.copy():
            if powerup.rect.top > SCREEN_HEIGHT:
                self.powerups.remove(powerup)
                self.all_sprites.remove(powerup)
    
    def check_collisions(self):
        """충돌 검사"""
        # 공과 패들 충돌
        for ball in self.balls:
            if pygame.sprite.collide_rect(ball, self.paddle) and ball.speed_y > 0:
                ball.bounce_off_paddle(self.paddle)
                
        # 공과 벽돌 충돌
        for ball in self.balls:
            hit_bricks = pygame.sprite.spritecollide(ball, self.bricks, True)
            if hit_bricks:
                ball.speed_y = -ball.speed_y
                
                for brick in hit_bricks:
                    self.score += brick.points
                    
                    # 파워업 생성 (20% 확률)
                    if random.random() < 0.2:
                        power_types = ['expand_paddle', 'multi_ball', 'extra_life']
                        power_type = random.choice(power_types)
                        powerup = PowerUp(brick.rect.centerx, brick.rect.centery, power_type)
                        self.powerups.add(powerup)
                        self.all_sprites.add(powerup)
                        
        # 패들과 파워업 충돌
        collected_powerups = pygame.sprite.spritecollide(self.paddle, self.powerups, True)
        for powerup in collected_powerups:
            self.apply_powerup(powerup.power_type)
    
    def apply_powerup(self, power_type):
        """파워업 효과 적용"""
        if power_type == 'expand_paddle':
            # 패들 확장 (임시로 더 넓게)
            self.paddle.image = pygame.Surface([PADDLE_WIDTH * 1.5, PADDLE_HEIGHT])
            self.paddle.image.fill(GREEN)
            
        elif power_type == 'multi_ball':
            # 추가 공 생성
            for _ in range(2):
                ball = Ball(self.paddle.rect.centerx, self.paddle.rect.top - 50)
                ball.stuck_to_paddle = False
                ball.speed_x = random.uniform(-BALL_SPEED, BALL_SPEED)
                ball.speed_y = -BALL_SPEED
                self.balls.add(ball)
                self.all_sprites.add(ball)
                
        elif power_type == 'extra_life':
            # 생명 추가
            self.lives += 1
    
    def restart_game(self):
        """게임 재시작"""
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_state = "playing"
        self.reset_game()
    
    def draw(self):
        """화면 그리기"""
        self.screen.fill(BLACK)
        
        if self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "playing":
            self.draw_game()
        elif self.game_state == "game_over":
            self.draw_game_over()
        elif self.game_state == "victory":
            self.draw_victory()
            
        pygame.display.flip()
    
    def draw_menu(self):
        """메뉴 화면 그리기"""
        title = self.font_large.render("벽돌깨기", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
        self.screen.blit(title, title_rect)
        
        instruction = self.font_medium.render("SPACE를 눌러서 시작", True, WHITE)
        inst_rect = instruction.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(instruction, inst_rect)
        
        controls = [
            "조작법:",
            "← → 화살표키 또는 마우스로 패들 이동",
            "SPACE로 공 발사"
        ]
        
        for i, text in enumerate(controls):
            rendered = self.font_small.render(text, True, WHITE)
            rect = rendered.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80 + i*30))
            self.screen.blit(rendered, rect)
    
    def draw_game(self):
        """게임 화면 그리기"""
        # 모든 스프라이트 그리기
        self.all_sprites.draw(self.screen)
        
        # UI 정보 그리기
        score_text = self.font_medium.render(f"점수: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        lives_text = self.font_medium.render(f"생명: {self.lives}", True, WHITE)
        self.screen.blit(lives_text, (10, 50))
        
        level_text = self.font_medium.render(f"레벨: {self.level}", True, WHITE)
        self.screen.blit(level_text, (SCREEN_WIDTH - 150, 10))
        
        # 공이 패들에 붙어있으면 안내 메시지
        for ball in self.balls:
            if ball.stuck_to_paddle:
                hint = self.font_small.render("SPACE를 눌러 공을 발사하세요", True, YELLOW)
                hint_rect = hint.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                self.screen.blit(hint, hint_rect)
                break
    
    def draw_game_over(self):
        """게임 오버 화면 그리기"""
        # 반투명 오버레이
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        game_over = self.font_large.render("게임 오버", True, RED)
        go_rect = game_over.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
        self.screen.blit(game_over, go_rect)
        
        final_score = self.font_medium.render(f"최종 점수: {self.score}", True, WHITE)
        fs_rect = final_score.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(final_score, fs_rect)
        
        restart = self.font_medium.render("R을 눌러서 다시 시작", True, WHITE)
        r_rect = restart.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
        self.screen.blit(restart, r_rect)
    
    def draw_victory(self):
        """승리 화면 그리기"""
        # 반투명 오버레이
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        victory = self.font_large.render("승리!", True, GREEN)
        v_rect = victory.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
        self.screen.blit(victory, v_rect)
        
        final_score = self.font_medium.render(f"최종 점수: {self.score}", True, WHITE)
        fs_rect = final_score.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(final_score, fs_rect)
        
        restart = self.font_medium.render("R을 눌러서 다시 시작", True, WHITE)
        r_rect = restart.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
        self.screen.blit(restart, r_rect)
    
    def run(self):
        """게임 메인 루프"""
        running = True
        
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
        pygame.quit()

# 게임 실행
if __name__ == "__main__":
    game = BreakoutGame()
    game.run()
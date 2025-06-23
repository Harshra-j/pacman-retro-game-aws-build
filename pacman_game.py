import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 330
UI_BAR_HEIGHT = 30
FPS = 30
CELL_SIZE = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 100, 255)
NEON_BLUE = (0, 150, 255)
GLOW_BLUE = (100, 200, 255)
RED = (255, 0, 0)
PINK = (255, 184, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 184, 82)
VULNERABLE_BLUE = (0, 0, 255)

# Enhanced maze layout for Google Doodle style (46x20 grid)
MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,1,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,2,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1],
    [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,1],
    [1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1,1,1,4,4,4,4,4,4,4,1,1,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1],
    [1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,2,1,4,4,4,4,4,4,4,4,4,4,4,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,2,1,2,1,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,1,2,1,2,1,0,0,0,0,0,0],
    [1,1,1,1,1,1,2,1,2,1,4,4,4,4,4,2,1,1,1,0,0,0,0,0,0,0,1,1,1,2,4,4,4,4,4,1,2,1,2,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,2,0,2,1,4,4,4,4,4,2,1,0,0,0,0,0,0,0,0,0,0,0,1,2,4,4,4,4,4,1,2,0,2,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,2,1,2,1,4,4,4,4,4,2,1,0,0,0,0,0,0,0,0,0,0,0,1,2,4,4,4,4,4,1,2,1,2,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,2,1,2,1,4,4,4,4,4,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,4,4,4,4,4,1,2,1,2,1,0,0,0,0,0,0],
    [1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1],
    [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,2,1,1],
    [1,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1,1],
    [1,1,1,2,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1],
    [1,3,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,3,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

class PacMan:
    def __init__(self, x, y):
        self.grid_x = x
        self.grid_y = y
        self.x = x * CELL_SIZE
        self.y = y * CELL_SIZE
        self.direction = 0
        self.next_direction = 0
        self.mouth_frame = 0
        self.animation_counter = 0
        self.speed = 1.5
        self.moving = False
        self.move_counter = 0
        
    def update(self):
        self.animation_counter += 1
        if self.animation_counter % 8 == 0:
            self.mouth_frame = (self.mouth_frame + 1) % 3
            
    def can_move(self, direction):
        dx, dy = [(1, 0), (0, -1), (-1, 0), (0, 1)][direction]
        new_x, new_y = self.grid_x + dx, self.grid_y + dy
        if 0 <= new_x < len(MAZE[0]) and 0 <= new_y < len(MAZE):
            return MAZE[new_y][new_x] != 1
        return False
            
    def move(self):
        self.move_counter += 1
        if self.move_counter % 8 != 0:
            return
            
        if self.can_move(self.next_direction):
            self.direction = self.next_direction
            
        if self.can_move(self.direction):
            dx, dy = [(1, 0), (0, -1), (-1, 0), (0, 1)][self.direction]
            self.grid_x += dx
            self.grid_y += dy
            self.x = self.grid_x * CELL_SIZE
            self.y = self.grid_y * CELL_SIZE
            
            if self.grid_x < 0:
                self.grid_x = len(MAZE[0]) - 1
                self.x = self.grid_x * CELL_SIZE
            elif self.grid_x >= len(MAZE[0]):
                self.grid_x = 0
                self.x = self.grid_x * CELL_SIZE
                
    def draw(self, screen):
        px, py = int(self.x + CELL_SIZE//2), int(self.y + CELL_SIZE//2)
        radius = CELL_SIZE//2 - 1
        
        # Draw Pac-Man body
        pygame.draw.circle(screen, YELLOW, (px, py), radius)
        
        # Draw mouth based on animation frame
        if self.mouth_frame > 0:
            mouth_size = 25 + (self.mouth_frame * 15)
            start_angle = [0, 90, 180, 270][self.direction] - mouth_size//2
            end_angle = start_angle + mouth_size
            
            mouth_points = [(px, py)]
            for angle in range(int(start_angle), int(end_angle), 5):
                x = px + radius * math.cos(math.radians(angle))
                y = py - radius * math.sin(math.radians(angle))
                mouth_points.append((x, y))
            pygame.draw.polygon(screen, BLACK, mouth_points)

class Ghost:
    def __init__(self, x, y, color, name):
        self.grid_x = x
        self.grid_y = y
        self.x = x * CELL_SIZE
        self.y = y * CELL_SIZE
        self.color = color
        self.name = name
        self.direction = random.randint(0, 3)
        self.speed = 1.2
        self.moving = True
        self.vulnerable = False
        self.vulnerable_timer = 0
        self.flash_timer = 0
        self.move_counter = 0
        
    def update(self, pacman_x, pacman_y, power_mode):
        if power_mode and not self.vulnerable:
            self.vulnerable = True
            self.vulnerable_timer = 300
            
        if self.vulnerable:
            self.vulnerable_timer -= 1
            self.flash_timer += 1
            if self.vulnerable_timer <= 0:
                self.vulnerable = False
                
        # AI behavior based on ghost personality
        if not self.vulnerable:
            if self.name == "blinky":  # Aggressive - chase directly
                dx, dy = pacman_x - self.grid_x, pacman_y - self.grid_y
                if abs(dx) > abs(dy):
                    self.direction = 0 if dx > 0 else 2
                else:
                    self.direction = 3 if dy > 0 else 1
            elif self.name == "pinky":  # Ambush - target ahead of Pac-Man
                target_x = pacman_x + 2 * [1, 0, -1, 0][pacman_x % 4]
                target_y = pacman_y + 2 * [0, -1, 0, 1][pacman_y % 4]
                dx, dy = target_x - self.grid_x, target_y - self.grid_y
                if abs(dx) > abs(dy):
                    self.direction = 0 if dx > 0 else 2
                else:
                    self.direction = 3 if dy > 0 else 1
            else:  # Random movement for cyan and orange
                if random.randint(0, 20) == 0:
                    self.direction = random.randint(0, 3)
        else:
            # Run away when vulnerable
            dx, dy = self.grid_x - pacman_x, self.grid_y - pacman_y
            if abs(dx) > abs(dy):
                self.direction = 0 if dx > 0 else 2
            else:
                self.direction = 3 if dy > 0 else 1
            
    def can_move(self, direction):
        dx, dy = [(1, 0), (0, -1), (-1, 0), (0, 1)][direction]
        new_x, new_y = self.grid_x + dx, self.grid_y + dy
        if 0 <= new_x < len(MAZE[0]) and 0 <= new_y < len(MAZE):
            return MAZE[new_y][new_x] != 1
        return False
            
    def move(self):
        self.move_counter += 1
        if self.move_counter % 10 != 0:
            return
            
        if not self.can_move(self.direction):
            for _ in range(4):
                new_dir = random.randint(0, 3)
                if self.can_move(new_dir):
                    self.direction = new_dir
                    break
        
        if self.can_move(self.direction):
            dx, dy = [(1, 0), (0, -1), (-1, 0), (0, 1)][self.direction]
            self.grid_x += dx
            self.grid_y += dy
            self.x = self.grid_x * CELL_SIZE
            self.y = self.grid_y * CELL_SIZE
            
            if self.grid_x < 0:
                self.grid_x = len(MAZE[0]) - 1
                self.x = self.grid_x * CELL_SIZE
            elif self.grid_x >= len(MAZE[0]):
                self.grid_x = 0
                self.x = self.grid_x * CELL_SIZE
                
    def draw(self, screen):
        px, py = int(self.x + CELL_SIZE//2), int(self.y + CELL_SIZE//2)
        radius = CELL_SIZE//2 - 1
        
        # Choose color based on vulnerability
        color = self.color
        if self.vulnerable:
            if self.vulnerable_timer < 60 and self.flash_timer % 10 < 5:
                color = WHITE
            else:
                color = VULNERABLE_BLUE
        
        # Ghost body (rounded top)
        pygame.draw.circle(screen, color, (px, py - 2), radius)
        pygame.draw.rect(screen, color, (px - radius, py - 2, radius * 2, radius + 2))
        
        # Ghost bottom wavy part
        wave_points = []
        for i in range(5):
            x = px - radius + i * (radius * 2 // 4)
            y = py + radius - 2 if i % 2 == 0 else py + radius + 2
            wave_points.append((x, y))
        wave_points.append((px + radius, py))
        wave_points.append((px - radius, py))
        pygame.draw.polygon(screen, color, wave_points)
        
        # Eyes based on ghost personality
        if not self.vulnerable or (self.vulnerable_timer < 60 and self.flash_timer % 10 < 5):
            if self.name == "blinky":  # Angry eyes
                pygame.draw.ellipse(screen, WHITE, (px - 5, py - 6, 4, 6))
                pygame.draw.ellipse(screen, WHITE, (px + 1, py - 6, 4, 6))
                pygame.draw.circle(screen, BLACK, (px - 3, py - 4), 2)
                pygame.draw.circle(screen, BLACK, (px + 3, py - 4), 2)
            elif self.name == "pinky":  # Round cute eyes
                pygame.draw.circle(screen, WHITE, (px - 3, py - 4), 3)
                pygame.draw.circle(screen, WHITE, (px + 3, py - 4), 3)
                pygame.draw.circle(screen, BLACK, (px - 3, py - 3), 2)
                pygame.draw.circle(screen, BLACK, (px + 3, py - 3), 2)
            elif self.name == "inky":  # Calm spaced eyes
                pygame.draw.circle(screen, WHITE, (px - 4, py - 4), 2)
                pygame.draw.circle(screen, WHITE, (px + 4, py - 4), 2)
                pygame.draw.circle(screen, BLACK, (px - 4, py - 4), 1)
                pygame.draw.circle(screen, BLACK, (px + 4, py - 4), 1)
            else:  # Clyde - goofy crossed eyes
                pygame.draw.circle(screen, WHITE, (px - 2, py - 4), 3)
                pygame.draw.circle(screen, WHITE, (px + 2, py - 4), 3)
                pygame.draw.circle(screen, BLACK, (px - 1, py - 4), 2)
                pygame.draw.circle(screen, BLACK, (px + 1, py - 4), 2)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PAC MAN")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 18)
        self.big_font = pygame.font.Font(None, 28)
        
        # Game state
        self.score = 0
        self.lives = 3
        self.game_state = "ready"
        self.ready_timer = 180
        self.power_mode = False
        self.power_timer = 0
        
        # Initialize game objects
        self.pacman = PacMan(1, 1)
        self.ghosts = [
            Ghost(21, 9, RED, "blinky"),
            Ghost(22, 9, PINK, "pinky"),
            Ghost(23, 9, CYAN, "inky"),
            Ghost(24, 9, ORANGE, "clyde")
        ]
        
        self.pellet_count = sum(row.count(2) + row.count(3) for row in MAZE)
        self.original_maze = [row[:] for row in MAZE]
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.pacman.next_direction = 0
        elif keys[pygame.K_UP]:
            self.pacman.next_direction = 1
        elif keys[pygame.K_LEFT]:
            self.pacman.next_direction = 2
        elif keys[pygame.K_DOWN]:
            self.pacman.next_direction = 3
            
        return True
        
    def update(self):
        if self.game_state == "ready":
            self.ready_timer -= 1
            if self.ready_timer <= 0:
                self.game_state = "playing"
        elif self.game_state == "playing":
            # Update power mode
            if self.power_mode:
                self.power_timer -= 1
                if self.power_timer <= 0:
                    self.power_mode = False
            
            # Update Pac-Man
            self.pacman.update()
            self.pacman.move()
            
            # Check pellet collection
            cell = MAZE[self.pacman.grid_y][self.pacman.grid_x]
            if cell == 2:
                MAZE[self.pacman.grid_y][self.pacman.grid_x] = 0
                self.score += 10
                self.pellet_count -= 1
            elif cell == 3:
                MAZE[self.pacman.grid_y][self.pacman.grid_x] = 0
                self.score += 50
                self.pellet_count -= 1
                self.power_mode = True
                self.power_timer = 300
                
            # Update ghosts
            for ghost in self.ghosts:
                ghost.update(self.pacman.grid_x, self.pacman.grid_y, self.power_mode)
                ghost.move()
                
                # Check collision
                if ghost.grid_x == self.pacman.grid_x and ghost.grid_y == self.pacman.grid_y:
                    if ghost.vulnerable:
                        ghost.grid_x, ghost.grid_y = 22, 9
                        ghost.x, ghost.y = 22 * CELL_SIZE, 9 * CELL_SIZE
                        ghost.vulnerable = False
                        self.score += 200
                    else:
                        self.lives -= 1
                        if self.lives <= 0:
                            self.game_state = "game_over"
                        else:
                            self.pacman.grid_x, self.pacman.grid_y = 1, 1
                            self.pacman.x, self.pacman.y = 1 * CELL_SIZE, 1 * CELL_SIZE
                            for i, g in enumerate(self.ghosts):
                                g.grid_x, g.grid_y = 21 + i, 9
                                g.x, g.y = (21 + i) * CELL_SIZE, 9 * CELL_SIZE
                        
            # Check win condition
            if self.pellet_count <= 0:
                self.game_state = "win"
                
    def draw_maze(self):
        for y, row in enumerate(MAZE):
            for x, cell in enumerate(row):
                px, py = x * CELL_SIZE, y * CELL_SIZE
                
                if cell == 1:  # Wall with neon glow effect
                    # Outer glow
                    pygame.draw.rect(self.screen, GLOW_BLUE, (px - 1, py - 1, CELL_SIZE + 2, CELL_SIZE + 2))
                    # Main wall
                    pygame.draw.rect(self.screen, NEON_BLUE, (px, py, CELL_SIZE, CELL_SIZE))
                    # Inner highlight for rounded effect
                    pygame.draw.rect(self.screen, BLUE, (px + 1, py + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                elif cell == 2:  # Pellet
                    pygame.draw.circle(self.screen, WHITE, (px + CELL_SIZE//2, py + CELL_SIZE//2), 1)
                elif cell == 3:  # Power pellet
                    # Animated power pellet
                    size = 4 + int(2 * math.sin(pygame.time.get_ticks() * 0.01))
                    pygame.draw.circle(self.screen, WHITE, (px + CELL_SIZE//2, py + CELL_SIZE//2), size)
                    
    def draw_ui(self):
        # Draw black UI bar at bottom
        pygame.draw.rect(self.screen, BLACK, (0, SCREEN_HEIGHT - UI_BAR_HEIGHT, SCREEN_WIDTH, UI_BAR_HEIGHT))
        
        # Score display on left
        score_text = self.font.render(f"SCORE: {self.score:05d}", True, WHITE)
        self.screen.blit(score_text, (10, SCREEN_HEIGHT - 25))
        
        # Lives display on right
        lives_text = self.font.render("LIVES:", True, WHITE)
        self.screen.blit(lives_text, (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 25))
        
        for i in range(self.lives):
            px = SCREEN_WIDTH - 50 + i * 15
            pygame.draw.circle(self.screen, YELLOW, (px, SCREEN_HEIGHT - 15), 6)
            # Small mouth
            mouth_points = [(px, SCREEN_HEIGHT - 15), (px + 4, SCREEN_HEIGHT - 18), (px + 4, SCREEN_HEIGHT - 12)]
            pygame.draw.polygon(self.screen, BLACK, mouth_points)
        
        # Cherry in center
        cherry_x = SCREEN_WIDTH // 2
        cherry_y = SCREEN_HEIGHT - 15
        # Cherry body
        pygame.draw.circle(self.screen, RED, (cherry_x - 3, cherry_y), 4)
        pygame.draw.circle(self.screen, RED, (cherry_x + 3, cherry_y), 4)
        # Cherry stem
        pygame.draw.line(self.screen, (0, 150, 0), (cherry_x - 2, cherry_y - 4), (cherry_x - 1, cherry_y - 8), 2)
        pygame.draw.line(self.screen, (0, 150, 0), (cherry_x + 2, cherry_y - 4), (cherry_x + 1, cherry_y - 8), 2)
        
        # Game state messages
        # Game state messages (centered on game area, not UI bar)
        game_center_y = (SCREEN_HEIGHT - UI_BAR_HEIGHT) // 2
        if self.game_state == "ready":
            ready_text = self.big_font.render("READY!", True, YELLOW)
            text_rect = ready_text.get_rect(center=(SCREEN_WIDTH//2, game_center_y))
            # Add shadow effect
            shadow_text = self.big_font.render("READY!", True, BLACK)
            shadow_rect = shadow_text.get_rect(center=(SCREEN_WIDTH//2 + 2, game_center_y + 2))
            self.screen.blit(shadow_text, shadow_rect)
            self.screen.blit(ready_text, text_rect)
        elif self.game_state == "game_over":
            game_over_text = self.big_font.render("GAME OVER", True, RED)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, game_center_y))
            shadow_text = self.big_font.render("GAME OVER", True, BLACK)
            shadow_rect = shadow_text.get_rect(center=(SCREEN_WIDTH//2 + 2, game_center_y + 2))
            self.screen.blit(shadow_text, shadow_rect)
            self.screen.blit(game_over_text, text_rect)
        elif self.game_state == "win":
            win_text = self.big_font.render("YOU WIN!", True, YELLOW)
            text_rect = win_text.get_rect(center=(SCREEN_WIDTH//2, game_center_y))
            shadow_text = self.big_font.render("YOU WIN!", True, BLACK)
            shadow_rect = shadow_text.get_rect(center=(SCREEN_WIDTH//2 + 2, game_center_y + 2))
            self.screen.blit(shadow_text, shadow_rect)
            self.screen.blit(win_text, text_rect)
            
    def draw(self):
        self.screen.fill(BLACK)
        self.draw_maze()
        
        if self.game_state in ["playing", "ready"]:
            self.pacman.draw(self.screen)
            for ghost in self.ghosts:
                ghost.draw(self.screen)
                
        self.draw_ui()
        pygame.display.flip()
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
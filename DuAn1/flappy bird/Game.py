import pygame,sys, random
# Tao Ham cho game
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos-700))
    
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)   
def check_vacham(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3,1)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect 
def score_display(game_state):
    if game_state == "Main_game":
        score_surface = game_font.render(str(int(score)), True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface, score_rect)
    if game_state == "Game_over":
        score_surface = game_font.render(f"Score:{int(score)}", True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface, score_rect)
        
        hight_score_surface = game_font.render(f"Highh Score: {int(hight_score)}", True,(255,255,255))
        hight_score_rect = hight_score_surface.get_rect(center = (216,630))
        screen.blit(hight_score_surface, hight_score_rect)
def update_score(score, hight_score):
    if score > hight_score:
        hight_score = score
    return hight_score
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
game_font = pygame.font.Font("DuAn1/04B_19.ttf",40)
# Tao Bien Cho Game
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
hight_score = 0
# Background
bg= pygame.image.load("DuAn1/assests/background-night.png").convert()
bg = pygame.transform.scale2x(bg)
# floor
floor = pygame.image.load("DuAn1/assests/floor.png").convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
# bird
bird_down = pygame.transform.scale2x(pygame.image.load("DuAn1/assests/yellowbird-downflap.png").convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load("DuAn1/assests/yellowbird-midflap.png").convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load("DuAn1/assests/yellowbird-upflap.png").convert_alpha())
bird_list = [bird_down, bird_mid, bird_up] # 0 1 2
bird_index = 0
bird = bird_list[bird_index] 

# bird= pygame.image.load("DuAn1/assests/yellowbird-midflap.png").convert_alpha()
# bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100, 384))

# tao timer 
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap,200)
# Tao ống
pipe_surface = pygame.image.load("DuAn1/assests/pipe-green.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
# tao timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [200, 250, 300]
# Tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load("DuAn1/assests/message.png").convert_alpha())
game_over_rect = game_over_surface.get_rect(center =(216,384))
# Chèn Âm Thanh
flap_sound = pygame.mixer.Sound("DuAn1/sound/sfx_wing.wav")
hit_sound = pygame.mixer.Sound("DuAn1/sound/sfx_hit.wav")
score_sound = pygame.mixer.Sound("DuAn1/sound/sfx_point.wav")
score_sound_countdown = 100
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
             bird_movement = 0
             bird_movement =-11
             flap_sound.play()
            if event.key == pygame.K_BACKSPACE and game_active==False:
             game_active = True
             pipe_list.clear()
             bird_rect.center = (100,384)
             bird_movement = 0
             score = 0
        if event.type == spawnpipe:
          pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
              bird_index += 1
            else:
              bird_index = 0
        bird, bird_rect = bird_animation()
          
          
    screen.blit(bg,(0,0))
    if game_active:
        # bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect)
        game_active=check_vacham(pipe_list)
        # pipe
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.01
        score_display("Main_game")
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface,game_over_rect)
        hight_score = update_score(score, hight_score)
        score_display("Game_over")
    
    # floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)

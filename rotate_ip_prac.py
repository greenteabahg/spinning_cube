import pygame
import math 

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()


#background 
background = pygame.Surface((1280,720))
#I'm going to try to make the font scale by replacing a number in the second argument with a variable dependent on the z


char_1 = "$"

#character's surface on screen

#determines size of font based on distance to screen
def font_findah(vector):
    pix_num = vector.z
    div = pix_num/28
    div = int(div)
    num = 30 - div
    return num 

#dot math projection 3d to 2d
def proj_1(vector):
    mat_A = pygame.math.Vector3(1,0,.25)
    mat_B = pygame.math.Vector3(0,1,.25)
    x = vector.dot(mat_A)
    y = vector.dot(mat_B)
    return pygame.math.Vector2(x,y)  

#func for blitting away background
def erase(*args):
    for arg in args:
        screen.blit(background, arg) 


#func for drawing points
def draw_char(char, *args):
    for arg in args:
        screen.blit(char, arg)

vec_A = pygame.math.Vector3(490,210,0) 
vec_B = pygame.math.Vector3(790,210,0)
vec_C = pygame.math.Vector3(490,210,300)
vec_D = pygame.math.Vector3(790,210,300)

pygame.display.update() 


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

    center_v = pygame.math.Vector3(640,360,100) 

    #calc vectors
    vec_A_calcd = proj_1(vec_A) 
    vec_B_calcd = proj_1(vec_B)
    vec_C_calcd = proj_1(vec_C)
    vec_D_calcd = proj_1(vec_D)

    #font for A 
    font_size_A = font_findah(vec_A)
    font_A = pygame.font.SysFont("Arial", font_size_A)
    char_A_surf = font_A.render(char_1, True, (255,255,255))
    
    #font for B
    font_size_B = font_findah(vec_B)
    font_B = pygame.font.SysFont("Arial", font_size_B)
    char_B_surf = font_B.render(char_1, True, (255,255,255))

    #font for C
    font_size_C = font_findah(vec_C)
    font_C = pygame.font.SysFont("Arial", font_size_C)
    char_C_surf = font_C.render(char_1, True, (255,255,255))

    #font for D
    font_size_D = font_findah(vec_D)
    font_D = pygame.font.SysFont("Arial", font_size_D)
    char_D_surf = font_D.render(char_1, True, (255,255,255))

    #input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        vec_A.update(vec_A.rotate(1, center_v)) 
        vec_B.update(vec_B.rotate(1, center_v))
        vec_C.update(vec_C.rotate(1, center_v))
        vec_D.update(vec_D.rotate(1, center_v)) 

    text_rect_A = char_A_surf.get_rect(center=vec_A_calcd)
    text_rect_B = char_B_surf.get_rect(center=vec_B_calcd)
    text_rect_C = char_C_surf.get_rect(center=vec_C_calcd)
    text_rect_D = char_D_surf.get_rect(center=vec_D_calcd)

    #screen.blit background func
    erase(text_rect_A, text_rect_B, text_rect_C, text_rect_D)
    #drawing vectors func
    screen.blit(char_A_surf, text_rect_A) 
    screen.blit(char_B_surf, text_rect_B) 
    screen.blit(char_C_surf, text_rect_C) 
    screen.blit(char_D_surf, text_rect_D) 

    pygame.display.flip()

    clock.tick(60)

pygame.quit() 

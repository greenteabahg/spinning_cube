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
vec_E = pygame.math.Vector3(490,510,0)
vec_F = pygame.math.Vector3(790,510,0)
vec_G = pygame.math.Vector3(490,510,300)
vec_H = pygame.math.Vector3(790,510,300)

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
    vec_E_calcd = proj_1(vec_E)
    vec_F_calcd = proj_1(vec_F)
    vec_G_calcd = proj_1(vec_G)
    vec_H_calcd = proj_1(vec_H)

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

    #font for E
    font_size_E = font_findah(vec_E)
    font_E = pygame.font.SysFont("Arial", font_size_E)
    char_E_surf = font_E.render(char_1, True, (255,255,255))

    #font for F
    font_size_F = font_findah(vec_F)
    font_F = pygame.font.SysFont("Arial", font_size_F)
    char_F_surf = font_F.render(char_1, True, (255,255,255))

    #font for G
    font_size_G = font_findah(vec_G)
    font_G = pygame.font.SysFont("Arial", font_size_G)
    char_G_surf = font_G.render(char_1, True, (255,255,255))

    #font for H
    font_size_H = font_findah(vec_H)
    font_H = pygame.font.SysFont("Arial", font_size_H)
    char_H_surf = font_H.render(char_1, True, (255,255,255))

    #input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        vec_A.update(vec_A.rotate(1, center_v)) 
        vec_B.update(vec_B.rotate(1, center_v))
        vec_C.update(vec_C.rotate(1, center_v))
        vec_D.update(vec_D.rotate(1, center_v)) 
        vec_E.update(vec_E.rotate(1, center_v))
        vec_F.update(vec_F.rotate(1, center_v))
        vec_G.update(vec_G.rotate(1, center_v))
        vec_H.update(vec_H.rotate(1, center_v))

    text_rect_A = char_A_surf.get_rect(center=vec_A_calcd)
    text_rect_B = char_B_surf.get_rect(center=vec_B_calcd)
    text_rect_C = char_C_surf.get_rect(center=vec_C_calcd)
    text_rect_D = char_D_surf.get_rect(center=vec_D_calcd)
    text_rect_E = char_E_surf.get_rect(center=vec_E_calcd)
    text_rect_F = char_F_surf.get_rect(center=vec_F_calcd)
    text_rect_G = char_G_surf.get_rect(center=vec_G_calcd)
    text_rect_H = char_H_surf.get_rect(center=vec_H_calcd)

    #screen.blit background func
    erase(text_rect_A, text_rect_B, text_rect_C, text_rect_D, text_rect_E, text_rect_F, text_rect_G, text_rect_H)

    #drawing vectors func
    screen.blit(char_A_surf, text_rect_A) 
    screen.blit(char_B_surf, text_rect_B) 
    screen.blit(char_C_surf, text_rect_C) 
    screen.blit(char_D_surf, text_rect_D) 
    screen.blit(char_E_surf, text_rect_E)
    screen.blit(char_F_surf, text_rect_F)
    screen.blit(char_G_surf, text_rect_G)
    screen.blit(char_H_surf, text_rect_H)

    pygame.display.flip()

    clock.tick(60)

pygame.quit() 

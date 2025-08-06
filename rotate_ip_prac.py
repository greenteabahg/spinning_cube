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

vec_A = pygame.math.Vector3(490,210,0) 

pygame.display.update() 


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

    center_v = pygame.math.Vector3(640,360,100) 
    vec_A_calcd = proj_1(vec_A) 
    
    font_size = font_findah(vec_A)
    font = pygame.font.SysFont("Arial", font_size)
    char_1_surf = font.render(char_1, True, (255,255,255))
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        vec_A.update(vec_A.rotate(1, center_v)) 
    
    text_rect_A = char_1_surf.get_rect(center=vec_A_calcd) 
    screen.blit(background, text_rect_A) 
    screen.blit(char_1_surf, text_rect_A)

    pygame.display.flip()

    clock.tick(60)

pygame.quit() 

import pygame
import numpy as np



pygame.init()
PYGAME_DETECT_AVX2 = 1
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30) 

# My three characters for three sides visible
char_1 = "$"
char_2 = "%"
char_3 = "!"

#test with one surface
text_surface_1 = font.render(char_1, True, (255,255,255)) #color, etc

#3d place ??
vec_A = pygame.math.Vector3(560,285,0) 
vec_B = pygame.math.Vector3(710,285,0)
vec_C = pygame.math.Vector3(560,435,0)
vec_D = pygame.math.Vector3(710,435,0)
#back of cube
vec_E = pygame.math.Vector3(560,285,150)
vec_F = pygame.math.Vector3(710,285,150)
vec_G = pygame.math.Vector3(560,435,150)
vec_H = pygame.math.Vector3(710,435,150)

#Okay i need a function for projecting the 3D vectors to 2D coordinates 

def proj(vector): 
     
    constant = np.array([[2,0,0],[0,0,2]])
    constant_add = np.array([[1],[1]])
    vec_mat = np.array([[vector.x],[vector.y], [vector.z]])
    first_result = np.matmul(constant, vec_mat) 
    fin_result = first_result + constant_add
    vec = (fin_result[0], fin_result[1])
    return(vec)

#now i try it 

vec_A_calcd = proj(vec_A) 
vec_B_calcd = proj(vec_B)
vec_C_calcd = proj(vec_C)
vec_D_calcd = proj(vec_D)
vec_E_calcd = proj(vec_E)
vec_F_calcd = proj(vec_F)
vec_G_calcd = proj(vec_G)
vec_H_calcd = proj(vec_H) 

#now I display it

text_rect_A = text_surface_1.get_rect(center =  vec_A_calcd) 
text_rect_B = text_surface_1.get_rect(center = vec_B_calcd) 
text_rect_C = text_surface_1.get_rect(center = vec_C_calcd)
text_rect_D = text_surface_1.get_rect(center = vec_D_calcd)


screen.blit(text_surface_1, text_rect_A)
#screen.blit(text_surface_1, text_rect_B)
#screen.blit(text_surface_1, text_rect_C)
#screen.blit(text_surface_1, text_rect_D) 


pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 



   # screen.fill("black")
      

    pygame.display.flip()

   # clock.tick(60)


pygame.quit() 

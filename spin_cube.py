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

#og cube points : x = 560/710, y= 285/435, z = 0/150 

vec_A = pygame.math.Vector3(490,210,0) 
vec_B = pygame.math.Vector3(790,210,0)
vec_C = pygame.math.Vector3(490,510,0)
vec_D = pygame.math.Vector3(790,510,0)
#back of cube
vec_E = pygame.math.Vector3(490,210,300)
vec_F = pygame.math.Vector3(790,210,300)
vec_G = pygame.math.Vector3(490,510,300)
vec_H = pygame.math.Vector3(790,510,300)

#Okay i need a function for projecting the 3D vectors to 2D coordinates 

#Im gonna leave this here for now, but supposedly I can use the dot product to find out where the point is in 2D

def proj(vector): 
     
    constant = np.array([[2,0,0],[0,0,2]])
    constant_add = np.array([[.1],[.1]])
    vec_mat = np.array([[vector[0]],[vector[1]], [vector[2]]])
    first_result = np.matmul(constant, vec_mat) 
    fin_result = first_result + constant_add
    vec = (fin_result[0], fin_result[1])
    return(vec)

#now i try it 

#proj_1 is using dot math
def proj_1(vector):
    matrix_A = pygame.math.Vector3(1,0,.25)
    matrix_B = pygame.math.Vector3(0,1,.25)
    x = vector.dot(matrix_A)
    y = vector.dot(matrix_B)
    return( x , y) 

vec_A_calcd = proj_1(vec_A) 
vec_B_calcd = proj_1(vec_B)
vec_C_calcd = proj_1(vec_C)
vec_D_calcd = proj_1(vec_D)
vec_E_calcd = proj_1(vec_E)
vec_F_calcd = proj_1(vec_F)
vec_G_calcd = proj_1(vec_G)
vec_H_calcd = proj_1(vec_H) 

print(vec_E_calcd) 
#now I display it

text_rect_A = text_surface_1.get_rect(center =  vec_A_calcd) 
text_rect_B = text_surface_1.get_rect(center = vec_B_calcd) 
text_rect_C = text_surface_1.get_rect(center = vec_C_calcd)
text_rect_D = text_surface_1.get_rect(center = vec_D_calcd)

#back side

text_rect_E = text_surface_1.get_rect(center = vec_E_calcd)
text_rect_F = text_surface_1.get_rect(center = vec_F_calcd)
text_rect_G = text_surface_1.get_rect(center = vec_G_calcd)
text_rect_H = text_surface_1.get_rect(center = vec_H_calcd)

#and now it appears on screen

screen.blit(text_surface_1, text_rect_A)
screen.blit(text_surface_1, text_rect_B)
screen.blit(text_surface_1, text_rect_C)
screen.blit(text_surface_1, text_rect_D) 

screen.blit(text_surface_1, text_rect_E)
screen.blit(text_surface_1, text_rect_F)
screen.blit(text_surface_1, text_rect_G)
screen.blit(text_surface_1, text_rect_H) 

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

import pygame, sys, time, random

pygame.init()

play_surface = pygame.display.set_mode((640, 640))
font = pygame.font.Font(None, 30)

fps = pygame.time.Clock()


def food():
    random_pos = random.randint(0,63)*10
    food_pos = [random_pos, random_pos]
    return food_pos

def main():

    snake_pos = [100, 50]
    snake_body = [[100,50], [90, 50], [80,50]]
    change = "RIGHT"
    food_pos = food()
    score = 0
    speed = 10

    run = True
    while run:
        for event in pygame.event.get():  #Obtiene todos los eventos que ocurren mientras la pantalla se esté ejecutando
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    change = "LEFT"
                elif event.key == pygame.K_UP:
                    change = "UP"
                elif event.key == pygame.K_DOWN:
                    change = "DOWN"

        if change == "RIGHT":
            snake_pos[0] += 10
        elif change == "LEFT":
            snake_pos[0] -= 10  
        elif change == "UP":
            snake_pos[1] -= 10   
        elif change == "DOWN":
            snake_pos[1] += 10   

        snake_body.insert(0, list(snake_pos)) 
        if snake_pos == food_pos:
            food_pos = food()
            score += 1
            if score%10 == 0:  #Aumentar velocidad cada 10 puntos
                speed = speed + 10
            print(str(score) + " - " + str(speed))
        else:
            snake_body.pop()

        play_surface.fill((31, 31, 31)) #Rellenar la pantalla con el color negro

        #Dibujar la serpiente
        for pos in snake_body:
            pygame.draw.rect(play_surface, (255,255,255), pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(play_surface, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        text = font.render(str(score), 0, (0, 120, 255))
        play_surface.blit(text, (610, 20))

        #Validar que no se estrelle contra los bordes de la ventana
        if snake_pos[0] <= 0 or snake_pos[0] >= 640 or snake_pos[1] <= 0 or snake_pos[1] >= 640:
            run = False
            print("Game Over !!!")


        pygame.display.flip() #Integrar todo en la pantalla
        fps.tick(speed) #Ajustar el nivel de velocidad (dificultad) del juego
       
#Ejecutar la funcion principal
main()
pygame.quit()
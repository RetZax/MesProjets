# Importer les bibliothèques nécessaires
import random
import pygame
import sys
import time

# Définir la vitesse du serpent
snake_speed = 20
# Definir la taille de la fenetre
window_x = 720
window_y = 480

# Définir la couleur
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255,0,0)
pink = pygame.Color(222,49,99)

# Initialisation de Pygamel
pygame.init()


# initialisation de la fenetre de jeu
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

#FPS controller
fps = pygame.time.Clock()

# Définir la position par défaut du serpent snake
snake_position = [100, 50]

# Défin les 4 premiers blocs du corps du serpent
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]
# emplacement des fruits(import random)
fruit_position = [random.randint(1, 72) * 10, random.randint(1, 40) *10]
fruit_spawn = True

direction = 'RIGHT'
change_direction = direction
# score initiale
score = 0


def show_score(choice, color, font, size):
    # Crée d'abord un objet police
    score_font = pygame.font.SysFont(font, size)
    # Créer une surface d'arrière-plan
    score_surface = score_font.render('Score: ' + str(score), True, color)
    # Créer un objet rectangulaire pour l'objet de surface de texte
    score_rect = score_surface.get_rect()
    # Afficher notre score
    game_window.blit(score_surface, score_rect)

def game_over():
    #Crée l'objet police my_font
    my_font = pygame.font.SysFont("Arial",50)
    # Créer la surface de texte sur laquelle le texte sera dessiné
    game_over_surface = my_font.render("ta perdu ! Your score is:" + str(score), True, red)
    # Créer un objet rectangulaire pour l'objet de surface du texte
    game_over_rect = game_over_surface.get_rect()
    #Definir la position du texte
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    #blit dessinera le texte a l'écran
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    #Après 2 secondes nous quitterons le programme
    time.sleep(5)
    # Désactiver la blibliothèque pygame
    pygame.quit()
    #Procèdures de sortie
    quit()

while True:
    for event in pygame.event.get():
        # Gestion des évenements clés
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_direction = 'UP'
            if event.key == pygame.K_DOWN:
                change_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_direction = 'RIGHT'
            # Déterminer si l'utilisateur a cliqué sur le bouton de
            # fermeture "X" et exécutez le segment de code "if"
        if event.type == pygame.QUIT:
            pygame.quit()
            # Désinstaller tous les modules sys.exit()
            sys.exit()



    #si deux touches sont pressées en même temps
    #Nous ne voulons pas que le serpent se déplace dans deux directions en même telos
    if change_direction == 'UP' and direction !='DOWN':
        direction = 'UP'
    if change_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Serpents en mouvements
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    #Croissance du serpent
    snake_body.insert(0, list(snake_position))
    # Si le fruit entre en coliision avec le serpent , le score augmente de 10
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randint(1, 72) * 10, random.randint(1, 40) *10]

    fruit_spawn = True
    game_window.fill(pink)

    # Dessiner un serpent
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    # Dessiner un fruit
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    #Toucher le murs
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()

    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    #Toucher le corps du serpent
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()





    show_score(1, white, 'Arial', 20)
    # Rafraichir l'écran de jeu
    pygame.display.update()
    fps.tick(snake_speed)
    # Boucle pour les éléments et écoute pour le statut


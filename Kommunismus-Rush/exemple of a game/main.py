from game import Game
import pygame

# ATTENTION UTILISER .PNG POUR LES IMAGES A FOND TRANSPARENT

# initialisation du module
pygame.init()

# generer le fenêtre du jeu ajout de .set_caption pour changer le nom
pygame.display.set_caption("Comet fall Game")
# gestion de la taille
screen_width = 1920
screen_height = 1020
screen = pygame.display.set_mode([screen_width, screen_height])

background = pygame.image.load('PygameAssets-main/bg.jpg')

banner = pygame.image.load('PygameAssets-main/banner.png')
pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 3.5


play_button = pygame.image.load('PygameAssets-main/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = banner.get_rect()
play_button_rect.x = screen.get_width() / 2.5
play_button_rect.y = screen.get_height() / 1.5


# chargement du jeu
game = Game()

running = True

clock = pygame.time.Clock()
# boucle du jeu
while running:
    # set the fps
    clock.tick(144)

    # appliquer une image aux coords (0, 0)
    screen.blit(background, (0, 0))

    # verifier si le jeu a commence
    if game.is_playing:
        game.update(screen)

    else:
        # ajouter ecran de bienvenue
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)
        
    # mettre à jour l'image :
    pygame.display.flip()

    # recuperation des evenements
    for event in pygame.event.get():
        # detecter si fermeture de fenêtre
        if event.type == pygame.QUIT:

            running = False
            pygame.quit()

        # detecter si touche de clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verif si la souris est sur le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                game.start()

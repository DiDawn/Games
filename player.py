import pygame.sprite
from projectile import Projectile


# création d'une classe reliée à la super class Sprite de pygame pour pouvoir l'utiliser dans le jeu
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        # initialiser la super class
        super().__init__()

        self.game = game

        # def des sats
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 2

        self.all_projectiles = pygame.sprite.Group()

        self.image = pygame.image.load('PygameAssets-main/player.png')
        # recup du rectangle de l'image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 700

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.game.all_players.remove(self)

            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner l'arriere d la barre de vie en rouge puis le devant pour que quand le devant s'enleve l'arriere se revele
        pygame.draw.rect(surface, (255, 0, 0),
                         [self.rect.x + 0.24 * self.rect.width, self.rect.y + 0.1 * self.rect.height, self.max_health,
                          7])

        pygame.draw.rect(surface, (111, 210, 46),
                         [self.rect.x + 0.24 * self.rect.width, self.rect.y + 0.1 * self.rect.height, self.health, 7])

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

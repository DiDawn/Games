import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.velocity = random.randint(1, 5)

        self.image = pygame.image.load('PygameAssets-main/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1600, 1920) - self.rect.width
        self.rect.y = 750

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.game.all_monsters.remove(self)

            self.game.spawn_monster()

    def update_health_bar(self, surface):

        # dessiner l'arriere d la barre de vie en rouge puis le devant pour que quand le devant s'enleve l'arriere se revele
        pygame.draw.rect(surface, (255, 0, 0),
                         [self.rect.x + 0.1 * self.rect.width, self.rect.y - 0.1 * self.rect.height, self.max_health, 5])

        pygame.draw.rect(surface, (111, 210, 46),
                         [self.rect.x + 0.1 * self.rect.width, self.rect.y - 0.1 * self.rect.height, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

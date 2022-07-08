import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()

        self.velocity = 5

        self.image = pygame.image.load('PygameAssets-main/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.origin_image = self.image
        self.angle = 0

        self.player = player
        self.rect.x = self.player.rect.x + 0.75 * self.player.rect.width
        self.rect.y = self.player.rect.y + 0.4 * self.player.rect.height

    def rotate(self):
        self.angle += 4
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def destroy(self):
        self.player.all_projectiles.remove(self)

    def move(self):

        self.rect.x += self.velocity

        self.rotate()

        # verif si le projectile rentre en, colision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.destroy()
            monster.damage(self.player.attack)

        if self.rect.x > 1920:
            self.destroy()

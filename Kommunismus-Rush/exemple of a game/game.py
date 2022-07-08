import pygame
from player import Player
from monster import Monster


class Game:

    def __init__(self):
        # def si le jeu à commencé
        self.is_playing = False

        # generer le joueur
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        
        # groupe de monstres
        self.all_monsters = pygame.sprite.Group()

        self.pressed = {}

    def start(self):
        self.is_playing = True
        for i in range(540):
            self.spawn_monster()

    def check_collision(self, sprite, group_sprite):
        return pygame.sprite.spritecollide(sprite, group_sprite, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)


        self.all_players.add(self.player)

    def game_over(self):
        #remettre le jeu à 0

        # ecrase l'ancien groupe de monstre pour le vider
        for monster in self.all_monsters:
            self.all_monsters.remove(monster)

        self.player.health = self.player.max_health

        self.is_playing = False

    def update(self, screen):
        # applique l'image du joueur
        if self.player.health > 0:
            screen.blit(self.player.image, self.player.rect)

        # update la barre de vie du joueur
        if self.player.health > 0:
            self.player.update_health_bar(screen)

        # fait avancer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # la mm pour les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # la mm pour les projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'enssemble de monstres
        self.all_monsters.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()

        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

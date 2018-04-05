"""Alien Module"""
import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""Initialize alien, Load alien image, Positions alien""""
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		
	"""Draw Alien"""
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	"""Flag for when Alien is at border of screen"""
	def check_border(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			
	"""Update Alien Position"""
	def update(self):
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x
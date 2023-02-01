from django.db import models

# Create your models here.

class Player(models):
    def __init__(self) -> None:
        super().__init__()
        self.id = 'fdkslafjsalk'
    
    def get_player_id(self):
        return self.id

from django.db import models
from .dv_config import TYPE_CHOICES
import random
import ctypes

import os
from .type import type_py

class Geometry(models.Model):



            # file.seek(0)
    def write_type_py():
        file_py = os.path.join('C:\\Users\\dvrch\\Desktop\\CV 2024\\BLABLABLA\\svelte django_film\\backend\\films_backend\\Base_threlte_dv\\type.py')
        new_type = random.choice([choice[0] for choice in TYPE_CHOICES])
        with open(file_py, 'w', encoding='utf-8') as file:
            file.truncate() 
            file.write(f"type_py = '{new_type}'\n")
        return type_py
    
  

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, 
    default= write_type_py)  # Correction de l'attribut pour utiliser type_py directement
    name = models.CharField(max_length=45, unique=True, blank=True, 
                            default=type_py)  # Correction de l'attribut pour utiliser type_py directement
    position = models.JSONField(default={"x": 0.0, "y": 0.0, "z": 0.0})  # Utilisation d'un callable pour JSONField
    rotation = models.JSONField(default={"x": 0.0, "y": 0.0, "z": 0.0})  # Utilisation d'un dictionnaire pour JSONField
    color = models.CharField(max_length=7, blank=True, default='#000000')  # Couleur

    def get_random_color():
        return Geometry.color
    
    def clean(self):
        if hasattr(self, 'color') and self.color and not self.color.startswith('#'):
            self.color = '#' + self.color    

    def format_position(self, x, y, z):
        self.position = {"x": x, "y": y, "z": z}  # Utilisation d'un dictionnaire pour JSONField

    def format_rotation(self, x, y, z):
        self.rotation = {"x": x, "y": y, "z": z}  # Utilisation d'un dictionnaire pour JSONField


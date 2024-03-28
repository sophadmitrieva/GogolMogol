import os
import pygame

literature_memes = set()
folder_path = r"C:\Users\ученик\PycharmProjects\gogolmogol\memes"
for filename in os.listdir(folder_path):
    meme = pygame.image.load(f"{filename}")
    literature_memes.add(meme)

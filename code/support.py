from os import walk
import time
import pygame


def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            if image == '.DS_Store':
                pass
            else:
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
    # print(surface_list)
    return surface_list

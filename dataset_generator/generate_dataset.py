from PIL import Image, ImageDraw
import os
import random
import math

IMAGE_SIZE = 64

CLASSES = ["circle", "square", "triangle"]

SPLITS = {
    "train": 800,
    "validation": 150,
    "test": 50
}

BASE_DIR ="../data"

def create_dirs():
    for split in SPLITS:
        for class_name in CLASSES:
            os.mkdirs(f"{BASE_DIR}/{split}/{class_name}", exit_ok = True)
def random_bbox():
    size = random.randint(25, 45)
    x = random.randint(5, IMAGE_SIZE - size - 5)
    y = random.randint(5, IMAGE_SIZE - size - 5)
    return [x, y , x+ size, y+size]
def draw_circle(draw):
    draw.ellipse(random_bbox(), outline = "black", width = random.randint(2, 4))

def draw_squared(draw):
    draw.rectangle(random_bbox(), outline = "black", width = random.randint(2, 4))
def draw_triangle(draw):
    margin = random.randint(8, 14)
    points = [
        (IMAGE_SIZE // 2, margin),
        (margin, IMAGE_SIZE -margin)
        (IMAGE_SIZE -margin, IMAGE_SIZE- margin)
    ]    
    draw.poligon(points, outline="black")
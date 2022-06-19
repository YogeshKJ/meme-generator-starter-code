import os
import random
from PIL import Image, ImageDraw
from random import randint


class MemeEngine:
    """Meme Generator!"""
    def __init__(self, output_dir):
        self.output_dir = output_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """Generates the meme and returns the path"""

        out_file = os.path.join(
            self.output_dir,
            f"meme-{random.randint(0, 10000000)}.jpg"
        )

        with Image.open(img_path) as im:
            resize_percentage = im.width // width
            height = im.height * resize_percentage
            im.resize((width, height))

            draw = ImageDraw.Draw(im)
            width = randint(0, im.width)
            height = randint(0, im.height)
            draw.text((width, height), f'{text} - {author}')

            im.save(out_file, 'PNG')

        return out_file

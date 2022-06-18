from PIL import Image, ImageDraw
from random import randint


class MemeEngine:
    """Meme Generator!"""
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """Generates the meme and returns the path"""

        with Image.open(img_path) as im:
            resize_percentage = im.width // width
            height = im.height * resize_percentage
            im.resize((width, height))

            draw = ImageDraw.Draw(im)
            width = randint(0, im.width)
            height = randint(0, im.height)
            draw.text((width, height), f'{text} - {author}')

            im.save(self.output_dir, 'PNG')

        return self.output_dir

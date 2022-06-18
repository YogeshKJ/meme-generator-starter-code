# Meme Generator

This is the code to generator memes ! \
Includes sample photos and quotes ! \
The user can create their own memes with custom images and quotes !

## Modules
There are two modules.

### MemeEngine
Handles the generation of the meme

### QuoteEngine
Handles the generation of quotes

## Installation
```commandline
pip install -r requirements.txt
```
## Usage
The user can interact with the application using CLI or as a web app.

### CLI
```commandline
python src/meme.py --body 'quote' --author 'author' --image 'image location' --help
```
### Flask
```commandline
python src/app.py
```
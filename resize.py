import os
from PIL import Image

src = 'data'

for sub in os.listdir(src):
    for concept in os.listdir(os.path.join(src, sub)):
        for file in os.listdir(os.path.join(src, sub, concept)):
            print(os.path.join(src, sub, concept, file))
            img = Image.open(os.path.join(src, sub, concept, file))
            img = img.resize((200,200))
            img.save(os.path.join(src, sub, concept, file))

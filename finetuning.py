from jinja2 import Environment, FileSystemLoader
import os 
from datetime import date
env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template('finetuning_outputs.jinja')

class_names = os.listdir('./data/sd2_ft')

update = date.today()

red_classes = []

with open("renders/finetuning_outputs.html", "w") as f:
    print(template.render(classes = class_names, red_classes = red_classes, update = str(update)), file = f)
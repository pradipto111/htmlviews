from jinja2 import Environment, FileSystemLoader
import os 
from datetime import date
env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template('rare_concepts.jinja')

class_names = os.listdir('./data/sd2')

update = date.today()

red_classes = ['Gymnastic_horizontal_bar',
               'tarantula',
               'madagaskar_cat',
               'Rock_Beauty',
               'grasshopper',
               'mousetrap',
               'mitten',
               'Saharan_horned_viper',
               'barracouta',
               'Payphone',
               'unicycle',]

with open("renders/rare_concepts.html", "w") as f:
    print(template.render(classes = class_names, red_classes = red_classes, update = str(update)), file = f)
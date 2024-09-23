from jinja2 import Environment, FileSystemLoader
import os 
from datetime import date
env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template('rare_concepts.jinja')

class_names = os.listdir('./data/cub/sd2/')
src = './data/cub/'


update = date.today()

red_classes = ['Brandt_s_Cormorant',
               'Spotted_Catbird',
               'Red_faced_Cormorant',
               'Chuck_will_s_widow',
               'Parakeet_Auklet',
               'Whip_poor_will',
               'White_necked_Raven',
               'Pomarine_Jaeger',
               'Nelson_s_Sparrow',
               'Least_Auklet']

with open("renders/rare_concepts_cub.html", "w") as f:
    print(template.render(classes = class_names, red_classes = red_classes, update = str(update)), file = f)
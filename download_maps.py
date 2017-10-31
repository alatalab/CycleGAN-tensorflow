import glob
import tqdm

import urllib.request
import random
from PIL import Image

for i in range(15000):
    latitude=35+15*random.random()
    longitude=90+30*random.random()
    zoom=random.randrange(7,13)
    url="https://maps.googleapis.com/maps/api/staticmap?center=%03.6f,%03.6f&zoom=%d&scale=false&size=640x640&maptype=satellite&key=AIzaSyDlEZ-zJl-N0jMPq1Az8tlcIMDkXY2zOec&format=png&visual_refresh=true"%(latitude,longitude,zoom)
    file="a"+str(i)+".png"
    urllib.request.urlretrieve(url,file)
    im= Image.open(file)
    im=im.crop((0,0,512,512))
    im.save(file)


import rembg
import easygui as eg
from PIL import Image
import time

start = time.time()
input_path = eg.fileopenbox(title='select the image')
output_path = eg.filesavebox(title='save the image to')

input = Image.open(input_path)
output = rembg.remove(input)
output.save(output_path.split('.')[0] + '_no_bg.png')
end = time.time()
print('time taken: ', end - start)


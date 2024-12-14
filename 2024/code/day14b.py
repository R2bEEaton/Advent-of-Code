from helpers.datagetter import aocd_data_in
from PIL import Image
import time

din, aocd_submit = aocd_data_in(split=True, numbers=True)
size = (101, 103)

i = 0
while True:
    img = Image.new("RGB", size)
    for robot in din:
        robot[0] += robot[2]
        robot[1] += robot[3]
        img.putpixel((robot[0] % size[0], robot[1] % size[1]), (255, 0, 0))
    i += 1
    img.save(f"14images/{i}.png")
    if i % 5000 == 0:
        time.sleep(10)

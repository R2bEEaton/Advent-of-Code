from helpers.datagetter import aocd_data_in
from PIL import Image, ImageDraw

din, aocd_submit = aocd_data_in(split=True, numbers=True)

ans = 0

scale = 0.1
img = Image.new("RGB", (1000, 1000), "black")
draw = ImageDraw.Draw(img)

colors = []
for i in range(len(din)):
    hue = int((i % 360))
    colors.append(f"hsl({hue}, 100%, 50%)")

for i, point in enumerate(din):
    x, y = point
    draw.point((x * scale, y * scale), fill=colors[i])
    print(f"Point {i}: {point} -> {colors[i]}")

img.save("output.png")
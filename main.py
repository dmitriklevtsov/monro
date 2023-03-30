from PIL import Image

image_monro = Image.open("monro.jpg")
#print(image_monro.mode)

red, green, blue = image_monro.split()

monro_red_left = red.crop((100, 0, 512, 512))
monro_red_m = red.crop((50, 0, 462, 512))
monroCropedRed = Image.blend(monro_red_left, monro_red_m, 0.5)

monro_blue_right = blue.crop((0, 0, 412, 512))
monro_blue_m = blue.crop((50, 0, 462, 512))
monroCropedBlue = Image.blend(monro_blue_right, monro_blue_m, 0.5)

monro_green_m = green.crop((50, 0, 462, 512))

new_monro = Image.merge("RGB", (monroCropedRed, monroCropedBlue, monro_green_m))
new_monro.save("newmonro.jpg")

new_monro.thumbnail((80,80))
new_monro.save("newmonrosmall.jpg")

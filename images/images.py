from PIL import Image

image = Image.open('./example_image.jpg')
print('=== file type:', type(image))
print('=== image:', image)
print('=== image size:', image.size)
print('=== image filename:', image.filename)
print('=== image format:', image.format)
print('=== image format description:', image.format_description)

print('=== cropping')

x = 2000
y = 2000
width = image.size[0] // 3
print(f'width: {width}')
height = image.size[1] // 10
print(f'height: {height}')
cropped = image.crop((x, y, width + x, height + y))
image.paste(im=cropped, box=(0, 0))
image.show()
image.resize((300, 500))
image.rotate(90).show()
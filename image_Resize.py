from PIL import Image

image = Image.open("python_logo.png")

print(f"Current Size of Image is {image.size}")

resized_image = image.resize((500,500))

resized_image.save("resized_python_logo.png")


def imageResizer(image_path, image_size):
    image = Image.open(image_path)
    print(f"Current Size of Image is {image.size}")

    resized_image = image.resize(image_size)
    resized_image.save("resized_"+str(image_path))


imageResizer("python1_logo.png",(1000,1000))
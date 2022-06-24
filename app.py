from PIL import Image


def read_img():
    img = Image.open("img_640x480.jpg")
    print("Successfully loaded image!")
    print("Image size: " + str(img.width) + " x " + str(img.height))


if __name__ == "__main__":
    read_img()
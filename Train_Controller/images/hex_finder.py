from PIL import Image
import collections

def find_dominant_color(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")

    # Resize the image to a small size for faster processing (adjust as needed)
    image.thumbnail((100, 100))

    # Get a list of all the RGB color values in the image
    pixels = list(image.getdata())

    # Count the occurrences of each color
    color_counter = collections.Counter(pixels)

    # Find the color that occurs most frequently
    most_common_color = color_counter.most_common(1)

    return most_common_color[0][0]

image_path = "C:/Users/Yun/Documents/ECE 1140/Train Code/ECE1140/Train_Controller/images/yellow.png"
dominant_color = find_dominant_color(image_path)
print("Dominant color in the image:", dominant_color)

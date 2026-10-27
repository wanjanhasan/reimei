from PIL import Image

# Characters ordered from darkest to lightest brightness
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=70):
  width, height = image.size
  # Aspect ratio adjustment for terminal characters
  ratio = height / width / 1.65
  new_height = int(new_width * ratio)
  return image.resize((new_width, new_height))


def grayify(image):
  return image.convert("L")


def pixels_to_ascii(image):
  pixels = image.getdata()
  # Map each pixel value (0-255) to one of the ASCII characters
  characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
  return characters


def main():
  path = input("Enter the path to your JFIF image: ")
  try:
    image = Image.open(path)
  except Exception as e:
    print(f"Error opening image: {e}")
    return

  new_width = 80
  image = resize_image(image, new_width)
  grayscale_image = grayify(image)

  ascii_str = pixels_to_ascii(grayscale_image)
  img_width = grayscale_image.width

  # Split the flat string into rows matching the image width
  ascii_img = "\n".join(
      ascii_str[i : i + img_width] for i in range(0, len(ascii_str), img_width)
  )

  # Print to terminal
  print(ascii_img)

  # Save the output to a text file for easy viewing
  with open("building_ascii.txt", "w") as f:
    f.write(ascii_img)
  print("\nSaved ASCII art to building_ascii.txt")


if __name__ == "__main__":
  main()
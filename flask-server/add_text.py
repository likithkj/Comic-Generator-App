from PIL import Image, ImageDraw, ImageFont

def add_text_to_panel(text, panel_image):
  text_image = generate_text_image(text)

  result_image = Image.new('RGB', (panel_image.width, panel_image.height + text_image.height))

  result_image.paste(panel_image, (0, 0))

  result_image.paste(text_image, (0, panel_image.height))

  return result_image

def generate_text_image(text):
    text = text.replace("\n", "") 

    width = 1024
    height = 128

    image = Image.new('RGB', (width, height), color='white')

    draw = ImageDraw.Draw(image)

    font_path = r"C:\Users\Likith K\Downloads\comics_generator-master\comics_generator-master\manga-temple.ttf"  # Adjust the path to the actual font file
    font_size = 30
    font = ImageFont.truetype(font=font_path, size=font_size)

    text_width = draw.textlength(text, font=font,direction='ltr')
    text_height  = draw.textlength(text, font=font,direction='ttb')
    print(text_width,text_height)

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    print(x,y)
    text_color = (0, 0, 0)

    draw.text((x, y), text, fill=text_color, font=font)
    
    return image


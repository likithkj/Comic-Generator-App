from PIL import Image

def resize_and_add_border(image, target_size, border_size):
    resized_image = Image.new("RGB", target_size, "black")
    resized_image.paste(image, ((target_size[0] - image.width) // 2, (target_size[1] - image.height) // 2))
    return resized_image

def create_strip(images):
    columns, rows = 2, 3

    output_width = columns * images[0].width + (columns - 1) * 10  
    output_height = rows * images[0].height + (rows - 1) * 10  

    result_image = Image.new("RGB", (output_width, output_height), "white")

    for i, img in enumerate(images):
        x = (i % columns) * (img.width + 10)  
        y = (i // columns) * (img.height + 10)  

        resized_img = resize_and_add_border(img, (images[0].width, images[0].height), 10)
        result_image.paste(resized_img, (x, y))

    return result_image.resize((1024, 1536))

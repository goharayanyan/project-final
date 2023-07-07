from PIL import Image, ImageOps
import math

def resize_image(image_path, width=None, height=None, fill_color=None):
    img = Image.open(image_path)
    orig_width, orig_height = img.size
    
    if orig_width is None or orig_height is None:
        # Handle case where image dimensions are not valid
        return None
    
    if width and height:
        # Both width and height are specified
        if orig_width / width > orig_height / height:
            # Resize based on width
            new_width = width
            new_height = int(round(orig_height * (width / float(orig_width))))
        else:
            # Resize based on height
            new_height = height
            new_width = int(round(orig_width * (height / float(orig_height))))
    elif width:
        # Only width is specified
        new_width = width
        new_height = int(round(orig_height * (width / float(orig_width))))
    elif height:
        # Only height is specified
        new_height = height
        new_width = int(round(orig_width * (height / float(orig_height))))
    else:
        # Neither width nor height is specified
        new_width = orig_width
        new_height = orig_height
    
    # Create new image with the specified size and fill color
    new_img = Image.new('RGB', (new_width, new_height), fill_color or (255, 255, 255))
    
    # Resize and crop the original image and paste it onto the new image
    img_ratio = orig_width / float(orig_height)
    new_ratio = new_width / float(new_height)
    if img_ratio > new_ratio:
        # Crop based on height
        crop_height = int(round(orig_height * new_ratio))
        crop_top = (orig_height - crop_height) // 2
        img = img.crop((0, crop_top, orig_width, crop_top + crop_height))
    elif img_ratio < new_ratio:
        # Crop based on width
        crop_width = int(round(orig_width / new_ratio))
        crop_left = (orig_width - crop_width) // 2
        img = img.crop((crop_left, 0, crop_left + crop_width, orig_height))
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    new_img.paste(img, ((new_width - img.size[0]) // 2, (new_height - img.size[1]) // 2))
    
    return new_img

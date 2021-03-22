from PIL import Image, ImageDraw,ImageFont
import requests, os

def download_img(url):
    response = requests.get(url)
    file_path = f"temp_imgs/{url.split('/')[-1]}.jpg"

    file = open(file_path, "wb")
    file.write(response.content)
    file.close()

    return file_path

def delete_img(url):
    file_path = f"temp_imgs/{url.split('/')[-1]}.jpg"
    os.remove(file_path)

def create_thumbnail(comments):
    img = Image.open("temp_imgs/base_img.png")
    draw = ImageDraw.Draw(img)
    
    num_comments = 3
    top = 660
    left = 20
    photo_size = 50
    name_pos = top - 30
    name_size = 18
    desc_size = 20
    comment_size = 420
    
    for comment in comments[:num_comments]:
        im1 = Image.open(download_img(comment["authorProfileImageUrl"]))

        img.paste(im1, (left, top))
        
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arialbd.ttf", name_size)
        draw.text((left, name_pos),comment["authorDisplayName"],
            fill='black',font=font)

        font = ImageFont.truetype("arial.ttf", desc_size)
        draw.text((left + photo_size, top),
            comment["textOriginal"][:33],
            fill='black',
            font=font)
            
        draw.text((left + photo_size, top + desc_size),
            comment["textOriginal"][33:66],
            fill='black',
            font=font)

        left += comment_size
        delete_img(comment["authorProfileImageUrl"])

    final_img = 'temp_imgs/thumb.png'
    img.save(final_img)
    return final_img
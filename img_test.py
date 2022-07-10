from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


username ="Faiyaz"

#font = ImageFont.load_default()
font =ImageFont.truetype("arial.ttf", 27)
img = Image.open('where.png')



draw = ImageDraw.Draw(img)
draw.text((520, 300),"Where "+username,(255,255,255),font=font,stroke_width=2, stroke_fill="#000")




img.save('temp.png')

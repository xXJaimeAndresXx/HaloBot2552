import requests
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from googletrans import Translator, constants
from pprint import pprint
import cv2
import numpy as np
import textwrap

translator = Translator()

def domain_info(main):
  img = cv2.imread('IMG/domain_2.jpg')
  print(img.shape)

  height, width, channel = img.shape

  text_img = np.ones((height, width))
  print(text_img.shape)
  font = cv2.FONT_HERSHEY_SIMPLEX

  text = main
  wrapped_text = textwrap.wrap(text, width=35)
  x, y = 10, 40
  font_size = 1
  font_thickness = 2

  for i, line in enumerate(wrapped_text):
      textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

      gap = textsize[1] + 10

      y = int((img.shape[0] + textsize[1]) / 2) + i * gap
      x = int((img.shape[1] - textsize[0]) / 2)

      cv2.putText(img, line, (x, y), font,
                  font_size, 
                  (255,255,255), 
                  font_thickness, 
                  lineType = cv2.LINE_AA)

  cv2.imshow("Result Image", img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def get_data(id):
    r2=requests.get("https://halo.fandom.com/es/api/v1/Articles/AsSimpleJson?id="+id)
    #print(r2.json())
    response2=r2.json()
    title= response2["sections"][0]["title"]
    main1= response2["sections"][0]["content"][0]["text"]
    try:
      main2=response2["sections"][0]["content"][1]["text"]
      main=main1+" "+main2
    except:
      main=main1
    #history= response2["sections"][1]["content"][0]["text"]
    return title,main
def get_image(id):
    r3=requests.get("https://halo.fandom.com/es/api/v1/Articles/AsSimpleJson?id="+id)
    response3=r3.json()
    image= response3["sections"][0]["images"][0]["src"]
    return image
def get_history(id):
    r4=requests.get("https://halo.fandom.com/es/api/v1/Articles/AsSimpleJson?id="+id)
    response4=r4.json()
    history=response4["sections"][1]["content"][0]["text"]
    return history




payload= {'action':'query', 'generator':'random','grnnamespace':'0','grnlimit':'1','prop':'info','format':'json'}
r= requests.get("https://halo.fandom.com/es/api.php",params=payload)
response= r.json()
#for key, values in response.items():
 #  print(key)


key= response["query"]["pages"]
#print(key)

for key, values in key.items() :
    id= key
    print ("Domain Entrance: "+id)

title,main= get_data(id)
translation = translator.translate(title, dest="en")
translation_main= translator.translate(main, dest="en")


print("Title: "+ title)
print("Body: "+ main)
try:
  history=get_history(id)
  print("History: "+ history)
except:
  print("History: <---CORRUPTED DOMAIN CAN NOT RETRIEVE MORE INFORMATION--->")

try:
  image=get_image(id)
  lore_image= requests.get(image)
  img=Image.open(BytesIO(lore_image.content))
  img.show()
  print("Image: "+ image)
except:
  print("Image: <---CORRUPTED DOMAIN CAN NOT RETRIEVE IMAGE DATA--->") 
  #domain_info(main)
  sp_int= Image.open("IMG/domain_1.jpg")
  font_type= ImageFont.truetype("./Courier-PS-Bold.ttf",20)
  draw= ImageDraw.Draw(sp_int)
  draw.text(xy=(545,92),text= "Subject: "+ translation.text, fill=(255,246,67),font=font_type)
  draw.text(xy=(610,198),text= "(halobot):", fill=(166,250,237),font=font_type)
  draw.text(xy=(610,327),text= "(halobot):", fill=(166,250,237),font=font_type)
  draw.text(xy=(306,655),text= "//file;-: "+ id, fill=(166,250,237),font=font_type)
  #draw.multiline_text(xy=(547,228),text= "hello\nWorld", fill=(255,246,67),font=font_type,spacing = 10, align ="right")
  sp_int.show()


translation = translator.translate(title, dest="en")
translation_main= translator.translate(main, dest="en")
print("-----------------------------------------------------------------------------")
print(f"{translation.text} ({translation.dest})")
print(f"{translation_main.text} ({translation_main.dest})")
try:
  translation_history= translator.translate(history, dest="en")
  print(f"{translation_history.text} ({translation_history.dest})")
except:
  pass


#print(title)

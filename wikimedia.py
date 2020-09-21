import requests
from PIL import Image
from io import BytesIO

def get_data(id):
    r2=requests.get("https://halo.fandom.com/api/v1/Articles/AsSimpleJson?id="+id)
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
    r3=requests.get("https://halo.fandom.com/api/v1/Articles/AsSimpleJson?id="+id)
    response3=r3.json()
    image= response3["sections"][0]["images"][0]["src"]
    return image
def get_history(id):
    r4=requests.get("https://halo.fandom.com/api/v1/Articles/AsSimpleJson?id="+id)
    response4=r4.json()
    history=response4["sections"][1]["content"][0]["text"]
    return history




payload= {'action':'query', 'generator':'random','grnnamespace':'0','grnlimit':'1','prop':'info','format':'json'}
r= requests.get("https://halo.fandom.com/api.php",params=payload)
response= r.json()
#for key, values in response.items():
 #  print(key)


key= response["query"]["pages"]
#print(key)

for key, values in key.items() :
    id= key
    print ("Domain Entrance: "+id)

title,main= get_data(id)


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




#print(title)

import requests as req
import ujson as json

with open('scryfall-default-cards.json', 'r') as f:
    json_text = f.read()

art_crop = []

card_dict = json.loads(json_text)

for i in card_dict:
    art_crop.append(card_dict[i]['image_uris']['art_crop'])

# print(card_dict[0]['image_uris']['art_crop'])




# Psuedo code
#
import ujson as json
import pandas as pd

# open json file and read it into json_text variable
with open('scryfall-default-cards.json', 'r') as f:
    json_text = f.read()

#  Load the json into the card_dict variable
card_dict = json.loads(json_text)

# Sample json of one card.
'''
{
  "object": "card",
  "id": "03f4341c-088b-4f35-b82b-3d98d8a93de4",
  "oracle_id": "d7ac4be1-dcca-49b6-8ddb-d1b0e6cf2dcf",
  "multiverse_ids": [
    416835
  ],
  "tcgplayer_id": 121434,
  "name": "Queen Marchesa",
  "lang": "en",
  "released_at": "2016-08-26",
  "uri": "https://api.scryfall.com/cards/03f4341c-088b-4f35-b82b-3d98d8a93de4",
  "scryfall_uri": "https://scryfall.com/card/cn2/78/queen-marchesa?utm_source=api",
  "layout": "normal",
  "highres_image": true,
  "image_uris": {
    "small": "https://img.scryfall.com/cards/small/en/cn2/78.jpg?1517813031",
    "normal": "https://img.scryfall.com/cards/normal/en/cn2/78.jpg?1517813031",
    "large": "https://img.scryfall.com/cards/large/en/cn2/78.jpg?1517813031",
    "png": "https://img.scryfall.com/cards/png/en/cn2/78.png?1517813031",
    "art_crop": "https://img.scryfall.com/cards/art_crop/en/cn2/78.jpg?1517813031",
    "border_crop": "https://img.scryfall.com/cards/border_crop/en/cn2/78.jpg?1517813031"
  },
  "mana_cost": "{1}{R}{W}{B}",
  "cmc": 4.0,
  "type_line": "Legendary Creature — Human Assassin",
  "oracle_text": "Deathtouch, haste\nWhen Queen Marchesa enters the battlefield, you become the monarch.\nAt the beginning of your upkeep, if an opponent is the monarch, create a 1/1 black Assassin creature token with deathtouch and haste.",
  "power": "3",
  "toughness": "3",
  "colors": [
    "B",
    "R",
    "W"
  ],
  "color_identity": [
    "B",
    "R",
    "W"
  ],
  "all_parts": [
    {
      "object": "related_card",
      "id": "03f4341c-088b-4f35-b82b-3d98d8a93de4",
      "component": "combo_piece",
      "name": "Queen Marchesa",
      "type_line": "Legendary Creature — Human Assassin",
      "uri": "https://api.scryfall.com/cards/03f4341c-088b-4f35-b82b-3d98d8a93de4"
    },
    {
      "object": "related_card",
      "id": "f577d422-59d7-43ab-a822-2d73d47e61dd",
      "component": "token",
      "name": "Assassin",
      "type_line": "Token Creature — Assassin",
      "uri": "https://api.scryfall.com/cards/f577d422-59d7-43ab-a822-2d73d47e61dd"
    }
  ],
  "legalities": {
    "standard": "not_legal",
    "future": "not_legal",
    "frontier": "not_legal",
    "modern": "not_legal",
    "legacy": "legal",
    "pauper": "not_legal",
    "vintage": "legal",
    "penny": "not_legal",
    "commander": "legal",
    "duel": "legal",
    "oldschool": "not_legal"
  },
  "games": [
    "paper"
  ],
  "reserved": false,
  "foil": true,
  "nonfoil": true,
  "oversized": false,
  "promo": false,
  "reprint": false,
  "set": "cn2",
  "set_name": "Conspiracy: Take the Crown",
  "set_uri": "https://api.scryfall.com/sets/ad1b8847-1905-4080-9e26-80691ea7c1ef",
  "set_search_uri": "https://api.scryfall.com/cards/search?order=set&q=e%3Acn2&unique=prints",
  "scryfall_set_uri": "https://scryfall.com/sets/cn2?utm_source=api",
  "rulings_uri": "https://api.scryfall.com/cards/03f4341c-088b-4f35-b82b-3d98d8a93de4/rulings",
  "prints_search_uri": "https://api.scryfall.com/cards/search?order=released&q=oracleid%3Ad7ac4be1-dcca-49b6-8ddb-d1b0e6cf2dcf&unique=prints",
  "collector_number": "78",
  "digital": false,
  "rarity": "mythic",
  "illustration_id": "4dd3219b-2923-425d-9dc8-c346a89d7d66",
  "artist": "Kieran Yanner",
  "border_color": "black",
  "frame": "2015",
  "frame_effect": "",
  "full_art": false,
  "story_spotlight": false,
  "edhrec_rank": 3072,
  "usd": "18.48",
  "eur": "14.74",
  "prices": {
    "usd": "18.48",
    "usd_foil": "119.46",
    "eur": "14.74",
    "tix": null
  },
  "related_uris": {
    "gatherer": "http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=416835",
    "tcgplayer_decks": "https://decks.tcgplayer.com/magic/deck/search?contains=Queen+Marchesa&page=1&partner=Scryfall&utm_campaign=affiliate&utm_medium=scryfall&utm_source=scryfall",
    "edhrec": "http://edhrec.com/route/?cc=Queen+Marchesa",
    "mtgtop8": "http://mtgtop8.com/search?MD_check=1&SB_check=1&cards=Queen+Marchesa"
  },
  "purchase_uris": {
    "tcgplayer": "https://shop.tcgplayer.com/magic/conspiracy-take-the-crown/queen-marchesa?partner=Scryfall&utm_campaign=affiliate&utm_medium=scryfall&utm_source=scryfall",
    "cardmarket": "https://www.cardmarket.com/en/Magic/Products/Singles/Conspiracy-Take-the-Crown/Queen-Marchesa?referrer=scryfall",
    "cardhoarder": "https://www.cardhoarder.com/cards?affiliate_id=scryfall&data%5Bsearch%5D=Queen+Marchesa&ref=card-profile&utm_campaign=affiliate&utm_medium=card&utm_source=scryfall"
  }
}
'''

'''
These are all list comprehensions which grab the 'id' of each card and a specific image uri. 
Where a uri does not exist a 'N/A' is inserted into the list.
Each list only contains key:values where the 'lang' == 'en'
'''

img_sm = [{d['id']: d.get('image_uris', {}).get('small', 'N/A')} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Khans of Tarkir']
img_normal = [{d['id']: d.get('image_uris', {}).get('normal', 'N/A')} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Khans of Tarkir']
img_lg = [{d['id']: d.get('image_uris', {}).get('large', 'N/A')} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Khans of Tarkir']
# img_lg_test = img_lg[1144:1180]
img_png = [{d['id']: d.get('image_uris', {}).get('png', 'N/A')} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Khans of Tarkir']
img_art_crop = [{d['id']: d.get('image_uris', {}).get('art_crop', 'N/A')} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Khans of Tarkir']
img_border_crop = [{d['id']: d.get('image_uris', {}).get('border_crop', 'N/A')} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'CKhans of Tarkir']

# This was a done to pull just the language into a list for analysis
language = [d['lang'] for d in card_dict]

len(set(language))

# Pushed the language list to a df to
df = pd.DataFrame(language, columns=['Lang'])
df.Lang.unique()
df.Lang.value_counts()

# ------- Variety of print statements to visualize output ------
print(img_art_crop)
# print(img_lg)
# print(img_sm[1144:1180])
# print(img_normal[:3])
# print(img_lg[:3])
# print(img_png[:3])
# print(img_art_crop[:3])
# print(img_border_crop[:3])
# print(card_dict[1:4])



import os
import urllib.request

# Loop through the final specified list and save 'large' images to local defined storage
# for dicts in img_lg:  # iterate over the list of dicts
#     for filename, url in dicts.items():  # for each dict, iterate over each key-value pair
#         fullfilename = os.path.join('lg_img_Khans_of_Tarkir/', filename + '_lg.jpg')  # location for storage and add suffix to file name
#         try:
#             urllib.request.urlretrieve(url, fullfilename)  # try to grab the image
#         except ValueError: # if there is no URL/image then fail silently
#             pass

# Loop through the final specified list and save 'art_crop' images to local defined storage
for dicts in img_art_crop:  # iterate over the list of dicts
    for filename, url in dicts.items():  # for each dict, iterate over each key-value pair
        fullfilename = os.path.join('art_crop_img_Khans_of_Tarkir/', filename + '_art_crop.jpg')  # location for storage and add suffix to file name
        try:
            urllib.request.urlretrieve(url, fullfilename)  # try to grab the image
        except ValueError: # if there is no URL/image then fail silently
            pass
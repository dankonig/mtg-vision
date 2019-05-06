# See https://github.com/dankonig/mtg-vision/blob/master/sample_card_json for example of json

import ujson as json
import pandas as pd

# open json file and read it into json_text variable
with open('scryfall-default-cards.json', 'r') as f:
    json_text = f.read()

#  Load the json into the card_dict variable
card_dict = json.loads(json_text)

'''
These are all list comprehensions which grab the 'id' of each card and a specific image uri. 
Where a uri does not exist a 'N/A' is inserted into the list.
Each list only contains key:values where the 'lang' == 'en'
'''

img_sm = [{d['id']: [d.get('image_uris', {}).get('small', 'N/A'), d.get('name'), d.get('collector_number')]} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Core Set 2019']
img_normal = [{d['id']: [d.get('image_uris', {}).get('normal', 'N/A'), d.get('name'), d.get('collector_number')]} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Core Set 2019']
img_lg = [{d['id']: [d.get('image_uris', {}).get('large', 'N/A'), d.get('name'), d.get('collector_number')]} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Core Set 2019']
# img_lg_test = img_lg[1144:1180]
img_png = [{d['id']: [d.get('image_uris', {}).get('png', 'N/A'), d.get('name'), d.get('collector_number')]} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Core Set 2019']
img_art_crop = [{d['id']: [d.get('image_uris', {}).get('art_crop', 'N/A'), d.get('name'), d.get('collector_number')]} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Core Set 2019']
img_border_crop = [{d['id']: [d.get('image_uris', {}).get('border_crop', 'N/A'), d.get('name'), d.get('collector_number')]} for d in card_dict if d['lang'] == 'en' and d['set_name'] == 'Core Set 2019']

# This was a done to pull just the language into a list for analysis
language = [d['lang'] for d in card_dict]

len(set(language))

# Pushed the language list to a df to
df = pd.DataFrame(language, columns=['Lang'])
df.Lang.unique()
df.Lang.value_counts()

# ------- Variety of print statements to visualize output ------
# print((img_sm))
2# print(img_sm[1144:1180])
# print(img_normal[:3])
# print(img_lg[:3])
# print(img_png[:3])
print(img_art_crop[:3])
# print(img_border_crop[:3])
# print(card_dict[1:4])



import os
import urllib.request

# Loop through the final specified list and save 'large' images to local defined storage
for dicts in img_lg:  # iterate over the list of dicts
    for filename, url in dicts.items():  # for each dict, iterate over each key-value pair
        fullfilename = os.path.join('lg_img_Core_2019/', url[2] + '_' + url[1] + '_' + filename + '_lg.jpg')  # location for storage and add suffix to file name
        try:
            urllib.request.urlretrieve(url[0], fullfilename)  # try to grab the image
        except ValueError: # if there is no URL/image then fail silently
            pass

# Loop through the final specified list and save 'art_crop' images to local defined storage
for dicts in img_art_crop:  # iterate over the list of dicts
    for filename, url in dicts.items():  # for each dict, iterate over each key-value pair
        fullfilename = os.path.join('art_crop_img_Core_2019/', url[2] + '_' + url[1] + '_' + filename + '_art_crop.jpg')  # location for storage and add suffix to file name
        try:
            urllib.request.urlretrieve(url[0], fullfilename)  # try to grab the image
        except ValueError: # if there is no URL/image then fail silently
            pass
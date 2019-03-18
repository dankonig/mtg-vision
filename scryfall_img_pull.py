import ujson as json

with open('scryfall-default-cards.json', 'r') as f:
    json_text = f.read()

card_dict = json.loads(json_text)

img_ids = [{d['id']: d.get('image_uris', {}).get('large', 'N/A')} for d in card_dict]

print(card_dict[:3])
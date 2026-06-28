"""
This file was created to parse the Factorio dump
 and generate themed JSON files.

"""

import json

DUMP_FACTORIO_JSON = "/Users/s1ugh/Library/Application Support/factorio/script-output/data-raw-dump.json"
ITEMS_FACTORIO_JSON = "items_factorio.json"
RECIPE_JSON = "recipe_factorio.json"
TARGET_CATEGORIES = ["item", "ammo", "armor", "gun", "tool", "capsule", "module"]

# JSON files created for items
def created_items_factorio(input_path, output_path, target):

    my_items = {}

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for category in target:
        if category in data:
            for item_id, item_data in data[category].items():
                if 'parameter' in item_id or 'unknow' in item_id:
                    continue
                my_items[item_id] = item_data
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(my_items, f, indent=4, ensure_ascii=False)

    print(f'Данные сохранены в {output_path}')
# JSON files created for recipe
def created_recipe_factorio(input_path, output_path):

    recipe_factorio = {}

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for recipe_name, recipe_details in data.get('recipe').items():
        if ('parameter' in recipe_name or 'unknow' in recipe_name):
            continue
        recipe_factorio[recipe_name] = recipe_details

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(recipe_factorio, f, indent=4, ensure_ascii=False)

    print(f'Данные записаны в {output_path}')


#created_items_factorio(DUMP_FACTORIO_JSON, items_factorio_json, target_categories)
created_recipe_factorio(DUMP_FACTORIO_JSON, RECIPE_JSON)

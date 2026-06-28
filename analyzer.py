import json

# Output items where stack_size = 100
def print_items_by_stack_size(input_path, target_size = 100):

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item_name, item_details in data.items():
        if item_details.get('stack_size') == target_size:
            print(f'{item_name}: {target_size} шт')

# Output recipes where target_ingredient = 'fluid'
def print_recipe_by_fluid(input_path, target_ingredient = 'fluid'):

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for recipe_name, recipe_details in data.items():

        ingredients = recipe_details.get('ingredients', [])

        if isinstance(ingredients, list):
            for item_by_recipe in ingredients:
                if target_ingredient == item_by_recipe.get('type'):
                    print(f'{recipe_name}')
                    break

# Output recipes where min_time >= 10
def print_slow_recipe(input_path, min_time = 10):

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for recipe_name, recipe_details in data.items():
        energy_required = recipe_details.get('energy_required', 0.5)
        if energy_required >= min_time:
            print(f'{recipe_name} - {energy_required}c')

# Output the max amount
def find_max_yield_recipe(input_path):

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    max_count = 0
    best_price = ''

    for recipe_name, recipe_details in data.items():
        results = recipe_details.get('results', [])
        for result in results:
            if result.get('amount') > max_count:
                max_count = result.get('amount')
                best_price = ''.join(recipe_name)
    print(f'{best_price} - {max_count}шт')

# Output recipes where target_ingredient = 'iron-plate'
def count_recipe_by_ingredient(input_path, target_ingredient = 'iron-plate'):

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    count_ = 0
    for _ , recipe_details in data.items():

        ingredients = recipe_details.get('ingredients', [])

        if isinstance(ingredients, list):

            for ingredient in ingredients:
                if isinstance(ingredient, dict):
                    if ingredient.get('name') == target_ingredient:
                        count_ += 1
    print(f'{target_ingredient} используется в {count_} рецептах')

# Output all items within the given parameters
def filter_items_by_stack_size(input_path, min_stack_size = 10, max_stack_size = 50):

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item_name, item_details in data.items():

        if ((item_details.get('stack_size') >= min_stack_size)
                and item_details.get('stack_size') <= max_stack_size):
            print(f'{item_name}: {item_details.get("stack_size")}')

# Output the longes recipe
def find_longest_recipe(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    max_count = 0
    longest_recipe = ''

    for recipe_name, recipe_details in data.items():
        energy_required = recipe_details.get('energy_required', 0.5)

        if energy_required > max_count:
            max_count = energy_required
            longest_recipe = recipe_name
    print(f'{longest_recipe} - {max_count}c')

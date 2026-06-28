from analyzer import(
    print_items_by_stack_size,
    print_recipe_by_fluid,
    print_slow_recipe,
    find_max_yield_recipe,
    count_recipe_by_ingredient,
    filter_items_by_stack_size,
    find_longest_recipe
)

ITEMS_FACTORIO_JSON = "items_factorio.json"
RECIPE_JSON = "recipe_factorio.json"

print_items_by_stack_size(ITEMS_FACTORIO_JSON)
print_recipe_by_fluid(RECIPE_JSON)
print_slow_recipe(RECIPE_JSON)
find_max_yield_recipe(RECIPE_JSON)
count_recipe_by_ingredient(RECIPE_JSON)
filter_items_by_stack_size(ITEMS_FACTORIO_JSON)
find_longest_recipe(RECIPE_JSON)

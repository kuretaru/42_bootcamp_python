import os

DEBUG = os.getenv('DEBUG', '0').lower() in ['1', 'true', 't']
FIRSTS_PARTS = os.getenv('FIRSTS_PARTS', '0').lower() in ['1', 'true', 't']
cookbook = dict()


def validate_recipe(cls):
    """
    Validator and decorator for the recipe.

    Attributes:
        cls (class): Class of the selected recipe.

    Returns:
        class: If function run successfuly.

    Raises:
        ValueError: If prep_time negative or zeroed integer. 
    """
    orig_init = cls.__init__

    def new_init(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)

        if not isinstance(self.prep_time, int) or self.prep_time<=0:
            raise ValueError(f"Preparation time for {cls.__name__} must be non-negative integer.")

        if DEBUG:
            print(f"Receipe {cls.__name__} succesfully go through our validation and is added to the cookbook!")

    cls.__init__ = new_init
    return cls


@validate_recipe
class Recipe:
    """
    Class for represantion one recipe-item in cookbook.

    Attributes:
        dish (str): Name of the dish.
        ingredients (list): List of the ingredients.
        meal (str): Type of the meal (e.g. "lunch" or "desert").
        prep_time (int): Non-negative preparation time (in minutes). 
    """
    def __init__(self, dish, ingredients, meal, prep_time):
        """An initialization of the instance of class."""
        self.dish = dish
        self.ingredients = ingredients
        self.meal = meal
        self.prep_time = prep_time

        cookbook[self.dish] = {
                "ingredients":ingredients,
                "meal":meal,
                "prep_time":prep_time
        }


def print_all_recipes(book):
    """
    Simple print for all the recipes in cookbook.

    Attributes:
        book (dict): Dictanory of the cookbook. 
    
    Returns:
        None: If cookbook is None.
    """
    if not book:
        print("Cookbook is empty!")
        return

    for name, details in book.items():
        ingredients_list = details["ingredients"]
        meal_type = details["meal"]
        prep_time_mins = details["prep_time"]
        
        print(f"The {name}'s ingredients", end=" ")
        if len(ingredients_list)>1:
            all_but_last = ", ".join(ingredients_list[:-1])
            ingredients_str = f"{all_but_last} and {ingredients_list[-1]}"
            print("are", end=" ")
        elif len(ingredients_list)==1:
            ingredients_str = ingredients_list[0]
            print("is", end=" ")
        else:
            ingredients_str = "nothing"
        print(f"{ingredients_str}. It's a {meal_type} and it takes {prep_time_mins} minutes of preparation.")


def print_all_names(book):
    """
    Prints every single dishes name.

    Attributes:
        book (dict): Dictanory of the cookbook.
    
    Returns:
        None: If cookbook is None.
    """
    if not book:
        print("Cookbook is empty!")
        return

    for each in book:
        print(each)


def print_only_details(recipe_name, book):
    """
    Search fot details of a specific recipe name.

    Attributes:
        recipe_name (str): Searchible name for the recipe.
        book (dict): Dictionary of the cookbook.
    
    Returns:
        None: If cookbook is None.
    """
    if not book:
        print("Cookbook is empty!")
        return

    if recipe_name in book:
        ingredients_list = book[recipe_name]["ingredients"]
        if len(ingredients_list)>1:
            all_but_last = ", ".join(ingredients_list[:-1])
            ingredients_str = f"{all_but_last} and {ingredients_list[-1]}"
        elif len(ingredients_list)==1:
            ingredients_str = ingredients_list[0]
        else:
            ingredients_str = "nothing"
        print(f"The {recipe_name}'s ingredients are {ingredients_str}. It's a {book[recipe_name]['meal']} and it takes {book[recipe_name]['prep_time']} minutes of preparation.")
    else:
        print("Recipe is not found! You can add it via calling manual_add_recipe(book) function.")


def remove_recipe_by_name(recipe_name, book):
    """
    Print a result of the attending to delete a recipe block in the dictionary.

    Attributes:
        recipe_name (str): Searchible name for the recipe.
        book (dict): Dictionary of the cookbook.
    
    Returns:
        None: If cookbook is None.

    """
    if not book:
        print("Cookbook is empty!")
        return

    try:
        del book[recipe_name]
        print(f"Recipe {recipe_name} has been succesfully deleted!")
    except KeyError:
        print(f"Error: Recipe {recipe_name} hasn't been deleted cuz it's not found. Try again.")


def manual_add_recipe(book):
    """
    Print a result of the attending to delete a recipe block in the dictionary.

    Attributes:
        book (dict): Dictionary of the cookbook.
    
    Returns:
        dict: New generated dict.
    """
    recipe_name = input (">>> Enter a name:\n")
    ingredients = []
    print(">>> Enter ingredients:")
    for line in iter(input, ''):
        ingredients.append(line)
    meal = input(">>> Enter meal type:\n")
    prep_time = input(">>> Enter preparation time:\n")
    book[recipe_name] = {
        "ingredients":ingredients,
        "meal":meal,
        "prep_time":prep_time
    }


def main():
    """
    Main func of the program. Generates a global dict cookbook and then outputs it via simple print.

    Raises:
        ValueError: If some abstraction, that tends to be an recipe isn't validated.  
    """
    options = ['Add a recipe', 'Delete a recipe', 'Print a recipe', 'Print the cookbook', 'Quit']
    if FIRSTS_PARTS:
        try:
            sandwitch = Recipe("sandwitch", ["ham","bread","cheese", "tomatoes"], "lunch", 10)
            cake = Recipe("cake", ["flour","sugar","eggs"], "dessert", 60)
            salad = Recipe("salad", ["avocado","argula","tomatoes", "spinach"], "lunch", 15)
        except ValueError as e:
            print(f"Error: {e}")
        print_all_recipes(cookbook)
        print_all_names(cookbook)
        print_only_details("cake", cookbook)
        remove_recipe_by_name("cake", cookbook)
        print_all_recipes(cookbook)
        manual_add_recipe(cookbook)
        print_all_recipes(cookbook)
    else:
        print(f"Welcome to the Python Cookbook !\nList of availible options:")
        for index, option in enumerate(options):
            print(f"{index}: {option}")
        while True:
            cur_option = input("\nPlease select an option:\n>> ")
            match cur_option:
                case "0":
                    manual_add_recipe(cookbook)
                case "1":
                    remove_recipe_by_name(input("Please enter a recipe name to attend deleting it.\n>> "), cookbook)
                case "2":
                    print_only_details(input("Please enter a recipe name to get its details:\n>> "), cookbook)
                case "3":
                    print_all_recipes(cookbook)
                case "4":
                    break
                case default:
                    print("Sorry, this option does not exist.\nList of availible options:")
                    for index, option in enumerate(options):
                        print(f"{index}: {option}")


if __name__ == "__main__":
    main()
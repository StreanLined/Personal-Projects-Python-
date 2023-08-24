import json

def load_recipes():
    try:
        with open("recipes.json", "r") as file:

            return json.load(file)
    except FileNotFoundError:
        return []

def save_recipes(recipes):
    with open("recipes.json", "w") as file:
        json.dump(recipes, file)

def add_recipes():
    recipe = {}
    recipe["name"] = input("Enter the recipe name: ").capitalize()
    recipe["dish_region"] = input("Enter the dish region: ").capitalize().lower()
    recipe["dish_country"] = input("Enter the dish country: ").capitalize().lower()
    recipe["primary_ingredient"] = [ingredient.strip().capitalize() for ingredient in input("Enter the primary ingredient: ").split(",")]

    all_ingredients = []
    while True:
        ingredient_name = input("Enter an ingredient name (or 'done' to finish): ").capitalize()
        if ingredient_name.lower() == "done":
            break

        amount = float(input("Enter the amount of the ingredient: "))
        unit = input("Enter the unit of measurement ('ml' or 'g'): ").lower()

        ingredient_data = {"name": ingredient_name, "amount": amount, "unit": unit}
        all_ingredients.append(ingredient_data)

    recipe["all_ingredients"] = all_ingredients
    recipe["cooking_time"] = int(input("Enter the cooking time (in minutes): "))

    recipes = load_recipes()  # Load existing recipes from the file
    recipes.append(recipe)  # Append the new recipe dictionary to the list of recipes

    save_recipes(recipes)   # Save the updated list of recipes to the file
    print(f"Recipe '{recipe['name']}' added successfully!")

def search_recipes():
    print("\nFilter recipes by:")
    print("1. Dish name")
    print("2. Region")
    print("3. Country")
    print("4. Primary ingredient")
    filter_option = input("Filter by: ")

    recipes = load_recipes()  # Load recipes from the file

    if filter_option == "1":
        dish_name = input("Enter dish name: ").strip().capitalize().lower()
        matching_recipes = [recipe for recipe in recipes if dish_name in recipe["name"].lower()]
    elif filter_option == "2":
        region = input("Enter region: ").strip().capitalize().lower()
        matching_recipes = [recipe for recipe in recipes if region in recipe["dish_region"].lower()]
    elif filter_option == "3":
        country = input("Enter country: ").strip().capitalize().lower()
        matching_recipes = [recipe for recipe in recipes if country in recipe["dish_country"].lower()]
    elif filter_option == "4":
        primary_ingredient = input("Enter primary ingredient: ").strip().capitalize().lower()
        matching_recipes = [recipe for recipe in recipes if primary_ingredient in [ing.lower() for ing in recipe["primary_ingredient"]]]
    else:
        print("Error. Invalid input")
        return

    if matching_recipes:
        print(f"\nNumber of recipes that match: {len(matching_recipes)}")
        print("Matching recipes:")
        for recipe in matching_recipes:
            print(f"Dish name: {recipe['name']}")
            print(f" - Region: {recipe['dish_region'].capitalize()}")
            print(f" - Country: {recipe['dish_country'].capitalize()}")
            print(f" - Cooking time: {recipe['cooking_time']} minutes")
            print(" - All ingredients:")
            for ingredient in recipe['all_ingredients']:
                print(f"   {ingredient['name']} {int(ingredient['amount'])}{ingredient['unit']}")

        input("\nPress any key to continue...")
    else:
        print("No recipes found matching the given criteria.")


def main():
    print("Welcome to the Cookbook Application!")
    recipes = load_recipes() #loads recipes.json
    print(f"Number of recipes: {len(recipes)}")

    while True:
        print("\n1. Add a new recipe")
        print("2. Search for recipes")
        print("3. Exit")

        choice = input("Option: ")

        if choice == "1":
            add_recipes()
        elif choice == "2":
            search_recipes()
        elif choice == "3":
            print("Thank you for using the Cookbook Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
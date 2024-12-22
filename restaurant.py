def add(menu, item):
    menu.append(item)
    return menu
def remove(menu, item):
    if item in menu:
        menu.remove(item)
        return menu
    else:
        return f"{item} is not on the menu."
def availability(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"
menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
updated_menu = add(menu, add_item)
remove_item = "Salad"
updated_menu = remove(updated_menu, remove_item)
check_item = "Pizza"
availability =availability(updated_menu, check_item)
print(f"Updated menu: {updated_menu}")
print(availability)
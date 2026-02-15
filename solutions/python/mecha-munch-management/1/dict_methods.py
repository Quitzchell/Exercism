"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    
    for item in items_to_add:
            current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    user_cart = {}
    return add_item(user_cart, notes)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfilment = {}
    for product, qty in cart.items():
        fulfilment[product] = [qty] + aisle_mapping.get(product)

    return dict(sorted(fulfilment.items(), reverse=True))
        
        


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order. 

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for product in fulfillment_cart:
        if store_inventory[product][0] - fulfillment_cart[product][0] == 0:
            store_inventory[product][0] = "Out of Stock"
        else:
            store_inventory[product][0] = store_inventory[product][0] - fulfillment_cart[product][0]

    return store_inventory

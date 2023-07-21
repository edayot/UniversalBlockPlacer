



from items_blocks import items, blocks
from beet import Context









def search_item(minecraft_id):
    for item in items:
        if item.minecraft_id==minecraft_id:
            return item
    return None




import json
import requests
from items_blocks import items, blocks
from classes import Item, Block, Blockstate, Block_with_blockstate


encoded_blockstates=[
    # for internal use
    "part",
    "half",
    "waterlogged",

    # for technical use (maybe not implemented)
    "delay",
    "mode",
    "inverted",
    # for technical use multiple block at once
    "flower_amount",
    "candles",
    "pickles",
    "layers",
    "eggs",

    # facing & other
    "face",
    "facing",
    "hinge",
    "rotation",
    "axis",
    "type",
    "attachment",
    "orientation",
    "hanging",        
]

def generate_items_id(items : list[Item]):
    for item in items:
        item.id=item.block_list[0].id

            






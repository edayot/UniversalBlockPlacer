
from .classes import Item, Block, Blockstate
import requests, json
from itertools import product



MC_VERSION="1.20.1"
itemlist_url="https://github.com/misode/mcmeta/blob/{mc_version}-registries/item/data.json?raw=true".format(mc_version=MC_VERSION)
blocklist_url="https://github.com/misode/mcmeta/blob/{mc_version}-registries/block/data.json?raw=true".format(mc_version=MC_VERSION)
blockstates_url="https://github.com/misode/mcmeta/blob/{mc_version}-summary/blocks/data.json?raw=true".format(mc_version=MC_VERSION)

blockstates=requests.get(blockstates_url).json()
itemlist=requests.get(itemlist_url).json()
blocklist=requests.get(blocklist_url).json()

items=[]
for item in itemlist:    
    items.append(Item(item))

blocks=[]
for block in blocklist:
    blocks.append(Block(block))



                
def generate_combinaisons(block: Block):
    L=[]
    for blockstate in block.blockstates:
        L.append(blockstate.possible_values)
    return list(product(*L))


for b in blocks:
    if b.minecraft_id in blockstates:
        for blockstate in blockstates[b.minecraft_id][1]:
            b.add_blockstate(
                Blockstate(
                    id=blockstate,
                    possible_values=blockstates[b.minecraft_id][0][blockstate],
                    default_value=blockstates[b.minecraft_id][1][blockstate]
                )
            )

for b in blocks:
    if b.has_blockstates():
        for combinaison in generate_combinaisons(b):
            b.add_blockstate_combinaison(
                {
                    b.blockstates[i].id:combinaison[i] for i in range(len(combinaison))
                }
            )
    else:
        b.add_blockstate_combinaison({})


different_block_ids=[]
for b in blocks:
    found=False
    for i in items:
        if i.minecraft_id==b.minecraft_id:
            i.add_block(b)
            found=True
    if not found:
        different_block_ids.append(b)
        

wall_blocks_suffix=[
    "_sign",
    "_banner",
    "_fan",
    "_head",
    "_torch",
    "_skull"
]

unwanted_blocks=[
    "bubble_column",
    "cave_air",
    "end_gateway",
    "end_portal",
    "fire",
    "soul_fire",
    "frosted_ice",
    "moving_piston",
    "nether_portal",
    "piston_head",
    "tall_seagrass",
    "void_air",
    
]

unwanted_endswith=["_stem","_cauldron","_cake","_plant"]
unwanted_startwith=["potted_"]

def special_case(b,item_id):
    for i in items:
        if i.minecraft_id==item_id:
            i.add_block(b)


for b in different_block_ids:
    if any(b.minecraft_id.endswith(suffix) for suffix in wall_blocks_suffix) and b.minecraft_id.replace("wall_","") in itemlist:
        for i in items:
            if i.minecraft_id==b.minecraft_id.replace("wall_",""):
                i.add_block(b)
    elif b.minecraft_id.endswith("s") and b.minecraft_id[0:-1] in itemlist:
        for i in items:
            if i.minecraft_id==b.minecraft_id[0:-1]:
                i.add_block(b)
    elif b.minecraft_id.endswith("es") and b.minecraft_id[0:-2] in itemlist:
        for i in items:
            if i.minecraft_id==b.minecraft_id[0:-2]:
                i.add_block(b)
    elif b.minecraft_id.endswith("_crop") and b.minecraft_id.replace("_crop","_pod") in itemlist:
        for i in items:
            if i.minecraft_id==b.minecraft_id.replace("_crop","_pod"):
                i.add_block(b)
    elif b.minecraft_id.endswith("_crop") and b.minecraft_id.replace("_crop","_seeds") in itemlist:
        for i in items:
            if i.minecraft_id==b.minecraft_id.replace("_crop","_seeds"):
                i.add_block(b)

    # Special cases
    elif b.minecraft_id=="redstone_wire":
        special_case(b,"redstone")
    elif b.minecraft_id=="bamboo_sapling":
        special_case(b,"bamboo")
    elif b.minecraft_id=="lava":
        special_case(b,"lava_bucket")
    elif b.minecraft_id=="water":
        special_case(b,"water_bucket")
    elif b.minecraft_id=="cave_vines":
        special_case(b,"cave_vines_plant")
    elif b.minecraft_id=="cocoa":
        special_case(b,"cocoa_beans")
    elif b.minecraft_id=="powder_snow":
        special_case(b,"powder_snow_bucket")
    elif b.minecraft_id=="tripwire":
        special_case(b,"string")
    elif b.minecraft_id=="sweet_berry_bush":
        special_case(b,"sweet_berries")
    else:
        if b.minecraft_id in unwanted_blocks or any([b.minecraft_id.endswith(ending) for ending in unwanted_endswith]) or any([b.minecraft_id.startswith(start) for start in unwanted_startwith]):
            pass
        else:
            print(b.minecraft_id)



# delete all items without blocks
items=[i for i in items if len(i.block_list)>0]
for i,item in enumerate(items):
    item.id=i


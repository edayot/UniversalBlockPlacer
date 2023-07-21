


import json
import requests
from dataclasses import dataclass,field

MC_VERSION="1.20.1"
itemlist_url="https://github.com/misode/mcmeta/blob/{mc_version}-registries/item/data.json?raw=true".format(mc_version=MC_VERSION)
blocklist_url="https://github.com/misode/mcmeta/blob/{mc_version}-registries/block/data.json?raw=true".format(mc_version=MC_VERSION)
blockstates_url="https://github.com/misode/mcmeta/blob/{mc_version}-summary/blocks/data.json?raw=true".format(mc_version=MC_VERSION)

blockstates=requests.get(blockstates_url).json()
itemlist=requests.get(itemlist_url).json()
blocklist=requests.get(blocklist_url).json()


allowed_blockstates=[
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

@dataclass
class Blockstate:
    id: str
    possible_values: list[str] = field(default_factory=list)
    default_value: str = field(default_factory=str)



@dataclass
class Block:
    minecraft_id: str
    blockstates: list[Blockstate] = field(default_factory=list)

    def add_blockstate(self,blockstate):
        if isinstance(blockstate,Blockstate):
            self.blockstates.append(blockstate)

@dataclass
class Item:
    minecraft_id: str
    # default value = []
    block_list: list[Block]=field(default_factory=list)

    def add_block(self,block):
        if isinstance(block,Block):
            self.block_list.append(block)




items=[]
for item in itemlist:    
    items.append(Item(item))

blocks=[]
for block in blocklist:
    blocks.append(Block(block))

for b in blocks:
    if block in blockstates:
        for blockstate in blockstates[block][1]:
            b.add_blockstate(
                Blockstate(
                    id=blockstate,
                    possible_values=blockstates[block][0][blockstate],
                    default_value=blockstates[block][1][blockstate]
                )
            )


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
        for i in items:
            if i.minecraft_id=="redstone":
                i.add_block(b)
    elif b.minecraft_id=="bamboo_sapling":
        for i in items:
            if i.minecraft_id=="bamboo":
                i.add_block(b)
    elif b.minecraft_id=="lava":
        for i in items:
            if i.minecraft_id=="lava_bucket":
                i.add_block(b)
    elif b.minecraft_id=="water":
        for i in items:
            if i.minecraft_id=="water_bucket":
                i.add_block(b)
    elif b.minecraft_id=="cave_vines":
        for i in items:
            if i.minecraft_id=="glow_berries":
                i.add_block(b)
    elif b.minecraft_id=="cocoa":
        for i in items:
            if i.minecraft_id=="cocoa_beans":
                i.add_block(b)
    elif b.minecraft_id=="powder_snow":
        for i in items:
            if i.minecraft_id=="powder_snow_bucket":
                i.add_block(b)
    elif b.minecraft_id=="tripwire":
        for i in items:
            if i.minecraft_id=="string":
                i.add_block(b)
    elif b.minecraft_id=="sweet_berry_bush":
        for i in items:
            if i.minecraft_id=="sweet_berries":
                i.add_block(b)
    else:
        if b.minecraft_id in unwanted_blocks or any([b.minecraft_id.endswith(ending) for ending in unwanted_endswith]) or any([b.minecraft_id.startswith(start) for start in unwanted_startwith]):
            pass
        else:
            print(b.minecraft_id)





















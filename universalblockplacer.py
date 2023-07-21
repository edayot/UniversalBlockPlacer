


import json
import requests

MC_VERSION="1.20.1"

itemlist_url="https://github.com/misode/mcmeta/blob/{mc_version}-registries/item/data.json?raw=true".format(mc_version=MC_VERSION)
blocklist_url="https://github.com/misode/mcmeta/blob/{mc_version}-registries/block/data.json?raw=true".format(mc_version=MC_VERSION)
blockstates_url="https://github.com/misode/mcmeta/blob/{mc_version}-summary/blocks/data.json?raw=true".format(mc_version=MC_VERSION)

blockstates=requests.get(blockstates_url).json()
itemlist=requests.get(itemlist_url).json()
blocklist=requests.get(blocklist_url).json()

item_to_blocks={}

different_block_ids=[]



for block in blocklist:
    if block in itemlist:
        if block in blockstates:
            item_to_blocks[block]={
                "blocks": {
                    block: blockstates[block]
                }
            }
        else:
            item_to_blocks[block]={
                "blocks": {
                    block: {}
                }
            }
    else:
        different_block_ids.append(block)


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

for block in different_block_ids:
    if (block.endswith("_sign") or block.endswith("_banner") or block.endswith("_fan") or block.endswith("_head") or block.endswith("_torch") or block.endswith("_skull")) and block.replace("wall_","") in itemlist:
        item_to_blocks[block.replace("wall_","")]["blocks"][block]=blockstates[block]
    elif block.endswith("s") and block[0:-1] in itemlist:
        if block[0:-1] in item_to_blocks:
            item_to_blocks[block[0:-1]]["blocks"][block]=blockstates[block]
        else:
            item_to_blocks[block[0:-1]]={
                "blocks": {
                    block: blockstates[block]
                }
            }
    elif block.endswith("es") and block[0:-2] in itemlist:
        if block[0:-2] in item_to_blocks:
            item_to_blocks[block[0:-2]]["blocks"][block]=blockstates[block]
        else:
            item_to_blocks[block[0:-2]]={
                "blocks": {
                    block: blockstates[block]
                }
            }
    elif block.endswith("_crop") and block.replace("_crop","_pod") in itemlist:
        if block.replace("_crop","_pod") in item_to_blocks:
            item_to_blocks[block.replace("_crop","_pod")]["blocks"][block]=blockstates[block]
        else:
            item_to_blocks[block.replace("_crop","_pod")]={
                "blocks": {
                    block: blockstates[block]
                }
            }
    elif block.endswith("_crop") and block.replace("_crop","_seeds") in itemlist:
        if block.replace("_crop","_seeds") in item_to_blocks:
            item_to_blocks[block.replace("_crop","_seeds")]["blocks"][block]=blockstates[block]
        else:
            item_to_blocks[block.replace("_crop","_seeds")]={
                "blocks": {
                    block: blockstates[block]
                }
            }


    # Special cases
    elif block=="redstone_wire":
        item_to_blocks["redstone"]={
            "blocks": {
                block: blockstates[block]
            }
        }
    elif block=="bamboo_sapling":
        item_to_blocks["bamboo"]={
            "blocks": {
                block: blockstates["bamboo"]
            }
        }
    elif block=="lava":
        item_to_blocks["lava_bucket"]={
            "blocks": {
                block: blockstates[block]
            }
        }
    elif block=="water":
        item_to_blocks["water_bucket"]={
            "blocks": {
                block: blockstates[block]
            }
        }
    elif block=="cave_vines":
        item_to_blocks["glow_berries"]={
            "blocks": {
                block: blockstates[block]
            }
        }
    elif block=="cocoa":
        item_to_blocks["cocoa_beans"]={
            "blocks": {
                block: blockstates[block]
            }
        }
    elif block=="powder_snow":
        item_to_blocks["powder_snow_bucket"]={
            "blocks": {
                block: {}
            }
        }
    elif block=="tripwire":
        item_to_blocks["string"]={
            "blocks": {
                block: blockstates[block]
            }
        }
    elif block=="sweet_berry_bush":
        item_to_blocks["sweet_berries"]={
            "blocks": {
                block: blockstates[block]
            }
        }
        
   


    elif block in unwanted_blocks or any([block.endswith(ending) for ending in unwanted_endswith]) or any([block.startswith(start) for start in unwanted_startwith]):
        pass
    else:
        print(block)



    







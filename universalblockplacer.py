


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


unwanted_blocks=[]

unwanted_endswith=["_stem","_cauldron","_cake"]
unwanted_startwith=["potted_"]

for block in different_block_ids:
    if (block.endswith("_sign") or block.endswith("_banner") or block.endswith("_fan") or block.endswith("_head") or block.endswith("_torch")) and block.replace("wall_","") in itemlist:
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
    elif block=="redstone_wire":
        item_to_blocks["redstone"]={
            "blocks": {
                block: blockstates[block]
            }
        }
    elif block in unwanted_blocks or any([block.endswith(ending) for ending in unwanted_endswith]) or any([block.startswith(start) for start in unwanted_startwith]):
        pass
    else:
        print(block)



    







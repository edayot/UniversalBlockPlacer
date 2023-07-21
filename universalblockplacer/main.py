



from .items_blocks import items, blocks
from .classes import Block
from beet import Context, DataPack, ResourcePack, ItemTag, BlockTag, Function, FunctionTag, Predicate, TreeNode



def generate_item_to_id(ctx: Context):
    #print(items[0])
    # get the len in bit on the max id
    max_id = max([i.id for i in items])
    len_id = len(bin(max_id)[2:])

    ctx.data.functions[f"universalblockplacer:v{ctx.project_version}/item_to_id"] = Function()
    ctx.data.functions[f"universalblockplacer:v{ctx.project_version}/item_to_id"].append(
        f"scoreboard players reset @s universalblockplacer.bit_id"
    )
    
    # generate the item tags
    for i in range(len_id):
        items_in_tag = {"values": []}
        for item in items:
            if item.id & (1 << i): # if the bit is 1
                items_in_tag["values"].append(item.minecraft_id)
        ctx.data.item_tags[f"universalblockplacer:v{ctx.project_version}/bit_id/{i}"]=ItemTag(items_in_tag)
        ctx.data.predicates[f"universalblockplacer:v{ctx.project_version}/bit_id/{i}"]=Predicate({
                "condition": "minecraft:entity_properties",
                "entity": "this",
                "predicate": {
                    "equipment": {
                        "mainhand": {
                            "tag": f"universalblockplacer:v{ctx.project_version}/bit_id/{i}"
                        }
                    }
                }
            }
        )
        ctx.data.functions[f"universalblockplacer:v{ctx.project_version}/item_to_id"].append(
            f"execute if predicate universalblockplacer:v{ctx.project_version}/bit_id/{i} run scoreboard players add @s universalblockplacer.bit_id {2**i}"
        )
    ctx.data.predicates[f"universalblockplacer:v{ctx.project_version}/bit_id/bonus"]=Predicate({
                "condition": "minecraft:entity_properties",
                "entity": "this",
                "predicate": {
                    "equipment": {
                        "mainhand": {
                            "items": [items[0].minecraft_id]
                        }
                    }
                }
            }
        )
    ctx.data.functions[f"universalblockplacer:v{ctx.project_version}/item_to_id"].append(
        f"execute if predicate universalblockplacer:v{ctx.project_version}/bit_id/bonus run scoreboard players add @s universalblockplacer.bit_id 0"
    )



def generate_block_from_ids(ctx: Context):
    # list of items[i].minecraft_id
    items_ids = [item.minecraft_id for item in items]
    for node, function in ctx.generate.function_tree(f"v{ctx.project_version}/tree/items/block_from_ids",items_ids):
        handle_content(ctx, node, function, 2)
    del ctx.data.functions[f"universalblockplacer:generated_0"]
    # create a tree for the blocks
    i=1
    for block in blocks:
        for node, function in ctx.generate.function_tree(f"v{ctx.project_version}/tree/blocks/{block.minecraft_id}",block.blockstates_combinaisons):
            handle_content2(ctx, node, function, 2, block)
        del ctx.data.functions[f"universalblockplacer:generated_{i}"]
        i+=1

    ctx.data.functions[f"universalblockplacer:v{ctx.project_version}/block_from_ids"] = Function()
    ctx.data.functions[f"universalblockplacer:v{ctx.project_version}/block_from_ids"].append(
        f"function universalblockplacer:v{ctx.project_version}/tree/items/block_from_ids"
    )

def generate_item_to_block(ctx: Context):
    ctx.data.functions[f"universalblockplacer:v{ctx.project_version}/item_to_block"] = Function()
    ctx.data.functions[f"universalblockplacer:v{ctx.project_version}/item_to_block"].append(
        f"function universalblockplacer:v{ctx.project_version}/item_to_id"
    )
    ctx.data.functions[f"universalblockplacer:v{ctx.project_version}/item_to_block"].append(
        f"function universalblockplacer:v{ctx.project_version}/block_from_ids"
    )




            
        
        
def handle_content2(ctx: Context, node: TreeNode[str], function: Function, n: int, block: Block):
    if node.root:
        ctx.generate(Function([f"function {node.parent}"]))
    if node.partition(n):
        function.lines.append(
            f"execute if score @s universalblockplacer.block_choice matches {node.range} run function {node.children}"
        )
    else:
        #print(node)
        a=','.join([f'{key}={value}' for key,value in node.value.items()])
        function.lines.append(
            f"execute if score @s universalblockplacer.block_choice matches {node.range} run setblock ^ ^ ^2 {block.minecraft_id}[{a}]"
        )
        if node.range=="0":
            a=','.join([f'{blockstate.id}={blockstate.default_value}' for blockstate in block.blockstates])
            function.lines.append(
                f"execute if score @s universalblockplacer.block_choice matches -1 run setblock ^ ^ ^2 {block.minecraft_id}[{a}]"
            
            )

    
    

def handle_content(ctx: Context, node: TreeNode[str], function: Function, n: int):
    if node.root:
        ctx.generate(Function([f"function {node.parent}"]))
    if node.partition(n):
        function.lines.append(
            f"execute if score @s universalblockplacer.bit_id matches {node.range} run function {node.children}"
        )
    else:
        function.lines.append(
            f"execute if score @s universalblockplacer.bit_id matches {node.range} run function universalblockplacer:v{ctx.project_version}/tree/blocks/{node.value}"
        )

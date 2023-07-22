
data modify entity @s HandItems[0] set value {id:"minecraft:stone",Count:1b}
data modify entity @s HandItems[0].id set from storage universalblockplacer:main temp.id_item

function universalblockplacer:impl/item_to_block

execute if score @s universalblockplacer.item_bit_id matches 0.. run item modify block ~ ~ ~1 container.0 universalblockplacer:impl/remove_1

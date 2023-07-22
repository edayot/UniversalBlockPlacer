data modify storage universalblockplacer:main temp.id_item set value ""
execute store success score #success universalblockplacer.math run data modify storage universalblockplacer:main temp.id_item set from block ~ ~ ~ Items[{Slot:0b}].id

execute if score #success universalblockplacer.math matches 1 if entity @s[tag=universalblockplacer.blockplacer.north] positioned ~ ~ ~-1 as 93682a08-d099-4e8f-a4a6-1e33a3692301 run function universalblockplacer:impl/blockplacer/place_block/north




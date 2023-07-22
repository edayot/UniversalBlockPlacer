scoreboard objectives add universalblockplacer.math dummy
scoreboard objectives add universalblockplacer.item_bit_id dummy
scoreboard objectives add universalblockplacer.block_bit_id dummy
scoreboard objectives add universalblockplacer.block_choice dummy

tag AirDox_ add convention.debug
execute as @a[tag=convention.debug] run function universalblockplacer:impl/print_version

# ItemsNBT
#define storage universalblockplacer:main

# Format :
#data modify storage simpledrawer:main ItemsNBT.drawer set value {id:"minecraft:furnace",Count:1b						,tag:{ctc:{id:"drawer",from:"airdox_:simpledrawer",traits:{"block":1b}}										,BlockEntityTag:{Items:[{id:"minecraft:stone",Count:1b,Slot:0b,tag:{simpledrawer:{type:"wood",hopper:0b},smithed:{block:{id:"simpledrawer:drawer"}}}}]}							,display:{Name:'{"translate":"simpledrawer.drawer.empty","color":"white","italic":false}'}}}

data modify storage universalblockplacer:main ItemsNBT.blockplacer set value {id:"minecraft:barrel",Count:1b,
    tag:{
        ctc:{id:"blockplacer",from:"airdox_:universalblockplacer",traits:{"block":1b}},
        BlockEntityTag:{Items:[{id:"minecraft:stone",Count:1b,Slot:0b,tag:{smithed:{block:{id:"universalblockplacer:blockplacer"}}}}]},
        display:{Name:'{"translate":"universalblockplacer.blockplacer","color":"white","italic":false}'}}}


schedule function universalblockplacer:impl/20tick 20t replace
schedule function universalblockplacer:impl/tick 1t replace

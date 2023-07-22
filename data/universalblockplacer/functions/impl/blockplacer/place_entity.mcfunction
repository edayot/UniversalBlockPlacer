


tag @s add smithed.block

tag @s add universalblockplacer.block
tag @s add universalblockplacer.blockplacer

tag @s add itemio.container
tag @s add itemio.container.hopper

data modify entity @s item.tag.itemio.ioconfig set value [{Slot:0b,mode:"input",allowed_side:{north:1b,south:1b,east:1b,west:1b,top:1b,bottom:1b}}]


execute if block ~ ~ ~ barrel[facing=north] run tag @s add universalblockplacer.blockplacer.north
execute if block ~ ~ ~ barrel[facing=south] run tag @s add universalblockplacer.blockplacer.south
execute if block ~ ~ ~ barrel[facing=east] run tag @s add universalblockplacer.blockplacer.east
execute if block ~ ~ ~ barrel[facing=west] run tag @s add universalblockplacer.blockplacer.west
execute if block ~ ~ ~ barrel[facing=up] run tag @s add universalblockplacer.blockplacer.up
execute if block ~ ~ ~ barrel[facing=down] run tag @s add universalblockplacer.blockplacer.down


function #itemio:calls/container/init






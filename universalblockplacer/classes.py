from dataclasses import dataclass,field

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
    def has_blockstates(self):
        return len(self.blockstates)>0

@dataclass
class Block_with_blockstate:
    block: Block
    id: int = field(default=-1)
    values: dict[str,str] = field(default_factory=dict)
    def __post_init__(self):
        if self.values=={}:
            # Initialize values
            self.values={self.block.blockstates[i].id:self.block.blockstates[i].default_value for i in range(len(self.block.blockstates))}


@dataclass
class Item:
    minecraft_id: str
    id: int = field(default=-1)
    # default value = []
    block_list: list[Block_with_blockstate]=field(default_factory=list)

    def add_block(self,block):
        if isinstance(block,Block_with_blockstate):
            self.block_list.append(block)
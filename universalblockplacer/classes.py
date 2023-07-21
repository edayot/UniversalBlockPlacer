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
    blockstates_combinaisons: list[dict] = field(default_factory=list)
    

    def add_blockstate(self,blockstate):
        if isinstance(blockstate,Blockstate):
            self.blockstates.append(blockstate)
    def has_blockstates(self):
        return len(self.blockstates)>0
    def add_blockstate_combinaison(self,combinaison):
        if isinstance(combinaison,dict):
            self.blockstates_combinaisons.append(combinaison)

@dataclass
class Item:
    minecraft_id: str
    id: int = field(default=-1)
    # default value = []
    block_list: list[Block]=field(default_factory=list)

    def add_block(self,block):
        if isinstance(block,Block):
            self.block_list.append(block)
from __future__ import annotations
import abc
import sys
from enum import Enum

NAME_MAP = {
    ''
}

class CookMethod(Enum):
    Roast = 0
    Oil = 1
    BBQ = 2
    
class Gender(Enum):
    Female = 0
    Male = 1
    
class ItemType(Enum):
    Chicken = 0
    Duck = 1
    Pork = 2
    
class MeatPart(Enum):
    Whole = 0
    Half = 1
    Head = 2
    Neck = 3
    Shoulder = 4
    Arm = 5
    Breast = 6
    Back = 7
    Belly = 8
    Ass = 9
    Thigh = 10

class IItem(abc.ABC):
    def __init__(self, item_type:ItemType, meat_part:MeatPart, cook_method:CookMethod, gender:Gender=Gender.Female, weight_tkg:float=None, price_tkg:float=None, price_item:float=None) -> None:
        super().__init__()
        self.__item_type = item_type
        self.__meat_part = meat_part
        self.__cook_method = cook_method
        self.__gender = gender
        self.__weight_tkg = weight_tkg
        self.__price_tkg = price_tkg
        self.__price_item = price_item
        
        self.__contains:list = []
        
    def __repr__(self) -> str:
        item_name = f'{self.cook_method.value}{self.item_type.value}{self.meat_part.value}'
        item_name_map = {'224':'叉燒','028':'燒肉'}
        cook_map = {0:'烤',1:'油',2:'蜜汁'}
        item_map = {0:'雞',1:'鴨',2:'豬'}
        part_map = {0:'全隻',1:'半隻',2:'頭',3:'脖子',4:'肩',5:'翅',6:'胸',7:'背',8:'五花',9:'屁股',10:'腿'}
        gender_map = {0:'母',1:'公'}
        if item_name in item_name_map:
            item_name = item_name_map[item_name]
        else:
            item_name = cook_map[self.cook_method.value] + item_map[self.item_type.value] + part_map[self.meat_part.value]
        if self.item_type.value != 2:
            item_name += gender_map[self.gender.value]
        return item_name

    @property
    def item_type(self):
        return self.__item_type
    
    @item_type.setter
    def item_type(self, value:ItemType):
        self.__item_type = value

    @property
    def meat_part(self):
        return self.__meat_part
    
    @meat_part.setter
    def meat_part(self, value:MeatPart):
        self.__meat_part = value

    @property
    def cook_method(self):
        return self.__cook_method
    
    @cook_method.setter
    def cook_method(self, value:CookMethod):
        self.__cook_method = bool(value)
        
    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self, value:Gender):
        self.__gender = value
        
    @property
    def contains(self):
        return self.__contains
    
    @contains.setter
    def contains(self, value:list):
        self.__contains = value
        
    @property
    def weight_tkg(self):
        return self.__weight_tkg
    
    @weight_tkg.setter
    def weight_tkg(self, value:float):
        self.__weight_tkg = max(float(value), 0)
    
    @property
    def price_tkg(self):
        return self.__price_tkg
    
    @price_tkg.setter
    def price_tkg(self, value:float):
        self.__price_tkg = max(float(value), 0)
        
    @property
    def price_item(self):
        return self.__price_item
    
    @price_item.setter
    def price_item(self, value:float):
        self.__price_item = max(float(value), 0)

class Item(IItem):
    def __init__(self, item_type: ItemType, meat_part: MeatPart, cook_method: CookMethod, gender: Gender = Gender.Female, weight_tkg: float = None, price_tkg: float = None, price_item: float = None) -> None:
        super().__init__(item_type, meat_part, cook_method, gender, weight_tkg, price_tkg, price_item)

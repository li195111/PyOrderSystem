from __future__ import annotations
from typing import List
from items import IProduct, WeightingProduct
from datetime import datetime

class IOrder(IProduct):
    '''訂單'''
    def __init__(self, order_datetime:datetime, items:list, phone:str,
                 name: str = 'Some People', price_item: float = 0, price: float = 0, number: float = 1) -> None:
        super().__init__(name, price_item, price, number)
        self.__order_datetime = order_datetime
        self.__items:List[WeightingProduct] = items
        self.__phone = phone
        self.calc()
        
    @property
    def order_datetime(self):
        return self.__order_datetime
    
    @order_datetime.setter
    def order_datetime(self, value:datetime):
        self.__order_datetime = value
        
    @property
    def items(self):
        return self.__items
        
    @items.setter
    def items(self, value:list):
        self.__items = list(value)
        self.calc()
        
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value:str):
        self.__phone = str(value)
    
    @property
    def details(self):
        return f'{self.order_datetime:%Y-%m-%d %H:%M} {self.name} {self.phone} {self.price} {self.items}'
        
    def calc(self):
        for item in self.items:
            self.price += item.price

class Order(IOrder):
    def __init__(self, order_datetime: datetime, items: list, phone: str, name: str = 'Some People', price_item: float = 0, price: float = 0, number: float = 1) -> None:
        super().__init__(order_datetime, items, phone, name, price_item, price, number)
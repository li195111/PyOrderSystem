from __future__ import annotations
import abc
from datetime import datetime

class IOrder(abc.ABC):
    '''訂單'''
    def __init__(self, order_datetime:datetime, items:list, name:str, phone:str) -> None:
        super().__init__()
        self.__order_datetime = order_datetime
        self.__items = items
        self.__name = name
        self.__phone = phone
        
    def __repr__(self) -> str:
        return f'{self.name} {self.order_datetime} {self.items} {self.phone}'
        
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
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value:str):
        self.__name = str(value)
        
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value:str):
        self.__phone = str(value)

class Order(IOrder):
    def __init__(self, order_datetime: datetime, items: list, name: str, phone: str) -> None:
        super().__init__(order_datetime, items, name, phone)
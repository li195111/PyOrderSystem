from __future__ import annotations
import abc

class IProduct(abc.ABC):
    def __init__(self, name:str='Some Product', price_item:float=0, price:float=0, number:float=1) -> None:
        super().__init__()
        self.__name = name
        self.__price_item = price_item
        self.__price = price
        self.__number = number
    
    def __repr__(self) -> str:
        return self.name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = str(value)
        
    @property
    def price_item(self):
        return self.__price_item
    
    @price_item.setter
    def price_item(self, value):
        self.__price_item = max(float(value),0)
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price = max(float(value),0)
        
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        self.__number = max(float(value),0)
        
    @abc.abstractmethod
    def details(self):
        '''Implements Method'''
        return f'{self.name} x {self.number:.1f} = {self.price}'
        
    @abc.abstractmethod
    def calc(self):
        '''Implements Method'''
        
class WeightingProduct(IProduct):
    def __init__(self, weight_tkg:float=0, price_tkg:float=0, weight_tael:float=0, price_tael:float=0,
                 name: str = 'Some Product', price_item: float = 0, price: float = 0, number: float = 1) -> None:
        super().__init__(name, price_item, price, number)
        if not price_tkg == 0:
            price_tael = price_tkg / 16
        if not price_tael == 0:
            price_tkg = price_tael * 16
        if not price == 0:
            price = float(price)
            
        self.__weight_tkg = weight_tkg
        self.__price_tkg = price_tkg
        self.__weight_tael = weight_tael
        self.__price_tael = price_tael
        self.calc()
        
    @property
    def weight_tkg(self):
        return self.__weight_tkg
    
    @weight_tkg.setter
    def weight_tkg(self, value:float):
        self.__weight_tkg = max(float(value), 0)
        self.__weight_tael = self.__weight_tkg * 16
        self.calc()
    
    @property
    def price_tkg(self):
        return self.__price_tkg
    
    @price_tkg.setter
    def price_tkg(self, value:float):
        self.__price_tkg = max(float(value), 0)
        self.__price_tael = self.__price_tkg / 16

    @property
    def weight_tael(self):
        return self.__weight_tael
    
    @weight_tael.setter
    def weight_tael(self, value:float):
        self.__weight_tael = max(float(value), 0)
        self.__weight_tkg = self.__weight_tael / 16
        self.calc()
        
    @property
    def price_tael(self):
        return self.__price_tael
    
    @price_tael.setter
    def price_tael(self, value:float):
        self.__price_tael = max(float(value), 0)
        self.__price_tkg = self.__price_tael * 16
        
    @property
    def details(self):
        product_name = f'{self.name}'
        if not self.price_tael == 0:
            product_name += f' {self.price_tael}/兩 x {self.weight_tael}兩'
        product_name += f' x {self.number:.1f} = {self.price}'
        return product_name
    
    @property
    def attributes(self):
        return {'weight_tkg':self.weight_tkg, 'price_tkg':self.price_tkg, 'weight_tael':self.weight_tael, 'price_tael':self.price_tael, 'name':self.name, 'price_item':self.price_item, 'price':self.price, 'number':self.number}

    def calc(self):
        if self.price_item == 0:
            self.price_item = self.price_tkg * self.weight_tkg
        self.price = self.price_item * self.number
        
class Item(WeightingProduct):
    def __init__(self, weight_tkg:float=0, price_tkg:float=0, weight_tael:float=0, price_tael:float=0,
                 name: str = 'Some Product', price_item: float = 0, price: float = 0, number: float = 1) -> None:
        super().__init__(weight_tkg, price_tkg, weight_tael, price_tael, name, price_item, price, number)
                
class Gender(WeightingProduct):
    def __init__(self, item:Item, gender:str='母') -> None:
        super().__init__(**item.attributes)
        self.__item = item
        self.gender = gender
        
    @property
    def name(self):
        return self.__item.name + f'({self.gender})'
        
class Cut(WeightingProduct):
    def __init__(self, item:Item, cut_part:str='全隻') -> None:
        super().__init__(**item.attributes)
        self.__item = item
        self.cut_part = cut_part
        
    @property
    def name(self):
        return self.__item.name + self.cut_part
    
class ForGod(WeightingProduct):
    def __init__(self, item:Item) -> None:
        super().__init__(**item.attributes)
        self.__item = item
        
    @property
    def name(self):
        return f'敬神{self.__item.name}'
    
if __name__ == "__main__":
    print (Cut(Gender(Item(name='烤鴨'),'母'),'半隻'))
    print (Cut(Gender(Item(name='敬神烤鴨'),'公'),'全隻'))
    print (Cut(Gender(Item(name='烤鴨'),'母'),'四分之一'))
from collections import Counter
from datetime import datetime
import configparser
import json
import enum

from items import Item, Cut, Gender, ForGod
from order import Order

if __name__ == "__main__":
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')
    categories = json.loads(cfg.get('Default','categories'))
    print (categories)
    category_map = {}
    for idx, cate in enumerate(categories):
        category_map[cate] = idx
    print (category_map)
    
    CATEGORIES = enum.Enum('Categories',category_map)
    print (CATEGORIES['敬神公鴨'])
        
    meanu = [Item(name='烤雞腿', price_item=70, number=2),
             Item(name='叉燒', price_tael=30),
             Item(name='肝腸', price_tael=30),
             Item(name='腊腸', price_tael=30),
             Item(name='燒肉', price_tael=30),
             
             Cut(Gender(Item(name='烤雞', price_tael=15),'母')),
             Cut(Gender(Item(name='烤雞', price_tael=15),'公')),
             Cut(Gender(Item(name='油雞', price_tael=15),'公'),'半隻'),
             Cut(Gender(Item(name='油雞', price_tael=15),'母'),),
             
             Cut(Gender(Item(name='烤鴨', price=680),'母')),
             ForGod(Cut(Gender(Item(name='烤鴨', price=720),'公'))),
             Cut(Gender(Item(name='烤鴨', price=350),'公'),'半隻'),
             
             Cut(Gender(Item(name='烤鴨', price_tael=18),'母')),             
             
             Cut(Gender(Item(name='烤鴨', price_tael=18),'母'),'四分之一'),
             Cut(Gender(Item(name='烤鴨', price_tael=18),'公'),'四分之一')
             ]
    
    print (Cut(Gender(Item(name='油雞', price_tael=15),'母'), '全隻'))
    # print (dict(Counter(meanu)))
    # meanu[1].weight_tael = 2
    
    # print (f'{meanu[0]} {meanu[0].price_item}/隻 x {meanu[0].number:.1f} = {meanu[0].price}')
    # print (f'{meanu[1]} {meanu[1].price_tael}/兩 x {meanu[1].weight_tael}兩 x {meanu[1].number:.1f} = {meanu[1].price_item}')
    # print (meanu[2].details)
    
    order1 = Order(name='李小姐', phone='0987654321', order_datetime=datetime(2022,1,31,10), items=meanu)
    
    print (order1.details)
    
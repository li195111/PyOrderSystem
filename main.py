from datetime import datetime
from items import Item, ItemType, MeatPart, CookMethod, Gender
from order import Order

if __name__ == "__main__":
    烤雞腿 = Item(ItemType.Chicken, MeatPart.Thigh, CookMethod.Roast)
    叉燒 = Item(ItemType.Pork, MeatPart.Shoulder, CookMethod.BBQ)
    燒肉 = Item(ItemType.Pork, MeatPart.Belly, CookMethod.Roast)
    烤鴨 = Item(ItemType.Duck, MeatPart.Breast, CookMethod.Roast)
    油雞 = Item(ItemType.Chicken, MeatPart.Breast, CookMethod.Oil)
    
    半隻油雞 = Item(ItemType.Chicken, MeatPart.Half, CookMethod.Oil)
    半隻烤鴨 = Item(ItemType.Duck, MeatPart.Half, CookMethod.Roast, Gender.Male)
    
    訂單1 = Order(datetime(2022,1,31,10), [烤雞腿, 半隻烤鴨, 叉燒], '李小姐', '0987654321')
    
    print (訂單1)
    
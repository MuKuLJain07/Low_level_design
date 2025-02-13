class items:
    def __init__(self, itemCode, itemName, itemPrice):
        self.__itemCode = itemCode
        self.__itemName = itemName
        self.__itemPrice = itemPrice

    def get_itemCode(self):
        return self.__itemCode
    
    def get_itemName(self):
        return self.__itemName
    
    def get_itemPrice(self):
        return self.__itemPrice
    
    def set_itemPrice(self, newPrice):
        if newPrice >= 0:
            self.__itemPrice = newPrice
        else:
            print("Invalid value is provided")


class twiggy:
    def __init__(self, itemsList, threshold):
        self.__itemsList = itemsList
        self.__threshold = threshold

    def get_menu(self):
        print("Item Code    Item Name       Item Price")
        for item in self.__itemsList:
            print(item.get_itemCode(),"    ",item.get_itemName(),"    ",item.get_itemPrice())
    
    def set_menu(self, newItemList):
        self.__itemsList = newItemList

    def set_threshold(self, newThreshold):
        if(newThreshold >= 0):
            self.__threshold = newThreshold
        else:
            print("Invalid threshold provided")

    def calculateBill(self, itemsOrdered):
        if(len(itemsOrdered) <= 0):                     # no item is ordered
            return 0
          
        self.totalBill = 0
        for item in itemsOrdered:
            flag = False
            for availableItem in self.__itemsList:
                if(availableItem.get_itemCode() == item):
                    self.totalBill += availableItem.get_itemPrice()
                    flag = True
                    break
            
            if(not flag):                    # if item ordered is not present in the menu
                return -1 

        if(self.totalBill >= self.__threshold):
            return self.totalBill + 50
        else:
            return self.totalBill


# creating items
item1 = items(101, "Pizza", 100)
item2 = items(102, "Pasta", 150)
item3 = items(103, "Burger", 50)
item4 = items(104, "Chowmein", 80)

# creating restaurants
restaurantA = twiggy([item1, item2, item3, item4], 300)

restaurantA.get_menu()

totalBill = restaurantA.calculateBill([101])
if(totalBill == -1):
    print("Invalid item code ordered")
else:
    print("Your total bill sums up to : ", totalBill)

"""

Write code for low level design of orders and inventory management system of a simple e-commerce platform.
You will need to have the capability of handling sellers, products and orders.

Inventory is number of items of a particular product in a seller's warehouse.

The way it works is, products numbered from 0 till productsCount-1 are sold on the website.
Sellers are also added along with the area pincodes that they are able to deliver goods in as well as the payment types which they support.
After that sellers add items they wish to sell.

Multiple sellers can sell the same item e.g the product-1 : bluetooth speaker boat stone 650 can be sold by multiple sellers throughout the country.

Multiple sellers can deliver goods to the same pincode as well.

For simplicity lets assume price of a specific product is same whether it is sold by seller-1 or seller-2 or any seller.

For Python solution, your code will be tested in a Single-Threaded environment.

Your solution should implement below methods :

Method : void init(Helper04 helper, int productsCount)
- use helper for printing logs else logs will not be visible.
- Use this method for initialize your global variables and all.
- productsCount is total number of products being sold on website.


Method : void createSeller(String sellerId, List[String] serviceablePincodes, List[String] paymentModes)
- Creates a new seller. Each seller sells many products and multiple sellers can sell the product with same productId
- sellerId will always be a non null, non blank unique string
- serviceablePincodes is list of pincodes where seller can deliver products
- paymentModes will be always one of "cash", "upi", "netbanking", "debit card" and "credit card"

Method : void addInventory(int productId, String sellerId, int delta)
- seller adds multiple items of a product for selling. e.g 50 grey pure cotton shirts.
- delta: number of items seller is adding e.g. 50 . It will always be a positive integer.
- productId and sellerId will always be valid.

Method : int getInventory(int productId, String sellerId)
- returns the number of items in warehouse for a product sold by a given seller,
- if the product or seller doesn't exist then returns 0

Method : createOrder(String orderId, String destinationPincode, String sellerId, int productId, int productCount, String paymentMode)
- creates order with orderId and reduces product inventory from seller by productCount
- buyer will choose both product and seller who will deliver the product and create an order.
- For simplicity lets assume that at this time only one product (1 or more counts) is purchased in a single order.
- orderId , sellerId and productId will always be valid.
- productCount is number of items customer is ordering, it will always be a positive integer
- paymentMode will always be one of "cash", "upi", "netbanking", "debit card" and "credit card"
- returns (in that order) : "order placed" or "pincode unserviceable" or "payment mode not supported" or "insufficient product inventory"

Example : Read the below method calls to get a better understanding of how this works.

init(helper, 10) : helper is initialized.
createSeller(seller-0, [110001, 560092, 452001, 700001], [netbanking, cash, upi])
createSeller(seller-1, [400050, 110001, 600032, 560092], [netbanking, cash, upi])
addInventory(0, seller-1, 52) returned "inventory added"
addInventory(0, seller-0, 32) returned "inventory added"
createOrder(order-1, 400050, seller-1, 0, 5, upi) returned "order placed"
getInventory(0, seller-1) returned 47
createOrder(order-2, 560092, seller-0, 0, 1, upi) returned "order placed"
getInventory(0, seller-0) returned 31
"""

class seller:
    def __init__(self, sellerId, productList, serviceablePincodes, paymentModes):
        self.__sellerId = sellerId
        self.__productList = productList
        self.__serviceablePincodes = serviceablePincodes
        self.__paymentModes = paymentModes

    def get_sellerId(self):
        return self.__sellerId

    def get_productList(self):
        return self.__productList

    def get_serviceablePincodes(self):
        return self.__serviceablePincodes

    def get_paymentModes(self):
        return self.__paymentModes

    def set_productList(self, productId, quantity):
        for product in self.__productList:
            if product.get_productId() == productId:
                product.set_quantity(product.get_quantity() + quantity)
                return
        print("Product not found in seller's inventory")

    def set_serviceablePincodes(self, newServiceablePincodes):
        self.__serviceablePincodes = newServiceablePincodes

    def set_paymentModes(self, newPaymentModes):
        self.__paymentModes = newPaymentModes


class product:
    def __init__(self, productId, quantity):
        self.__productId = productId
        self.__quantity = quantity

    def get_productId(self):
        return self.__productId

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, newQuantity):
        if newQuantity >= 0:
            self.__quantity = newQuantity
        else:
            print("Invalid Quantity Provided")


class marketplace:
    def __init__(self, sellerIDs):
        self.__sellerIds = sellerIDs

    def addInventory(self, productId, sellerId, delta):
        for seller in self.__sellerIds:
            if seller.get_sellerId() == sellerId:
                seller.set_productList(productId, delta)
                print("Item added to the inventory")
                return
        print("Seller not found")

    def getInventory(self, sellerId, productId):
        for seller in self.__sellerIds:
            if seller.get_sellerId() == sellerId:
                for product in seller.get_productList():
                    if product.get_productId() == productId:
                        return product.get_quantity()
        return 0

    def createOrder(self, orderId, destinationPincode, sellerId, productId, productCount, paymentMode):
        for seller in self.__sellerIds:
            if seller.get_sellerId() == sellerId:
                if destinationPincode not in seller.get_serviceablePincodes():
                    print("pincode unserviceable")
                    return 0
                if paymentMode not in seller.get_paymentModes():
                    print("payment mode not supported")
                    return 0

                for product in seller.get_productList():
                    if product.get_productId() == productId:
                        if product.get_quantity() >= productCount:
                            product.set_quantity(product.get_quantity() - productCount)
                            print("order placed !!")
                            return 1
                        else:
                            print("insufficient product inventory")
                            return 0

                print("Product Not Found")
                return 0
        print("Seller not found")
        return 0


if __name__ == "__main__":
    # defining products
    product1 = product(0, 0)
    product2 = product(1, 0)
    product3 = product(2, 0)
    product4 = product(3, 0)
    product5 = product(4, 0)
    product6 = product(5, 0)

    # creating seller
    Seller_0 = seller("seller-0", [product1, product2, product3], {110001, 560092, 452001, 700001}, {"netbanking", "cash", "upi"})
    Seller_1 = seller("seller-1", [product1, product4, product5, product6], {400050, 110001, 600032, 560092}, {"netbanking", "cash", "upi"})

    marketA = marketplace([Seller_0, Seller_1])

    marketA.addInventory(0, "seller-1", 52)
    marketA.addInventory(0, "seller-0", 32)

    marketA.createOrder("order-1", 400050, "seller-1", 0, 5, "upi")
    print("Current available items: ", marketA.getInventory("seller-1", 0))



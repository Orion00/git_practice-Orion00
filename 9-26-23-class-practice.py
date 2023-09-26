class Product:
    def __init__(self, product_id, product_name, product_price) -> None:
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
    
    def discount_price(self,dis) -> float:
        if (dis < 0.0) | (dis > 100.0):
            return False
        return (100-dis)*self.product_price/100
        
    def change_price(self,price) -> None:
        self.product_price = price

apples: Product = Product(12,"Apples",1.50)

print(apples.discount_price(30))
#print(apples.product_price)
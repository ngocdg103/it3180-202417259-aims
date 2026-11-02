MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def total_cost_with_discount(self, total, percent):
        return total * (100 - percent) / 100

    def print_cart(self):

            # kiểm tra giỏ hàng trống:
            if not self.items:
                print("The cart is empty")
                return
    
            print("***********************CART***********************")
            print("Ordered Items:")
            for i, dvd in enumerate(self.items, start=1):
                print(f"{i}. {dvd.title}")
            print("***************************************************")
    

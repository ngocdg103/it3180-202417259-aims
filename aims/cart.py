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
        print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")
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
        
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
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
    def sort_by_title(self):
        self.items.sort(key=lambda dvd: dvd.title)
        print("Cart has been sorted by title")

    def sort_by_cost(self):
        # Sắp xếp theo giá giảm dần (từ cao xuống thấp)
        self.items.sort(key=lambda dvd: dvd.cost, reverse=True)
        print("Cart has been sorted by cost")

# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.product_of_numbers = [1]
        self.last_pos = -1
        

    def add(self, num: int) -> None:
        if num != 0: 
            self.product_of_numbers.append(self.product_of_numbers[-1] * num)    
        else:
            self.last_pos = len(self.product_of_numbers)
            self.product_of_numbers.append(self.product_of_numbers[-1])

    def getProduct(self, k: int) -> int:
        size = len(self.product_of_numbers)
        if size - k <= self.last_pos:
            return 0
        else:
            return self.product_of_numbers[-1] // self.product_of_numbers[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
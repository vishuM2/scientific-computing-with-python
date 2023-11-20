class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    return sum(item['amount'] for item in self.ledger)

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
      return True
    return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    title = f"{self.category:*^30}\n"
    items = "\n".join(f"{item['description'][:23]} {item['amount']:.2f}"
                      for item in self.ledger)
    total = sum(item['amount'] for item in self.ledger)
    output = f"{title}{items}\nTotal: {total:.2f}"
    return output


def create_spend_chart(categories):
  chart = "Percentage spent by category\n"
  spendings = [
      -sum(item['amount'] for item in category.ledger if item['amount'] < 0)
      for category in categories
  ]
  total_spending = sum(spendings)
  percentages = [
      int(spending / total_spending * 100) for spending in spendings
  ]

  for i in range(100, -1, -10):
    chart += f"{i:3}| {''.join('o' if percent >= i else ' ' for percent in percentages)}\n"

  chart += "    ----------\n"

  max_len = max(len(category.category) for category in categories)
  for i in range(max_len):
    chart += "     "
    chart += "  ".join(
        category.category[i] if i < len(category.category) else " "
        for category in categories)
    chart += "\n"

  return chart.rstrip()


# Example usage with user inputs:
food_category = Category(input("Enter the category for food: "))
clothing_category = Category(input("Enter the category for clothing: "))
auto_category = Category(input("Enter the category for auto: "))

food_category.deposit(float(input("Enter initial deposit for food: ")),
                      "initial deposit")
food_category.withdraw(float(input("Enter the amount for groceries: ")),
                       "groceries")
food_category.withdraw(
    float(input("Enter the amount for restaurant and more food: ")),
    "restaurant and more foo")
food_category.transfer(
    float(input("Enter the amount for transfer to clothing: ")),
    clothing_category)

clothing_category.deposit(float(input("Enter initial deposit for clothing: ")),
                          "initial deposit")
clothing_category.withdraw(
    float(input("Enter the amount for buying clothes: ")), "buying clothes")

auto_category.deposit(float(input("Enter initial deposit for auto: ")),
                      "initial deposit")
auto_category.withdraw(float(input("Enter the amount for car insurance: ")),
                       "car insurance")

print(food_category)
print(clothing_category)
print(auto_category)

categories_list = [food_category, clothing_category, auto_category]
chart = create_spend_chart(categories_list)
print(chart)
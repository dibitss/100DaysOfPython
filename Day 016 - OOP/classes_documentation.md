# MenuItem Class

## Attributes:

- ***name***

  _(str) The name of the drink._
  
  _e.g. “latte”_

- ***cost***
  
  _(float) The price of the drink._

  _e.g 1.5_

- ***ingredients***

  _(dictionary) The ingredients and amounts required to make the drink._

  _e.g. {“water”: 100, “coffee”: 16}_
___

# Menu Class

## Methods:

- ***get_items()***
  _Returns all the names of the available menu items as a concatenated string._

  _e.g. “latte/espresso/cappuccino”_

- ***find_drink(order_name)***

  _Parameter order_name: (str) The name of the drinks order._

  _Searches the menu for a particular drink by name. Returns a MenuItem object if it exists, otherwise returns None._
___
# CoffeeMaker Class

## Methods:

- ***report()***

  _Prints a report of all resources._

  _e.g._

  _Water: 300ml_

  _Milk: 200ml_

  _Coffee: 100g_

- ***is_resource_sufficient(drink)***

  _Parameter drink: (MenuItem) The MenuItem object to make._

  _Returns True when the drink order can be made, False if ingredients are insufficient._

  _e.g._

  _True_

- ***make_coffee(order)***

  _Parameter order: (MenuItem) The MenuItem object to make._

  _Deducts the required ingredients from the resources._
___
# MoneyMachine Class

## Methods:

- ***report()***

  _Prints the current profit_

  _e.g._

  _Money: $0_

- ***make_payment(cost)***

  _Parameter cost: (float) The cost of the drink._

  _Returns True when payment is accepted, or False if insufficient._

  _e.g. False_
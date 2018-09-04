class Menu(object):
	"""Implements the menu class"""
	def __init__(self):
		self.menu = {
			"burger": 500,
			"milkshake": 300,
			"friedchicken": 600
		}
	def get_item_price(self, item_name):
		return self.menu[item_name]

class Order(object):
	""" Implements order class"""
	def __init__(self):
		self.orders = {}





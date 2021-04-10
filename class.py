class Budget:
	def __init__(self, **kwargs):
		self.food=kwargs.get('food',0)
		self.clothing=kwargs.get('clothing', 0)
		self.entertainment=kwargs.get('Entertainment', 0)

	def deposit(self, **kwargs):
		for kwarg in kwargs:
			setattr(self, kwarg, getattr(self,kwarg)+kwargs[kwarg])

	def withdraw(self, **kwargs):
		for kwarg in kwargs:
			setattr(self, kwarg, getattr(self,kwarg)-kwargs[kwarg])

	def compute_categories(self, *args):
		for arg in args:
			 print(getattr(self, arg))
	
	def transfer_balance_among_categories(self, provider, reciever, amount):
		if amount <= getattr(self, provider, 0):
			setattr(self, provider, getattr(self, provider, 0)-amount)
			setattr(self, reciever, getattr(self, reciever, 0)+amount)
		else:
			print('insufficient funds to transfer')
		
			

#Check
budget=Budget(entertainment=60)
budget.deposit(clothing=80, entertainment=70)
print(budget.food)
print(budget.clothing)
print(budget.entertainment)
budget.compute_categories('food', 'clothing')
budget.transfer_balance_among_categories('food', 'clothing', 30)
print(budget.food)
print(budget.clothing)

#Check
#Check
budget=Budget(entertainment=60, food=70)
budget.deposit(clothing=80, entertainment=70)
print(budget.food)
print(budget.clothing)
print(budget.entertainment)
budget.compute_categories('food', 'clothing')
budget.transfer_balance_among_categories('food', 'clothing', 30)
print(budget.food)
print(budget.clothing)











class Parent () :
	def _init_ (self, last_name, eye_color):
		print ("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

billy_cyrus = Parent ("Cyrus", "blue")
print (billy_cyrus.last_name)
#parent class
class animal:
  #properties
	multicellular = True
	#Eykaryotic means cells with nuclues
	eukaryotic = True
	#function breathe
	def breathe(self):
		print("I breathe oxygen.")
  #function feed
	def feed(self):
		print("I eat food.")

#child class
class herbivorous(animal):
	#function feed
	def feed(self):
		print("I eat only plants. I am vegetarian.")
herbi = herbivorous()
herbi.feed()
#calling some other function
herbi.breathe()
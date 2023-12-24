print("WELCOME TO OUR SHOP")
print("")
male_or_female = input("Which clothes you want, Male or Female ? ")
cloth_for = input("For whome you want cloths? kids, teens or adults : ")
print("")
print("which type of dresses you prefer? ")
print("We have following collection for you choose from them ")
		
if(male_or_female == "Male"):
		
	if(cloth_for == "kids" or cloth_for == "teens"):
		print("\n Jeans \n Jackets \n Sherwani \n T-shirts \n Kurtas \n Suit \n Trouser \n Shirts \n Blazer \n Pants \n Sweaters \n Shorts \n ")
		dress_type_male = input("Dress Type : ")
		cloth_price_range = float(input("In which price range : "))
		size_kid_male = input("Size : S or M or L or XL ? ")
		
		if(cloth_price_range <= 50000 and cloth_price_range >= 200):
		
			if(dress_type_male == "Jeans" or dress_type_male == "Sherwani" or dress_type_male == "T-shirts" or dress_type_male == "Kurtas" or dress_type_male == "Suit" or dress_type_male == "Trouser" or dress_type_male == "Shirts" or dress_type_male == "Blazer" or dress_type_male == "Jackets" or dress_type_male == "Sweaters" or dress_type_male == "Pants" or dress_type_male == "Shorts"):
				pack_or_not = input("We have your choice.... Can we pack them? ")
				
				if(pack_or_not == "yes"):
					print("We have packed your choice dress for you ")
				else:
					print("We have no such type dress here... Sorry...")
		else:
			print("Sorry we don't have kids attires in this price range ")
				
	elif(cloth_for == "adults"):
		print("\n Bussiness attire \t Bussiness casual \t Casual attire \t Ultra casual\n")
		dress_type_male = input("Dress Type : ")
		cloth_price_range = float(input("In which price range : "))
		size_adult_male = input("Size : S or M or L or XL ? ")
		
		if(dress_type_male == "Bussiness attire"):
			print("\n bussines suit \n Light Shirt \n Suit Pant \nS Leather belt \n Classic NetTie \n Vest \n Striped Blazer")
			dress_type_male = input("Dress Type : ")
			if(cloth_price_range <= 5000000 and cloth_price_range >= 5000):
				if(dress_type_male == "Bussines suit" or dress_type_male == "Light Shirt" or dress_type_male == "Suit Pant " or dress_type_male == "Leather belt" or dress_type_male == "Classic NetTie" or dress_type_male == "Vest" or dress_type_male == "Striped Blazer"):
					pack_or_not = input("We have your choice.... Can we pack them? ")
					
					if(pack_or_not == "yes"):
						print("We have packed your choice dress for you ")
					else:
						print("We have no such type dress here... Sorry...")
					"""print("Colors available ")
				print("\n BLACK \n CHARCOAL \n NAVY \n GREY \n LIGHT GREY \n WHITE \n CHAMPAGNE \n BLUE INDIGO \n BROWN \n LIGHT BROWN \n OLIVE GREEN")
				dress_color = input("Which colour you prefer ? ")"""
				
			else:
				print("Sorry we don't have business attires in this price range ")
				
		elif(dress_type_male == "Bussiness casual"):
			print("\n Dress Shirt \n Blazer \n Leather belt \n Trouser \n Sports Jacket \n Wool pants ")
			dress_type_male = input("Dress Type : ")
			if(cloth_price_range <= 500000 and cloth_price_range >= 500):
				if(dress_type_male == "Dress Shirt" or dress_type_male == "Blazer" or dress_type_male == "Leather belt " or dress_type_male == "Trouser" or dress_type_male == "Sports Jacket " or dress_type_male == "Wool pants"):
					pack_or_not = input("We have your choice.... Can we pack them? ")
					
					if(pack_or_not == "yes"):
						print("We have packed your choice dress for you ")
					else:
						print("We have no such type dress here... Sorry...")
			else:
				print("Sorry we don't have business attires in this price range, we have 500 to 500000 range ")
			
		elif(dress_type_male == "Casual attire "):
			print("\n Check shirts \n Pants \n Leather belt \n Shorts ")
			dress_type_male = input("Dress Type : ")
			if(cloth_price_range <= 50000):
				if(dress_type_male == "Check Shirt" or dress_type_male == "Pants" or dress_type_male == "Leather belt " or dress_type_male == "Shorts"):
					pack_or_not = input("We have your choice.... Can we pack them? ")
		
					if(pack_or_not == "yes"):
						print("We have packed your choice dress for you ")
					else:
						print("We have no such type dress here... Sorry...")
			else:
				print("Sorry we don't have business attires in this price range ")
			
		elif(dress_type_male == "Ultra casual "):
			print("\n Collared T-shirts \n T-shirts \n Jeans \n Hooded sweater \n Collared sweater \n Shorts ")
			dress_type_male = input("Dress Type : ")
			if(cloth_price_range <= 50000):
				print("")
			else:
				print("Sorry we don't have business attires in this price range ")

		
elif(male_or_female == "Female"):

	if(cloth_for == "kids" or cloth_for == "teens"):
	
		print("\n Jeans \n Jackets \n Skirts \n Tops \n T-shirts \n Kurtas \n Suit \n Trouser \n Shirts \n Blazer \n Pants \n Sweaters \n Shorts \n ")
		dress_type_female = input("Dress Type : ")
		cloth_price_range = float(input("In which price range : "))
		size_kids_female = input("Size : S or M or L or XL ? ")
		
		if(cloth_price_range <= 50000 and cloth_price_range >= 200):
			
			if(dress_type_female == "Jeans" or dress_type_female == "Skirts" or dress_type_female == "Tops" or dress_type_female == "T-shirts" or dress_type_female == "Kurtas" or dress_type_female == "Suit" or dress_type_female == "Trouser" or dress_type_female == "Shirts" or dress_type_female == "Blazer" or dress_type_female == "Jackets" or dress_type_female == "Sweaters" or dress_type_female == "Pants" or dress_type_female == "Shorts"):
				pack_or_not = input("We have your choice.... Can we pack them? ")
				if(pack_or_not == "yes"):
					print("We have packed your choice dress for you ")
				else:
					print("We have no such type dress here... Sorry...")
		else:
			print("Sorry we don't have business attires in this price range ")
				
	elif(cloth_for == "adults"):
		
		print("\n Bussiness attire \t Bussiness casual \t Casual attire \t Ultra casual\n")
		dress_type_female = input("Dress Type : ")
		cloth_price_range = float(input("In which price range : "))
		size_adult_female = input("Size : S or M or L or XL ? ")
		
		if(dress_type_female == "Bussiness attire"):
			
			print("\n Classic suit \n Suit pants \n Jacket \n Bright color shirts \n Blazer \n Short Sleev Jackets \n Skirts")
			dress_type_female = input("Dress Type : ")
			if(cloth_price_range <= 50000000 and cloth_price_range >= 5000):
				if(dress_type_female == "Classic suit" or dress_type_female == "Suit pants" or dress_type_female == "Jacket" or dress_type_female == "Bright color shirts" or dress_type_female == "Blazer" or dress_type_female == "Skirts" or dress_type_female == "Short Sleev Jackets" ):
					pack_or_not = input("We have your choice.... Can we pack them? ")
		
					if(pack_or_not == "yes"):
						print("We have packed your choice dress for you ")
					else:
						print("We have no such type dress here... Sorry...")
			else:
				print("Sorry we don't have business attires in this price range, we have range 5000 to 50000000")
				
		elif(dress_type_female == "Bussiness casual"):
			print("\n Trouser \n Skirts \n Bright color shirts \n Blazer \n Cotton Pants \n Classic suits \n Suit pants ")
			dress_type_female = input("Dress Type : ")
			if(cloth_price_range <= 50000):
				if(dress_type_female == "Classic suit" or dress_type_female == "Suit pants" or dress_type_female == "Bright color shirts" or dress_type_female == "Blazer" or dress_type_female == "Skirts" or dress_type_female == "Short Sleev Jackets" ):
					pack_or_not = input("We have your choice.... Can we pack them? ")
		
					if(pack_or_not == "yes"):
						print("We have packed your choice dress for you ")
					else:
						print("We have no such type dress here... Sorry...")
			else:
				print("Sorry we don't have business attires in this price range, we have price range 200 to 50000")
			
		elif(dress_type_female == "Casual attire "):
			print("\n Kurta \n Skirts \n Jeans \n Tops \n Collared Shirts ")
			dress_type_female = input("Dress Type : ")
			if(cloth_price_range <= 50000 and cloth_price_range >= 200):
				if(dress_type_female == "Kurta" or dress_type_female == "Tops" or dress_type_female == "Collared shirts" or dress_type_female == "Jeans" or dress_type_female == "Skirts"):
					pack_or_not = input("We have your choice.... Can we pack them? ")
		
					if(pack_or_not == "yes"):
						print("We have packed your choice dress for you ")
					else:
						print("We have no such type dress here... Sorry...")
			else:
				print("Sorry we don't have business attires in this price range, we have price range 200 to 50000")
			
		elif(dress_type_female == "Ultra casual "):
			print("\n Tops \n T-Shirts \n Skirts \n Jeans \n Hooded sweater \n Collared sweater \n Shorts ")
			dress_type_female = input("Dress Type : ")
			if(cloth_price_range <= 50000 and cloth_price_range >= 200):
				if(dress_type_female == "Jeans" or dress_type_female == "Skirts" or dress_type_female == "Tops" or dress_type_female == "T-shirts" or dress_type_female == "Hooded sweater" or dress_type_female == " Collared sweaters" or dress_type_female == "Shorts"):
					pack_or_not = input("We have your choice.... Can we pack them? ")
					if(pack_or_not == "yes"):
						print("We have packed your choice dress for you ")
						print("Here you go...")
					else:
						print("We have no such type dress here... Sorry...")
			else:
				print("Sorry we don't have business attires in this price range , we have price range 200 to 50000")
		
		


print("***************************THANK YOU!**************************")
print("******************** - PLEASE COME AGAIN - ********************")
import numpy as np

first_name = np.array(["Shweta"])
print("first name array : ", first_name)

last_name = np.array(["Mankar"])
print("last name array : ", last_name)

full_name = np.char.add(first_name, last_name)
print("Concatinated strings", full_name)

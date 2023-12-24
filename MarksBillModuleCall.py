from MarksBillModule import *

studPerDict,studTop,studPerDictTop = marks(shweta=[42,90,78,88,99],arti=[62,90,89,93,78],sayali=[89,90,99,89,87])
print(studPerDict,studTop,studPerDictTop)


amtWithDiscount = bill(60,8,3)
print("Total paid bill after discount is ",amtWithDiscount)


amtWithDiscount = bill(600,700,450,780)
print("Total paid bill after discount is ",amtWithDiscount)
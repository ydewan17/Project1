#Exception

num1 = 5 
num2=0

# try:
# 	print (num1/num2)   #this fail nad continue except
# except:
# 	print("Damn, that didn't work")
# print ( "That is alt")



# str1 = 'la137'   

# try:
#     num3 = int(str1)
# except:
# 	print("thats not an integer!")
# else:
#     print(num3 + 10)

#------------------------------------------

# str1 = '137'   

# try:
#     num3 = int(str1)
# except:
# 	print("thats not an integer!")
# else:
# 	print(num3 + 10)

# ------------------------------------

# str1 = '1-37'   

# try:
#     num3 = int(str1)
# except ValueError:
# 	print("thats not an integer!")                      #ValuError
# else:
# 	print(num3 + 10)

# -------------------------------

# str1 = ['1-37']   

# try:
#     num3 = int(str1)
# except ValueError:
# 	print("thats not an integer!")                     # TypeError
# except TypeError:
# 	print("I need a string!")

# else:
# 	print(num3 + 10)




#-------------------------------

# str1 = '137' 

# try:
#     num3 = int(str1)
# except ValueError:
# 	print("thats not an integer!")                     # Right value
# except TypeError:
# 	print("I need a string!")

# else:
# 	print(num3 + 10)
# finally:
# 	print("I'll always do this")

#--------------------------------------

# str1 = '137' 

# try:
#     num3 = int(str1)
# except ValueError:
# 	print("thats not an integer!")                     # Right value
# except TypeError:                           
# 	print("I need a string!")

# else:                                                #finally
# 	print(num3 + 10)
# finally:
# 	print("I'll always do this")



f= open ("LICENSE","r")

try:
	print(f2.readline())

finally:
	print("always always always close the file")

	f.close()
   
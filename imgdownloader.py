import urllib.request
import csv

products = [] #list of finded prducts
noProducts = True #just a flag
counter=0 #in order to count results
#Find product 1
product = input('Nombre del producto:\n')
csv_file = csv.reader(open('testImg.csv', "r"), delimiter=";")

for row in csv_file:
        if product in row[1]:  #add dynamic row selection
            products.append(row)
            counter= counter + 1
            print (str(counter) + ":") 
            print (row)
            noProducts = False
            imgURL = row[12]
            print (imgURL)
            urllib.request.urlretrieve(imgURL, "D:/"+ product + "_" + str(counter) + ".jpg") #improve: save in current directory

if noProducts == True:
    print("No hay productos con ese criterio de búsqueda") 

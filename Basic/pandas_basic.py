import pandas as pd
from geopy.geocoders import ArcGIS
address = pd.read_csv(r'C:\Users\ssubh\Downloads\supermarkets.csv')

address["Continent"] = address.shape[0]*["North America"]# adds north america to the columns 

address_t = address.T # switches coulums and rows
address_t["My Address"] = ["My City","My Country",10,7,"My Shop","My State","My Continent",'North America'] # adds row as a coloumn
address = address_t.T #switches the coulums and rows back with the new row

nom = ArcGIS()
address["Coordinates"] = address["Address"].apply(nom.geocode) #makes a new coloum and takes the adresses and puts 
                                                                #and puts it through the geocode function
address["longitude"] = address["Address"].apply(lambda x: x.laditude if x=! else None) #makes a new coloum and takes the adresses and uses a lambda funcuton


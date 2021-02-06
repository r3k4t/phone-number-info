
import os
import sys
from phone_iso3166.network import*

os.system('clear')

print ("              +===================================+")
print ("              |          SIM Company              |")
print ("              +===================================+")
print ("              | Author : Rahat Khan Tusar(rkt)    |")   
print ("              | Github : https://github.com/r3k4t |")
print ("              +===================================+")
print
phone_number=raw_input('Enter a phone number :')
cn=raw_input('Enter a country name(Ex:BD,US,UK etc.):')
phone=phone_number
network(238,1)
print (country_networks(cn))






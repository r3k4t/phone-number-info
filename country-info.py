
import os
import sys

os.system('clear')

print ('+===================================+')
print ('|         Country Info              |')
print ('+===================================+')
print ('| Author : Rahat Khan Tusar(rkt)    |')
print ('| Github : https://github.com/r3k4t |')
print ('+===================================+')
print
from phone_iso3166.country import phone_country
phone_number=raw_input("Enter a phone number : ")
print ('Country              :'+ phone_country(phone_number))
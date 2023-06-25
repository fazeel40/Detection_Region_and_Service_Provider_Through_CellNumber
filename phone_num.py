import phonenumbers
from phonenumbers import geocoder

number = "+923126690033"
ch_num = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_num,"en"))

from phonenumbers import carrier
service_pr = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_pr,"en"))
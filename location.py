from googlegeocoder import GoogleGeocoder
from math import sin,cos,sqrt,atan2,radians
from decimal import Decimal

geocoder = GoogleGeocoder("AIzaSyB0Pz6VjrQmWPCCbDbWDuyjo79GhDJPOlI")
search = geocoder.get("C-65,Noida,Sector-2,India")
search2=geocoder.get("Noida,Sector-142,India")

search[0].geometry.location
search2[0].geometry.location

fromlatitude= search[0].geometry.location.lat
fromlongitude=search[0].geometry.location.lng

tolatitude= search2[0].geometry.location.lat
tolongitude= search2[0].geometry.location.lng
R = 6373.0
fromlongitude2= Decimal(fromlongitude)
fromlatitude2 = Decimal(fromlatitude)
# print(fromlongitude2,fromlatitude2)

distanceLongitude = tolongitude - fromlongitude
distanceLatitude = tolatitude - fromlatitude


a = sin(distanceLatitude / 2)**2 + cos(fromlatitude) * cos(tolatitude) * sin(distanceLongitude / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
distance = R * c
distance2=distance/100
Distance=distance2*1.85
d=round(Distance)
d2 =str(d) +'Km'

print(d2)


# print(tolongitude,tolatitude)
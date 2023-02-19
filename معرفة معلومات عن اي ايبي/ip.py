from geoip import geolite2


#هذا الكود لمعرفة معلومات عن اي ايبي في العالم
ip = "24.51.57.13"

locator = geolite2.lookup(ip)

# timezone => print("America/Chicago")
# continent => print("NA")
# country => print("sudan")
if locator is None:
    print("Unknow")
else:
    # print(locator.timezone)    
    # print(locator.continent) 
    print(locator.country) 
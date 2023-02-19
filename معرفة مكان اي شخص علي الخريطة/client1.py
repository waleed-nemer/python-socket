import geocoder
import folium

# معرفة الاشخاص عن طريق الخريطة 


# هذا الكود عبارة متغير + عنوان الايبي الخاص بي 
our_ip = geocoder.ip("me")

#متغير يسمي الموقع ثم اعطيه الايبي 
location = our_ip.latlng

# متغير الخريطة ثم اعطيه الموقع + حجم التكبير 
our_map = folium.Map(location=location, zoom_start=10)

#هذا الكود يضع الموقع علي الخريطة 
folium.Marker(location).add_to(our_map)

# هذا الكود يضع بيانات الخريطة في صفحة بمتداد اتش تي ام ايل
our_map.save("map.html")

#هنا نطبع الموقع 
print(location)
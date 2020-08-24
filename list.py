students = ["Beyza", "Kevser", "Ufuk"]
print(students)

# append ile ekleme yaparız
students.append("Beril")
print(students)

# remove ile listeden çıkarabiliriz
students.remove("Beyza")
print(students)
print(students[2])
students[0] = "Beyza"
print(students)
students.append("Kevser")
print(students)   

# List constructor
city = list(("Ankara", "İstanbul", "Bursa"))
print(city)
# .count sayıyı belirtir
print("Ankara Sayısı = " + str((city.count("Ankara"))))
# index kaçıncı sırada olduğunu belirtir
print("Bursa Kaçıncı Sırada? = " + str(city.index("Bursa")))
# .pop belirtilen değeri çıkartamak için kullanılır
city.pop(1)
print(city)
# .insert yerleştirmek için kullanılır
city.insert(3, "İzmir")
print(city)
city.reverse()
print(city)
city.sort()
print(city)
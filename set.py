studentSets = {"Beyza", "Kevser", "Ufuk"}
print(studentSets)
for students in studentSets:
    print(students)
    
if "Beyza" in studentSets:
    print("It's on the list.")
    
# ekleme yapmak için .add
studentSets.add("Beril")
print(studentSets)
# birden fazla ekleme yapacaksak .update kulanırız [] parantezi unutma!!
studentSets.update(["Hamdi", "Selin", "Emir"])
print(studentSets)    
print(len(studentSets))
# .pop listeden son elemanı silmeye yarar.
studentSets.pop()
print(studentSets)


# setUnion file

setA = {"Cherry", "Peach", "Banana", "Strawberry"}
setB = {"Apple", "Google", "Microsoft"}
# print(setA | setB)

# İkinci yol 
setC = setA.union(setB)
print(setC)

# setIntersection file (kesişim)

setX = {"Finland", "Norway", "Sweden"}
setY = {"Sweden", "Holland", "Italy"}
print(setX & setY)
print(setX - setY)

techList = ["Apple", "Microsoft", "Samsung", "Dell", "HP"]
print(techList)
print(techList[0:2])

techList[0] = "Tesla"
print(techList)

techList.remove("Samsung")
print(techList)

techList.insert(3, "Tesla")
print(techList)

print(len(techList))
print("Microsoft" in techList)
print("Tesla" in techList)

techList.clear()
print(techList)

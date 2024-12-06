person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
print(person["name"] , person["hobby"]) 
print(person)
person["surname"]="Nowak"
person["mariage"]=False
person["gender"]="male"
person["hobby"].append("bicycle")
person["phone"]["mark"]="313131444"
for key , value in person.items():
    print(key,value)

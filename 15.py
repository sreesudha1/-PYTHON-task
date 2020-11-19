##person = {"name" : ["reddy","sudha"] , "age":23, "salary":34000 , "gender":"female" , "sports":["kabadi","cricket"] , ("a","b"):["sachin","sandeep"]}
##person1 = {"native place":"kadapa"}
##print(person["name"])
##print(person["age"])
##print(person["salary"])
##print(person["gender"])          
##print(person["sports"][0])          
##person["name"][1]="sree"
##print(person)
##person.update(person1)
##print(person)
##print(person.get("address"))
##print(person[("a","b")])
##print(person["a","b"][0])

##print(person["name"],["age"],["salary"],["gender"],["sports"][0])

##person.pop("sports")
##print(person)
##
##person.clear()
##print(person)

numbers = {1:1, 3:9, 5:25, 7:49 ,9:81}
##print(1 in numbers)
##
##print(2 in numbers)
##
##print(3 not in numbers)
##
##print(25 in numbers)

##for i in numbers:
##    print(numbers[i])
    
print(all(numbers))

print(any(numbers))

print(len(numbers))

print(sorted(numbers))

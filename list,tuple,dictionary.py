#list

mylist = ["python","java","c"]
#methods
print(mylist)
print("length is")
print(len(mylist))

print("type of")
print(type(mylist))

print("access lilst")
print(mylist[1])

print("negative index")
print(mylist[-1])

print("range")
print(mylist[0:2])
print(mylist[:2])
print(mylist[1:])

print("is in list")
if "c" in mylist:
  print("Yes, 'c' is in the  list")
  
print("change the value in list")
mylist[1] = "blackcurrant"
print(mylist)

print("change two item")
mylist[0:2] = ["blackcurrant", "watermelon","banana"]
print(mylist)

print("to add item in list")
mylist.append("orange")
print(mylist)

print("insert to second item")
mylist.insert(1, "orange")
print(mylist)

print("extend")
tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical)
print(mylist)

print("remove the item in list")
mylist.remove("banana")
print(mylist)

print("remove using pop")
mylist.pop(1)
print(mylist)

print("sortingn list")
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

print("decending order")
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

print("joining list")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)
#---------------------------------------------------------------------------------------
#tuple


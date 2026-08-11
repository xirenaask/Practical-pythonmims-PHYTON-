#C -17//5 and -17 % 5 and one line comment 
#set 6 5 marks

#q1 data types and operatorswrite program to compute and print _17 // 5 and -17 % 5 add note one line commentexplaining why floor division result is not simply whate a calculators button would show

print(-17 // 5)
print(-17 % 5)
 #floor division rounds down to the nearest integer' so -3.4 becomes -4

#Q2[strings] take a full name input eg(eg Tirup parmar) and print only the initials innthe form t.p
name = input("Enter full name:  ")
parts = name.split()
print(parts[0][0] + "." + parts[1][0] + ".")


#Q3 [list and tuples]  let lst={10,20,30} print lstt + (40,50) and lst*2 one below the other and add comment explaining the differnce between list concententation and list repetition
lst = [10,20,30]
print(lst + [40,50])
print(lst * 2)
# + concentrates (joins ) lists, while * reapeats the list multiple times 

#Q4{sets and dictionaries }let d= {"a":1 "b":2} do d["a"] =100  and print the dictionarybefore and after  add comment explaining wheater this created a new entry or updates the exisiting one
d = {"a": 1, "b" : 2}
print(d)

d["a"] = 100
print(d)

# this updates the exsisting entry for key "a"; it does not create a new entry

qyzrox-guJpi1-juwbok

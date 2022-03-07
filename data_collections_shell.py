Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello how are you and I am fine"
>>> tokens = text.split()
>>> tokens
['hello', 'how', 'are', 'you', 'and', 'I', 'am', 'fine']
>>> tokens = text.lower().split()
>>> tokens
['hello', 'how', 'are', 'you', 'and', 'i', 'am', 'fine']
>>> stopwords = ["are","you","and","i","am"]
>>> for word in tokens:
	if word not in stopwords:
		print(word)

		
hello
how
fine
>>> data = []
>>> data = list()
>>> data = [3,4,2,3,5,6,7,4,3,6,78,4.5,6.5]
>>> type(data)
<class 'list'>
>>> data[0]
3
>>> data[0:4]
[3, 4, 2, 3]
>>> data[2:10:2]
[2, 5, 7, 3]
>>> data = []
>>> data.append(4)
>>> data.append(12)
>>> data.append(3)
>>> data.append(31)
>>> data
[4, 12, 3, 31]
>>> data.append(3,4,5,3,3)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    data.append(3,4,5,3,3)
TypeError: list.append() takes exactly one argument (5 given)
>>> data.extend(3,4,5,3,3)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data.extend(3,4,5,3,3)
TypeError: list.extend() takes exactly one argument (5 given)
>>> data.extend([3,4,5,3,3])
>>> data
[4, 12, 3, 31, 3, 4, 5, 3, 3]
>>> data.append([3,4,5,3,3])
>>> data
[4, 12, 3, 31, 3, 4, 5, 3, 3, [3, 4, 5, 3, 3]]
>>> data.pop()
[3, 4, 5, 3, 3]
>>> data.pop()
3
>>> data.pop()
3
>>> data
[4, 12, 3, 31, 3, 4, 5]
>>> data.pop(3)
31
>>> data
[4, 12, 3, 3, 4, 5]
>>> data.insert(3,12)
>>> data.insert(5,21)
>>> data
[4, 12, 3, 12, 3, 21, 4, 5]
>>> data.remove(0)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    data.remove(0)
ValueError: list.remove(x): x not in list
>>> data.remove(4)
>>> data
[12, 3, 12, 3, 21, 4, 5]
>>> data.count(12)
2
>>> data.index(5)
6
>>> data.reverse()
>>> data
[5, 4, 21, 3, 12, 3, 12]
>>> data.sort()
>>> data
[3, 3, 4, 5, 12, 12, 21]
>>> data.sort(reverse=True)
>>> data
[21, 12, 12, 5, 4, 3, 3]
>>> data = []
>>> for i in range(1,51):
	if i % 2 == 0:
		data.append(i)

		
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> for i in range(len(data)):
	print(data[i])

	
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
>>> for item in data:
	print(item)

	
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
>>> data = []
>>> for i in range(1,51):
	if i % 2 == 0:
		data.append(i)

		
>>> data = [i for i in range(10)]
>>> data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> data = [i for i in range(10) if i % 2 == 0]
>>> data
[0, 2, 4, 6, 8]
>>> data[0] = 100
>>> data
[100, 2, 4, 6, 8]
>>> data = (4,3,4,5,6)
>>> data = 4,3,4,5,6
>>> data
(4, 3, 4, 5, 6)
>>> data[0] = 121
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    data[0] = 121
TypeError: 'tuple' object does not support item assignment
>>> del data[0]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    del data[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = (i for i in range(1,11))
>>> data
<generator object <genexpr> at 0x000001B859FF8EB0>
>>> data = (4,3,4,5,6)
>>> data = {"name" : "John", "salary":45000, "dept":"IT"}
>>> data
{'name': 'John', 'salary': 45000, 'dept': 'IT'}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['name']
'John'
>>> data['salary']
45000
>>> data['dept']
'IT'
>>> data["address"] = "Mumbai"
>>> data
{'name': 'John', 'salary': 45000, 'dept': 'IT', 'address': 'Mumbai'}
>>> data.keys()
dict_keys(['name', 'salary', 'dept', 'address'])
>>> data.values()
dict_values(['John', 45000, 'IT', 'Mumbai'])
>>> data.items()
dict_items([('name', 'John'), ('salary', 45000), ('dept', 'IT'), ('address', 'Mumbai')])
>>> data["phone"]
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    data["phone"]
KeyError: 'phone'
>>> data.get("name")
'John'
>>> data.get("phone")
>>> data.get("phone","Not available")
'Not available'
>>> data.get("project_id","Not available")
'Not available'
>>> data.get("dept","Not available")
'IT'
>>> data.pop("address")
'Mumbai'
>>> data
{'name': 'John', 'salary': 45000, 'dept': 'IT'}
>>> data.popitem()
('dept', 'IT')
>>> data
{'name': 'John', 'salary': 45000}
>>> for item in data:
	print(item)

	
name
salary
>>> for item in data:
	print(item, "::", data[item])

	
name :: John
salary :: 45000
>>> for item in data.values():
	print(item)

	
John
45000
>>> #data = [{}, {}, {}, {}]
>>> #data = {"" : [], "" : [], "" : []}
>>> 
========= RESTART: D:/Batches/2022/Jan Python Morning US/dict_exercise_1.py =========
>>> data
{'names': ['John', 'Mac', 'Sam', 'Paul', 'Nick'], 'dept': ['IT', 'HR', 'IT', 'IT', 'HR'], 'salary': [45000, 55000, 50000, 25000, 68000]}
>>> data["name"]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    data["name"]
KeyError: 'name'
>>> data["names"]
['John', 'Mac', 'Sam', 'Paul', 'Nick']
>>> data["names"][0]
'John'
>>> data["salary"][2]
50000
>>> 
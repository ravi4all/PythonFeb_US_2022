Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world"
>>> text = 'hello world'
>>> text = """hello world"""
>>> text = '''hello world'''
>>> text = "Hello world, this is Python Programming"
>>> text[0]
'H'
>>> len(text)
39
>>> text[12]
' '
>>> text[14]
'h'
>>> text[38]
'g'
>>> text[-1]
'g'
>>> text[0:4]
'Hell'
>>> text[0:5]
'Hello'
>>> text[10:30]
'd, this is Python Pr'
>>> text[:]
'Hello world, this is Python Programming'
>>> text[0:]
'Hello world, this is Python Programming'
>>> text[0:100]
'Hello world, this is Python Programming'
>>> text[:20]
'Hello world, this is'
>>> text[10:1]
''
>>> text[10:1:-1]
'dlrow oll'
>>> text[::-1]
'gnimmargorP nohtyP si siht ,dlrow olleH'
>>> text[-1:-10:-2]
'gimro'
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[0:20:2]
'Hlowrd hsi'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text
'Hello world, this is Python Programming'
>>> text.lower()
'hello world, this is python programming'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text.swapcase()
'hELLO WORLD, THIS IS pYTHON pROGRAMMING'
>>> text.count('i')
3
>>> text.count('o')
4
>>> text.count('o',2,10)
2
>>> text.index('o')
4
>>> text.index('o',0)
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.index('o',26)
30
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.find('o',26)
30
>>> text.find('z')
-1
>>> char = 'o'
>>> count = text.count(char)
>>> index = 0
>>> for i in range(count):
	index = text.index(char, index)
	print(index)
	index += 1

	
4
7
25
30
>>> text.split()
['Hello', 'world,', 'this', 'is', 'Python', 'Programming']
>>> text.split(",")
['Hello world', ' this is Python Programming']
>>> text.isalnum()
False
>>> text.isalpha()
False
>>> text.islower()
False
>>> text.isupper()
False
>>> text.isprintable()
True
>>> text.index('o')
4
>>> text.rindex('o')
30
>>> text.rfind('o')
30
>>> 
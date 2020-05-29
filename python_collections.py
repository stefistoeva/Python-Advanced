# Python Collections (Arrays):
# There are four collection data types in the Python programming language:
#       -> List is a collection which is ordered and changeable. Allows duplicate members.
#       -> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#       -> Set is a collection which is unordered and unindexed. No duplicate members.
#       -> Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#
# 1. List
#     Stacks - Last in element in a stack first out
#           stack = []
#           stack.append()
#           stack.pop()
#     Queues - First in element in a queues first out
#           from collections import deque
#           deque = deque()
#           deque.append()
#           deque.popleft()
# 2. Tuple
#       tuple = (1, 2, 3, 1, 1) | with a single element -> tuple = (1, )
#       -> Immutable objects
#       -> There are only two available tuple methods:
#       tuple.count(1) # 3 (count of num 1)
#       tuple.index(1) # 0 index (return index of the first element encountered)
# 3. Sets
#       -> Every element of a set is unique
#       -> Mutable objects
#       a = set()
#       a = set([1, 2, 3, 4])
#       b = set([3, 4, 5, 6])
#       Operations:
#           a | b # Union -> {1, 2, 3, 4, 5, 6} <=> a.union(b)
#           a & b # Intersection -> {3, 4} <=> a.intersection(b)
#           a < b # Subset -> False <=> a.issubset(b) (a <= b) and a.issuperset(b) (a >= b)
#           a - b # Difference -> {1, 2} <=> a.difference(b)
#           a ^ b # Symmetric Difference -> {1, 2, 5, 6} <=> a.symmetric_difference(b)
# 4. Dictionary
#       -> Key-value pairs. Keys must be of immutable type and must be unique.Dictionaries are mutable.
#       my_dictionary = {}
#       my_dictionary = {'name': 'Jack', 'age': 26}
#       print(my_dictionary['name']) # Jack
#       print(my_dictionary.get('age') # 26
#       my_dictionary.keys() || my_dictionary.values() || my_dictionary.items()
#       -> Dictionary Methods:
#           my_dictionary.clear() # {}
#           my_dictionary.copy() # {'name': 'Jack', 'age': 26}
#           my_dictionary.pop(1) # Jack
#           my_dictionary.popitem() # ('age: 26)
#       -> Sorted() Method
#           sorted(iterable[, key][, reverse])
#           lambda -> You can use lambda functions in the sort() method as in the filter() and map() functions
#

from collections import deque

my_list = ["apple", "banana", "cherry"]
print(list)

my_stack = []
my_deque = deque()
my_tuple = (1, 2, 3, 1, 1)
my_set = set()
my_dictionary = {}


# Example 2 - Basic Operator
x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# Example 3 - Python Operator
# Exercise 18-a: Assignment Operator
lst = ["yellow", "white", "blue"]
print(lst)

# Exercise 18-b: Division Operator
a = 10
b = 3
result = a/b
print(result)

# Exercise 18-c: Addition using
vertical_speed = 750
vertical_speed += 100
print(vertical_speed)

# Exercise 18-d: Modulus
remainder = 1000 % 400
print(remainder)

# Exercise 18-e: Power Operator
p_result = 11111**2
print(p_result)

# Exercise 18-f: Comparison Operator
lst = ["Mango", "Kiwi", "Melon", "Cherry"]
answer_1 = ""
if lst[0] == "strawberry":
    answer_1 = "yes"
else:
    answer_1 = "no"

print(answer_1)

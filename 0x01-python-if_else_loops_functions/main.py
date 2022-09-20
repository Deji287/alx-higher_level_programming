#!/usr/bin/env python3
print("---------Task 7-------------")
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

print("-----------------Task 8----------------")
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")

print("-------------Task 9---------------")
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

print("--------------------Task 10--------------------")
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

print("--------------Task 11-----------------")
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

print('----------------Task 12--------------')
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

print("-------------Task 101------------------")
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))

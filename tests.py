# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info, get_file_content
import os

'''  # Testing for function....successful
test = get_files_info("calculator", ".")
test1 = get_files_info("calculator", "pkg")
test2 = get_files_info("calculator", "/bin")
test3 = get_files_info("calculator", "../")
print(test)
print(test1)
print(test2)
print(test3)
'''
#test = get_file_content("calculator", "lorem.txt") #testing file
test1 = get_file_content("calculator", "main.py")
test2 = get_file_content("calculator", "pkg/calculator.py")
test3 = get_file_content("calculator", "/bin/cat")

print(test1)
print(test2)
print(test3)

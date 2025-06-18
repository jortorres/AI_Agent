# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info
import os

test = get_files_info("calculator", ".")
test1 = get_files_info("calculator", "pkg")
test2 = get_files_info("calculator", "/bin")
test3 = get_files_info("calculator", "../")
print(test)
print(test1)
print(test2)
print(test3)

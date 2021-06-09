import re
file1 = open('sample.html')
file2 = file1.read()
list_of_words = re.findall(r'python',file2)
print(len(list_of_words))
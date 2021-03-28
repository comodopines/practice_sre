# Open a file in read mode
with open('filename', mode='r') as my_file:
  for line in my_file:
    print(line)

# Open a file in write mode
with open('filename', mode='w') as my_file:
    print(line, file=my_file)
# https://stackabuse.com/writing-to-a-file-with-pythons-print-function/

# Open a file in write mode
with open('filename', mode='w') as my_file:
    my_file.write(line+'\n')
    
# all file mode explained
#https://stackoverflow.com/a/30566011

r,w,a,r+,w+,a+
#w truncates



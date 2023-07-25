import os
import datetime

# os.remove("./Python-file/removed.txt")

# os.rename("older name of the file","New name of the file")

os.path.exists('./Python-file/removed.text') # False
print(os.path.exists('./Python-file/test.txt'))# True

# More file infromation

timestamp= os.path.getmtime("./Python-file/test.txt")
modefied_time = datetime.datetime.fromtimestamp(timestamp)
print("The siz of the file is :", os.path.getsize("./Python-file/test.txt"))
print('Last Modified timestatmp is :',modefied_time)

print("The Absolut path of the file is :", os.path.abspath("./Python-file/test.txt"))
print("Current working directory is :", os.getcwd())


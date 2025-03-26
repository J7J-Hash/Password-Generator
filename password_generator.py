#Import Libraries
!pip install outputformat
import outputformat as ouf
from IPython.display import clear_output
import time
import random
import string
string.ascii_letters
i = 0
j = 0
GeneratedPassword = []

clear_output()
ouf.linetitle("Password Generator", style="double")
print("Coded By J7J")
print("")
PasswordLength = int(input("Password Length: "))
IncludeNumbers = input("Include Numbers? (Y/N) ")
print("")

if IncludeNumbers == "Y":
  while i < PasswordLength:
    if random.randint(1,2) == 1:
      randChar = random.choice(string.ascii_letters)
      GeneratedPassword.append(randChar)
      i += 1
    elif random.randint(1,2) == 1:
      randChar = random.randint(0,9)
      GeneratedPassword.append(randChar)
      i += 1

if IncludeNumbers == "N":
  while i < PasswordLength:
    randChar = random.choice(string.ascii_letters)
    GeneratedPassword.append(randChar)
    i += 1

clear_output()
LoadQuant = 0
while LoadQuant < 100:
  LoadQuant += random.randint(5,25)
  ouf.linetitle("Loading...", style="double")
  if LoadQuant >= 100:
    break
  else:
    ouf.bar(LoadQuant, 100, length=50)
    time.sleep(1)
    clear_output()

clear_output()
ouf.linetitle("Loading Complete", style="double")
ouf.bar(100, 100, length=50)
time.sleep(2)
clear_output()

ouf.linetitle("Here is your Password:", style="double")
print(*GeneratedPassword, sep="")

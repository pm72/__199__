import random, time

print("Gavagorot kamateli...\n")

your_number = my_number = 0

for i in range(5):
    print("Round {}:".format(i+1))
    
    print("\tSheni gagorebaa: ", end="")
    shoot1 = random.randint(1, 6)
    time.sleep(0.5)
    print(shoot1)
    
    print("\tChemi gagorebaa: ", end="")
    shoot2 = random.randint(1, 6)
    time.sleep(0.5)
    print(shoot2)
    
    if shoot1 > shoot2: your_number += 1
    elif shoot2 > shoot1: my_number += 1
    
    time.sleep(0.5)
    print("\t{} : {}\n".format(your_number, my_number))

    
time.sleep(1)
if your_number > my_number: print("Shen moige!")
elif my_number > your_number: print("Me movige!")
else: print("Yaimi")



# --------------
input("\n\nDone!..")
print('hello')
print('hi')
print('hi hello')

passkey=4563
for i in range(1,4):
    Pin=eval(input("Enter A 4-Digit PIN"))
    if(Pin==passkey):
         print("Successfully Logined")
    else:
        for j in range(3):
            if(Pin!=passkey and (j!=3 and print("Trials exuasted"))):
                print("Invalid Pin")
            
                print("Ran out of trials")
                break
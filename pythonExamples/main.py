import random as rand

# proper set up of a main function in Python

def printMessages(message1, messsage2):
   print(message1, "is", messsage2)

def printRandomMessage(message1, message2):
   print(message1, "is", rand.choice(message2))

def main():
   # print("Hello World!")
   message1 = "Coding"
   message2 = ["fun", "hard", "easy", "interesting", "trivial", "dumb", "binary"]
   # printMessages(message1, message2[0])
   # printMessages(message1, message2[1])
   # printMessages(message1, message2[2])
   # printMessages(message1, message2[3])
   
   for i in range(10):
      printRandomMessage(message1, message2)

if __name__ == "__main__":
   main()
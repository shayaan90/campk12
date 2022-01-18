import random
n=random.randint(1,10)
p=input("whats your name?")
g=0
print('ok ' +p+ ' im guessing a number between 1 and 10:')

while g<5:
  guess=int(input())
  g+=1
  if guess<n:
    print("your guess is low")
  if guess>n:
    print("your guess is high")
  if guess==n:
    break
if guess==n:
  print("you guessed the right number in "+str(g)+" tries")
else:
  print("you did not guess the right number")
s

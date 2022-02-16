import random

rd = []
score = 0


    
for i in range(3):
    rd.append(random.randrange(0,10))
print(rd[0], rd[1], rd[2])

if rd[0] == rd[1] or rd[1] == rd[2] or rd[2] == rd[0]:
    score += 1
  
elif rd[0] == rd[1] == rd[2]:
    score += 1
    print("JACPOT!!")
    


print(score)
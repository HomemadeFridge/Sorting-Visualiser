from random import randint
import pygame
k = []
final = []
testcase = 0
for i in range(0,100):
    k.append(randint(0,1000))

print(", ".join(map(str, k))+'\n\n\n')
print("STALIN SORT!\n\n\n")

for i in range(0,len(k)):
    if k[i] > testcase:
        final.append(k[i])
        testcase = k[i]
    #else:
        #final.append(testcase)
print(", ".join(map(str, final)))
#display = pygame.display.set_mode((1000,500))
#pygame.display.set_caption("Stalin Sort")

#def drawsorts():
#    global display, k
#    for i in range(0,100):
#        pygame.draw.rect(display,)
        

while True:
    None
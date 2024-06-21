##Sorting Visualiser
from random import randint
import pygame
pygame.init()
carryOn = True
vals = [0,1,0]
GotIt = False
comparisons = 0
font = pygame.font.Font("BAHNSCHRIFT.TTF",20)
frfont = pygame.font.Font("BAHNSCHRIFT.TTF",15)
lfont = pygame.font.Font("BAHNSCHRIFT.TTF",90)
timecount = 0
timesthrough = 0

##colours

GREY = (200,200,200)
BLACK = (0,0,0)
GREEN = (0,200,0)

framerate = pygame.time.Clock()

##list generation
k = []
ksorted = []
final = []
testcase = 0
length = int(input("Please enter the length of list:\n>"))
frames = int(input("Please enter the framerate you wish to run the visualiser at:\n>"))
for i in range(0,length):
    temp = randint(0,1000)
    k.append(temp)
    ksorted.append(temp)
ksorted.sort()

##sorting algs
def bubblesort(a):
    for i in range(0,len(a)):
        for j in range(0,len(a) - 1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return a

def bubblesort2(a,vals):
    if a[vals[0]] > a[vals[1]]:
        temp = a[vals[0]]
        a[vals[0]] = a[vals[1]]
        a[vals[1]] = temp
    vals[0] += 1
    vals[1] += 1
    if vals[0] >= len(a)-1:
        vals[0] = 0
        vals[1] = 1
    return a, vals

def insertionsort(b):
    for i in range(1,len(b)):
        current = b[i]
        while i > 0 and b[i-1] > current:
            b[i] = b[i-1]
            i = i-1
            b[i] = current
    return b

def insertionsort2(b, vals):
    if vals[1] >= len(b):
        vals[1] = 1
    current = b[vals[1]]
    if vals[1] > 0 and b[vals[1] - 1] > current:
        b[vals[1]] = b[vals[1] - 1]
        vals[1] -= 1
        b[vals[1]] = current
    else:
        vals[1] += 1
    return b, vals

# def mersort(x,vals):
#     global timecount, timesthrough
#     if timesthrough == 0:
#         if x[vals[0]] >= x[vals[1]]:
#             temp = x[vals[0]]
#             x[vals[0]] = x[vals[1]]
#             x[vals[1]] = temp
#         vals[0]+=2
#         vals[1]+=2
#         timecount += 1
#     if timecount == len(x)//2:
#         timesthrough += 1
#         vals[0] = 0
#         vals[1] = 1
#     if timesthrough == 1:
#         x.sort()
#     return x,vals

# def msort(b, vals):
#     def merge(b, left, mid, right):
#         left_sublist = b[left:mid]
#         right_sublist = b[mid:right]
#         i = j = 0
#         k = left

#         while i < len(left_sublist) and j < len(right_sublist):
#             if left_sublist[i] <= right_sublist[j]:
#                 b[k] = left_sublist[i]
#                 i += 1
#             else:
#                 b[k] = right_sublist[j]
#                 j += 1
#             k += 1

#         while i < len(left_sublist):
#             b[k] = left_sublist[i]
#             i += 1
#             k += 1
#         while j < len(right_sublist):
#             b[k] = right_sublist[j]
#             j += 1
#             k += 1

#     left, mid, right = vals

#     mid = min(mid, len(b))
#     right = min(right, len(b))

#     if mid < right:
#         merge(b, left, mid, right)
    
#     new_left = left + (right - left) * 2
#     new_mid = min(new_left + (mid - left), len(b))
#     new_right = min(new_mid + (mid - left), len(b))

#     if new_left >= len(b):
#         left = 0
#         mid = 1
#         right = min(2, len(b))
#     else:
#         left = new_left
#         mid = new_mid
#         right = new_right

#     vals[:] = [left, mid, right]
#     return b, vals
def msort(k, vals):
    if vals[2] == 0:
        vals[0]+= 1
        vals[1] += 1
        if vals[1] >= len(k):
            vals[0] -= 1
            vals[1] -= 1
            vals[2] = 1
    elif vals[2] == 1:
        vals[0] -= 1
        vals[1] -= 1
        if vals[0] <= 0:
            vals[0] += 1
            vals[1] += 1
            vals[2] = 0
    return vals

def stalinsort(k,vals):
    global GotIt
    if k[vals[0]] > vals[2]:
        vals[2] = k[vals[0]]
    else:
        k[vals[0]] = vals[2]
    vals[0] += 1
    vals[1] += 1
    if vals[1] >= len(k):
        if k[vals[0]] > vals[2]:
            vals[2] = k[vals[0]]
        else:
            k[vals[0]] = vals[2]
        vals[1] = 1
        vals[0] = 0
        GotIt = True

##def insertionsort2(b,vals):
    #current = b[vals[1]]
    #while vals[1] > 0 and b[vals[0]] > current:
        #b[vals[1]] = b[vals[0]]
        #vals[1] -= 1
        #b[vals[1]] = current
    #vals[0] += 1
    #vals[1] += 1
    #if vals[0] >= vals[1]:
        #vals[0] = 0
        #vals[1] = 1
    #return b, vals

##

def drawsorts():
    global display, k, GREY, GREEN, vals, GotIt, sortingalg
    for i in range(0,length):
        if GotIt:
            pygame.draw.rect(display, GREEN,[i*(1000//length),600-(k[i]//2),(1000//length),k[i]//2])
        else:
            pygame.draw.rect(display, GREY,[i*(1000//length),600-(k[i]//2),(1000//length),k[i]//2])
    if sortingalg == 'B':
        pygame.draw.rect(display, GREEN,[vals[1]*(1000//length),600-(k[vals[1]]//2),(1000//length),k[vals[1]]//2])
    else:
        for i in range(0, 2):
            if vals[i] < len(k):
                pygame.draw.rect(display, GREEN, [vals[i] * (1000 // length), 600 - (k[vals[i]] // 2), (1000 // length), k[vals[i]] // 2])

sortingalg = str(input("PICK A SORTING ALGORITHM TO VISUALISE:\nA) BUBBLE SORT\nB) INSERTION SORT\nC) MERGE SORT\nD) STALIN SORT\n>")).upper()

display = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Sorting Visualiser")
if sortingalg == "C":
    vals = [0,1,0]
else:
    vals[2] = k[0]


while carryOn:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            carryOn = False
    display.fill(BLACK)
    drawsorts()

    if sortingalg == 'A' and GotIt == False:
        bubblesort2(k, vals)
        alg = "Bubble Sort"
    elif sortingalg == 'B' and GotIt == False:
        insertionsort2(k,vals)
        alg = "Insertion Sort"
    elif sortingalg == 'C' and GotIt == False:
        text = lfont.render("Sorry, doesn't work!", 1, GREEN)
        display.blit(text, (200,5))
        text = frfont.render("Don't really know why... Mergesort step by step doesn't seem to work. The other sorts work though :) Watch the green dance!", 1, GREEN)
        display.blit(text, (170,98))
        vals = msort(k,vals)
        alg = "Merge Sort"
    elif sortingalg == 'D' and GotIt == False:
        stalinsort(k,vals)
        alg = "Stalin Sort"
    if k == ksorted:
        GotIt = True
    elif k!= ksorted and not GotIt:
        comparisons += 1
    

    text = font.render(f'Algorithm: {alg}', 1, GREY)
    display.blit(text, (5,5))
    text = font.render(f'Comparisons: {str(comparisons)}', 1, GREY)
    display.blit(text, (5,25))
    text = font.render(f'Runtime: {str(comparisons/frames)[:5]}s', 1, GREY)
    display.blit(text, (5,45))
    text = frfont.render(f'{str(frames)} FPS', 1, GREY)
    display.blit(text, (5,65))

    pygame.display.flip()
    framerate.tick(frames)

pygame.quit()
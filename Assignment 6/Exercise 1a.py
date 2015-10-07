__author__ = 'elvin'

width = 5
height = 5
answer = ''

for x in range(0,height,1):
    for y in range(0,width,1):
        answer += '*'
    answer += '\n'

print answer
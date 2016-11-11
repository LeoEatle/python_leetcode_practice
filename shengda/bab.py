time = raw_input()
time = int(time)
# list = ['A']
#
# for i in range(time):
#     for element in list:
#         if element == 'A':
#             list.remove('A')
#             list.append('B')
#         if element == 'B':
#             list.append('A')
countA = 1
countB = 0
for i in range(time):
    tempA = countA
    tempB = countB
    countA = tempA - tempA + tempB
    countB = tempB + tempA
print countA, countB
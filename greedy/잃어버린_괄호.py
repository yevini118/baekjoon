plus = input().split('-')

answer = sum(map(int,plus[0].split('+')))
for i in range(1, len(plus)):
    answer -= sum(map(int,plus[i].split('+')))

print(answer)

#최초 답안

# import re

# expression = input()
# nums = list(map(int, re.split('[-+]', expression)))
# operations = re.findall('[-+]', expression)

# new_expression = ''
# sum = nums[0]
# for i in range(len(operations)):

#     if operations[i] == '+':
#         sum += nums[i+1]
#     else:
#         new_expression += str(sum) + '-'
#         sum = nums[i+1]
    
# new_expression += str(sum)

# print(eval(new_expression))

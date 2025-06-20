# define file name
magic8 = '/Users/tiffanynguyen/Documents/8ballresponses.txt'
# verify that the file can be read
try:
    with open(magic8, 'r') as file:
        responses = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print(f'error, file {magic8} not found.')
    exit()
#
# main program
# ask user for input
import random
#
while True:
    input('please ask a (yes/no) question: ')
    answer = random.choice(responses)
    print('magic 8 Ball says:', answer)
    again = input('do you want to ask another question? (yes/no): ')
    if again.lower() not in ['y', 'yes']:
        break
#
print('program ends.')

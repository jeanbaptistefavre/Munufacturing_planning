import os

def save_code_txt():
#Saves all the pythons files in txt
    for element in os.listdir('C:/Users/212471971/Desktop/Manufacturing Planning'):
        if element.endswith('.py'):
            file_1 = open(element, 'r')
            file_2 = open('code txt/' + element[:-3] + '.txt', 'w')
            for line in file_1:
                file_2.write(line)

'''save_code_txt()'''

def save_code_py():
#Saves all the pythons files in txt
    for element in os.listdir('C:/Users/JB/Desktop/Code_Manufacturing_planning'):
        if element.endswith('.txt'):
            file_1 = open(element, 'r')
            file_2 = open(element[:-4] + '.py', 'w')
            for line in file_1:
                file_2.write(line)

save_code_py()

def pointer_1_smaller(pointer_1, pointer_2):
#compares tuple
    if pointer_1[0] > pointer_2[0]:
        return False
    elif pointer_1[0] < pointer_2[0]:
        return True
    else:
        if pointer_1[1] > pointer_2[1]:
            return False
        elif pointer_1[1] < pointer_2[1]:
            return True
        else:
            return True
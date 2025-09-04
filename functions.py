import sys

#Functions
def multiplication(list):
    for index, token in enumerate(list):
        if token == '*':
            product = list[index-1] * list[index+1]
            list[index-1] = product
            print(list[index])
            list.pop(index)
            print("Popped: {list[index]}")
            list.pop(index+1)
            
    return list

def division(list):
    for index, token in enumerate(list):
        if token == '/':
            product = list[index-1] / list[index+2]

def addition(list):
    for index, token in enumerate(list):
        if token == '+':
            product = list[index-1] + list[index+2]

def subtraction(list):
    for index, token in enumerate(list):
        if token == '-':
            product = list[index-1] - list[index+2]





def main():
    
    equation = [-2, 4, 2.4, '*', 10, "/", 2]
    print(equation)

    newList = multiplication(equation)
    print(newList)
    



if __name__ == "__main__":
    main()
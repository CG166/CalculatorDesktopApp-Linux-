import sys

#Functions

def evaluate(list):
    for index, token in enumerate(list):
        if token == '*':
            product = list[index-1] * list[index+1]
            list[index-1] = product
            print(list[index])
            list.pop(index)
            print(list[index])
            list.pop(index)

    for index, token in enumerate(list):
        if token == '/':
            product = list[index-1] / list[index+1]
            list[index-1] = product
            print(list[index])
            list.pop(index)
            print(list[index])
            list.pop(index)

    for index, token in enumerate(list):
        if token == '+':
            product = list[index-1] + list[index+1]
            list[index-1] = product
            print(list[index])
            list.pop(index)
            print(list[index])
            list.pop(index)
    
    for index, token in enumerate(list):
        if token == '-':
            product = list[index-1] - list[index+1]
            list[index-1] = product
            print(list[index])
            list.pop(index)
            print(list[index])
            list.pop(index)

    answer = str(list[0])
            
    return answer


def main():
    
    equation = [-2, '+', 4, '-', 2.4, '*', 10, "/", 2]
    print(equation)

    newList = evaluate(equation)
    print(newList)
    



if __name__ == "__main__":
    main()
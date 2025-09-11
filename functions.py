import sys

#Functions

def evaluate(list):
    for index, token in enumerate(list):
        if token == '*':
            product = list[index-1] * list[index+1]
            #print(list[index-1])
            list[index-1] = product
            #print(" multiplied by ")
            list.pop(index)
            #print(list[index])
            list.pop(index)
            #print(f"The product is: {list[index-1]}\n")
            
    for index, token in enumerate(list):
        if token == '/':
            product = list[index-1] / list[index+1]
            #print(list[index-1])
            list[index-1] = product
            #print(" divided by ")
            list.pop(index)
            #print(list[index])
            list.pop(index)
            #print(f"The product is: {list[index-1]}\n")

    for index, token in enumerate(list):
        if token == '+':
            product = list[index-1] + list[index+1]
            #print(list[index-1])
            list[index-1] = product
            #print(" added to ")
            list.pop(index)
            #print(list[index])
            list.pop(index)
            #print(f"The product is: {list[index-1]}\n")
    
    for index, token in enumerate(list):
        if token == '-':
            product = list[index-1] - list[index+1]
            #print(list[index-1])
            list[index-1] = product
            #print(" subtracted by ")
            list.pop(index)
            #print(list[index])
            list.pop(index)
            #print(f"The product is: {list[index-1]}\n")

    #print(f"Final form of list after all evaluation: {list}")
    #print(list)
    #print(f"Final Answer before string conversion: {list[0]}")
    answer = str(list[0])[:13]
    #print(f"The final answer is: {answer}")
            
    return answer
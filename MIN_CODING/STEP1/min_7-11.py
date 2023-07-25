def input_number():
    num = int(input())
    return num

def process(num):
    result_array = [num + i for i in range(9)]
    return result_array

def output_array(array):
    for i in range(0, len(array), 3): # 0 3 6
        pivot = [str(num) for num in array[i:i+3]]
        print(' '.join(pivot))


num_input = input_number()
result_array = process(num_input)
output_array(result_array)

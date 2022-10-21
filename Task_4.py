# Пари наприклад: 3 + 2 = 5, 2 + 3 = 5 - це одна пара
def finding_pairs_target(list_input, target):
    number_pairs = 0
    for i in range(len(list_input)):
        for j in range(i, len(list_input)):
            if list_input[i] + list_input[j] == target:
                number_pairs += 1
                print(f'a[{i}] + a[{j}] = {list_input[i]} + {list_input[j]} = {target}')
            
    return print(f'count = {number_pairs}')

def main():
    print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], target = 9:")
    finding_pairs_target([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 9)
    print("[3, 4, 56, 3, 4, 0, 12, 43, 6, 7, 8], target = 13:")
    finding_pairs_target([3, 4, 56, 3, 4, 0, 12, 43, 6, 7, 8], 13)
main()             

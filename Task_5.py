def alphabetical_order(string_input):
    
    def sort_surname(input_name):
        return input_name[0]

    def sort_name(input_name):
        return input_name[1]
    
    name = []
    temp = ""
    temp_list = []
    output_list = []
    list_names = string_input.upper().split(';')
    
    for i in range(len(list_names)):
        name.append((list_names[i].split(':')[1],list_names[i].split(':')[0]))
        name.sort(key = sort_surname)

    for i in range(len(name)):
        if name[i][0] != temp:
            temp_list.sort(key = sort_name)
            for t in temp_list:
                output_list.append(t)
                temp_list = []

        temp = name[i][0]        
        temp_list.append(name[i])   

        if i == len(name) - 1:
            temp_list.sort(key = sort_name)
            for j in range(len(temp_list)):
                output_list.append(temp_list[j])
    
    return output_list

def show(list_str):
    for i in list_str:
        print(f'({i[0]}, {i[1]}) ', end='')
def main():
    output = alphabetical_order("Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill")
    show(output)
    
main()
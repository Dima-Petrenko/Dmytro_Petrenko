def first_non_repeating_letter(input_string):
    list_input_string = list(input_string)
    
    def letter_checking(letter):
        return len(list(filter(lambda x: x.lower() == i.lower(), list_input_string))) == 1
            
    for i in list_input_string:
        if  letter_checking(i) == True:
            return i
    
    return ""
        
def main():
    print("Result 'Fdafr':",first_non_repeating_letter("Fdafr"))
    print("Result 'FdDafRar':",first_non_repeating_letter("FdDafRar"))
    print("Result 'STaST':",first_non_repeating_letter("STaST"))
    print("Result 'Teera':",first_non_repeating_letter("Teera"))
main()        
                            
  
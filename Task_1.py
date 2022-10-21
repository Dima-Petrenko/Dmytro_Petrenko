def list_filter(list_unfiltered):
    list_filtered = list(filter(lambda x: type(x) == int, list_unfiltered))
    return list_filtered
def main():
    print(list_filter([1, 2, 'a', 'b']))
    print(list_filter([1, 'a', 'b', 0, 15]))
    print(list_filter([1, 2, 'aasf', '1', '123', 123]))
main()
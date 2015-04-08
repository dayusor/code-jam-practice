def get_struct_from_file(file_name):
    """ Get struct from the file as follow:
        [
        [3, [1, 2, 3], [4, 5, 6]], ..., [2, [1, 2,], [1, 2]]
        ]
    """
    with open(file_name, 'r') as fh:
        file_list = fh.readlines()

    # lets remove newline character for each element
    file_list = [file_list[i].strip() for i in range(len(file_list))]

    # get the number of tests
    T = int(file_list.pop(0))

    main_list = []
    main_list = [[int(file_list[i])] for i in range(0, len(file_list), 3)]
    counter = 0
    for i in range(0, len(file_list), 3):
        main_list[counter].append(sorted([int(i) for i in (file_list[i + 1]).split()]))
        main_list[counter].append(sorted([int(i) for i in (file_list[i + 2]).split()], reverse=True))
        counter += 1
    return main_list




main_list = get_struct_from_file('A-large-practice.in')
#for i in main_list:
counter = 1
for i in main_list:
    total_sum = 0
    for j in range(i[0]):
        total_sum += i[1][j]*i[2][j]
    print('Case #{}: {}'.format(counter, total_sum))
    counter += 1

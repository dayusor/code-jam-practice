import sys
sys.setrecursionlimit(1500)

def build_structure(file_path):
    with open(file_path, 'r') as fh:
        lines = fh.readlines()

    N = int(lines.pop(0))
    S = int(lines.pop(0))
    final_list = []
    each_case_list = []
    aux_list = []
    counter = -1

    for i in range(0, len(lines) + 1):
        counter += 1
        if i < len(lines):
            if counter != S:
                aux_list.append(lines[i].strip())
            else:
                S = int(lines[i].strip())
                each_case_list.append(aux_list)
                aux_list = []
                counter = -1
                if len(each_case_list) == 2:
                    final_list.append(each_case_list)
                    each_case_list = []
                    each_case_counter = 0
        else:
            each_case_list.append(aux_list)
            final_list.append(each_case_list)

    return N, final_list

def spit_switch_times(each_case_list, current_switch_times=0, biggest_one=0):
    indexes_list = []
    for j in range(0, len(each_case_list[0])):
        try:
            indexes_list.append(each_case_list[1].index(each_case_list[0][j]))
        except ValueError:
            return current_switch_times

    biggest_one = max(indexes_list)
    current_switch_times += 1
    each_case_list[1] = each_case_list[1][biggest_one:]
    return spit_switch_times(each_case_list, current_switch_times, biggest_one)

N, struct = build_structure('A-large-practice.in')
for i in range(0, N):
    print('Case #{}: {}'.format(i+1, spit_switch_times(struct[i])))

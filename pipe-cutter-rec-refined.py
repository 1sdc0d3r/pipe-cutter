# pipe_cuts = [3, 3, 3, 3, 3, 5, 5, 5, 7, 7, 7, 7, 13, 13, 15, 15]
from time import clock_getres


pipe_cuts_dict = {3: 5, 5: 3, 7: 4, 13: 2, 15: 2}


# extract all cuts into a list
def get_cuts(pipe_cuts_dic):
    needed_cuts = []
    for pipe in pipe_cuts_dic:
        for i in range(pipe_cuts_dic[pipe]):
            needed_cuts.append(pipe)
            pipe_cuts_dic[pipe] -= 1
    return set(needed_cuts)


pipe_cuts = get_cuts(dict(pipe_cuts_dict))


def combination_rec(target, current_sum, start, output, result):
    if current_sum == target:
        output.append(result.copy())

    for i in pipe_cuts:
        temp_sum = current_sum + i
        if temp_sum <= target:
            result.append(i)
            combination_rec(target, temp_sum, i, output, result)
            result.pop()
        else:
            return


def combination(target):
    output = []
    result = []
    combination_rec(target, 0, 1, output, result)

    output_reduced = []
    for x in output:
        list.sort(x)
        if x not in output_reduced:
            output_reduced.append(x)

    return output_reduced


# res1 = combination(10)
# print(res1)
res2 = combination(20)
# print(res2)


def valid_combo_reducer(pipe_cuts_dict, pipe_cuts_com):
    for combo in pipe_cuts_com:
        cuts_copy = pipe_cuts_dict.copy()
        for x in combo:
            if cuts_copy[x] - 1 > 0:
                cuts_copy[x] -= 1
            else:
                pipe_cuts_com.remove(combo)
                break
    return pipe_cuts_com


valid_combos = valid_combo_reducer(pipe_cuts_dict, res2)


def leftover_pipe():
    cuts_copy = pipe_cuts_dict.copy()
    for combo in valid_combos:
        for x in combo:
            if cuts_copy[x] - 1 > 0:
                cuts_copy[x] -= 1
            else:
                # recursive go through each list for least pipe leftover
                print(False)


leftover_pipe()

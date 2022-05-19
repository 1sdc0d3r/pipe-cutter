# pipe_cuts = [3, 3, 3, 3, 3, 5, 5, 5, 7, 7, 7, 7, 13, 13, 15, 15]

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
print("pipe cuts: ", pipe_cuts)

all_combos = []


def all_perfect_combination_rec(target, current_sum, start, output, result):
    if current_sum == target:
        output.append(result.copy())

    for i in pipe_cuts:
        temp_sum = current_sum + i
        if temp_sum <= target:
            result.append(i)
            all_perfect_combination_rec(target, temp_sum, i, output, result)
            # !!!!!!!!!!!!!!! This is not needed for perfect_combo_rec
            # print(result)  # This result variable is all possible combinations
            # print("TEST", [x for x in result])
            # result.sort()
            result_copy = result.copy()
            result_copy.sort()

            if result_copy not in all_combos:
                all_combos.append(result_copy)
            # !!!!!!!!!!!!!!!!

            result.pop()
        else:
            return


# * sort function here then reduce, faster than sorting in every recursion
def all_perfect_comb_reduced(target):
    output = []
    result = []
    all_perfect_combination_rec(target, 0, 1, output, result)
    # print("PERFECT OUTPUT", output)
    output_reduced = []
    # output_reduced_comp = [x for x in output if x not in output_reduced_comp]

    for x in output:
        list.sort(x)
        if x not in output_reduced:
            output_reduced.append(x)

    return output_reduced


# res1 = all_perfect_comb_reduced(10)
# print(res1)
res2 = all_perfect_comb_reduced(20)
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
# print("valid combos:", valid_combos)


#!!!!!!!!!!
all_combos.sort()  # * Human view -- Dupes/No-Dupes: 131/41 combos
# print(f"ALL: {all_combos} - len: {len(all_combos)}")
all_valid_combos = valid_combo_reducer(
    pipe_cuts_dict, all_combos)  # * 37 valid combos
print(all_valid_combos)
#!!!!!!!!!!

# From the all_valid_combos can I find combos with least amount of waste. See what combos of combos would result in the min amount of pipe?


def leftover_pipe():
    cuts_copy = pipe_cuts_dict.copy()
    for combo in valid_combos:
        for x in combo:
            if cuts_copy[x] - 1 > 0:
                cuts_copy[x] -= 1
            else:
                # recursive go through each list for least pipe leftover
                # print(False)
                pass  # ! temp pass


leftover_pipe()

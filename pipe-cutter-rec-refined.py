# todo valid_combo_reducer -> check max number of cuts allowed for tolerance
# multiple pipe lengths available (run combination's on each and put together)

# pipe_cuts = [3, 3, 3, 3, 3, 5, 5, 5, 7, 7, 7, 7, 13, 13, 15, 15]

pipe_cuts_dict = {3: 5, 5: 3, 7: 4, 13: 2, 15: 2}
full_pipe_length = 20
# * With multiple lengths find all combos that can work for either one, combine them, remove duplicates, then find combo of combos


#! extract all cuts from dict into a list
def get_cuts(pipe_cuts_dic):
    needed_cuts = []
    for pipe in pipe_cuts_dic:
        for i in range(pipe_cuts_dic[pipe]):
            needed_cuts.append(pipe)
            pipe_cuts_dic[pipe] -= 1
    return needed_cuts


pipe_cuts = get_cuts(dict(pipe_cuts_dict))
# print("pipe cuts: ", pipe_cuts)

all_combos = []


def find_combinations_rec(target, current_sum, start, output, result):
    # if current_sum == target: #* Perfect combos only -> append to output

    if len(result.copy()):  # * This is needed for first recursion only []
        output.append(result.copy())

    for i in pipe_cuts:
        temp_sum = current_sum + i
        if temp_sum <= target:
            result.append(i)
            find_combinations_rec(target, temp_sum, i, output, result)
            result.pop()
        else:
            return


#! Attempting to modulize to separate functionality
# def get_all_combinations(target):
#     output = []
#     result = []
#     find_combinations_rec(target, 0, 1, output, result)
#     return len(output)


# print(get_all_combinations(full_pipe_length))


# * sort function here then reduce, faster than sorting in every recursion
def all_combinations_reduced(target):
    output = []
    result = []
    find_combinations_rec(target, 0, 1, output, result)
    output_reduced = []
    # output_reduced_computation = [x for x in output if x not in output_reduced_computation]

    for x in output:
        list.sort(x)
        if x not in output_reduced:
            output_reduced.append(x)

    print(len(output_reduced))
    return output_reduced


res2 = all_combinations_reduced(full_pipe_length)
# print(res2)


def valid_combo_reducer(pipe_cuts_dict, pipe_cuts_com):
    for combo in pipe_cuts_com:
        cuts_copy = pipe_cuts_dict.copy()
        for x in combo:
            if cuts_copy[x] > 0:
                cuts_copy[x] -= 1
            else:
                pipe_cuts_com.remove(combo)
                break
    return pipe_cuts_com


valid_combos = valid_combo_reducer(pipe_cuts_dict, res2)
# print("valid combos:", valid_combos, f'Len: {len(valid_combos)}')


#!!!!!!!!!!
all_combos.sort()  # * Human view -- Dupes/No-Dupes: 131/40 combos
# print(f"ALL: {all_combos} - len: {len(all_combos)}")
all_valid_combos = valid_combo_reducer(
    pipe_cuts_dict, all_combos)  # * 37 valid combos
# print(all_valid_combos, f'ALL: {len(all_valid_combos)}')
#!!!!!!!!!!

# From the all_valid_combos can I find combos with least amount of waste. See what combos of combos would result in the min amount of pipe?


def leftover_pipe_length(combo_list):
    cut_dict = pipe_cuts_dict.copy()

    for combo in combo_list:
        for x in combo:
            if cut_dict[x] > 0:
                cut_dict[x] -= 1
            else:
                # just in case a invalid combo gets sent in - bugs happen (do I need to return if a combo doesn't work? validator should have caught it if not)
                pass
    return sum(get_cuts(cut_dict))

# remove all cuts in combos from dictionary copy
# use sum(getCuts())


# leftover_pipe_length([[3, 3, 3], [3, 3, 3, 3, 3, 5, 15]]) # 79"


# use perfect combo's first?
# filter combos based on leftover cuts?
# separate smaller functions then put into one larger one to run
# brute force all combos

# * check to see if combo is still valid with leftover cuts (sub-function)
def combo_still_valid(cut_dict, combo):
    cut_dict_copy = cut_dict.copy()
    for cut in combo:
        if cut_dict_copy[cut] > 0:
            cut_dict_copy[cut] -= 1
        else:
            return False
    return True

# * check leftover pipe length from list of combos


def find_best_combo_of_combos(cut_dict, combo_list):
    lowest_combo_list = []
    lowest_pipe_length = None

    cur_pipe_cuts_needed = cut_dict.copy()
    cur_combo_list = []

    for combo in combo_list:
        if not combo_still_valid(cur_pipe_cuts_needed, combo):
            pass


# check combo if still valid
# add combo to cur_combo_list
# remove cuts in combo1 from pipe_cuts_needed
# check cur_pipe_cuts_needed for any cuts left
    # if so repeat check-add-remove
    # if not check leftover_pipe_length()
        # if new length < lowest_pipe_length
            # lowest_combo_list becomes cur_combo_list
            # set lowest_pipe_length


# what about combo1 maxing out, then combo 2 until 0 cuts needed left, then pop off last one and find next combo then pop 2 off all the way to empty then start on combo2 maxing out??


find_best_combo_of_combos(pipe_cuts_dict, all_valid_combos)

# combo_matrix [[[3, 3, 3, 3, 3], [5, 5, 5]...],[3, 3, 3, 3, 5], [3, 5, 5]...]]
# [[combo1, combo1, combo2], [combo1, combo2, combo7]]
# check each combo-list for leftover cuts. If one is found replace lowest combo variable. Is matrix needed then? check each combo of combos for leftover pipe

# recursive find_best_combo_of_combos?

# variable pipe lengths? black iron milled 18-22ft


# def find_combinations_rec(target, current_sum, start, output, result):
#     if current_sum == target:
#         output.append(result.copy())

#     for i in pipe_cuts:
#         temp_sum = current_sum + i
#         if temp_sum <= target:
#             result.append(i)
#             find_combinations_rec(target, temp_sum, i, output, result)
#             # !!!!!!!!!!!!!!! This is not needed for perfect_combo_rec
#             # print(result)  # This result variable is all possible combinations
#             # print("TEST", [x for x in result])
#             # result.sort()
#             result_copy = result.copy()
#             result_copy.sort()

#             if result_copy not in all_combos:
#                 all_combos.append(result_copy)
#             # !!!!!!!!!!!!!!!!

#             result.pop()
#         else:
#             return

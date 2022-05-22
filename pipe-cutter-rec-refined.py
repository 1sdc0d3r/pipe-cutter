from ast import comprehension
from time import time
# todo valid_combo_reducer -> check max number of cuts allowed for tolerance
# multiple pipe lengths available (run combination's on each and put together)

# pipe_cuts = [3, 3, 3, 3, 3, 5, 5, 5, 7, 7, 7, 7, 13, 13, 15, 15]

pipe_cuts_dict = {3: 5, 5: 3, 7: 4, 13: 2, 15: 2}
cur_full_pipe_length = 20
# * With multiple lengths find all combos that can work for either one, combine them, remove duplicates, then find combo of combos


#! extract all cuts from dict into a list
def get_cuts(pipe_cuts_dic): return [
    pipe for pipe in pipe_cuts_dic for i in range(pipe_cuts_dic[pipe])]
# needed_cuts = []
# for pipe in pipe_cuts_dic:
#     for i in range(pipe_cuts_dic[pipe]):
#         needed_cuts.append(pipe)
# return needed_cuts


pipe_cuts = get_cuts(pipe_cuts_dict)
# print("pipe cuts: ", pipe_cuts)


rec_result = []  # used for recursion
rec_combos = []  # All combos


def find_combinations_rec(target, current_sum, start, output, result=[]):
    # if current_sum == target: #* Perfect combos only -> append to output

    # * DRY and runs once
    sorted_result = sorted(result)
    if len(result) and sorted_result not in output:
        output.append(sorted_result)

    for i in pipe_cuts:
        temp_sum = current_sum + i
        if temp_sum <= target:
            result.append(i)
            find_combinations_rec(target, temp_sum, i, output, result)
            result.pop()
        else:
            return


find_combinations_rec(cur_full_pipe_length, 0, 1, rec_combos, rec_result)
# print(f'Total: {len(rec_combos)}')


#! Filter combos that would not work based on cuts needed
def valid_combo_reducer(pipe_cuts_dict, cut_combos):
    for combo in cut_combos:
        cuts_copy = pipe_cuts_dict.copy()
        for x in combo:
            if cuts_copy[x] > 0:
                cuts_copy[x] -= 1
            else:
                cut_combos.remove(combo)
                break
    return cut_combos


valid_combos = valid_combo_reducer(pipe_cuts_dict, rec_combos)
# print(f'Valid: {len(valid_combos)}')


def leftover_dict_length(cut_dic, combo_list):
    cut_dict = cut_dic.copy()

    for combo in combo_list:
        for x in combo:
            if cut_dict[x] > 0:
                cut_dict[x] -= 1
            else:
                # just in case a invalid combo gets sent in - bugs happen (do I need to return if a combo doesn't work? validator should have caught it if not)
                pass

    return sum(get_cuts(cut_dict))


def combos_list_leftover_pipe(combo_list):
    leftover_pipe = 0
    for combo in combo_list:
        leftover_pipe += (cur_full_pipe_length - sum(combo))
    return leftover_pipe


# print(combos_list_leftover_pipe([[3], [3], [3], [3], [3], [5],
#                            [5], [5], [7], [7], [7], [7], [13], [13], [15], [15]]))  # 206


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


def find_best_combo_of_combos(cut_dict, combo_list):
    lowest_combo_list = []
    lowest_pipe_length = None

    cur_pipe_cuts_dict = cut_dict.copy()
    cur_combo_list = []
    cur_combo_index = 0
    # cur_combo = []

    for i in range(len(combo_list)):
        cur_combo_index += i
        # while(leftover_dict_length(cur_combo_list) - combos_list_leftover_pipe(cur_combo_list)):  # this works...kinda
        while True:
            # print(lowest_pipe_length)
            # print(cur_combo_list)
            if combo_still_valid(
                    cur_pipe_cuts_dict, combo_list[cur_combo_index]):
                # print(f'valid: {combo_list[cur_combo_index]}')
                cur_combo_list.append(combo_list[cur_combo_index])
                for cut in combo_list[cur_combo_index]:
                    if cur_pipe_cuts_dict[cut] > 0:
                        cur_pipe_cuts_dict[cut] -= 1
            elif cur_combo_index+1 < len(combo_list):
                cur_combo_index += 1
            else:  # does this need to be outside the while loop?
                cur_leftover_pipe = combos_list_leftover_pipe(
                    cur_combo_list)
                cut_dict_empty = leftover_dict_length(
                    cur_pipe_cuts_dict, cur_combo_list) == 0
                # print("cur", cur_combo_list)
                if lowest_pipe_length == None or cur_leftover_pipe < lowest_pipe_length and cut_dict_empty:
                    lowest_pipe_length = cur_leftover_pipe
                    lowest_combo_list = cur_combo_list
                cur_combo_index = 0
                cur_combo_list = []
                cur_pipe_cuts_dict = cut_dict.copy()
                break  # * out of while loop

    # print("needed", cur_pipe_cuts_dict)
    print(f'low_combo: {lowest_combo_list} low_length: {lowest_pipe_length}')


find_best_combo_of_combos(pipe_cuts_dict, valid_combos)

# check combo if still valid
# add combo to cur_combo_list
# remove cuts in combo1 from pipe_cuts_needed
# check cur_pipe_cuts_dict for any cuts left
# if so repeat check-add-remove
# if not check leftover_dict_length()
# if new length < lowest_pipe_length
# lowest_combo_list becomes cur_combo_list
# set lowest_pipe_length

# what about combo1 maxing out, then combo 2 until 0 cuts needed left, then pop off last one and find next combo then pop 2 off all the way to empty then start on combo2 maxing out??

# find_best_combo_of_combos(pipe_cuts_dict, all_valid_combos)

#! Don't need to do combo_matrix, just check each combo
# combo_matrix [[[3, 3, 3, 3, 3], [5, 5, 5]...],[3, 3, 3, 3, 5], [3, 5, 5]...]]
# [[combo1, combo1, combo2], [combo1, combo2, combo7]]
# check each combo-list for leftover cuts. If one is found replace lowest combo variable. Is matrix needed then? check each combo of combos for leftover pipe

# recursive find_best_combo_of_combos?

# function to remove cuts from dict? DRY

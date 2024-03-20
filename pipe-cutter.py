import time
import functools
start_time = time.time()
# todo validate_combo -> check max number of cuts allowed for tolerance
# multiple pipe lengths available (run combination's on each and put together)

test_dict1 = {3: 5, 5: 4, 7: 4, 13: 2, 15: 2} # 21
test_dict2 = {3: 15, 5: 20, 7: 22, 13: 20, 15: 8}  # total:
test_dict3 = {3: 5, 5: 4, 7: 3, 13: 2, 15: 1}  # total: 40 - 3

pipe_cuts_dict = test_dict1
cur_full_pipe_length = 15
# * With multiple lengths find all combos that can work for either one, combine them, remove duplicates, then find combo of combos


#! extract all cuts from dict into a list
def extract_cuts_list(pipe_cuts_dic): return [
    pipe for pipe in pipe_cuts_dic for i in range(pipe_cuts_dic[pipe])]


#! Validates combo based on cuts cuts in a dictionary
def validate_combo(cut_dict, combo):
    cuts_copy = cut_dict.copy()
    for cut in combo:
        if cuts_copy[cut] > 0:
            cuts_copy[cut] -= 1
        else:
            return False
    return True


def dict_empty(cut_dic, combo_list):
    cut_dict = cut_dic.copy()

    for combo in combo_list:
        # print(combo)
        for cut in combo:
            if cut_dict[cut] > 0:
                cut_dict[cut] -= 1
            # else statement just in case a invalid combo gets sent in - bugs happen (do I need to return if a combo doesn't work? validator should have caught it if not)

    return sum(extract_cuts_list(cut_dict)) == 0


def combos_leftover_pipe(combo_list):
    leftover_pipe = 0
    for combo in combo_list:
        leftover_pipe += (cur_full_pipe_length - sum(combo))
    return leftover_pipe


# rec_result = []  # used for recursion
rec_combos = []  # All combos
perfect_combos = [] # Perfect cut combos

extracted_cuts_list = extract_cuts_list(pipe_cuts_dict)

key_cuts = pipe_cuts_dict.keys()

def find_combinations_rec(target, current_sum, output, result=[]):
    # * sorted function - DRY and runs once per recursion
    sorted_result = sorted(result)
    # print(sorted_result)
    # * checks if combo is valid and not in output
    if validate_combo(pipe_cuts_dict, result):
        output.append(sorted_result)

        #* Perfect combos only -> append to output
        if current_sum == target: perfect_combos.append(sorted_result);

    for cut in key_cuts:
        temp_sum = current_sum + cut

        if temp_sum <= target:
            result.append(cut)
            if(sorted(result) not in output):
                find_combinations_rec(target, temp_sum, output, result)
            result.pop()
        else:
            return


find_combinations_rec(cur_full_pipe_length, 0, rec_combos)
print(f'Total: {len(rec_combos)}')
# print(rec_combos)
# print(perfect_combos)


#! low_combo is filling up with smaller combos then not allowing the next combos in.
# ? matrix of combos
def find_best_combo_of_combos(cut_dict, combo_list):
    lowest_combo_list = []
    lowest_pipe_length = None

    cur_pipe_cuts_dict = cut_dict.copy()
    cur_combo = []
    cur_combo_list = []
    cur_combo_index = 0
    # cur_combo_index_modifier = 0
    cur_leftover_pipe = 0

    for i in range(len(combo_list)):
        cur_combo_index += i
        # print(i)
        # cur_combo_index_modifier += 1
        # print(i, cur_combo_index_modifier)
        # cur_leftover_pipe = 0
        while True:
            cur_combo = combo_list[cur_combo_index]
            # print(cur_combo)
            # print(cur_combo_list)
            if validate_combo(
                    cur_pipe_cuts_dict, cur_combo):
                cur_combo_list.append(cur_combo)
                cur_leftover_pipe += (cur_full_pipe_length-sum(cur_combo))

                for cut in cur_combo:
                    # ? Do I need this 'if' if combo's are already validated
                    if cur_pipe_cuts_dict[cut] > 0:
                        cur_pipe_cuts_dict[cut] -= 1

            elif cur_combo_index+1 < len(combo_list):
                cur_combo_index += 1

            else:  # ? does this need to be outside the while loop?
                if (lowest_pipe_length == None or cur_leftover_pipe < lowest_pipe_length) and dict_empty(
                        cur_pipe_cuts_dict, cur_combo_list):
                    lowest_pipe_length = cur_leftover_pipe
                    lowest_combo_list = cur_combo_list
                cur_combo_index = 0
                cur_combo_list = []
                cur_leftover_pipe = 0
                cur_pipe_cuts_dict = cut_dict.copy()
                break  # * While loop

    # print("needed", cur_pipe_cuts_dict)
    # print(f'low_combo: {lowest_combo_list} low_length: {lowest_pipe_length}')
    # print(pipe_cuts_dict)


# find_best_combo_of_combos(pipe_cuts_dict, rec_combos)

# check combo if still valid
# add combo to cur_combo_list
# remove cuts in combo1 from pipe_cuts_needed
# check cur_pipe_cuts_dict for any cuts left
# if so repeat check-add-remove
# if not check dict_empty()
# if new length < lowest_pipe_length
# lowest_combo_list becomes cur_combo_list
# set lowest_pipe_length

# what about combo1 maxing out, then combo 2 until 0 cuts needed left, then pop off last one and find next combo then pop 2 off all the way to empty then start on combo2 maxing out??

#! Don't need to do combo_matrix, just check each combo against lowest combo
# combo_matrix [[[3, 3, 3, 3, 3], [5, 5, 5]...],[3, 3, 3, 3, 5], [3, 5, 5]...]]
# [[combo1, combo1, combo2], [combo1, combo2, combo7]]
# check each combo-list for leftover cuts. If one is found replace lowest combo variable. Is matrix needed then? check each combo of combos for leftover pipe

# recursive find_best_combo_of_combos?

# function to remove cuts from dict? DRY


# use a node tree to map out all possible combinations then do searches on the tree to determine if it has a low amount oy waste. GONNA GIVE IT A TRY - dont do that, use the node tree to optimize getting cuts and combos maybe
# print(perfect_combos)

def best_combo_of_combos(cut_dict, combo_list):
    lowest_combo_list = []
    lowest_pipe_length = None
    start_index=0
    # start_index=rec_combos.index(perfect_combos[0])

    def rec_combo(cur_pipe_cuts_dict=cut_dict, cur_combo_list=[], cur_combo_index=start_index):
        nonlocal lowest_pipe_length, lowest_combo_list
        cur_leftover_pipe = None
        print(cur_combo_list)
        # print(sum(extract_cuts_list(cur_pipe_cuts_dict)))
        if (sum(extract_cuts_list(cur_pipe_cuts_dict)) == 0): #empty dict
            cur_leftover_pipe = combos_leftover_pipe(cur_combo_list)
            if lowest_pipe_length is None or cur_leftover_pipe < lowest_pipe_length:
                lowest_pipe_length=cur_leftover_pipe;
                lowest_combo_list = cur_combo_list.copy()
                # print("update:", lowest_pipe_length)
                return
        if cur_combo_index == len(combo_list): 
            # print("max")
            return

        cur_combo = combo_list[cur_combo_index]
        # print("combo:",cur_combo)
        if validate_combo(cur_pipe_cuts_dict, cur_combo):
            cur_combo_list.append(cur_combo)
            for cut in cur_combo:
                cur_pipe_cuts_dict[cut] -= 1

            rec_combo(cur_pipe_cuts_dict, cur_combo_list, cur_combo_index+1)

            for cut in cur_combo:
                cur_pipe_cuts_dict[cut] += 1
            cur_combo_list.pop()


        rec_combo(cur_pipe_cuts_dict, cur_combo_list, cur_combo_index+1)

        # else:
            # rec_combo(cur_pipe_cuts_dict, cur_combo_list,cur_combo_index)
        #     # cur_combo_index += 1
        # rec_combo(cur_pipe_cuts_dict, cur_combo_list,cur_combo_index+1)



    rec_combo()
    print("lowest list:", lowest_combo_list, lowest_pipe_length)
    # return( lowest_combo_list, lowest_pipe_length)
    # print(lowest_pipe_length)

# rec_combos.reverse()
best_combo_of_combos(pipe_cuts_dict, rec_combos);
# avgTime = 0
# for i in range(5):
    # avgTime+=time.time() - start_time

# print(avgTime/5)

# what about using a dict for each combo and store the value as the leftover pipe from that combo
print(time.time()-start_time)

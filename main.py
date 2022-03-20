
# Online Python - IDE, Editor, Compiler, Interpreter
pipe_cuts = {3: 5, 5: 3, 7: 4, 13: 2, 15: 2}


def cutter():
    pipe_length_standard = 20
    pipes_required = 0
    cur_pipe_length = 20
    leftover_pipe = 0
    combinations = []
    cur_cuts = []
    needed_cuts = get_cuts(pipe_cuts)

    # find all cut combinations that add up to pipe_length_standard.
    # would it be best to match all perfect cuts then mix/match rest?

    # for pipe1 in pipe_cuts: #matches all perfect cuts
    #     for pipe2 in pipe_cuts:
    # if pipe1+pipe2 == pipe_length_standard and pipe1 is not pipe2:
    #     pipes_required+=1
    #     pipe_cuts[pipe1] -= 1
    #     pipe_cuts[pipe2] -= 1
    #     combinations.append([pipe, pipe2])

    # cur_cuts=[]
    # for pipe in pipe_cuts: #leftover cuts to split
    #     while pipe_cuts[pipe] > 0:
    #         if cur_pipe_length - pipe >= 0:
    #             cur_pipe_length = cur_pipe_length - pipe
    #             pipe_cuts[pipe]-=1
    #             cur_cuts.append(pipe)
    #             print("cur", cur_cuts)

    #         else:
    #             print("else")
    #             leftover_pipe+=cur_pipe_length
    #             cur_pipe_length = pipe_length_standard
    #             pipes_required+=1
    #             cur_cuts.append(leftover_pipe)
    #             # combinations.append(cur_cuts)

    return f"pipes:{pipes_required}, leftover:{leftover_pipe}, cuts_required:{pipe_cuts}, combo:{combinations}"


# print(cutter())

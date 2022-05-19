
# Online Python - IDE, Editor, Compiler, Interpreter
pipe_cuts = {3.75: 5, 5: 3, 7: 4, 13: 2, 15: 2}


def cutter():
    pipe_length_standard = 20
    pipes_required = 0
    cur_pipe_length = 20
    leftover_pipe = 0
    combinations = {}
    for pipe in pipe_cuts:  # pipe = length of pipe required
        for pipe2 in pipe_cuts:
            while pipe_cuts[pipe] > 0:
                print(pipe_cuts[pipe])
                if pipe+pipe2 == pipe_length_standard:
                    pipes_required += 1
                    pipe_cuts[pipe] -= 1
                    pipe_cuts[pipe2] -= 1

            # while pipe_cuts[pipe] > 0:
            #     if cur_pipe_length - pipe >= 0:
            #         cur_pipe_length = cur_pipe_length - pipe
            #         pipe_cuts[pipe]-=1

            #     else:
            #         leftover_pipe+=cur_pipe_length
            #         cur_pipe_length = pipe_length_standard
            #         pipes_required+=1

    return f"pipes:{pipes_required}, leftover:{leftover_pipe}, cuts_required:{pipe_cuts}"


print(cutter())

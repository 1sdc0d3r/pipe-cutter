const test_data = {
    small: {
        3: 5,
        5: 4,
        7: 4,
        13: 2,
        15: 2
    },
    large: {
        3: 15,
        5: 20,
        7: 22,
        13: 20,
        15: 12
    }
}

const pipe_cuts_obj = test_data['small'];
const cur_full_pipe_length = 20;

function extract_cuts_arr(pipe_cuts) {
    const extracted_cuts = []
    for (key in pipe_cuts) {
        for (let i = 0; i < pipe_cuts[key]; i++) {
            extracted_cuts.push(parseInt(key))
        }
    }
    return extracted_cuts
}

// function decrement_pipe_cuts(combo) {
//* DRY OUT
// }
//! Validates combo based on cuts cuts in a object
function validate_combo(pipe_cuts_obj, combo) {
    pipe_cuts = {
        ...pipe_cuts_obj
    }
    for (let i = 0; i < combo.length; i++) {
        if (pipe_cuts[combo[i]] > 0) {
            pipe_cuts[combo[i]] -= 1
        } else return false;
    }
    return true
}
// console.log((validate_combo(pipe_cuts_obj, [13, 13])))

function check_obj_empty(pipe_cuts_obj, combo_list) {
    pipe_cuts = {
        ...pipe_cuts_obj
    }
    for (let i = 0; i < combo_list.length; i++) {
        const cur_combo = combo_list[i]
        for (let j = 0; j < cur_combo.length; j++) {
            const cur_cut = cur_combo[j]
            if (cur_cut > 0) {
                pipe_cuts[cur_cut] -= 1
            }
        }
    }
    return extract_cuts_arr(pipe_cuts).reduce((prev, cur) => prev += cur) === 0
}

const rec_result = [] //* used for recursion
const rec_combos = [] //* All combos
const cut_arr = extract_cuts_arr(pipe_cuts_obj);

function find_combinations_rec(target, cur_sum, start, output, result) {
    result.sort((a, b) => a - b);
    // console.log(output)
    // console.log(output.includes(result))
    // console.log(output, result)
    // console.log(validate_combo(pipe_cuts_obj, result))
    // console.log((result.length && !output.includes(result) && validate_combo(pipe_cuts_obj, result)))
    if (result.length && !output.includes(result) && validate_combo(pipe_cuts_obj, result)) {
        //! output here is being set to result and not result not getting pushed in
        output.push(result)
    }

    for (let i = 0; i < cut_arr.length; i++) {
        const cut = cut_arr[i];
        const temp_sum = cur_sum + cut;
        if (temp_sum <= target) {
            console.log(result)
            result.push(cut);
            // console.log(output, result)
            find_combinations_rec(target, temp_sum, cut, output, result)
            result.pop()
        } else return;
    }
}

find_combinations_rec(cur_full_pipe_length, 0, 1, rec_combos, rec_result)
console.log(rec_combos)
//! THIS FUNCTION ISN"T WORKING YET

/*
Probability problem

find all possible cuts

find out how much waste for each combo

compare the highest amount of least waste to total cuts needed ratio of each

find out which ratio will leave least amount of pipe length leftover

recursion with possible cut ratios of leftover cuts



FULL -- What if you only took the combo of combos using only the least amount of pipe leftover then fill in the rest with combos left over
*/
const test_dict1 = {
    3: 5,
    5: 4,
    7: 4,
    13: 2,
    15: 2
}
const test_dict2 = {
    3: 15,
    5: 20,
    7: 22,
    13: 20,
    15: 8
}

const test_dict3 = {
    3: 5,
    5: 4,
    7: 3,
    13: 2,
    15: 1
}

//* mock data from find_combinations_rec;
const possible_combos = [
    [3],
    [3, 3],
    [3, 3, 3],
    [3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 5],
    [3, 3, 3, 3, 5],
    [3, 3, 3, 3, 7],
    [3, 3, 3, 5],
    [3, 3, 3, 5, 5],
    [3, 3, 3, 7],
    [3, 3, 5],
    [3, 3, 5, 5],
    [3, 3, 5, 7],
    [3, 3, 7],
    [3, 3, 7, 7],
    [3, 3, 13],
    [3, 5],
    [3, 5, 5],
    [3, 5, 5, 5],
    [3, 5, 5, 7],
    [3, 5, 7],
    [3, 7],
    [3, 7, 7],
    [3, 13],
    [3, 15],
    [5],
    [5, 5],
    [5, 5, 5],
    [5, 5, 5, 5],
    [5, 5, 7],
    [5, 7],
    [5, 7, 7],
    [5, 13],
    [5, 15],
    [7],
    [7, 7],
    [7, 13],
    [13],
    [15]
]
// possible_combos.sort((a, b) => )

cur_full_pipe_length = 20
cut_dict = test_dict3


const extracted_cuts = extract_pipe_cuts(cut_dict)
// console.log(extracted_cuts)

function extract_pipe_cuts(cut_dict) {
    let cuts = [];
    const keys = Object.keys(cut_dict)

    for (let i = 0; i < keys.length; i++) {
        const key = keys[i];
        for (let i = 0; i < cut_dict[key]; i++) cuts.push(key)
    }

    return cuts
}

function validate_combo(combo, cuts = extract_pipe_cuts(cut_dict)) {
    for (let i = 0; i < combo.length; i++) {
        const cut = combo[i];
        if (cuts[cut] > 0) {
            cuts[cut] -= 1;
        } else return false
    }
    return true
}

const rec_result = [] // used for recursion
const rec_combos = [] // All combos

//! Recursion not functioning properly
function find_combinations_rec(target_sum, current_sum, result, output) {
    result.sort();
    console.log({
        current_sum,
        result,
        output,
    })
    console.log("result length", result.length)

    if (result.length && !output.includes(result) && validate_combo(result)) {
        output.push(result)
        console.log("NEW", result)
    }

    for (let i = 0; i < extracted_cuts.length; i++) {
        const cut = parseInt(extracted_cuts[i])
        current_sum = parseInt(current_sum) + parseInt(cut);
        console.log("Loop", i, {
            cut,
            current_sum
        })
        if (current_sum <= target_sum) {
            result.push(cut)
            console.log("RECURSION")
            find_combinations_rec(target_sum, current_sum, result, output)
        } else break
    }
}

// find_combinations_rec(cur_full_pipe_length, 0, rec_result, rec_combos)
// console.log(rec_combos, rec_combos.length)

function find_combo_leftover_pipe(combo) {
    return cur_full_pipe_length - combo.reduce((prev, cur) => prev + cur)
}

possible_combos.sort((a, b) => find_combo_leftover_pipe(a) - find_combo_leftover_pipe(b))

console.log(possible_combos)

function sort_combos_by_leftover_pipe(combo_list) {
    const sorted_list = {}
    for (let i = 0; i < combo_list.length; i++) {
        combo_list[i]
    }
}

// function find_combo_to_cuts_ratio(combo) {

// }

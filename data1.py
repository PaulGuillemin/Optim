import numpy as np

machines = {
    0: [3973, 5354, 3591, 4320],
    1: [3213, 4634, 2277, 3836],
    2: [4420, 4322, 3729, 3677],
    3: [2888, 3106, 2717, 2323]
}

services = np.array([
    3, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
])

processus = np.array([
    [10, 1, 1], [11, 425, 435], [12, 1, 1], [13, 3, 3], [7, 218, 388], [7, 236, 223], [14, 89, 165], 
    [15, 8, 10], [4, 92, 120], [16, 3, 3], [3, 59, 45], [17, 25, 29], [18, 10, 8], [19, 16, 18], 
    [20, 4, 3], [21, 1, 1], [22, 2, 3], [23, 71, 84], [24, 12, 10], [25, 1, 1], [26, 18, 14], 
    [8, 48, 44], [27, 2, 1], [4, 59, 108], [28, 61, 52], [29, 150, 290], [30, 699, 409], [31, 2, 1], 
    [32, 423, 306], [33, 131, 233], [2, 225, 443], [8, 35, 55], [34, 1, 1], [35, 50, 89], [36, 195, 388], 
    [37, 205, 300], [38, 415, 590], [39, 14, 14], [6, 107, 156], [3, 102, 85], [40, 28, 24], [41, 130, 78], 
    [9, 4, 3], [9, 8, 7], [42, 27, 35], [43, 5, 6], [44, 1, 1], [2, 369, 579], [5, 2, 3], [1, 2, 2], 
    [45, 2, 2], [46, 1, 1], [1, 63, 48], [47, 6, 8], [1, 10, 8], [48, 2, 1], [49, 1, 1], [0, 745, 749], 
    [50, 596, 1066], [51, 79, 92], [52, 4, 3], [53, 150, 222], [3, 34, 22], [54, 55, 30], [4, 138, 158], 
    [9, 1, 1], [55, 135, 166], [56, 133, 124], [57, 74, 86], [0, 569, 832], [58, 14, 12], [0, 648, 879], 
    [59, 11, 15], [60, 1, 1], [61, 528, 613], [62, 9, 9], [63, 1, 1], [64, 1, 1], [65, 64, 47], 
    [66, 1, 1], [67, 205, 167], [68, 319, 591], [3, 174, 105], [69, 1, 1], [70, 177, 180], [0, 7, 12], 
    [71, 18, 18], [72, 414, 243], [73, 1, 1], [6, 7, 12], [74, 507, 335], [75, 217, 186], [76, 334, 426], 
    [2, 157, 100], [7, 447, 524], [77, 399, 799], [78, 123, 186], [1, 26, 14], [5, 10, 7], [4, 25, 18]
])
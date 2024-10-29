/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
    const res = [];
    const global_max = Math.max(...candies);
    for (let candy of candies) {
        if (candy + extraCandies >= global_max) {
            res.push(true)
        } else {
            res.push(false)
        }
    }
    console.log(res);
    return res;
};

const candies = [2, 3, 5, 1, 3];
const extraCandies = 3;
kidsWithCandies(candies, extraCandies);

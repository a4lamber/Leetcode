/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const hashmap = new Map();
    for (var i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (hashmap.has(complement)) {
            return [i,hashmap.get(complement)];
        }
        //  
        hashmap.set(nums[i],i);
    }
};

const nums = [2,7,11,15];
const target = 9;
console.log(twoSum(nums,target));

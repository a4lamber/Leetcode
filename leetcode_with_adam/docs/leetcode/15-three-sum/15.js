/**
 * @param {number[]} nums
 * @return {number[][]}
 * find out any triplets that nums[i] + nums[j] + nums[k] = 0
 * get results in an array [[1,2,-3],[2,-2,0]] without duplicate
 */
var threeSum = function(nums) {
    // 1. sort the array
    // 2. traverse the array 
    // 3. define the helper function
    console.log('start');
    nums.sort((a,b) => a-b);
    console.log(nums); 
    var triplets = [];

    var helper = function(nums,start,triplets) {
        var l = start + 1;
        var r = nums.length - 1;
        while (l < r) {
            const total = nums[start] + nums[l] + nums[r];
            if (total < 0) {
                l++;
            } else if (total > 0) {
                r--;
            } else {
                triplets.push([nums[start],nums[l],nums[r]]);
                l++;
                r--;
                while (l < r && nums[l] === nums[l-1]) {
                    l++;
                }
                while (l < r && nums[r] === nums[r+1]) {
                    r--;
                }
            }
        }
    }
    for (var i = 0;i < nums.length;i++) {
        if (nums[i] > 0) {
            break;
        } 
        if (i == 0 || nums[i] != nums[i-1]) {
            // do something
            helper(nums,i,triplets);
        }
    }
    console.log(triplets);
    return triplets;
};

const nums = [-1,0,1,2,-1,-4];
threeSum(nums);

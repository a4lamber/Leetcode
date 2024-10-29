import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        HashMap<Integer,Integer> hashmap = new HashMap<Integer,Integer>();        
        
        for (int i = 0; i<nums.length; i++) {
            int complement = target - nums[i];
            if (hashmap.containsKey(complement)) {
                res[0] = hashmap.get(complement);
                res[1] = i;
                break;
            }
            hashmap.put(nums[i],i);
        }

        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {2,7,11,15};
        int target = 9;
        
        int[] res = solution.twoSum(nums,target);
        //
        System.out.println("result:" + res[0] +"," + res[1]);
    }
}

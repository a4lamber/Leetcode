import java.util.ArrayList;

class Solution {
    public ArrayList<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // 1. find the maximum, called localmax
        // 2. iterate through the array and compare num+extra >= localmax
        ArrayList<Boolean> res = new ArrayList<>();
        int globalMax = candies[0];
        for (int i = 0; i < candies.length;i++) {
            globalMax = Math.max(globalMax,candies[i]);
        }

        for (int i = 0; i < candies.length;i++) {
            if (candies[i] + extraCandies >= globalMax) {
                res.add(true);
            } else {
                res.add(false);
            }
        }
        System.out.println(res);

        return res;
    }

    public static void main(String[] args) {
        int[] candies = {4,2,1,1,2};
        int extraCandies = 3; 
        Solution solution = new Solution();
        solution.kidsWithCandies(candies, extraCandies);
    }
}

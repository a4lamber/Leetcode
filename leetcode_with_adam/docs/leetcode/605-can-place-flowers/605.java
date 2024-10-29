class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        // initialize an array of zero with 2 unit larger than flowerbed
        // grab it
        // 
        int[] biggerFlowerbed = new int[flowerbed.length + 2];
        
        for (int i = 1; i < 1 + flowerbed.length; i++) {
            biggerFlowerbed[i] = flowerbed[i-1];
        }
        int counter = 0;
        // if left is 1, then we don't plant
        for (int i = 1; i < biggerFlowerbed.length - 1; i++) {
            // planted
            if (biggerFlowerbed[i] == 1) {
                continue;
            }
            // check if neighbors are empty (eligible for plant)
            if (biggerFlowerbed[i-1] == 0 && biggerFlowerbed[i+1] == 0) {
                counter++;
                biggerFlowerbed[i] = 1;
            } 
        }
        if (counter >= n) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        // 1. migrate the flowerbed --> bigger flowerbed with dummy header and dummy tail just like
        // how we uniformally treat insert/delete for linked list
        //
        Solution solution = new Solution(); 
        int[] flowerbed = {1,0,0,0,1};
        int n = 1;

        boolean res = solution.canPlaceFlowers(flowerbed,n);
    }
}

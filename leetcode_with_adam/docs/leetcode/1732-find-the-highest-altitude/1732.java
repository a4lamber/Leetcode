class Solution {
    public int largestAltitude(int[] gain) {
        int globalMax = 0;
        int prefixSum = 0;

        for (int delta:gain) {
            prefixSum = prefixSum + delta;
            globalMax = Math.max(prefixSum,globalMax);
        }
        return globalMax;
    }
}

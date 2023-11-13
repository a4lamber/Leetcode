class Solution {
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        // one pass Solution
        // traverse the soluton one time only
        int i = -1;
        int j = -1;
        int minimumLength = wordsDict.length;

        for (int index = 0; index < wordsDict.length; index++) {
            // mark occurence of word1
            if (wordsDict[index].equals(word1)) {
                i = index;
            }
            
            // mark occurence
            if (wordsDict[index].equals(word2)) {
                j = index;
            }
            
            //always comparing the closest occurence of both words
            if (i != -1 && j != -1){
                // emulate math.abs()
                int currentLength = i - j;
                if (currentLength < 0) {
                    currentLength *= -1;
                }

                // update current length
                if (currentLength < minimumLength) {
                    minimumLength = currentLength;
                }

                // optimization, no need to go further if minimumLength is one
                if (minimumLength == 1) {
                    return minimumLength;
                }
            }
        }


        return minimumLength;
    }
}
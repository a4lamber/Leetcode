class Solution {
    public String mergeAlternately(String word1, String word2) {
        /*
         "abc" and "pqr" --> "apbqcr"
         rules:
         - starting with word1
         - append longer word to the tail of it
        */
        char[] charArray = new char[word1.length() + word2.length()]; 
        
        int sharedLength = Math.min(word1.length(),word2.length());
        for (int i = 0; i < sharedLength;i++) {
            charArray[i*2] = word1.charAt(i);
            charArray[i*2 + 1] = word2.charAt(i);
        }
        int newStart = sharedLength * 2;
        // append the shorter one
        if (word1.length() > word2.length()) {
            for (int j = sharedLength; j < word1.length();j++) {
                charArray[newStart] = word1.charAt(j);
                newStart++;
            }
        } 
        if (word1.length() < word2.length()) 
        {
            for (int j = sharedLength; j < word2.length(); j++) {
                charArray[newStart] = word2.charAt(j);
                newStart++;
            } 
        }
        System.out.println(charArray);
        String res = new String(charArray);
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        String word1 = "abc";
        String word2 = "pqrzz";

        solution.mergeAlternately(word1,word2);

    }
}

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    var left = 0;
    var res = 0;
    const hashset = new Set();
    for (var right = 0; right < s.length; right++) {
        while (hashset.has(s[right])) {
            hashset.delete(s[left]);
            left++;
        }
        // now we has no duplicate
        hashset.add(s[right]);
        res = Math.max(res, right - left + 1);
    }
    console.log(res);
    return res;
};

const s = 'abcabcbb';

lengthOfLongestSubstring(s);

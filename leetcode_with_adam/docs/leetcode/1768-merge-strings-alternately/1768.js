/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
    const res = [];
    var i = 0;
    while (i < Math.min(word1.length, word2.length)) {
        res.push(word1.charAt(i));
        res.push(word2.charAt(i));
        i++;
    }
    if (word1.length > word2.length) {
        res.push(word1.slice(i));
    }
    else if (word1.length > word2.length) {
        res.push(word2.slice(i));
    }
    return res.join('');
}

const word1 = 'abcd';
const word2 = 'pqr';

mergeAlternately(word1, word2);



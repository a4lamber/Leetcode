/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    const vowels = new Set(['a','e','i','o','u','A','E','I','O','U']);
    const stack = [];
    const res = [];

    for (const c of s) {
        if (vowels.has(c)) {
            stack.push(c);        
        }
    }

    for (const c of s) {
        if (vowels.has(c)) {
            res.push(stack.pop());
        }
        else {
            res.push(c);
        }
    }
    console.log(...res);
    return res.join(''); 
};

const s = 'hello';

reverseVowels(s);

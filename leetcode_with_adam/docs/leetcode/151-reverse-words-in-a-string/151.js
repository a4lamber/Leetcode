/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    // - get rid of the leading and string zero
    // - split if only has
    var res = s.trim().split(' ').filter(word => word !== '').reverse();
    console.log(...res);
    return res.join(' '); 
};

//const s = "the sky is blue";
//const s = "  hello world  ";
const s = "a good   example";

reverseWords(s);

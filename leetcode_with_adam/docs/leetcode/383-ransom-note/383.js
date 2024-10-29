/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
    const counter = new Map();
    for (const c of magazine) {
        if (counter.has(c)) {
            counter.set(c, counter.get(c) + 1);
        } else {
            counter.set(c, 1);
        }
    }
    console.log(counter);
    for (const c of ransomNote) {
        if (!counter.has(c)) {
            return false;
        } else {
            counter.set(c, counter.get(c) - 1);
            if (counter.get(c) < 0) {
                return false;
            }
        }
    }
    return true;
};

const ransomNote = "aa";
const magazine = "aab";
canConstruct(ransomNote, magazine);

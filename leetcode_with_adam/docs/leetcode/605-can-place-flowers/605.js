/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    // create a larger array and prepend and append 0, size is 2 + flowerbed.length
    // iterate throught the index 1 to 1 + flowerbed.length,  
    // - if 1, we skip the rest of the iteration
    // - else, we check for left,right condition if yes, we increment the counter 
    //
    const bigger_flowerbed = [0];
    bigger_flowerbed.push(...flowerbed);
    bigger_flowerbed.push(0);

    var counter = 0;
    for (let i = 0; i < 1 + flowerbed.length; i++) {
        if (bigger_flowerbed[i] === 1) {
            continue;
        }

        if (bigger_flowerbed[i-1] == 0 && bigger_flowerbed[i+1] == 0) {
            counter += 1;
            bigger_flowerbed[i] = 1;
        }
     }
    
    console.log(bigger_flowerbed);
    console.log(counter);
    return true ? counter >= n : false
};

const flowerbed = [1,0,0,0,1];
const n = 1;

canPlaceFlowers(flowerbed,n);

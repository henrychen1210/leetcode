/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    const countOne = (num) => {
        let s = num.toString(2)
        let res = 0;

        for(let i = 0; i < s.length; i++) {
            if (s.at(i) == '1'){
                res += 1
            }
        }

        return res
    }

    return arr.toSorted(function(a, b){
        let countA = countOne(a);
        let countB = countOne(b);

        if (countA != countB) {
            return countA - countB;
        }
        else {
            return a - b
        }
    })
}
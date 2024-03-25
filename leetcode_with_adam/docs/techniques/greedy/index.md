# Greedy (贪心算法)

> 贪心算法, 是指在每一步选择中都采取在当前状态下最好或最优的选择, 从而"希望"导致结果是全局最好或最优的算法. 是**没有模版的**, 难点在于如何证明贪心的正确性. 通常要用数学归纳法，反证法去证明后使用，或者直接懵(不一定能过).

探险算法的几个特点是:

- 很难证明；也很难想到你的贪心策略是什么
- 不会回溯，因为贪心算法一旦做出选择 at time `t`，就不会改变过去的选择 (`0..t-1`)。一旦改变了，那就是dp. 这种性质叫**无后效性**, 通常你可以通过这个来验证你的贪心的策略是否满足这个条件，是必要条件.贪心算法，最多只保存前一步的最优解, prev and curr two pointer足够了.
- 广度优先，Dijkstras algorithm都属于greedy. 只是在其问题策略的选择上，刚好得到最优解. 更严谨的说，是其算法部分步骤，用了贪心的思路. 

基本解题思路:

- 建立数学模型来描述问题.
- 把求解的问题分成若干个子问题.
- 对每一个子问题求解，得到子问题的局部最优解.
- 把子问题的解局部最优解合成原来问题的一个近似最优解.

!!! note "[给钱问题](https://blog.csdn.net/youhuakongzhi/article/details/100518166)"
    中国的货币，只看元，有1元，2元，5元，10元，20元，50元，100元。如果我要16元，可以拿16个1元，或者8个2元，但怎么样能用最少的张数来凑出16元呢？如果用贪心策略，就是我们每一次拿那张面值最大的钱。比如目标是16元，我们先拿20拿不起，就拿10元，还不够，就拿5元，还不够，就拿1元，这样就是最少的张数，最后我们的结果是`[10,5,1]`.

    但如果假设有个国家的货币是1元，3元，4元，如果要拿6元，我们用贪心策略，就是拿4元，1元，1元，`[4,1,1]`. 但实际上最少的张数是3元，3元, `[3,3]`. 所以贪心策略，就不能用在这个问题上.


     

## 相关题目

贪心算法通常很少做完单独的考点，通常和其它知识点一起考察，贪心的思想作为其中某一步骤的策略. 但不排除有一些题目是纯粹的贪心算法，可以单独考察.



|number|类型|贪心策略|solution|
|---|---|---|---|
|[1710 Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/description/)|sort + greedy or heap + greedy|`策略是:永远装箱子中装有units最多的箱子`。这题很棒，和dp的区别是，每个箱子占据的体积都为1，而不是变量。如果是变量，这就是一道dp的knapsack题目. 由此可以看，greedy是dp的一个特例|[solution](../../leetcode/1710-maximum-units-on-a-truck/index.md)|
|[11 container with most water](https://leetcode.com/problems/container-with-most-water/)|two pointer(反向) + greedy|`策略: 永远移动最短的height`, 因为随着反向双指针不断内缩，width不断减小，为了maximize volume, 必须修补最短的height, 不让其成为自己的短板。|[solution](../../leetcode/11-container-with-most-water/index.md)|
|1328 Break a Palindrome|贪心|||
|[55 Jump Game](https://leetcode.com/problems/jump-game/description/)|greedy|`策略: 永远走最有潜力的那一步`, 枚举子问题中所有可以走的步数中，能让自己reach最远的距离.|[solution](../../leetcode/55-jump-game/index.md)|
|134 Gas Station|贪心|||
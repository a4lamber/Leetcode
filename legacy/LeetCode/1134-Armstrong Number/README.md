For simple question, interviewer tends to ask you questions with constraints
- solve it without any built in or library funciton


这是锻炼你solving problem with constraints的能力;

> trick: log可以用来获取number of digit

$$
\begin{align*}
log_{10}1 = 0\\
log_{10}2 = 0.301\\
log_{10}9 = 0.954\\
log_{10}10 = 1\\
log_{10}99 = 1.995\\
log_{10}100 = 2\\
\dots\\
log_{10}1000 = 3\\

\end{align*}
$$

# Algorithm
- get the number of digits in `n` for calculating `floor(log10n) + 1` 
- call `getSumOfKthPowerDigits()` by using the digit rolling trick with `n%10` and `n/10`


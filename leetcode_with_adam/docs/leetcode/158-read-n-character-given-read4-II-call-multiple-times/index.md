
# 158 Read n character given read 4 II - call multiple times

这题和157的区别是，假设有一个file size 10

- 157就读一次, 比如call `read(buf,12)` once. 读不完file拉倒
- 158要call `read(buf,n)` multiple time, for example. `read(buf,4)`, 还剩6个，`read(buf,5)`还剩1个，`read(buf,3)`, 读完了

所以我们需要一个manage state来maintain read4()的情况, for example

- file size = 10, 
  - read(5,buff), we called buff4 twice. The buff[0:5] are filled but buff4[1:4] are still ready to be loaed in the next time `read()` being called


## Approach 1  Without Queue



## Approach 2 With Queue


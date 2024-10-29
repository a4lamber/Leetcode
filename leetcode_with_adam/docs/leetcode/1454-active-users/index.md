---
tags:
    - database
---

# [1454 Active Users](https://leetcode.com/problems/active-users/description/?envType=problem-list-v2&envId=database)

This problem is so good that it's worth digging deep into it




## Gaps and Islands Problem

This is a very common problem in DS called Gaps and Islands problem, mentioned in this [blog](https://mattboegner.com/improve-your-sql-skills-master-the-gaps-islands-problem/) and this [stackoverflow post](https://stackoverflow.com/questions/26117179/sql-count-consecutive-days).

In general, gap and island problem is about change of status in a temporal series, such as to find out the length for each happy duration 

|date|mood|
|-|-|
|2023-01-01|happy|
|2023-01-02|happy|
|2023-01-03|happy|
|2023-01-04|happy|
|2023-01-05|sad|
|2023-01-06|sad|
|2023-01-07|happy|
|2023-01-08|happy|
|2023-01-09|happy|
|2023-01-10|happy|
|...|...|

It's easier to spot that we are happy on holiday and weekends and sad on workday. But to be more general, we can have a server and it's traffic on POST and GET,

|date|# of POST|# of GET|
|-|-|-|
|2023-01-01|10022|9202|
|2023-01-02|12313|12913|
|2023-01-03|9999|2323|
|2023-01-04|2123|2342|
|2023-01-05|2342|3242|
|2023-01-06|3253|3424|
|2023-01-07|3245|3242|
|2023-01-08|8875|4364|
|2023-01-09|4958|3451|
|2023-01-10|4245|4322|
|...|...|

If total sum of POST and GET request are over 10000, then it's overloaded. We wish to determine the seasonality of it to spot trend, so the step to solve this typical gap and island problem is,

- add a helper column to determine the status if not given
- use `DENSE_RANK()` to get the rank of dates called `grouping`
- group by `grouping` column 
- calculate duration of each consecutive status by max(date) - min(date)

## Problem

After we understand the procedure of solving gap and island problem, now let's solve it for this question. The data set is shown as below

```
Input: 
Accounts table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Winston  |
| 7  | Jonathan |
+----+----------+
Logins table:
+----+------------+
| id | login_date |
+----+------------+
| 7  | 2020-05-30 |
| 1  | 2020-05-30 |
| 7  | 2020-05-31 |
| 7  | 2020-06-01 |
| 7  | 2020-06-02 |
| 7  | 2020-06-02 |
| 7  | 2020-06-03 |
| 1  | 2020-06-07 |
| 7  | 2020-06-10 |
+----+------------+
```

Active users are those who logged in to their accounts for five or more consecutive days.

Write a solution to find the id and the name of active users. Return the result table ordered by id.

The result format is in the following example.


## Approach 

As for this problem, we noticed a trend

```
  id   login_date. prev_date    diff
| 7  | 2023-05-30 | null        |. null
| 7  | 2023-05-31 | 2020-05-30 | 1 day
| 7  | 2023-06-01 | 2020-05-31 | 1 day
| 7  | 2023-06-02 | 2020-06-01 | 1 day
| 7  | 2023-06-03 | 2020-06-02 | 1 day
| 7  | 2023-06-08 | 2020-06-03
```

if it's consecutive from `2023-05-30` to `2023-06-03` for 5 days and you use `LAG(login_date)`, you have at least 4 days that the difference between login_date and prev_date equals to 1. 

What does that tell us is, we can do some kind of grouping. That's our first step

### Step 1 grouping with DENSE_RANK()

```sql
SELECT
    id,
    login_date,
    DENSE_RANK() OVER (PARTITION BY id ORDER BY login_date ASC) AS rk
FROM
    Logins
```

The result is,

```
| id | login_date | rk |
| -- | ---------- | -- |
| 1  | 2020-05-30 | 1  |
| 1  | 2020-06-07 | 2  |
| 7  | 2020-05-30 | 1  |
| 7  | 2020-05-31 | 2  |
| 7  | 2020-06-01 | 3  |
| 7  | 2020-06-02 | 4  |
| 7  | 2020-06-02 | 4  |
| 7  | 2020-06-03 | 5  |
| 7  | 2020-06-10 | 6  |
```

We notice that, the `dense_rank()` is also growing as long as days elapses. If days are consecutive, it increments by 1. So does dense_rank(). Let's move to next step

### Step 2

```

WITH cte_0 AS (
    SELECT
        id,
        login_date,
        DENSE_RANK() OVER (PARTITION BY id ORDER BY login_date ASC) AS rk
    FROM
        Logins
)
SELECT 
    id,
    login_date,
    DATE_ADD(login_date, INTERVAL -rk DAY) as groupings
FROM 
    cte_0
```

We notice that

```
| id | login_date | groupings  |
| -- | ---------- | ---------- |
| 1  | 2020-05-30 | 2020-05-29 |  
| 1  | 2020-06-07 | 2020-06-05 |
| 7  | 2020-05-30 | 2020-05-29 |  -
| 7  | 2020-05-31 | 2020-05-29 |  -
| 7  | 2020-06-01 | 2020-05-29 |  -
| 7  | 2020-06-02 | 2020-05-29 |  -
| 7  | 2020-06-02 | 2020-05-29 |  -
| 7  | 2020-06-03 | 2020-05-29 |  -
| 7  | 2020-06-10 | 2020-06-04 |
```

Each consecutive days got grouped together, and each group of consecutive days have different grouping identifier,

### Step 3 Final step


!!! tip
    We determine each consecutive days group 

```sql
WITH cte_0 AS (
    SELECT
        id,
        login_date,
        DENSE_RANK() OVER (PARTITION BY id ORDER BY login_date ASC) AS rk
    FROM
        Logins
), cte_1 as (
SELECT 
    id,
    login_date,
    DATE_ADD(login_date, INTERVAL -rk DAY) as groupings
FROM 
    cte_0)
,cte_2 as (
select
    id,
    DATEDIFF(MAX(login_date),MIN(login_date)) as duration
from
    cte_1
group by id, groupings
-- interest in at least 5 consecutive days, so >= 4 is enough
having DATEDIFF(MAX(login_date),MIN(login_date)) >= 4)
select
    distinct a.id,
    a.name
from
    cte_2
inner join Accounts as a on
cte_2.id = a.id
order by a.id
```
# Dating

In this session, we will use `MySQL` as an example,


## Functions for Dates and Times

### Date Arithmetic

|-|description|example|
|-|-|-|
|`DATE_ADD(date, INTERVAL value unit)`|-|`SELECT date_add('2024-10-12', INTERVAL 5 day)`|
|`DATE_SUB(date, INTERVAL value unit)`|-|`SELECT date_sub('2024-10-12', INTERVAL 2 month)`|
|`DATEDIFF(date1,date2)`|returns the differences in days|`select datediff('2024-10-12','2024-10-10')`|
|`TIMESTAMPDIFF(unit, datetime1, datetime2)`|Returns the difference in the specified unit (e.g., SECOND, MINUTE, HOUR, DAY, MONTH, YEAR)|`SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-10-27'); -- Returns 300`|
|-|-|`SELECT DATE_FORMAT('2024-10-27 14:35:22', '%Y-%m');`|
c

!!! note
    Unit can be `year`, `month`, `day`
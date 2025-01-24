# Principles of using Reactive libraries

- <mark style="color:red;"> <mark style="color:red;">**The principle is to implement using only UniTasks**</mark>.
- Avoid UniRx due to performance issues.
- R3 (successor to UniRx) does not have significant performance issues, but for code uniformity, it is recommended to avoid using it.
  - Exceptions are limited to special cases that are very easy to implement using R3.



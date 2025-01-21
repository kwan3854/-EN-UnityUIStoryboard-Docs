# Principles of using Reactive libraries

* <mark style="color:red;">**Implement using only UniTasks**</mark>.
* UniRx is avoided due to performance issues.
* R3 (successor to UniRx) does not have significant performance issues, but should be avoided for code uniformity.
  * Exceptions are limited to special cases where R3 is very easy to implement.


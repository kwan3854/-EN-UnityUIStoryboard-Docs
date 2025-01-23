# Class Design

- Based on MVPs, common or bloat-prone processing, such as communication and screen transitions, is handled by other classes at the right time. 
- The lifetime of a Model only lasts within its screen, and persistent data is kept in the Repository.
- There is one Presenter for each screen.
- As you have more elements on the screen, Presenter tends to get bigger, so we break out the big processing into separate classes to reduce the processing Presenter does directly.
- Model and View are also one in the default 1 screen, but split them if the screen is bloated or if the on-screen elements are independent.

<figure><img src="../../.gitbook/assets/ScreenSystem.png" alt=""><figcaption><p>ScreenSystem Architecture</p></figcaption></figure>

- Names like UseCase and Repository adopt terminology used in other architectures, such as clean architecture, but are not consistent with clean architecture.
- They are designed to reference clean architecture and other architectures, but with the goal of reducing complexity and ease of use.



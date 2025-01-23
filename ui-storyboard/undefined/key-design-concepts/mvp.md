# About the MVP concept

Before we start writing code in earnest, we need to talk about the concept of structure.

## MVP vs. MVVM

### For a canonical MVP

- A canonical MVP is one that creates a Model, View, and Presenter and communicates with them through an interface without considering their specific implementations in order to make them less dependent on each other.
- This is a design that takes into account the reusability of each UI element, and is a very valid approach when there are many UI structures that can be reused throughout the project.
- However, this design requires a significant amount of time/effort.

### For a canonical MVVM

- MVVM is a great way to eliminate the need to manually modify data from the presenter side to the view side.
- By binding data from the view and model together on the view model side, changes in the model's values are displayed directly in the view UI at the desired time.

## The problem with the traditional approach is that

### Characteristics of Unity games

- Because of the nature of games, there is very little UI structure that is reused, unlike typical apps or the web.
  - To be more precise, it's difficult to identify UI components that are reused across multiple screens, or MVPs.
  - And even a small change in design often requires a big change in scope.
  - This is where the traditional, rigid MVP and MVVM implementations often get in the way of project progress.
- MVVM and UGUI
  - Data binding, the core of MVVM, must be supported at the UI framework level to be implemented.
  - `UGUI`is a UI framework that was designed without any consideration for this. (The recent Unity push of `UIToolKit`which we've been pushing lately, replaces `Unity6 LTS`but it doesn't yet support `UIToolKit`is still an incomplete framework to use in a production product).
  - Binding data to the UI is also heavily tied to performance issues. (Games are much more affected by this performance issue than regular apps/web)

## I decided to do this.

{% hint style="warning" %}
I'm not arguing that this is necessarily the right way to do things. I think the most important thing is that the team agrees on a consistent structure and applies it consistently throughout the project. In that regard, I am suggesting that this structure has worked best in my experience. If your project has different characteristics than the game projects I've worked on, and it's more efficient to use a different structure, then that's up to the team to decide.
{% endhint %}

### MVPs have one set of each

- When implementing an MVP, write it as a single set of MVPs, excluding the possibility that it could be used elsewhere.
- A single screen must have one Model, one View, and one Presenter.
- In other words, we don't use interfaces to extract common logic.
- If your plans change, you only need to modify that one set, without affecting the UI of the other screens.
- This makes it easier to use <mark style="color:red;">.**Rapid development cycles**</mark>.and we've seen that it's possible to make quick fixes.

### Using MVRP

- Bind some sort of data to the UI using ReactiveProperty, which is supported by UniTask, UniRx (R3), etc.

### Extracting public logic can be done later using

- If you're working on a project and realize that a truly common UI is being used more than 2-3 times over, it's never too late to extract it into an interface.

### Hybrids of MVP \& MVVM

By using the above two approaches, we believe we have a UI code structure that fits the domain specifics of games.



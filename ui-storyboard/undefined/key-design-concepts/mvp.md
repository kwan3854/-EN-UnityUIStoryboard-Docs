# About the MVP concept

Before we start writing code in earnest, we need to talk about the concept of structure.

## MVP vs MVVM

### For the canonical MVP

* A canonical MVP requires that you create a Model, View, and Presenter and make them communicate through interfaces without considering their specific implementations in order to make them less dependent on each other.
* This is a design that takes into account the reusability of each UI element, and is a very valid approach when there are many UI structures that can be reused throughout the project.
* However, this design requires a significant amount of time/effort.

### For the canonical MVVM

* MVVM is a great way to avoid having to manually modify data from the presenter side to the view side.
* On the View Model side, it binds the data of the View and Model together, so that changes in the Model's values are displayed directly in the View's UI at the desired time.

## The problem with the traditional approach.

### The nature of Unity games

* Because of the nature of games, there are very few reused UI structures, unlike typical apps or the web.
  * To be more precise, it's difficult to identify a UI component that can be reused across multiple screens, an MVP.
  * And even small changes in design often require large-scale modifications.
  * This is where the traditional, rigid MVP and MVVM implementation often becomes a hindrance to project progress.
* MVVM and UGUI
  * Data binding, which is the core of MVVM, must be supported at the UI framework level to be implemented.
  * UGUI is a UI framework that was designed without this in mind (Unity's recently pushed UIToolKit supports this starting with Unity6 LTS, but UIToolKit is still an incomplete framework for production use).
  * Binding data to the UI is also heavily tied to performance issues. (Games are much more affected by this performance issue than regular apps/web)

## I decided to do this.

{% hint style="warning" %}
I'm not claiming that this is necessarily the right way to do things. I think the most important thing is that the team agrees on a consistent structure and applies it consistently throughout the project. In that regard, I am suggesting that this structure has worked best in my experience. If your project has different characteristics than the game projects I've worked on, and it's more efficient to use a different structure, then you can discuss and decide as a team.
{% endhint %}

### MVPs are a set of

* When implementing MVPs, write them as a single set of MVPs, excluding the possibility that they could be used elsewhere.
* There must be one Model, one View, and one Presenter on a screen.
* Do not use interfaces to extract common logic parts.
* If the plan changes, only one set needs to be modified, and the UI of the other screens is not affected.
* In our experience, this allows for a <mark style="color:red;">faster development cycle</mark> and allows for quick fixes.

### Using MVRP

* Bind some sort of data to the UI using ReactiveProperties, such as those supported by UniTask or UniRx (R3).

### Extracting public logic can be done later using

* If you realize that a truly common UI is used more than 2-3 times in a project, it's never too late to extract it into an interface.

### Combines the best of MVP & MVVM in a game context

By using the above two methods, I think we have a UI code structure that fits the domain characteristics of games.

# Relationship with UnityScreenNavigator

* ScreenSystem is a wrapper library for UnityScreenNavigator.
* The biggest significance of ScreenSystem is the introduction of VContainer (DI).
* Along with this comes the introduction of the Onion Architecture approach.
* ScreenSystem uses only two of the three types of tabbed UIs that exist in UnityScreenNavigator: `Page`, `Modal`, and `Sheet`. (Tabbed UIs like Sheet are designed to be viewed as a type of view, not as a transition on the screen.)
* The `Page` is the base of the screen and is always visible.
* When the `Page` is updated, the entire screen is updated.
* A `Modal` is a kind of dialog that appears above the `Page`.
* Modals can be stacked on top of each other.
* Screen transitions are accomplished through transitions in the Prefab.

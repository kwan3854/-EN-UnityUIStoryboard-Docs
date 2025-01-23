# Relationship to UnityScreenNavigator

- ScreenSystem is a wrapper library for UnityScreenNavigator.
- The most significant contribution of ScreenSystem is the introduction of VContainer(DI).
- Along with this comes the introduction of the Onion Architecture approach.
- The ScreenSystem uses the `Page`, `Modal`, `Sheet` λ `Page`and `Modal` (Tabbed UIs like Sheet are designed to be viewed as a kind of view, not as a transition between screens).
- `Page`is the base of the screen and is always visible.
- `Page`is updated, the entire screen is updated.
- `Modal`The `Page` as the kind of dialog you see above.
- `Modal`can be stacked.
- Screen transitions are accomplished via transitions in the Prefab.



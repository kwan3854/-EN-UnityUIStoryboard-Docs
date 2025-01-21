# Builder

### Concepts

* BuilderBase is one of the features of ScreenSystem, which works with DI Container to create screens and generate Pages and Modals.
* Elements to be used in the next screen can be defined and passed as Parameters.
* For example, let's say you have a UI where you tap an item in the inventory to go to the item detail page.
  * The ID of the selected item can be passed as a parameter to the next screen.

### Example code

```csharp
public class TestPageBuilder : PageBuilderBase<TestLifecycle, TestPageView>
{ }
    public TestBuilder(bool playAnimation = true, bool stack = true) : base(playAnimation, stack) { }
}

// passing parameters to the next screen
public class TestPageBuilder : PageBuilderBase<TestLifecycle, TestView, TestPageParameter>
{ TestView
    public TestBuilder(TestParameter parameter, bool playAnimation = true, bool stack = true) : base(parameter, playAnimation, stack) { }
}
```

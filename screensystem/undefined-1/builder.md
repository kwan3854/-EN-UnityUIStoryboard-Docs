# Builder

### Concepts

- BuilderBase is a feature of the ScreenSystem that works with DI Containers to create screens and generate Pages and Modals.
- The elements to be used in the next screen can be defined and passed as Parameters.
- For example, imagine a UI where tapping an item in your inventory takes you to the item detail page.
  - You can pass the ID of the selected item via a parameter to the next screen.

### Example code

```csharp
public class TestPageBuilder : PageBuilderBase<TestLifecycle, TestPageView>
{
    public TestBuilder(bool playAnimation = true, bool stack = true) : base(playAnimation, stack) { }
}

// 다음 화면에 파라미터를 전달하는 경우
public class TestPageBuilder : PageBuilderBase<TestLifecycle, TestView, TestPageParameter>
{
    public TestBuilder(TestParameter parameter, bool playAnimation = true, bool stack = true) : base(parameter, playAnimation, stack) { }
}
```



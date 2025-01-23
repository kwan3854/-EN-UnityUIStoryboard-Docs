# LifetimeScope

### concept

- A unit specific to a VContainer.
- **Create only one for a single screen. **<mark style="color:red;">**(no exceptions)**</mark>.

### Uses

- Specifies class dependencies within the screen.
- Hand the view to the Presenter (Lifecycle).

### How to implement

- Implement by inheriting from LifetimeScope or LifetimeScopeWithParameter.
- Receive and use a pageView via SerializeField.
- Add mock information such as communication.

### Example code

```csharp
public class TestLifetimeScope : LifetimeScope
{
    [SerializeField] private TestView _view;

    protected override void Configure(IContainerBuilder builder)
    {
        base.Configure(builder);
        builder.RegisterComponent(_view); // View 등록
        builder.Register<TestPageLifecycle>(Lifetime.Singleton);  // 화면별 Lifecycle 등록
        builder.Register<TestUseCase>(Lifetime.Singleton); // 통신의 UseCase 등록
        AddMockInDebug(builder);  // 통신 Mock 플러그인 삽입
    }
}
```



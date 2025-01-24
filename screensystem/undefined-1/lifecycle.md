# Lifecycle

### Concepts

- The actual entry point to the screen.
- It acts as the Presenter in the MVP.
- Create it on a per-screen basis.
- We call it Lifecycle because it's associated with the lifetime of the screen.
- **Create only one on a screen. **<mark style="color:red;">**(no exceptions)**</mark>.

### Implementation policy

- The constructor is only responsible for getting a reference to each class imported from the LifetimeScope (it doesn't do any other complicated processing)
- Before switching screens `WillPushEnterAsync` we do the following
  - Create a Model.
  - Initialize the View (pass the created model to the View).
- After switching screens `DidPushEnter` Subscribe to handling the View button in
  \*.
  If you enable button handling after screen transitions, button input events will not be fired during transitions (button presses during transitions can be frustrating in many ways).
- Specify AssetName (the name of the prep) in an attribute of the class.

### Example code

```csharp
[AssetName("TestPage")]
public class TestPageLifecycle : LifecyclePageBase
{
    // 생성자에서 받는 것을 선언합니다.
    private readonly TestPageView _view;
    private readonly PageEventPublisher _publisher;
    private readonly ModalManager _modalManager;

    // 생성자 인젝션
    [Inject]
    public TestPageLifecycle(TestPageView view, PageEventPublisher publisher, ModalManager modalManager) : base(view)
    {
        _view = view;
        _publisher = publisher;
        _modalManager = modalManager;
    }

    // 화면 전환 전 타이밍에 View 초기화하기
    protected override UniTask WillPushEnterAsync(CancellationToken cancellationToken)
    {
        var testModel = new TestPageModel();
        _view.SetView(testModel);
        return UniTask.CompletedTask;
    }

    // 화면 전환 후 버튼 이벤트 등록하기
    public override void DidPushEnter()
    {
        base.DidPushEnter();
        // 페이지 표시
        _view.OnClickPage.Subscribe(_ => {
          _publisher.SendPushEvent(new NextPageBuilder());
        });
        // Modal 표시
        _view.OnClickModal.Subscribe(_ => {
          _modalManager.Push(new NextModalBuilder()).Forget();
        });
    }
}
```

{% hint style="success" %}
PageEventPublisher and ModalManager are functions of the ScreenSystem that are responsible for switching between Page and Modal, respectively. Next, we build the screen that will open with Builder.
{% endhint %}



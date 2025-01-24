# View

### Concepts

- The View that corresponds to the V in MVP.
- **Create only one on a single screen.** <mark style="color:green;">(with exceptions)</mark>.

### Implementation policy

- Implemented by inheriting from ScreenSystem's PageViewBase, ModalViewBase.

- Receives a Model from the Lifecycle and builds the screen.

- UI elements, such as each button, get a reference to a SerializeField.

- Each button's event is exposed as an IObservable.

- Dynamically growing parts of the View, such as lists, are created within this View.
  
  - This means that the View has the structure
  - Events also become bridges, but we allow them because they are easier to manage.
  - However, by limiting the role of the View to the following two roles, we avoid the complexity of each processing.
    - Taking a Model and building the screen UI
    - Firing Events

- UI Animation reduces the amount of scripting by relying on non-scripted data such as Animator and Timeline.

- Use a UniTask to wait for the animation to finish.

- 1Screen 1View is the principle
  
  - For the reasons above, it's not a big deal if a View gets bloated.

- Depending on your project, you may want to interface the Model instead of passing it directly to the View. (We recommend interfacing in the following cases)
  
  - If a View or Model is reused across multiple screens

### Example code

```csharp
public class TestPageView : PageViewBase
{
    [SerializeField] private TextMeshProUGUI _messageText;
    [SerializeField] private Button _nextPageButton;
    [SerializeField] private Button _nextModalButton;
    
    // 버튼은 클릭 이벤트만 공개한다
    public IObservable<Unit> OnClickPage => _nextPageButton.OnClickAsObservable();
    public IObservable<Unit> OnClickModal => _nextModalButton.OnClickAsObservable();

    // Model을 받아 화면 구성하기
    public void SetView(TestPageModel model)
    {
        _messageText.SetText(model.TestMessage);
    }
}
```

- Event handling for buttons can also be implemented using IUniTaskAyncEnumerable and ForEachAwaitAsync in UniTask rather than UniRx.
  - When implemented with UniTask, it is easier to implement blocking-like processing, such as not performing the next processing until asynchronous processing such as communication processing is completed when a button is pressed.
  - UniTasks also make debugging easier with UniTask Tracker.
  - Whether to use UniRx or UniTask depends largely on the developer's skills and knowledge. (Choose whichever you are more comfortable with).

### See also: Sample button processing with UniTask

```csharp
// View
public IUniTaskAsyncEnumerable<AsyncUnit> OnClickAsync => _button.OnClickAsAsyncEnumerable();

// Presenter
_view.OnClickAsync.ForEachAwaitAsync(async _ =>
{
    // 비동기 처리, 특히 통신 처리 및 화면 전환 처리
    // await ~~
    // 함수 내 처리가 완료될 때까지 다음 처리가 실행되지 않는다.
});
```



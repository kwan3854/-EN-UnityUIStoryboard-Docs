# View

### Concepts

* A View corresponding to the V in MVP.
* **Write only one per screen** <mark style="color:green;">(with exceptions)</mark>.

### Implementation policy

* Implement by inheriting PageViewBase, ModalViewBase from ScreenSystem.
* Get the Model from Lifecycle to build the screen.
* UI elements such as each button are referenced by SerializeField.
* Each button's event is exposed as an IObservable.
* Dynamically growing parts of the View, such as lists, are created within this View.
  * In other words, the View has the structure of a View
  * Events also become bridges, but this is acceptable because it makes event management easier.
  * However, by limiting the role of the View to the following two roles, we can avoid the complexity of each processing.
    * Receiving a Model and building the UI of the screen.
    * Firing events
* Reduce the amount of scripting by relying on non-script data such as Animator and Timeline for UI animations.
* Use UniTasks to wait for the animation to finish.
* 1 Screen 1 View is the rule
  * For the above reasons, it doesn't matter if a View gets too big.
* Depending on your project, you may want to interface your Model instead of passing it directly to the View. (Interfacing is recommended in the following cases)

    * A View or Model is reused across multiple screens.



### Example code

```csharp
public class TestPageView : PageViewBase
{ }
    [SerializeField] private TextMeshProUGUI _messageText;
    [SerializeField] private Button _nextPageButton;
    [SerializeField] private Button _nextModalButton;
    
    // The button only exposes click events
    public IObservable<Unit> OnClickPage => _nextPageButton.OnClickAsObservable();
    public IObservable<Unit> OnClickModal => _nextModalButton.OnClickAsObservable();

    // Get the model and configure the screen
    public void SetView(TestPageModel model)
    { _MessageText.
        _messageText.SetText(model.TestMessage);
    }
}
```

* Event handling for buttons can also be implemented using IUniTaskAyncEnumerable and ForEachAwaitAsync in UniTask instead of UniRx.
  * When implemented with UniTask, it is easy to implement blocking-like processing, such as not performing the next processing until asynchronous processing such as communication processing is completed when a button is pressed.
  * Debugging is easier with UniTask Tracker when using UniTask.
  * The decision to use UniRx or UniTask is highly dependent on the developer's skills and knowledge. (Choose whichever you are more comfortable with).

### Note: Sample button processing using UniTask

```csharp
// View
public IUniTaskAsyncEnumerable<AsyncUnit> OnClickAsync => _button.OnClickAsAsyncEnumerable();

// Presenter
_view.OnClickAsync.ForEachAwaitAsync(async _ =>
{
    // Asynchronous processing, especially handling communication and screen transitions.
    // await ~~]
    // The next processing is not executed until the processing within the function is complete.
});
```

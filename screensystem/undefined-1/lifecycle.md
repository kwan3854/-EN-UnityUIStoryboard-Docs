# Lifecycle

### Concepts

* The actual EntryPoint of the screen.
* Acts as a Presenter in the MVP.
* Created on a per-screen basis.
* We call it Lifecycle because it is a concept that is associated with the life of the screen.
* Create only one per screen:&#x20;**<mark style="color:red;">**(No exceptions)**</mark>

### Implementation Policy

* The constructor is only responsible for getting a reference to each class imported from the LifetimeScope (it doesn't do any other complicated processing)
* Inside `WillPushEnterAsync` before the screen transition, do the following.
  * Create a Model.
  * Initialize the View (passing the created model to the View).
* After the screen transition, inside `DidPushEnter`, subscribe to the View button handling.
  *.
    Enable button handling after screen transitions so that no button input events are fired during transitions (button presses during transitions can cause a lot of trouble).
* Specify AssetName (the name of the prep) in the attribute of the class.

### Example code.

```csharp
[AssetName("TestPage")]
public class TestPageLifecycle : LifecyclePageBase
{ }
    // Declare what we receive in the constructor
    private readonly TestPageView _view;
    private readonly PageEventPublisher _publisher;
    private readonly ModalManager _modalManager;

    // Inject constructor.
    [Inject].
    public TestPageLifecycle(TestPageView view, PageEventPublisher publisher, ModalManager modalManager) : base(view)
    }
        _view = view;
        _publisher = publisher;
        _modalManager = modalManager;
    }

    // Initialize the view at the pre-switch timing
    protected override UniTask WillPushEnterAsync(CancellationToken cancellationToken)
    { }
        var testModel = new TestPageModel();
        _view.SetView(testModel);
        } return UniTask.CompletedTask;
    }

    // Register the button event after the screen transition
    public override void DidPushEnter()
    return
        base.DidPushEnter();
        // Show the page
        _view.OnClickPage.Subscribe(_ => {
          _publisher.SendPushEvent(new NextPageBuilder());
        });
        // Show Modal
        _view.OnClickModal.Subscribe(_ => {
          _modalManager.Push(new NextModalBuilder()).Forget();
        });
    }
}
```

{% hint style="success" %}
PageEventPublisher and ModalManager are features of the ScreenSystem that are responsible for switching between Page and Modal, respectively. Next, we build the screen that will open with Builder.
{% endhint %}


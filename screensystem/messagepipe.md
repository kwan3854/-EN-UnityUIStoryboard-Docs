# Screen-to-screen messaging with MessagePipe

Sometimes you want updates on screen A to be reflected on screen B, which is open at the same time.

For example, when a character is buffed, the status screen one screen over should also reflect the data update. This can be accomplished through messaging using MessagePipe.

The source screen sends a notification of the update, and the screens you want to reflect it on each receive a notification and reflect it on their respective screens based on the content of the notification.

***

### Below is a set of classes and flows for implementing messaging.

#### Message classes

Categorize what you want to notify in a message into classes.

```csharp
public class MessagePipeTestMessage
{
    // 변경 내용을 정의해 둡니다.
    public readonly int Count;
    
    public MessagePipeTestMessage(int count)
    {
        Count = count;
    }
}
```

#### RootLifetimeScope

Register for notification processing in a parent LifetimeScope, such as RootLifetimeScope.

```csharp
protected override void Configure(IContainerBuilder builder)
{
    var options = builder.RegisterMessagePipe();
    builder.RegisterMessageBroker<MessagePipeTestMessage>(options);
}
```

#### Message Publisher

The side issuing the notification uses Publisher to send notifications when updates are made.

```csharp
private readonly IPublisher<MessagePipeTestMessage> _testMessagePublisher;

_testMessagePublisher.Publish(new MessagePipeTestMessage(_parameter.ModalCount));
```

#### Message Subscriber

The side that subscribes to the notification uses Subscribe to describe the handling of updates when the message is received.

```csharp
private ISubscriber<MessagePipeTestMessage> _testMessageSubscriber;

_testMessageSubscriber.Subscribe(m =>
{
    // 받은 업데이트 내용을 바탕으로 Model과 View에 반영합니다.
    _view.UpdateModalCount(m.Count);
}).AddTo(_disposeCancellationTokenSource.Token);
```

***

As shown above, messaging is happening by creating a registration in LifetimeScope, publish-side processing, and subscription-side processing, and updates are happening on multiple screens. We utilize MessagePipe because it is a useful library for implementing messaging, whether in-game or not.



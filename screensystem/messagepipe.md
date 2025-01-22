# Screen-to-screen messaging with MessagePipe

Sometimes you want an update on screen A to be reflected on screen B, which is open at the same time.

For example, when you make a character enhancement, the data update should also be reflected on the status screen one screen ahead. This can be accomplished through messaging with MessagePipe.

The source screen sends a notification of the update, and the screens you want to reflect it on each receive a notification and reflect it to their respective screens based on the content of the notification.

***]

### Here is a set of classes and flows for implementing messaging.

#### Message Classes

We categorize what we want to communicate in a message into classes.

```csharp
public class MessagePipeTestMessage
{ }
    // Define what we want to change.
    public readonly int Count;
    
    public MessagePipeTestMessage(int count)
    { // Define the change
        Count = count;
    }
}
```

#### RootLifetimeScope

Register for notification processing in a parent LifetimeScope, such as the RootLifetimeScope.

```csharp
protected override void Configure(IContainerBuilder builder)
{ ```csharp
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

The side that subscribes to the notification uses Subscribe to describe the processing of updates when the message is received.

```csharp
private ISubscriber<MessagePipeTestMessage> _testMessageSubscriber;

_testMessageSubscriber.Subscribe(m =>
{ }
    // Reflect the received updates to the Model and View.
    _view.UpdateModalCount(m.Count);
}).AddTo(_disposeCancellationTokenSource.Token);
```

***]

As shown above, we've created registration, publish-side processing, and subscription-side processing in LifetimeScope, messaging is happening, and multiple screens are being updated. We utilize MessagePipe because it's a great library for implementing messaging, whether it's in-game or not.

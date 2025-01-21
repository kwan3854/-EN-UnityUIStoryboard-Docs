# UseCase

### Concept

* A class that primarily has only **one constructor and one execution function**.
* A class that doesn't do any side effects on the data it receives.
* It could be made as a static function, but we categorized it as a generic class because it works well with DI.

### When to use UseCase?

* Communication processing.
* Common processing that is used across multiple screens
* When writing in Lifecycle would make it bloated and less readable

In particular, communication processing is categorized as a UseCase because it is often called from multiple screens, and the processing content is likely to be bloated.

#### Make sure to use UseCase in these cases.

For example, the character information acquisition communication is called in multiple screens, such as when switching in-game, the organization screen, and the enhancement screen. Since the same processing is done in multiple places, UseCase is used to manage it as a single class.

#### Can't we just treat everything as a UseCase instead of a Lifecycle?

You could UseCase all the processing besides communication, but you'll end up with a lot of one-off UseCases that are only used once. This can lead to poor readability and less efficient development.

Our approach is that if we see a common process being used more than two or three times by other common processes, we try to UseCase it each time to clean it up.

### Example code

Below is a sample UseCase for communication. It is written not only to communicate and receive the result, but also to include UI display during communication, error handling, etc. Users (such as Lifecycle) can handle communication, including error handling, by simply calling DoConnect.

```csharp
public class TestUseCase
{ }
    private readonly IHttpClient _httpClient; // Communication execution class
    private readonly NetworkErrorUseCase _networkErrorUseCase; // error countermeasures such as screen switching due to communication error
    private readonly NetworkLoadingController _loadingController; // Display during communication

    [Inject].
    public HomePageUseCase(IHttpClient httpClient, NetworkErrorUseCase networkErrorUseCase, NetworkLoadingController loadingController)
    {
        _httpClient = httpClient;
        _networkErrorUseCase = networkErrorUseCase;
        _loadingController = loadingController;
    }

    // Calling and executing DoConnect
    public async UniTask<TestPageLifecycle.NetworkParameter> DoConnect(CancellationToken cancellationToken) => await DoConnectInternal(cancellationToken, 0);

    // DoConnect internal processing
    // On error, get the number of previous retries and recurse.
    private async UniTask<TestPageLifecycle.NetworkParameter> DoConnectInternal(CancellationToken cancellationToken, int retryCount)
    { }
        // While communicating... and start communication.
        _loadingController.Activate();
        var connection = await _httpClient.Call<TestConnectResponse>(new TestConnectRequest(), cancellationToken);
        _loadingController.InActivate();

        // Handle on failure
        if (!connection.result.IsSuccess())
        { }
            // For example, during maintenance, mark maintenance and revert to title.
            if (connection.response?.status.IsInMaintenanceMode ?? false)
            { }
                await _networkErrorUseCase.ShowMaintenanceToTitle(connection.response?.status.error);
                return null;
            }
            
            // Let the user choose whether to retry when an error occurs.
            // There is a maximum number of retries, which can force the title to be reverted.
            var isRetry = await _networkErrorUseCase.ShowErrorWithRetry(retryCount);
            if (isRetry)
            { retryCount
                retryCount++;
                return await DoConnectInternal(cancellationToken, retryCount);
            }
            } return null;
        }

        // Return a response if the communication is successful.
        return new TestPageLifecycle.NetworkParameter()
        { TestConnectResponse
            TestConnectResponse = result.response
        };
    }
}
```


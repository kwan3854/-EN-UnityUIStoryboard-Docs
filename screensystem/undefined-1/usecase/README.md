# UseCase

### Concepts

- Primarily **One constructor and one execution function**and an execution function.
- A class that does not perform any side effects on the data it receives.
- It could be made as a static function, but we've categorized it as a generic class because it works well with DI.

### When to use UseCase?

- Handling communication
- Common processing used across multiple screens
- If you write it in Lifecycle, it will be bloated and hard to read

In particular, communication processing is often called from multiple screens, and the processing content is likely to be bloated, so we categorize it as a UseCase.

#### UseCase should be used in these cases.

For example, the character information acquisition communication is called in multiple screens, such as during in-game transitions, the formation screen, and the enhancement screen. Since the same processing occurs in multiple places, UseCases allow you to bundle them together and manage them as a single class.

#### Can't I just UseCase everything instead of Lifecycle?

You can UseCase all processing besides communication, but you'll end up with a lot of one-off UseCases that are only used once. This can lead to poor readability and less efficient development.

If we see it being used more than 2-3 times in other common processing, we try to clean it up by UseCasing it each time.

### Example code

Below is a sample UseCase for communication. It is written not only to communicate and receive results, but also to include UI display during communication, error handling, etc. Users (such as Lifecycle) can handle communication, including error handling, by simply calling DoConnect.

```csharp
public class TestUseCase
{
    private readonly IHttpClient _httpClient; // 통신 실행 클래스
    private readonly NetworkErrorUseCase _networkErrorUseCase; // 통신 오류에 따른 화면 전환 등의 오류 대책
    private readonly NetworkLoadingController _loadingController; // 통신 중 표시

    [Inject]
    public HomePageUseCase(IHttpClient httpClient, NetworkErrorUseCase networkErrorUseCase, NetworkLoadingController loadingController)
    {
        _httpClient = httpClient;
        _networkErrorUseCase = networkErrorUseCase;
        _loadingController = loadingController;
    }

    // DoConnect를 호출하고 실행하기
    public async UniTask<TestPageLifecycle.NetworkParameter> DoConnect(CancellationToken cancellationToken) => await DoConnectInternal(cancellationToken, 0);

    // DoConnect 내부 처리
    // 오류 발생 시 이전까지의 재시도 횟수를 받아 재귀 처리한다.
    private async UniTask<TestPageLifecycle.NetworkParameter> DoConnectInternal(CancellationToken cancellationToken, int retryCount)
    {
        // 통신 중... 의 UI를 표시하고 통신을 시작합니다.
        _loadingController.Activate();
        var connection = await _httpClient.Call<TestConnectResponse>(new TestConnectRequest(), cancellationToken);
        _loadingController.InActivate();

        // 실패 시 처리
        if (!connection.result.IsSuccess())
        {
            // 예를 들어, 유지보수 중에는 유지보수 표시를 하고 제목으로 되돌립니다.
            if (connection.response?.status.IsInMaintenanceMode ?? false)
            {
                await _networkErrorUseCase.ShowMaintenanceToTitle(connection.response?.status.error);
                return null;
            }
            
            // 오류 발생 시 재시도 여부를 선택하게 한다.
            // 재시도에는 최대 횟수가 설정되어 있으며, 이를 초과하면 강제로 타이틀을 되돌릴 수 있다.
            var isRetry = await _networkErrorUseCase.ShowErrorWithRetry(retryCount);
            if (isRetry)
            {
                retryCount++;
                return await DoConnectInternal(cancellationToken, retryCount);
            }
            return null;
        }

        // 통신에 성공하면 응답을 반환합니다.
        return new TestPageLifecycle.NetworkParameter()
        {
            TestConnectResponse = result.response
        };
    }
}
```



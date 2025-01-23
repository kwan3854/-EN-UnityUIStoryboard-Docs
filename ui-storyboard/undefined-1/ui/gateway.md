# Gateway

- Responsible for direct communication with the real world
- Must be configured as an interface
- It should only serve to communicate and never **business logic, domain logic, etc.**.

```csharp
public interface IHttpClientGateway
{
    // Return json object from server using newtonsoft json
    public UniTask<TResponse> RequestAsync<TRequest, TResponse>(string url, TRequest requestData);
}
```

```csharp
public class HttpClientGateway : IHttpClientGateway
{
    public async UniTask<TResponse> RequestAsync<TRequest, TResponse>(string url, TRequest requestData)
    {
        string jsonRequest = JsonConvert.SerializeObject(requestData); // 직렬화
        string jsonResponse = "{}"; // 서버에서 받은 JSON 응답
        await UniTask.Delay(1000); // 서버 통신 대신 1초 대기
        return JsonConvert.DeserializeObject<TResponse>(jsonResponse); // 역직렬화
    }
}
```



# Gateway

* Responsible for direct communication with the real world
* Must be configured as an interface
* Should only be responsible for simple communication and should never contain **business logic, domain logic**.

```csharp
public interface IHttpClientGateway
{ }
    // Return json object from server using newtonsoft json
    public UniTask<TResponse> RequestAsync<TRequest, TResponse>(string url, TRequest requestData);
}
```

```csharp
public class HttpClientGateway : IHttpClientGateway
{ }
    public async UniTask<TResponse> RequestAsync<TRequest, TResponse>(string url, TRequest requestData)
    { }
        string jsonRequest = JsonConvert.SerializeObject(requestData); // serialize
        string jsonResponse = "{}"; // JSON response received from the server
        await UniTask.Delay(1000); // wait 1 second instead of communicating with the server
        return JsonConvert.DeserializeObject<TResponse>(jsonResponse); // deserialize
    }
}
```

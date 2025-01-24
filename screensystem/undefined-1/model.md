# Model

### Concepts

- Created in Lifecycle.
- It has the actual data on the screen.
- **You only write one per screen. **<mark style="color:green;"> <mark style="color:green;">**(with exceptions)**</mark>.

### Implementation policy

- Hold values in the form of properties based on most communication results or master data.
- All update processing within the Model is called by Lifecycle.
- **1Screen 1Model**is the default.
  - Depending on the communication content or complexity, the Model can be split.
  - However, if it becomes too granular, it is essential to link with Lifecycle to pass information between models, so in principle, we adhere to 1Model, but if it is clear that the model has become too large, we split it.
  - If you want to manage multiple elements such as list information, you can also create a Model within a Model.

### Example code

```csharp
public class TestPageModel
{
    public readonly string TestMessage;

    public TestPageModel() {
        // 통신 결과나 마스터 데이터를 기반으로 Model을 구축하기도 한다.
        TestMessage = "Test Page";
    }
}
```



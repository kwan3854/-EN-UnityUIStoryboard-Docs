# Model

### Concept

* Created in the Lifecycle.
* Has actual data in the screen.
* Only one is created per screen:&#x20;**<mark style="color:green;">**(with exceptions)**</mark>

### Implementation policy

* Hold values in the form of properties based on most communication results or master data.
* All update processing within the Model is called by Lifecycle.
* **1Screen 1Model** is the default.
  * Models can be split based on communication content or complexity.
  * In principle, we adhere to 1Model because it is essential to link with Lifecycle to pass information between models, but if it is clear that the model has become too large, we split it.
  * If you want to manage multiple elements such as list information, you can also create a Model within a Model.

### Example code

```csharp
public class TestPageModel
{ class TestPageModel
    public readonly string TestMessage;

    public TestPageModel() {
        // You can also build a model based on communication results or master data.
        TestMessage = "Test Page";
    }
}
```

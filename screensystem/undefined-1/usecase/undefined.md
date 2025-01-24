# About the timing of communication processing on screen transitions

### Timing of screen and communication processing and data processing guidelines

Outgames often use communication results to construct screens when displaying screens.

For example, you may display the character screen after acquiring character data. In this case, if the next screen requires a communication response, the communication is performed on the previous screen and the communication response is passed to the next screen as a parameter.

{% hint style="info" %}

### Shouldn't this be done?

**If the data resulting from the communication that occurred on the previous screen determines what data should be processed on the next screen,**

We had attempted to communicate within the Lifecycle of the next screen independently of the previous screen and use the responses to build it, but due to the design specifications of UnityScreenNavigator, it didn't handle well enough to cancel the screen transition and return to the previous screen (preventing the next screen from appearing in the first place) in the event of a communication error. This resulted in an uninitialized screen being displayed in the event of a communication error, so we changed it to handle the screen transition after the previous screen has communicated normally.
{% endhint %}



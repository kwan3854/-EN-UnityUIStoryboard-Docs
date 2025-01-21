# About the timing of communication processing based on screen transitions

### Timing of screen and communication processing and data processing instructions

Outgames often use communication results to organize screens when displaying screens.

For example, a character screen may be displayed after acquiring character data. In this case, if a communication response is required from the next screen, communication is performed on the previous screen and the communication response is passed to the next screen as a parameter.

{% hint style="info" %}
### Shouldn't this be done like this?

**If the data resulting from the communication that occurred on the previous screen determines the data that needs to be processed on the next screen,** then

We were attempting to communicate within the lifecycle of the next screen independently of the previous screen and use the responses to build it, but due to the design specification of UnityScreenNavigator, it didn't handle well enough to cancel the screen transition and return to the previous screen (preventing the next screen from appearing in the first place) in the event of a communication error. This resulted in an uninitialized screen being displayed in the event of a communication error, so we've changed it to handle the screen transition after the previous screen has communicated normally.
{% endhint %}


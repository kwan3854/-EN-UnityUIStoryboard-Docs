# Test & Mockup Policy

* For each screen (Page/Modal), there is a pair of real implementation code + mockup (for testing) code.
* Injecting a mockup implementation instead of the actual implementation via DI allows you to verify behavior directly in a separate test scene.
  * The test scene is set up for testing all the way up to the DI.
* This structure allows for quick UI/logic validation early in feature development.

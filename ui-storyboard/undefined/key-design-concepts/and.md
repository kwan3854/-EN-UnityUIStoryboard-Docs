# Test \& Mockup Policy

- For each screen (Page/Modal), there is a pair of actual implementation code + mockup (for testing) code.
- By injecting the mockup implementation instead of the real one via DI, you can check the behavior directly in a separate test scene.
  - The test scene is all set up for testing, including the DI.
- This structure allows for quick UI/logic validation early in feature development.



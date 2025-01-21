# UI/UX Design Principles

1. UI design, animations, etc. are the responsibility of UI/UX designers.
   1. developers are discouraged from implementing animations in code with Tween, etc. (to prevent conflicts, ease of maintenance).
2. Colors, fonts, etc. are centrally managed (using uPalette).
   1. Maintain a consistent theme/branding, not individualized.
3. All resources are addressable, and Addler is used to manage resource lifecycle (similar to RAII).
   1. Don't use the Resources folder. (No advantage over Addressable)

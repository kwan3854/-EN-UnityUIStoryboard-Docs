# UI/UX Design Principles

1. UI design, animations, etc. are the responsibility of the UI/UX designer.
  1. Make it a rule that developers don't implement animations in code with Tween, etc. (crash prevention, maintainability).
2. Manage colors, fonts, etc. centrally (leverage uPalette).
  1. Maintain a consistent theme/branding, rather than customizing individually.
3. All resources are managed as Addressable, with Addler for resource lifetime management (similar to RAII).
  1. The Resources folder is not used. (No advantage over Addressable)



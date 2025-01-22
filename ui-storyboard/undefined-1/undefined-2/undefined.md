# Determine the reference resolution

## Landscape or Portrait?

* First, decide whether you want to reference a landscape or portrait resolution.
* Unlike web-front development, gaming apps like ours are typically developed with a choice of either landscape or portrait resolutions, and fully responsive design is not considered by default.&#x20;
* Choose portrait for casual games that are oriented towards one-handed gaming, or landscape for more serious games.

## High resolution or low resolution?

* FHD, QHD, UHD... Monitor resolutions are getting higher and higher.
* So is it a good idea to future-proof your references with high resolution? -> No.
* The UI doesn't need to be high resolution.
  * UI resources have a **very, very large impact on performance**.
  * At the same time, users don't notice much of a difference when resources are high resolution.
* For moderate mobile orientation, FHD or lower resolutions are sufficient.
* For example, one of our most popular UI assets is designed for 978x1664 resolution.

*** For example, one of our popular UI assets is built for 978x1664 resolution.

For the purposes of this example guide, we'll use 1080x1920.

## Register the reference resolution in the settings

<figure><img src="../../../../.gitbook/assets/StoryboardSettings.png" alt=""><figcaption></figcaption></figure>

* The reference resolution registered here will be used as the basis for automatically generating thumbnails for Page and Modal preps in the Storyboard.
* The same resolution will be used in the Canvas that will be used in the actual game later on.

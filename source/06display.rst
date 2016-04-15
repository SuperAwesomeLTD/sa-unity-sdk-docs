Display ads
===========

In the next sections we'll see how to display banners, inline video ads, interstitials and fullscreen video ads.

We'll assume we have the same setup as the previous section, but we'll also add
four SuperAwesome display objects that we'll want to show at the press of a button
in our app.

.. code-block:: c#

    public class MainScript : MonoBehaviour, SALoaderInterface {

        // create the loader reference
        SALoader loader = null;

        // create multiple SAAd references
        SAAd bannerAdData = null;
        SAAd interstitialAdData = null;
        SAAd videoAdData = null;

        // the three display objects
        SABannerAd banner = null;
        SAInterstitialAd interstitial = null;
        SAVideoAd video = null;

        // rest of your implementation ...
    }

Banner ads
^^^^^^^^^^

To following code snippet shows you how to add a **SABannerAd** object to your app.

.. code-block:: c#

    public class MainScript : MonoBehaviour, SALoaderInterface {

        // rest of your implementation and
        // load ad data here ...

        public void showBanner() {
            if (bannerAdData != null) {
                banner = SABannerAd.createInstance ();
                banner.setAd (bannerAdData);
                banner.position = SABannerAd.BannerPosition.BOTTOM;
                banner.size = SABannerAd.BannerSize.BANNER_320_50;
                banner.play ();
            }
        }
    }

Notice that the SABannerAd class is calling the Android or iOS native components to display on screen.

The two functions to pay attention here are **setAd(SAAd ad)** and **play()**.

* **setAd(SAAd ad)** takes a SAAd object as parameter, in this case bannerAdData. It tells the banner what ad data to try to display.
* **play()** actually starts the display process on screen.

Interstitial ads
^^^^^^^^^^^^^^^^

Interstitial ads are represented by objects of type **SAInterstitialAd**.

.. code-block:: c#

    public class MainScript : MonoBehaviour, SALoaderInterface {

        // rest of your implementation and
        // load ad data here ...

        public void showInterstitial() {
            if (interstitialAdData != null) {
                interstitial = SAInterstitialAd.createInstance ();
                interstitial.setAd(interstitialAdData);
                interstitial.play();
            }
        }
    }

Again, notice the presence of setAd(SAAd ad) and play() - they perform the same role as for banner ads.
Interstitials are shown as fullscreen ads, on top of any existing content.
For Android a new Activity will be launched and for iOS a new View Controller.
Interstitial ads have their own SDK-provided close button.

Fullscreen video ads
^^^^^^^^^^^^^^^^^^^^

Finally, fullscreen video ads are represented by **SAVideoAd**.

.. code-block:: c#

    public class MainScript : MonoBehaviour, SALoaderInterface {

        // rest of your implementation and
        // load ad data here ...

        public void showVideo() {
            if (videoAdData != null) {
                video = SAVideoAd.createInstance ();
                video.setAd(videoAdData);
                video.shouldShowCloseButton = true;
                video.shouldAutomaticallyCloseAtEnd = true;
                video.play ();
            }
        }
    }

They're similar to interstitial ads, but notice there are two parameters you can set, **shouldShowCloseButton** and
**shouldAutomaticallyCloseAtEnd**.

Ad callbacks
============

Once an ad starts playing, it will send back callbacks to notify you that it has finished different lifecycle activities.
To respond to them we'll use a similar interface / delegate pattern as with SALoaderInterface.

Standard ad callbacks
^^^^^^^^^^^^^^^^^^^^^

To catch standard ad callbacks:

* your script must implement the **SAAdInterface** interface:

.. code-block:: c#

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAAdInterface {

        SAAd bannerAdData = null;
        SABannerAd banner = null;

        // rest of the implementation ...
    }

* the script must be set as delegate for your display objects:

.. code-block:: c#

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAAdInterface {

        // rest of your implementation and
        // load ad data here ...

        public void showBanner() {
            if (bannerAdData != null) {
                banner = SABannerAd.createInstance ();
                banner.setAd (bannerAdData);
                banner.adDelegate = this;
                banner.position = SABannerAd.BannerPosition.BOTTOM;
                banner.size = SABannerAd.BannerSize.BANNER_320_50;
                banner.play ();
            }
        }
    }

* your script must implement the callback methods specified by SAAdInterface:

.. code-block:: c#

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAAdInterface {

        // rest of your implementation and
        // load ad data here ...

        public void adWasShown(int placementId) {
            // called when an ad is first shown
        }

        public void adFailedToShow(int placementId) {
            // called when an ad is not shown
            // because of some internal errors
            // or lack of internet connectivity
        }

        public void adWasClosed(int placementId) {
            // available only for interstitial and
            // fullscreen video ads
            //
            // signals when an ad is closes
        }

        public void adWasClicked(int placementId) {
            // called when an ad is clicked
        }

        public void adHasIncorrectPlacement(int placementId) {
            // called when an ad has an incorrect
            // placement type for the ad it's trying to
            // show
            // e.g. a SAVideoAd object with a bannerAdData
            // SAAd object
        }
    }

Parental gate callbacks
^^^^^^^^^^^^^^^^^^^^^^^

To catch parental gate callbacks:

* your script must implement the **SAParentalGateInterface** interface:

.. code-block:: c#

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAParentalGateInterface {

        SAAd bannerAdData = null;
        SABannerAd banner = null;

        // rest of the implementation ...
    }

* the script must be set as delegate for your display objects:

.. code-block:: c#

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAParentalGateInterface {

        // rest of your implementation and
        // load ad data here ...

        public void showBanner() {
            if (bannerAdData != null) {
                banner = SABannerAd.createInstance ();
                banner.setAd (bannerAdData);
                banner.parentalGateDelegate = this;
                banner.position = SABannerAd.BannerPosition.BOTTOM;
                banner.size = SABannerAd.BannerSize.BANNER_320_50;
                banner.play ();
            }
        }
    }

* your script must implement the callback methods specified by SAAdInterface:

.. code-block:: c#

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAParentalGateInterface {

        // rest of your implementation and
        // load ad data here ...

        public void parentalGateWasCanceled(int placementId) {
            // this function is called when a
            // parental gate pop-up "cancel" button is pressed
        }

        public void parentalGateWasFailed(int placementId) {
            // this function is called when a
            // parental gate pop-up "continue" button is
            // pressed and the parental gate
            // failed (because the numbers weren't OK)
        }

        public void parentalGateWasSucceded(int placementId) {
            // this function is called when a
            // parental gate pop-up "continue" button is
            // pressed and the parental gate succeeded
        }
    }

Video callbacks
^^^^^^^^^^^^^^^

To catch video ad callbacks (available only for SAVideoAd objects):

* your script must implement the **SAVideoAdInterface** interface:

.. code-block:: c#

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAVideoAdInterface {

        SAAd videoAdData = null;
        SAVideoAd video = null;

        // rest of the implementation ...
    }

* the script must be set as delegate for your display objects:

.. code-block:: c#

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAVideoAdInterface {

        // rest of your implementation and
        // load ad data here ...

        public void showVideo() {
            if (videoAdData != null) {
                video = SAVideoAd.createInstance ();
                video.setAd(videoAdData);
                video.shouldShowCloseButton = true;
                video.shouldAutomaticallyCloseAtEnd = true;
                video.videoAdDelegate = this;
                video.play ();
            }
        }
    }

* your script must implement the callback methods specified by SAAdInterface:

.. code-block:: c#

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAVideoAdInterface {

        // rest of your implementation and
        // load ad data here ...

        public void adStarted(int placementId) {
            // fired when an ad has started
        }

        public void videoStarted(int placementId) {
            // fired when a video ad has started
        }

        public void videoReachedFirstQuartile(int placementId) {
            // fired when a video ad has reached 1/4 of total duration
        }

        public void videoReachedMidpoint(int placementId) {
            // fired when a video ad has reached 1/2 of total duration
        }

        public void videoReachedThirdQuartile(int placementId) {
            // fired when a video ad has reached 3/4 of total duration
        }

        public void videoEnded(int placementId) {
            // fired when a video ad has ended
        }

        public void adEnded(int placementId) {
            // fired when an ad has ended
        }

        public void allAdsEnded(int placementId) {
            // fired when all ads have ended
        }
    }

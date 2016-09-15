Banner Ads
==========

The following block of code creates and loads a banner ad:

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        private SABannerAd banner = null;

        // initialization
        void Start () {

            // create a new banner
            banner = SABannerAd.createInstance ();

            // Enabling test mode will load
            // one of our test ads
            // By default it is disabled
            banner.enableTestMode ();

            // The parental gate requires users to
            // perform a simple math operation when
            // clicking on an ad
            banner.enableParentalGate ();

            // Finally you can start the loading
            // process by telling the SDK to load an
            // ad for a certain placement
            banner.load (30471);
        }
    }

Once you've loaded an ad, you can also display it:

.. code-block:: c#

    public void onClick () {

        // It's good practice to check first
        // if there is an ad available
        if (banner.hasAdAvailable ()) {

            // you can also setup a size
            // for your banner
            banner.setSize_320_50 ();

            // a background color
            banner.setColorGray ();

            // or display it on the top or bottom
            // of the screen
            banner.setPositionTop ();

            // if all is OK you may play the ad
            banner.play ();
        }
    }

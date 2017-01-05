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

            // to display test ads
            banner.enableTestMode ();

            // ask users to add two numbers when clicking on an ad
            banner.enableParentalGate ();

            // start loading ad data for a placement
            banner.load (30471);
        }
    }

Once you've loaded an ad, you can also display it:

.. code-block:: c#

    public void onClick () {

        // check if ad is loaded
        if (banner.hasAdAvailable ()) {

            // set a size template
            banner.setSize_320_50 ();

            // set a background color
            banner.setColorGray ();

            // choose between top or bottom
            banner.setPositionTop ();

            // display the ad
            banner.play ();
        }
    }

Video Ads
=========

The following code block sets up a video ad and loads it:

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        // initialization
        void Start () {

            // to display test ads
            SAVideoAd.enableTestMode ();

            // ask users to add two numbers when clicking on an ad
            SAVideoAd.enableParentalGate ();

            // lock orientation to portrait or landscape
            SAVideoAd.setOrientationPortrait ();

            // enable or disable the android back button
            SAVideoAd.enableBackButton ();

            // enable or disable a close button
            SAVideoAd.disableCloseButton ();

            // enable or disable auto-closing at the end
            SAVideoAd.disableCloseAtEnd ();

            // start loading ad data for a placement
            SAVideoAd.load (30479);
        }
    }

Once you've loaded an ad, you can also display it:

.. code-block:: c#

    public void playVideo () {

        // check if ad is loaded
        if (SAVideoAd.hasAdAvailable (30479)) {

            // display the ad
            SAVideoAd.play (30479);
        }
    }

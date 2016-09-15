Interstitial Ads
================

The following code block sets up an interstitial ad and loads it:

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        // initialization
        void Start () {

            // Enabling test mode will load
            // one of our test ads
            // By default it is disabled
            SAInterstitialAd.enableTestMode ();

            // You can also specify a certain
            // orientation for your interstitial ad
            SAInterstitialAd.setOrientationPortrait ();

            // The parental gate requires users to
            // perform a simple math operation when
            // clicking on an ad
            SAInterstitialAd.enableParentalGate ();

            // Finally you can start the loading
            // process by telling the SDK to load an
            // ad for a certain placement
            SAInterstitialAd.load (30473);
        }
    }

Once you've loaded an ad, you can also display it:

.. code-block:: c#

    public void playInterstitial () {

        // It's good practice to check first
        // if there is an ad available
        if (SAInterstitialAd.hasAdAvailable (30473)) {

            // if all is OK you may play the ad
            SAInterstitialAd.play (30473);
        }
    }

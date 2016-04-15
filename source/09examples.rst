Examples
========

Simple example
^^^^^^^^^^^^^^

The first example shows how you can add a banner ad in your app with just a
few lines of code.

.. code-block:: c#

    using UnityEngine;
    using System.Collections;
    using SuperAwesome;

    public class MainScript : MonoBehaviour, SALoaderInterface {

        // create the a loader and banner
        SALoader loader = null;
        SABannerAd banner = null;

        void Start () {

            // setup AwesomeAds
            SuperAwesome.SuperAwesome.instance.enableTestMode ();

            loader = SALoader.createInstance ();
            loader.loaderDelegate = this;
            loader.loadAd (30471);
        }

        // Update is called once per frame
        void Update () {

        }

        public void didLoadAd(SAAd ad) {
            banner = SABannerAd.createInstance ();
            banner.setAd (ad);
            banner.position = SABannerAd.BannerPosition.BOTTOM;
            banner.size = SABannerAd.BannerSize.BANNER_320_50;
            banner.play ();
        }

        public void didFailToLoadAd(int placementId) {
            // at this moment no ad could be found
        }
    }

Complex example
^^^^^^^^^^^^^^^

This example shows how you can add different types of ads and make them respond to
multiple callbacks.

.. code-block:: c#

    using UnityEngine;
    using System.Collections;
    using SuperAwesome;

    public class MainScript : MonoBehaviour,
                              SALoaderInterface,
                              SAAdInterface,
                              SAParentalGateInterface,
                              SAVideoAdInterface {

        // create the loader reference
        SALoader loader = null;

        // create multiple SAAd references
        SAAd bannerAdData = null;
        SAAd interstitialAdData = null;
        SAAd videoAdData = null;

        // create multiple display ads
        SABannerAd banner = null;
        SAInterstitialAd interstitial = null;
        SAVideoAd video = null;

        void Start () {

            // setup AwesomeAds
            SuperAwesome.SuperAwesome.instance.enableTestMode ();

            loader = SALoader.createInstance ();
            loader.loaderDelegate = this;
            // load all ad data in parallel
            loader.loadAd(30471);
            banner.loadAd(30473);
            banner.loadAd(30479);
        }

        // Update is called once per frame
        void Update () {

        }

        //
        // SALoaderInterface implementation
        public void didLoadAd(SAAd ad) {
            // at this moment ad data is ready
            // and can be saved
            if (ad.placementId == 30471) {
                bannerAdData = ad;
            } else if (ad.placementId == 30473) {
                interstitialAdData = ad;
            } else if (ad.placementId == 30479) {
                videoAdData = ad;
            }
        }

        public void didFailToLoadAd(int placementId) {
            // at this moment no ad could be found
        }

        //
        // button clicks
        public void showBanner() {
            if (bannerAdData != null) {
                banner = SABannerAd.createInstance ();
                banner.setAd (bannerAdData);
                banner.position = SABannerAd.BannerPosition.BOTTOM;
                banner.size = SABannerAd.BannerSize.BANNER_320_50;
                banner.adDelegate = this;
                banner.play ();
            }
        }

        public void showInterstitial() {
            if (interstitialAdData != null) {
                interstitial = SAInterstitialAd.createInstance ();
                interstitial.setAd(interstitialAdData);
                interstitial.isParentalGateEnabled = true;
                interstitial.parentalGateDelagete = this;
                interstitial.play();
            }
        }

        public void showVideo() {
            if (videoAdData != null) {
                video = SAVideoAd.createInstance ();
                video.setAd(videoAdData);
                video.shouldShowCloseButton = true;
                video.shouldAutomaticallyCloseAtEnd = true;
                video.adDelegate = this;
                video.isParentalGateEnabled = false;
                video.videoAdDelegate = this;
                video.play ();
            }
        }

        //
        // SAAdInterface implementation
        public void adWasShown(int placementId) {
            Debug.Log("Ad " + placementId + " was loaded");
        }

        public void adFailedToShow(int placementId) {}
        public void adWasClosed(int placementId) {}
        public void adWasClicked(int placementId) {}
        public void adHasIncorrectPlacement(int placementId) {}

        //
        // SAParentalGateInterface implementation
        public void parentalGateWasCanceled(int placementId) {}
        public void parentalGateWasFailed(int placementId) {}
        public void parentalGateWasSucceded(int placementId) {}

        //
        // SAVideoAdInterface implementation
        public void adStarted(int placementId) {}
        public void videoStarted(int placementId) {}
        public void videoReachedFirstQuartile(int placementId) {}

        public void videoReachedMidpoint(int placementId) {
            Debug.Log("Ad " + placementId + " reached midpoint");
        }

        public void videoReachedThirdQuartile(int placementId) {}
        public void videoEnded(int placementId) {}
        public void adEnded(int placementId) {}
        public void allAdsEnded(int placementId) {}
    }

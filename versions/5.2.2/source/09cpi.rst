Handle CPI
==========

You can install and use the SuperAwesome SDK as an advertiser as well, if you want to measure your CPI (Cost per Install)
performance.

In order to do that you can call:

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        // Use this for initialization
        void Start () {
          SuperAwesome.SuperAwesome.instance.handleCPI ((success) => {
            // this callback method will indicate if the AwesomeAds server
            // considered the install event you sent a success or not
          });
        }

        // Update is called once per frame
        void Update () {
            // ...
        }
    }

On Android you also have to make sure that the following receiver is registered in your ApplicationManifest.xml file
(and it should be automatically added by the SuperAwesome SDK when you build to Android):

.. code-block:: shell

    <receiver android:name="tv.superawesome.sdk.cpi.SACPI"
              android:exported="false"
              android:permission="tv.superawesome.sdk.SuperAwesomeSDK">
              <intent-filter>
                <action android:name="com.android.vending.INSTALL_REFERRER"/>
              </intent-filter>
   </receiver>

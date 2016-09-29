Handle CPI
==========

You can install and use the SuperAwesome SDK as an advertiser as well, if you want to measure your CPI (Cost per Install)
performance.

In order to do that you can call:

.. code-block:: c#

    public class MainScript : MonoBehaviour {

        // Use this for initialization
        void Start () {
            SuperAwesome.SuperAwesome.instance.handleCPI ();
        }

        // Update is called once per frame
        void Update () {
            // ...
        }
    }

The previous call will have an direct effect on your iOS build.

On Android on the other hand you don't have to explicitly call **handleCPI**, you just have to make sure that
the following receiver is registered in your ApplicationManifest.xml file (and it should be automatically added by the
SuperAwesome SDK when you build to Android):

.. code-block:: shell

    <receiver android:name="tv.superawesome.sdk.cpi.SACPI" android:exported="true">
        <intent-filter><action android:name="com.android.vending.INSTALL_REFERRER"/></intent-filter>
    </receiver>

# Alerts from the US National Weather Service  (nws_alerts)

An updated version of the nws_alerts custom integration for Home Assistant originally found at github.com/eracknaphobia/nws_custom_component and more recently https://github.com/finity69x2/nws_alerts.

This integration retrieves updated weather alerts every minute from the US NWS API (by default but it can be changed in the config options).

You can configure the integration to use your NWS Zone, your precise location via GPS coordinates or you can get dynamic location alerts by configuring the integration to use a device_tracker entity from HA as long as that device tracker provides GPS coordinates.

The integration presents the number of currently active alerts as the state of the sensor and lists many alert details as a list in the attributes of the sensor.

## Installation:

<b>Manually:</b>

Clone the Repository and copy the "nws_alerts" directory to your "custom_components" directory in your config directory

```<config directory>/custom_components/nws_alerts/...```

<b>HACS:</b>

open the HACS section of Home Assistant.

Click the "+ Explore & Download Repositories" button in the bottom right corner.

In the window that opens search for "NWS Alerts".

In the window that opens when you select it click om "Install This Repository in HACS"

After installing the integration you can then configure it using the instructions in the following section.

## Configuration:

There are two ways to configure this integration.

<b>You can configure the integration via the "Configuration->Integrations" section of the Home Assistant UI:</b>

Click on "+ Add Integration" buuton in the bottom right corner.

Search for "NWS Alerts" in the list of integrations and follow the UI prompts to configure the sensor.

You can find your Zone or County ID by going to https://alerts.weather.gov/, scroll down to your state and click on the “zone list” and/or "county list" then look for the entry for your county.

There are a few configuration method options to select from.

Please see the following link to help you decide which option to use:

https://github.com/SirIndubitable/nws_alerts/blob/master/lookup_options.md

If you select the "Using a device tracker" option under the "GPS Location" option then HA will use the GPS coordinates provided by that tracker to query for alerts so you should follow the same recommendations for using GPS coordinates when using that option.

After you restart Home Assistant then you should have a new sensor called "sensor.nws_alerts" in your system.

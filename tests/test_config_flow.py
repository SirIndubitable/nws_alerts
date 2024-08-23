"""Test for config flow"""

from unittest.mock import patch

import pytest
from homeassistant import config_entries, setup
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType

from custom_components.nws_alerts.const import DOMAIN

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize(
    "steps,title,data",
    [
        (
            "Zone Form",
            [
                {"next_step_id": "zone"},
                {
                    "name": "Zone Form",
                    "zone_id": "AZZ540,AZC013",
                    "interval": 5,
                    "timeout": 120,
                },
            ],
            {
                "name": "Zone Form",
                "zone_id": "AZZ540,AZC013",
                "interval": 5,
                "timeout": 120,
            },
        ),
        (
            "GPS Form",
            [
                {"next_step_id": "gps"},
                {"next_step_id": "gps_loc"},
                {
                    "name": "GPS Form",
                    "gps_loc": "123,-456",
                    "interval": 5,
                    "timeout": 120,
                },
            ],
            {
                "name": "GPS Form",
                "gps_loc": "123,-456",
                "interval": 5,
                "timeout": 120,
            },
        ),
    ],
)
async def test_form(
    title: str,
    steps: list,
    data: dict,
    hass: HomeAssistant,
):
    """Test we get the form."""
    await setup.async_setup_component(hass, "persistent_notification", {})

    with (
        patch(
            "custom_components.nws_alerts.config_flow._get_zone_list", return_value=None
        ),
        patch(
            "custom_components.nws_alerts.async_setup_entry",
            return_value=True,
        ) as mock_setup_entry,
    ):
        result = await hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_USER}
        )

        for index, step in enumerate(steps):
            if index == (len(steps) - 1):
                assert result["type"] == FlowResultType.FORM
            else:
                assert result["type"] == FlowResultType.MENU

            result = await hass.config_entries.flow.async_configure(
                result["flow_id"], step
            )
            await hass.async_block_till_done()

        assert result["title"] == title
        assert result["type"] == "create_entry"
        assert result["data"] == data

        await hass.async_block_till_done()
        assert len(mock_setup_entry.mock_calls) == 1


# @pytest.mark.parametrize(
#     "user_input",
#     [
#         {
#             DOMAIN: {
#                 CONF_NAME: "NWS Alerts",
#                 CONF_ZONE_ID: "AZZ540,AZC013",
#             },
#         },
#     ],
# )
# async def test_import(hass, user_input):
#     """Test importing a gateway."""
#     await setup.async_setup_component(hass, "persistent_notification", {})

#     with patch(
#         "custom_components.nws_alerts.async_setup_entry",
#         return_value=True,
#     ):
#         result = await hass.config_entries.flow.async_init(
#             DOMAIN, data=user_input, context={"source": config_entries.SOURCE_IMPORT}
#         )
#         await hass.async_block_till_done()

#     assert result["type"] == "create_entry"

from decimal import Decimal
from typing import Any, Dict

from pydantic import Field, SecretStr

from hummingbot.client.config.config_data_types import BaseConnectorConfigMap, ClientFieldData
from hummingbot.core.data_type.trade_fee import TradeFeeSchema

CENTRALIZED = True
EXAMPLE_PAIR = "ZRX-ETH"

DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.001"),
    taker_percent_fee_decimal=Decimal("0.001"),
    buy_percent_fee_deducted_from_returns=True
)


def is_exchange_information_valid(exchange_info: Dict[str, Any]) -> bool:
    """
    Verifies if a trading pair is enabled to operate with based on its exchange information
    :param exchange_info: the exchange information for a trading pair
    :return: True if the trading pair is enabled, False otherwise
    """
    return exchange_info.get("status", None) == "TRADING" and "SPOT" in exchange_info.get("permissions", list())


class GsudemoConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="gsudemo", const=True, client_data=None)
    gsudemo_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your GSU-demo API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    gsudemo_api_secret: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your GSU-demo API secret",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )

    class Config:
        title = "gsudemo"


KEYS = GsudemoConfigMap.construct()

OTHER_DOMAINS = ["gsudemo_us"]
OTHER_DOMAINS_PARAMETER = {"gsudemo_us": "us"}
OTHER_DOMAINS_EXAMPLE_PAIR = {"gsudemo_us": "BTC-USDT"}
OTHER_DOMAINS_DEFAULT_FEES = {"gsudemo_us": DEFAULT_FEES}


class GsudemoUSConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="gsudemo_us", const=True, client_data=None)
    gsudemo_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your gsudemo US API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    gsudemo_api_secret: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your gsudemo US API secret",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )

    class Config:
        title = "gsudemo_us"


OTHER_DOMAINS_KEYS = {"gsudemo_us": gsudemoUSConfigMap.construct()}

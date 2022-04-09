from brownie import FundMe, MockV3Aggregator, network, config
from scripts.utils import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVS


def deploy_fund_me():
    account = get_account()
    # 0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract fund_me deployed with address {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()

from brownie import FundMe, accounts

from scripts.utils import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entranceFee = fund_me.getEntranceFee()
    print(f"The enty fee is {entranceFee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entranceFee})


def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()

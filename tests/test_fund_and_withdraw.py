from brownie import accounts, network, exceptions
import pytest
from scripts.deploy import deploy_fund_me
from scripts.utils import LOCAL_BLOCKCHAIN_ENVS, get_account


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVS:
        pytest.skip("only for locat testing")

    account = get_account()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})

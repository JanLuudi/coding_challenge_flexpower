import sqlite3
import pandas as pd


def compute_total_buy_volume() -> float:
    """
    Compute the total buy volume of trades in the "epex_12_20_12_13" table in the "trades.sqlite" database.
    The function returns a float representing the total buy volume.
    """
    con = sqlite3.connect("data/trades.sqlite")
    # Load the relevant data
    trades = pd.read_sql_query(
        "SELECT quantity * price AS value, side from 'epex_12_20_12_13';", con
    )
    trades_groups = trades.groupby("side").sum()
    return trades_groups.loc["buy"].value


def compute_total_sell_volume() -> float:
    """
    Compute the total sell volume of trades in the "epex_12_20_12_13" table in the "trades.sqlite" database.
    The function returns a float representing the total sell volume.
    """
    con = sqlite3.connect("data/trades.sqlite")
    # Load the relevant data
    trades = pd.read_sql_query(
        "SELECT quantity * price AS value, side from 'epex_12_20_12_13';", con
    )
    trades_groups = trades.groupby("side").sum()
    return trades_groups.loc["sell"].value


def compute_pnl(strategy_id: str) -> float:
    """
    Compute the profit and loss (PNL) of a specific strategy in the "epex_12_20_12_13" table in the "trades.sqlite" database.
    The function returns a float representing the PNL for the given strategy.

    Parameters:
        strategy_id: The id of the strategy to compute PNL for
    """
    con = sqlite3.connect("data/trades.sqlite")
    # Load the relevant data
    trades = pd.read_sql_query(
        "SELECT quantity * price AS value, side, strategy from 'epex_12_20_12_13';",
        con,
    )
    if strategy_id not in trades.strategy.unique():
        return 0

    strategy = trades.groupby("strategy").get_group(strategy_id)
    mapping = {"buy": -1, "sell": 1}
    strat_value = sum(strategy.value * strategy.side.map(mapping))

    return strat_value

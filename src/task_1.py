from src.trading_methods import (
    compute_total_buy_volume,
    compute_total_sell_volume,
)

if __name__ == "__main__":
    print(f"Total buy volume in the dataset is {compute_total_buy_volume()} €")
    print(
        f"Total sell volume in the dataset is {compute_total_sell_volume()} €"
    )

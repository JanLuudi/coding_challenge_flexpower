from flask import Flask, jsonify
from datetime import datetime
from src.trading_methods import compute_pnl

app = Flask(__name__)


@app.route("/pnl/<strategy_id>", methods=["GET"])
def pnl(strategy_id):
    """
    Endpoint for computing the profit and loss (PNL) of a specific strategy.
    The endpoint returns a JSON object containing the PNL value, unit, capture time, and strategy id.

    Parameters:
        strategy_id: The id of the strategy to compute PNL for
    """
    result = compute_pnl(strategy_id)
    return jsonify(
        strategy=strategy_id,
        value=result,
        unit="euro",
        capture_time=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
    )


if __name__ == "__main__":
    # normally, you would use the host address of the target web application
    app.run(host="0.0.0.0")

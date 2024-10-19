from flask import Flask, jsonify, request

from services.yfinance import fetch_stock_data, fetch_currency_data

app = Flask(__name__)

@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock_data(ticker):
    try:
        interval_param = request.args.get('interval', '1mo')
        period_param = request.args.get('period', '1y')

        data = fetch_stock_data(ticker, interval_param, period_param)
        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/currency/<ticker>', methods=['GET'])
def get_currency_data(ticker):
    try:
        interval_param = request.args.get('interval', '1mo')
        period_param = request.args.get('period', '1y')

        data = fetch_currency_data(ticker, interval_param, period_param)
        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

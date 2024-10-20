import psycopg2
import json
from services.finance_api import convert_asset_to_currency

def get_customer_asset_types_from_db(customer_id):
    try:
        connection = psycopg2.connect(
            dbname='collabothon',
            user='root',
            password='12345',
            host='localhost',
            port='5432'
        )

        cursor = connection.cursor()

        cursor.execute('''
            SELECT name, amount, type FROM customers_assets ca
            INNER JOIN assets a on ca.asset_id = a.asset_id
            WHERE customer_id = %s''', (customer_id,))

        rows = cursor.fetchall()

        colnames = [desc[0] for desc in cursor.description]

        assets = [dict(zip(colnames, row)) for row in rows]

        summary = {}

        for asset in assets:
            ticker = asset['name']
            value = float(asset['amount'])
            asset_type = asset['type']

            converted_asset = convert_asset_to_currency(ticker, value, asset_type, convert_to='USD')
            if 'error' in converted_asset:
                print(converted_asset['error'])
                continue

            _, asset_type, converted_value = converted_asset

            if asset_type in summary:
                summary[asset_type] += converted_value
            else:
                summary[asset_type] = converted_value

        cursor.close()
        connection.close()
        return summary

    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return json.dumps({"error": str(error)})

def get_customer_assets_from_db(customer_id):
    try:
        connection = psycopg2.connect(
            dbname='collabothon',
            user='root',
            password='12345',
            host='localhost',
            port='5432'
        )

        cursor = connection.cursor()

        cursor.execute('''
            SELECT name, amount, type FROM customers_assets ca
            INNER JOIN assets a on ca.asset_id = a.asset_id 
            WHERE customer_id = %s''', (customer_id,))

        rows = cursor.fetchall()

        colnames = [desc[0] for desc in cursor.description]

        assets = [dict(zip(colnames, row)) for row in rows]

        cursor.close()
        connection.close()

        return assets

    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return json.dumps({"error": str(error)})

if __name__ == '__main__':
    customer_id = 1
    assets_json = get_customer_asset_types_from_db(customer_id)
    print(assets_json)

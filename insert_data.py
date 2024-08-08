import pandas as pd
from get_data import get_data
from connector import set_connection

gas_prices = get_data('gas_prices')
new_train = get_data('new_train')
client = get_data('client')
electricity_prices = get_data('electricity_prices')
forecast_weather = get_data('forecast_weather')
historical_weather = get_data('historical_weather')
weather_station_to_county_mapping = get_data('weather_station_to_county_mapping')

with set_connection() as ps:
    gas_prices.to_sql(
        name='gas_prices',
        schema='energy_data',
        con=ps,
        index=False,
        if_exists='append'
    )
    new_train.to_sql(
        name='new_train',
        schema='energy_data',
        con=ps,
        index=False,
        if_exists='append'
    )
    client.to_sql(
        name='client',
        schema='energy_data',
        con=ps,
        index=False,
        if_exists='append'
    )
    electricity_prices.to_sql(
        name='electricity_prices',
        schema='energy_data',
        con=ps,
        index=False,
        if_exists='append'
    )
    forecast_weather.to_sql(
        name='forecast_weather',
        schema='energy_data',
        con=ps,
        index=False,
        if_exists='append'
    )
    historical_weather.to_sql(
        name='historical_weather',
        schema='energy_data',
        con=ps,
        index=False,
        if_exists='append'
    )
    weather_station_to_county_mapping.to_sql(
        name='weather_station_to_county_mapping',
        schema='energy_data',
        con=ps,
        index=False,
        if_exists='append'
    )


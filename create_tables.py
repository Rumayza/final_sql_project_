from connector import set_connection
from sqlalchemy import text

tbl_creation_query = """
SET search_path = energy_data;

CREATE TABLE IF NOT EXISTS gas_prices (
    forecast_date DATE ,
    lowest_price_per_mwh FLOAT NOT NULL,
    highest_price_per_mwh FLOAT NOT NULL,
    origin_date DATE,
    data_block_id INT
);

CREATE TABLE IF NOT EXISTS new_train (
    row_id SERIAL,
    county INT,
    county_name VARCHAR,
    is_business INT,
    product_type INT, 
    target FLOAT,
    is_consumption INT,
    datetime date,
    data_block_id INT, 
    prediction_unit_id INT
);

CREATE TABLE IF NOT EXISTS client (
    county INT,
    product_type INT,
    eic_count INT,
    installed_capacity FLOAT,
    is_business INT,
    date DATE,
    data_block_id INT
);

CREATE TABLE IF NOT EXISTS electricity_prices (
    forecast_date DATE, 
    euros_per_mwh FLOAT NOT NULL,
    origin_date DATE NOT NULL,
    data_block_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS forecast_weather (
    latitude FLOAT,
    longitude FLOAT, 
    origin_datetime TIMESTAMP,
    hours_ahead INT,
    temperature FLOAT, 
    dewpoint FLOAT,
    cloudcover_high FLOAT,
    cloudcover_low FLOAT,
    cloudcover_mid FLOAT,
    cloudcover_total FLOAT,
    TenMetreUWindComponent FLOAT,
    TenMetreVWindComponent FLOAT,
    data_block_id INT,
    forecast_datetime TIMESTAMP,
    direct_solar_radiation FLOAT,
    surface_solar_radiation_downwards FLOAT,
    snowfall FLOAT,
    total_precipitation FLOAT
);

CREATE TABLE IF NOT EXISTS historical_weather (
    datetime TIMESTAMP ,
    temperature FLOAT,
    dewpoint FLOAT, 
    rain FLOAT, 
    snowfall FLOAT,
    surface_pressure FLOAT,
    cloudcover_total INT,
    cloudcover_low INT, 
    cloudcover_mid INT,
    cloudcover_high INT,
    windspeed_10m FLOAT,
    winddirection_10m INT,
    shortwave_radiation FLOAT,
    direct_solar_radiation FLOAT,
    diffuse_radiation FLOAT,
    latitude FLOAT,
    longitude FLOAT,
    data_block_id FLOAT
);

CREATE TABLE IF NOT EXISTS weather_station_to_county_mapping (
    county float,  
    county_name VARCHAR,
    longitude FLOAT,
    latitude FLOAT
);
"""

with set_connection() as ps:
    ps.execute(text(tbl_creation_query))
    ps.commit()

# Flight Load Forecasting

## 1. Background and Overview
This project forecasts flight load factors by processing and analyzing flight segment data from the [BTS DB28DS dataset](https://www.bts.gov/browse-statistical-products-and-data/bts-publications/data-bank-28ds-t-100-domestic-segment-data). The data is downloaded, unzipped, processed, and aggregated to create a comprehensive dataset for predictive modeling. 

### Business Goals:
The business goal is to forecast monthly load factors for specific origin-destination routes to optimize airline operations, revenue management, and customer satisfaction. By leveraging historical data on available seats, passengers transported, and other operational metrics, the goal is to:

- **Improve Capacity Utilization**: By forecasting load factors at the route level, the airline can adjust flight frequencies, aircraft size, and seat allocation to align with expected demand, ensuring that resources are used efficiently and minimizing underfilled or overfilled flights.

- **Enhance Revenue Management**: Accurate load factor predictions enable the airline to implement dynamic pricing strategies, optimizing ticket prices based on demand forecasts. This helps maximize revenue per flight while maintaining high load factors on popular routes and dates.

- **Optimize Operational Efficiency**: Forecasting at the monthly and route level allows for better crew scheduling, fuel planning, and ground services coordination, leading to cost savings and improved operational efficiency.

- **Support Strategic Network Decisions**: Insights from load factor forecasts will guide decisions about route expansions, seasonal adjustments, or discontinuations of underperforming routes, ensuring that the airline's network is aligned with market demand trends.

## 2. Data Structure Overview
The raw dataset is downloaded from the BTS website and contains flight-level details, which include:
- **Date**: Year and month of the flight.
- **Route**: Origin and destination airports.
- **Carrier**: Airline operating the flight.
- **Passengers**: Number of passengers flown.
- **Available Seats**: Total seat capacity on the flight.
- **Load Factor**: The calculated ratio of passengers to available seats.
  
### Data Processing Steps:
1. **Downloading and Unzipping**: Files are downloaded using `requests` and unzipped into the working directory.
2. **Processing `.asc` Files**: Each file is loaded into a Pandas DataFrame. Depending on the number of columns (28 or 29), the files are cleaned, and columns are assigned appropriate names.
3. **Filtering by Carrier**: Data is filtered to focus on American Airlines (Carrier Code: "AA").
4. **Load Factor Calculation**: A new column for load factor is calculated using `Passengers Transported / Available Seats`.

## 3. Executive Summary
This project uses historical flight segment data to develop forecasts of flight load factors. By processing and aggregating multiple months of BTS data, it provides insights into seat occupancy trends, particularly for American Airlines. Forecasts help optimize pricing, fleet management, and resource allocation for airlines.

## 4. Insights Deep Dive
- **Load Factor Trends**: Load factors vary significantly across months and routes, with higher occupancy during holiday seasons.
- **Carrier-Specific Insights**: By filtering for American Airlines, the analysis provides focused insights into this carrier’s operational efficiency.
- **Capacity Utilization**: Analysis reveals certain routes and times of year where capacity is under- or over-utilized.

## 5. Recommendations
- **Dynamic Pricing**: Airlines can use forecasted load factors to dynamically adjust pricing to match demand.
- **Route Adjustments**: Forecasting identifies high-demand routes, enabling airlines to adjust flight frequencies or allocate larger aircraft.
- **Operational Planning**: Anticipate higher staffing and resources during peak seasons based on load factor predictions.
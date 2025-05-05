# strava-insights
Turn your Strava runs into data gold. This project pulls your running stats, works its magic with dbt and Dagster, and serves up slick visual insights on a dashboard. Run, fetch, transform, repeat.

The outline of the project is:
1. Scrape data from Strava using Strava API (Dagster / Airflow)
2. Run a pre-processing script to fetch gpx data (Dagster / Airflow)
3. Create incremental model scripts using dbt 
   1. Rolling average of pace over a 1 week(?) window 
   2. Rolling average of pace (for 5k - 10k runs) over a 1 week(?) window 
   3. Rolling average of heart rate over a 1 week(?) window 
   4. Last (e.g. in the last 6 months) fastest x distance run (including fastest x km in an x+y km distance run)
4. Progress on Goals 
5. Use streamlit to present the data visualizations 
6. Use pytest for unit / integration testing

## How to run
### 1. Authenticate with Strava

#### Acknowledgements
<img src="assets/api_logo_pwrdBy_strava_horiz_white.png" width="150" alt="Strava API Logo" />

## TODO:
- [ ] Integrate with Strava
  - Use OAuth
    - Use Access Token to access oauth/authorize endpoint 
    - Receive code
    - Use code to get access token
    - Implement refresh token logic
  - Automate the authentication process
  - Determine if required to integrate with webhook, could be useful when getting new activities

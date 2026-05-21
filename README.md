# YOUTUBE TRENDING ANALYTICS PIPELINE

## Project Overview
This project builds an End-to-End Data Pipeline to automate the collection, storage, transformation, and visualization of YouTube Trending video data in Vietnam. The system helps marketers and content creators identify media leaders, track content performance, and measure channel consistency based on data.

* **Live Interactive Dashboard:** [[Youtube Trending Dashboard](https://datastudio.google.com/s/nFdE2rnvzSA)]

---

## System Architecture
The data pipeline is designed with a modern Cloud Data Stack:
Python (Scraper/API) ➔ Google BigQuery (Data Warehouse) ➔ Data Studio (BI Dashboard)

1. **Data Ingestion:** A Python script automates fetching daily trending video metrics (Views, Likes, Comments, Titles, Channels) via the YouTube API.
2. **Data Warehouse:** Raw data is loaded into Google BigQuery to handle large-scale datasets efficiently.
3. **Data Transformation (SQL):** Cleaned data by removing duplicates, casting data types (STRING, INTEGER, TIMESTAMP), and optimizing for reporting performance.
> *The complete production script can be found in [transform_data.sql](./transform_data.sql).*
4. **Data Visualization:** Built an interactive Looker Studio dashboard focusing on data-driven UI/UX.

---

## Dashboard Key Metrics & Features
The final report provides multi-dimensional insights:
* **Overview Analytics:** Real-time tracking of Total Views, Total Likes, and Total Comments.
* **Top 10 Most Viewed Videos:** Leaderboard utilizing a Visual Table with Bars to handle long video titles without UI clutter.
* **Top Channels on Trending:** A chart analyzing appearance frequency (Record Count) instead of raw views to measure long-term performance and brand consistency.
* **Detailed Data Registry:** A granular lookup table supporting full pagination and text wrapping for end-users.

---

## Tech Stack & Tools
* **Language:** Python (pandas, google-cloud-bigquery)
* **Cloud Platform:** Google Cloud Platform (GCP)
* **Data Warehouse:** Google BigQuery (SQL)
* **Business Intelligence (BI):** Data Studio

---

## How To Run This Project
1. Clone the repository: `git clone https://github.com/TranKhoa895/Youtube-Trending-Analytics-Pipeline.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Setup Google Cloud Credentials (`credentials.json`).
4. Run the Python extraction script: `python main.py`

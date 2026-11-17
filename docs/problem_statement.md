
# Problem Statement
## Amazon India – Revenue Leakage & Profitability Command Center

### 1. Business Scenario

A fast-growing Indian ethnic-wear brand sells kurtas, sets, sarees and western dresses through Amazon India and other online marketplaces.

Although order volumes and sales are increasing, the business is not experiencing the expected growth in cash realization.

Management suspects revenue leakage due to:

- Order cancellations.
- Returns to seller.
- Stock-outs of popular sizes.
- Dead stock in warehouses.
- Inconsistent marketplace pricing.
- Inventory and fulfilment inefficiencies.

### 2. Stakeholder

The primary stakeholder is the business founder and management team.

They need a data-driven system to understand where revenue is being lost and which business operations require immediate attention.

### 3. Business Objective

Develop a Revenue Leakage & Profitability Command Center that identifies, measures and explains revenue leakage in Indian Rupees.

The system will convert raw commercial datasets into actionable business insights using Python, SQL, statistics, machine learning and Streamlit.

### 4. Key Business Questions

1. How much gross sales value is lost through cancellations and returns?
2. Which categories, sizes and SKUs have the highest leakage?
3. Which states and cities generate the most demand?
4. Does Amazon fulfilment perform better than merchant fulfilment?
5. Do promotions increase order value or return risk?
6. How do B2B and B2C orders differ?
7. Which SKUs contribute most to revenue?
8. Which products are at stock-out risk or represent dead stock?
9. Where do marketplace prices differ?
10. Which orders have the highest cancellation or return risk?
11. What will demand look like over the next 14 days?
12. Which business actions can recover the most revenue?

### 5. KPI Tree

Gross Sales
    |
    ├── Order Cancellations
    |
    ├── Returns to Seller
    |
    └── Other Identified Leakage
             |
             v
       Total Revenue Leakage
             |
             v
       Net Realised Revenue

### 6. Primary KPIs

- Gross Sales (₹)
- Net Realised Revenue (₹)
- Revenue Leakage (₹)
- Revenue Leakage Percentage
- Average Order Value (₹)
- Units Sold
- Cancellation Rate
- Return Rate
- Stock-out Risk SKUs
- Dead Stock SKUs
- Marketplace Price Gap

### 7. Project Assumptions

- The supplied Amazon India dataset is anonymized commercial data.
- Revenue leakage definitions will be documented before calculations.
- Orders still in transit will not automatically be classified as cancellations or returns.
- Missing values will be investigated before treatment.
- Transfer price will be used as a cost proxy where appropriate.
- All financial calculations will use Indian Rupees (₹).
- Forecasts will be limited by the available historical data.
- Machine learning predictions will not be treated as guaranteed business outcomes.

### 8. Expected Deliverables

- Data quality audit.
- Cleaned analytical dataset.
- SQLite star schema.
- Advanced SQL analysis.
- Exploratory data analysis.
- Revenue leakage diagnostics.
- Inventory and pricing intelligence.
- Machine learning risk classifier.
- 14-day demand forecast.
- Interactive Streamlit dashboard.
- Executive summary and business recommendations.

### 9. Technology

Python, Pandas, NumPy, SQLite, SQL, SciPy, Statsmodels, Matplotlib, Seaborn, Plotly, Scikit-learn, Streamlit and GitHub.

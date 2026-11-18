
# Amazon India – Revenue Leakage & Profitability Command Center
https://amazonindiaprojectreport-hkdhbuqfbmhcoucah9c9f3.streamlit.app/
An end-to-end Data Analytics project focused on identifying revenue leakage, analyzing profitability, monitoring inventory, comparing marketplace pricing, and predicting order cancellation and return risks.

## Project Overview

The project analyzes Amazon India seller data to understand why increasing sales do not necessarily translate into increasing realized revenue.

The goal is to develop an interactive Revenue Leakage & Profitability Command Center that helps business stakeholders identify financial losses and prioritize corrective actions.

## Business Objectives

- Analyze gross sales and net realized revenue.
- Identify cancellations and returns.
- Quantify revenue leakage in Indian Rupees.
- Analyze product, category, size, state and city performance.
- Identify stock-out risks and dead stock.
- Compare prices across marketplaces.
- Build machine learning models for order risk prediction.
- Forecast demand for the next 14 days.
- Develop an interactive Streamlit dashboard.

## Technology Stack

- Python
- Pandas and NumPy
- SQLite and SQL
- Matplotlib and Seaborn
- Plotly
- SciPy and Statsmodels
- Scikit-learn
- Streamlit
- Git and GitHub

## Project Structure

```text
amazon-india-revenue-leakage/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
├── sql/
├── src/
├── app/
│   └── pages/
├── models/
├── images/
├── requirements.txt
├── .gitignore
└── README.md
```

## Project Status

Phase 01 – Project Setup

Further phases will be documented as the project progresses.

## Dataset

Source: https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data

Raw datasets will not be committed to GitHub.

## Author

Arushicoder

GitHub: https://github.com/arushicoder



## Business Results

| Metric | Result |
|---|---:|
| Order lines analysed | 128,975 |
| Unique orders | 120,378 |
| Gross recorded order value | ₹78,592,678.30 |
| Cancellation/return value proxy | ₹8,296,548.30 |
| Net revenue proxy | ₹70,296,130.00 |
| Adverse order-line rate | 15.84% |

> **Interpretation:** The cancellation/return value is a historical order-value
> proxy. It is not verified cash loss or audited net revenue.

## Key Insights

- **Overall recorded value:** Gross recorded order value is ₹78,592,678.30. Evidence: 128,975 order lines; 120,378 unique orders.
- **Cancellation and return exposure:** Cancellation/return order-value proxy is ₹8,296,548.30, equal to 10.56% of gross recorded value. Evidence: 20,430 adverse order lines out of 128,975 total lines.
- **Net revenue proxy:** Gross recorded value less cancellation/return value proxy is ₹70,296,130.00. Evidence: Calculated as gross recorded order value minus amounts on cancelled and returned order lines.
- **Outcome maturity:** 79,776 order lines (61.85%) are not classified as delivered or cancellation/return outcomes. Evidence: 28,769 delivered lines and 20,430 adverse lines.
- **Category revenue concentration:** SET has the highest recorded value at ₹39,204,124.03. Evidence: Category share: 49.88%; adverse value proxy: ₹4,167,111.03.
- **Category leakage concentration:** SET has the largest cancellation/return value proxy at ₹4,167,111.03. Evidence: Adverse order-line rate: 16.26%.
- **Geographic demand:** MAHARASHTRA has the highest recorded value at ₹13,335,534.14. Evidence: Recorded value share: 16.97%.
- **Geographic adverse outcomes:** MAHARASHTRA has the highest adverse value proxy at ₹1,278,607.14. Evidence: Adverse rate: 14.52%.
- **Fulfilment reliability comparison:** MERCHANT has an adverse rate of 22.81% versus AMAZON at 12.79%. Evidence: Difference: 10.02 percentage points.
- **SKU revenue concentration:** 1,974 SKUs (27.44% of listed SKUs) account for at least 80% of recorded SKU value. Evidence: Based on cumulative recorded order-line amount by SKU.
- **Promotion comparison:** Promoted and non-promoted order lines have been compared. Evidence: promo_group  order_lines  recorded_value  adverse_lines  adverse_value_proxy  units  adverse_rate_pct  value_share_pct
       True        79822      53588435.0           2389            1395341.0  79851          2.992909        68.185022
      False        49153      25004243.3          18041            6901207.3  36798         36.703762        31.814978
- **B2B versus B2C:** B2B and B2C order-line performance differs across recorded value and adverse outcomes. Evidence: customer_segment  order_lines  recorded_value  adverse_lines  adverse_value_proxy  units  adverse_rate_pct  value_share_pct
             B2C       128104     78001457.51          20348           8258738.51 115809         15.883969        99.247741
             B2B          871       591220.79             82             37809.79    840          9.414466         0.752259

## Prioritized Recommendations

| Priority | Recommendation | Scenario opportunity | Effort | Owner |
|---:|---|---:|---|---|
| 1 | Introduce pre-dispatch checks for high-risk orders and investigate recurring cancellation/return reasons. | ₹414,827.41 | Medium | Operations / Fulfilment Manager |
| 2 | Audit product descriptions, size charts, product quality and return reasons in the highest-leakage category. | ₹208,355.55 | Medium | Category / Quality Manager |
| 3 | Review delivery exceptions, service levels and customer contact processes in the highest-leakage state. | ₹63,930.36 | Medium | Logistics Manager |
| 4 | Run a fulfilment performance review and test targeted process changes against a comparable control group. | ₹228,371.82 | Medium | Fulfilment Manager |
| 5 | Prioritise replenishment reviews for stock-out-risk SKUs using demand, available stock and supplier lead time. | ₹0.00 | High | Inventory / Supply Chain Manager |
| 6 | Review marketplace price-parity gaps above the project's 10% threshold and validate margin using actual cost data. | ₹0.00 | Medium | Marketplace / Pricing Manager |

### Limitations

- The source period covers approximately three months.
- The dataset represents one seller and does not establish market-wide results.
- Recorded order amounts are not verified cash receipts.
- Transfer price is a cost proxy, not a complete contribution-margin calculation.
- Pending/in-transit order lines are not treated as confirmed successful outcomes.
- Recommendation impacts are illustrative 5% scenarios applied to historical
  exposure proxies; they are not guaranteed savings.
- Forecasts should be validated with additional history and actual operational data.


from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ============================================================
# 1. CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="NOVA | Amazon India Intelligence",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

APP_DIR = Path(__file__).resolve().parent
PROJECT_DIR = APP_DIR.parent
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

ORDERS_FILE = PROCESSED_DIR / "orders_clean.csv"

REPORT_FILES = {
    "14-Day Forecast": "phase_08_14_day_forecast.csv",
    "Forecast Metrics": "phase_08_forecast_metrics.csv",
    "Model Metrics": "phase_08_model_metrics.csv",
    "Feature Importance": "phase_08_feature_importance.csv",
    "Risk Scores": "phase_08_test_risk_scores.csv",
    "High-Risk Orders": "phase_08_top_10_percent_risk_orders.csv",
}


# ============================================================
# 2. PREMIUM FUTURISTIC THEME
# ============================================================

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #172747 0%, transparent 40%),
        radial-gradient(ellipse at 90% 10%, #241746 0%, transparent 35%),
        #080E1B;

    color: #EAF2FF;
}

/* REMOVE TOP SPACE */

.block-container {
    padding-top: 1.7rem;
    padding-bottom: 2rem;
    max-width: 1600px;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111C32, #0A1120);
    border-right: 1px solid rgba(0, 220, 255, 0.16);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] p {
    color: #EAF2FF;
}

/* HEADER */

.hero {
    background:
        linear-gradient(115deg,
        rgba(18, 37, 66, 0.97),
        rgba(31, 22, 61, 0.96));

    border: 1px solid rgba(70, 210, 255, 0.28);
    border-radius: 22px;
    padding: 25px 28px;
    margin-bottom: 22px;

    box-shadow:
        0 0 35px rgba(0, 190, 255, 0.08),
        inset 0 0 25px rgba(110, 80, 255, 0.06);
}

.hero-title {
    color: #FFFFFF;
    font-size: 30px;
    font-weight: 800;
    letter-spacing: 0.5px;
}

.hero-subtitle {
    color: #A9BCD9;
    font-size: 13px;
    margin-top: 7px;
    letter-spacing: 1.1px;
}

/* ROBOT */

.robot {
    width: 72px;
    height: 72px;
    border-radius: 22px;

    background: linear-gradient(145deg, #123D62, #35225E);
    border: 1px solid rgba(0, 229, 255, 0.65);

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 39px;

    box-shadow:
        0 0 15px rgba(0, 225, 255, 0.42),
        0 0 35px rgba(0, 225, 255, 0.16);

    animation: robotGlow 2.8s ease-in-out infinite;
}

@keyframes robotGlow {
    0%, 100% {
        box-shadow: 0 0 12px rgba(0,225,255,.25);
        transform: translateY(0);
    }
    50% {
        box-shadow: 0 0 30px rgba(0,225,255,.55);
        transform: translateY(-3px);
    }
}

/* PULSING STATUS */

.status-row {
    display: flex;
    align-items: center;
    gap: 9px;
    color: #8DEDD7;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-top: 12px;
}

.pulse-dot {
    height: 9px;
    width: 9px;
    border-radius: 50%;
    background: #00E6A8;

    box-shadow: 0 0 0 0 rgba(0, 230, 168, .65);
    animation: pulse 1.7s infinite;
}

@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(0, 230, 168, .65);
    }
    70% {
        box-shadow: 0 0 0 10px rgba(0, 230, 168, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(0, 230, 168, 0);
    }
}

/* SECTION TITLES */

.section-heading {
    color: #EAF2FF;
    font-size: 20px;
    font-weight: 750;
    margin: 20px 0 12px 0;
}

.section-caption {
    color: #8DA4C3;
    font-size: 12px;
    margin-bottom: 15px;
}

/* KPI CARDS */

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        rgba(24, 43, 72, .98),
        rgba(14, 25, 45, .98)
    );

    border: 1px solid rgba(100, 170, 230, .22);
    border-radius: 17px;

    padding: 19px 17px;

    min-height: 112px;

    box-shadow:
        0 10px 25px rgba(0, 0, 0, .20),
        inset 0 1px rgba(255,255,255,.035);

    transition: all .25s ease;
}

[data-testid="stMetric"]:hover {
    border-color: rgba(0, 220, 255, .65);
    transform: translateY(-3px);
    box-shadow: 0 0 22px rgba(0, 210, 255, .13);
}

[data-testid="stMetricLabel"] {
    color: #A8BDD8 !important;
    font-size: 12px !important;
}

[data-testid="stMetricValue"] {
    color: #F4F8FF !important;
    font-weight: 750 !important;
    font-size: 25px !important;
}

/* NAVIGATION */

[data-testid="stRadio"] label {
    color: #C7D8F0 !important;
    font-weight: 600;
}

/* INPUTS */

[data-baseweb="select"] > div {
    background-color: #14233A;
    border-color: #304968;
    border-radius: 9px;
}

/* BUTTONS */

.stDownloadButton button {
    background: linear-gradient(100deg, #087EA4, #6544BD);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    padding: 9px 18px;
}

.stDownloadButton button:hover {
    border: 1px solid #35DFFF;
    color: white;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border: 1px solid rgba(100, 170, 230, .2);
    border-radius: 12px;
}

/* DIVIDER */

hr {
    border-color: rgba(100, 150, 200, .18);
}

/* FOOTER */

.footer {
    text-align: center;
    color: #7087A7;
    font-size: 11px;
    padding: 20px;
    letter-spacing: .7px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 3. HELPER FUNCTIONS
# ============================================================

def format_inr(value):
    value = float(value or 0)

    if abs(value) >= 10000000:
        return f"₹{value / 10000000:.2f} Cr"

    if abs(value) >= 100000:
        return f"₹{value / 100000:.2f} L"

    return f"₹{value:,.0f}"


def read_csv(path):
    if not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path, low_memory=False)
    except Exception:
        return pd.DataFrame()


def chart_style(fig, height=390):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(12,22,39,0.65)",
        font=dict(
            family="Arial",
            color="#DCEAFF",
            size=11
        ),
        title=dict(
            font=dict(size=16, color="#F3F7FF")
        ),
        height=height,
        margin=dict(l=25, r=25, t=65, b=35),
        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        )
    )

    fig.update_xaxes(
        gridcolor="rgba(130,160,200,0.12)",
        zerolinecolor="rgba(130,160,200,0.12)"
    )

    fig.update_yaxes(
        gridcolor="rgba(130,160,200,0.12)",
        zerolinecolor="rgba(130,160,200,0.12)"
    )

    return fig


def display_chart(fig, height=390):
    fig = chart_style(fig, height)
    st.plotly_chart(fig, use_container_width=True)


def safe_sum(data, column):
    if column not in data.columns:
        return 0.0

    return pd.to_numeric(
        data[column], errors="coerce"
    ).fillna(0).sum()


def download_csv(data, filename, label):
    if data.empty:
        return

    st.download_button(
        label=label,
        data=data.to_csv(index=False).encode("utf-8"),
        file_name=filename,
        mime="text/csv"
    )


# ============================================================
# 4. LOAD ORDERS — CSV ONLY
# ============================================================

@st.cache_data
def load_orders(path, modified_time):
    data = pd.read_csv(path, low_memory=False)

    data.columns = [
        str(c).strip().lower()
        for c in data.columns
    ]

    required = ["date", "amount", "qty", "status"]
    missing = [c for c in required if c not in data.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    data["date"] = pd.to_datetime(
        data["date"], errors="coerce"
    )

    data["amount"] = pd.to_numeric(
        data["amount"], errors="coerce"
    ).fillna(0)

    data["qty"] = pd.to_numeric(
        data["qty"], errors="coerce"
    ).fillna(0)

    data["status"] = (
        data["status"].fillna("UNKNOWN")
        .astype(str).str.strip().str.upper()
    )

    for column in [
        "category", "ship_state", "ship_city",
        "fulfilment", "sales_channel", "size", "sku"
    ]:
        if column in data.columns:
            data[column] = (
                data[column].fillna("Unknown")
                .astype(str).str.strip()
            )

    return data


if not ORDERS_FILE.exists():
    st.error(
        f"Could not find orders_clean.csv at:\n{ORDERS_FILE}"
    )
    st.info(
        "Place orders_clean.csv inside data/processed/ "
        "and restart the application."
    )
    st.stop()

try:
    df = load_orders(
        str(ORDERS_FILE),
        ORDERS_FILE.stat().st_mtime
    )
except Exception as error:
    st.error(f"Could not load orders: {error}")
    st.stop()

if df.empty:
    st.error("The orders CSV contains no records.")
    st.stop()

valid_dates = df["date"].dropna()

if valid_dates.empty:
    st.error("No valid dates were found in the orders CSV.")
    st.stop()


# ============================================================
# 5. LOAD PHASE 07 AND PHASE 08 REPORTS
# ============================================================

reports = {}

for label, filename in REPORT_FILES.items():
    reports[label] = read_csv(PROCESSED_DIR / filename)

phase07_reports = {}

for path in PROCESSED_DIR.glob("*.csv"):
    if "phase_07" in path.name.lower():
        report = read_csv(path)
        if not report.empty:
            phase07_reports[path.stem] = report


# ============================================================
# 6. SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div style="text-align:center; padding:12px 0;">
        <div style="font-size:42px;">🤖</div>
        <div style="font-size:20px;font-weight:800;color:#EAF5FF;">
            NOVA AI
        </div>
        <div style="font-size:10px;letter-spacing:2px;color:#65DFFF;">
            INTELLIGENCE SYSTEM
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Executive Overview",
        "Leakage Explorer",
        "Geography",
        "Product & Inventory",
        "Pricing Parity",
        "Risk Predictor"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ◈ GLOBAL FILTERS")

date_min = valid_dates.min().date()
date_max = valid_dates.max().date()

date_range = st.sidebar.date_input(
    "Analysis period",
    value=(date_min, date_max),
    min_value=date_min,
    max_value=date_max
)

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
elif isinstance(date_range, (tuple, list)) and len(date_range) == 1:
    start_date = date_range[0]
    end_date = date_range[0]
else:
    start_date, end_date = date_min, date_max


def options_for(column):
    if column not in df.columns:
        return []

    return sorted(
        df[column].dropna().astype(str).unique().tolist()
    )


categories = options_for("category")
states = options_for("ship_state")
fulfilments = options_for("fulfilment")

selected_categories = st.sidebar.multiselect(
    "Product category",
    categories,
    default=categories
)

selected_states = st.sidebar.multiselect(
    "Shipping state",
    states,
    default=states
)

selected_fulfilments = st.sidebar.multiselect(
    "Fulfilment type",
    fulfilments,
    default=fulfilments
)

customer_type = st.sidebar.selectbox(
    "Customer segment",
    ["All Customers", "B2B", "B2C"]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div style="font-size:11px;color:#7F99B8;">
    <span style="color:#00E6A8;">●</span> SYSTEM READY
    <br>Amazon India Analytics
    <br>Revenue Intelligence v1.0
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 7. APPLY FILTERS
# ============================================================

filtered = df[
    (df["date"].dt.date >= start_date)
    & (df["date"].dt.date <= end_date)
].copy()

for column, values in [
    ("category", selected_categories),
    ("ship_state", selected_states),
    ("fulfilment", selected_fulfilments)
]:
    if column in filtered.columns:
        filtered = filtered[
            filtered[column].astype(str).isin(values)
        ]

if customer_type != "All Customers" and "b2b" in filtered.columns:

    b2b = filtered["b2b"].astype(str).str.lower().isin(
        ["true", "1", "yes", "1.0"]
    )

    filtered = filtered[
        b2b if customer_type == "B2B" else ~b2b
    ]


# ============================================================
# 8. BUSINESS METRICS
# ============================================================

positive_statuses = [
    "CANCELLED",
    "SHIPPED - RETURNED TO SELLER",
    "SHIPPED - RETURNING TO SELLER"
]

delivered_statuses = [
    "SHIPPED - DELIVERED TO BUYER"
]

gross_sales = safe_sum(filtered, "amount")

adverse_mask = filtered["status"].isin(positive_statuses)

leakage = safe_sum(
    filtered.loc[adverse_mask],
    "amount"
)

net_revenue_proxy = gross_sales - leakage

leakage_pct = (
    leakage / gross_sales * 100
    if gross_sales > 0 else 0
)

delivered = filtered[
    filtered["status"].isin(delivered_statuses)
]

units = safe_sum(delivered, "qty")

orders_count = (
    filtered["order_id"].nunique()
    if "order_id" in filtered.columns
    else len(filtered)
)

aov = (
    gross_sales / orders_count
    if orders_count > 0 else 0
)


# ============================================================
# 9. PREMIUM HEADER
# ============================================================

header_left, header_right = st.columns([5, 1])

with header_left:
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">
                AMAZON INDIA
                <span style="color:#50DFFF;"> / </span>
                INTELLIGENCE CENTER
            </div>
            <div class="hero-subtitle">
                REVENUE INTELLIGENCE • PROFITABILITY • RISK ANALYTICS
            </div>
            <div class="status-row">
                <span class="pulse-dot"></span>
                NOVA SYSTEM ONLINE
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with header_right:
    st.markdown(
        """
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            height:130px;">
            <div class="robot">🤖</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.caption(
    f"ANALYSIS WINDOW: {start_date} → {end_date} "
    f"| {len(filtered):,} ORDER LINES"
)


# ============================================================
# 10. KPI CARDS
# ============================================================

if filtered.empty:
    st.warning("No records match the selected filters.")
else:

    st.markdown(
        '<div class="section-heading">◈ BUSINESS PERFORMANCE</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Gross Sales", format_inr(gross_sales))
    c2.metric("Net Revenue Proxy", format_inr(net_revenue_proxy))
    c3.metric("Estimated Leakage", format_inr(leakage), f"{leakage_pct:.2f}%")
    c4.metric("Delivered Units", f"{units:,.0f}")

    c5, c6, c7 = st.columns(3)

    c5.metric("Average Order Value", format_inr(aov))
    c6.metric("Unique Orders", f"{orders_count:,}")
    c7.metric("Order Lines", f"{len(filtered):,}")

st.caption(
    "Net Revenue Proxy subtracts recorded amounts for cancelled and returned "
    "orders from gross recorded order amounts. It is not verified accounting "
    "revenue or confirmed cash loss."
)

st.divider()


# ============================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# ============================================================

if page == "Executive Overview":

    st.markdown(
        '<div class="section-heading">◈ EXECUTIVE OVERVIEW</div>',
        unsafe_allow_html=True
    )

    if filtered.empty:
        st.info("No records available.")
    else:

        left, right = st.columns(2)

        with left:

            daily = (
                filtered.groupby(filtered["date"].dt.date)["amount"]
                .sum()
                .reset_index()
            )

            daily.columns = ["date", "revenue"]

            daily["moving_average"] = (
                daily["revenue"].rolling(7, min_periods=1).mean()
            )

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=daily["date"],
                y=daily["revenue"],
                mode="lines",
                name="Daily Revenue",
                line=dict(width=2, color="#22D3EE")
            ))

            fig.add_trace(go.Scatter(
                x=daily["date"],
                y=daily["moving_average"],
                mode="lines",
                name="7-Day Average",
                line=dict(width=3, color="#A78BFA", dash="dash")
            ))

            fig.update_layout(
                title="Daily Revenue Trend",
                xaxis_title="Date",
                yaxis_title="Revenue (₹)"
            )

            display_chart(fig)

        with right:

            category_data = (
                filtered.groupby("category")["amount"]
                .sum()
                .sort_values()
                .reset_index()
            )

            fig = px.bar(
                category_data,
                x="amount",
                y="category",
                orientation="h",
                title="Category Revenue",
                labels={"amount": "Revenue (₹)"}
            )

            display_chart(fig)

        left, right = st.columns(2)

        with left:

            outcome = (
                filtered["status"].value_counts().reset_index()
            )

            outcome.columns = ["status", "count"]

            fig = px.pie(
                outcome,
                names="status",
                values="count",
                hole=0.65,
                title="Order Status Mix"
            )

            display_chart(fig)

        with right:

            if "fulfilment" in filtered.columns:

                fulfilment_data = (
                    filtered.groupby("fulfilment")["amount"]
                    .sum()
                    .reset_index()
                )

                fig = px.bar(
                    fulfilment_data,
                    x="fulfilment",
                    y="amount",
                    title="Fulfilment Revenue",
                    labels={"amount": "Revenue (₹)"}
                )

                display_chart(fig)

        weekday = filtered.copy()
        weekday["day"] = weekday["date"].dt.day_name()

        weekday_order = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]

        weekday_data = (
            weekday.groupby("day")["amount"]
            .sum()
            .reindex(weekday_order)
            .fillna(0)
            .reset_index()
        )

        fig = px.bar(
            weekday_data,
            x="day",
            y="amount",
            title="Weekly Revenue Pattern",
            labels={"amount": "Revenue (₹)"}
        )

        display_chart(fig)


# ============================================================
# PAGE 2 — LEAKAGE EXPLORER
# ============================================================

elif page == "Leakage Explorer":

    st.markdown(
        '<div class="section-heading">◈ REVENUE LEAKAGE MONITOR</div>',
        unsafe_allow_html=True
    )

    leakage_df = filtered[
        filtered["status"].isin(positive_statuses)
    ].copy()

    if leakage_df.empty:
        st.info("No adverse order outcomes found in this selection.")
    else:

        left, right = st.columns(2)

        with left:

            data = (
                leakage_df.groupby("category")["amount"]
                .sum().sort_values().reset_index()
            )

            fig = px.bar(
                data,
                x="amount",
                y="category",
                orientation="h",
                title="Leakage by Category",
                labels={"amount": "Amount (₹)"}
            )

            display_chart(fig)

        with right:

            data = (
                leakage_df.groupby("fulfilment")["amount"]
                .sum().reset_index()
            )

            fig = px.bar(
                data,
                x="fulfilment",
                y="amount",
                title="Leakage by Fulfilment",
                labels={"amount": "Amount (₹)"}
            )

            display_chart(fig)

        left, right = st.columns(2)

        with left:

            data = (
                leakage_df.groupby("status")["amount"]
                .sum().reset_index()
            )

            fig = px.bar(
                data,
                x="status",
                y="amount",
                title="Leakage by Outcome",
                labels={"amount": "Amount (₹)"}
            )

            display_chart(fig)

        with right:

            data = (
                leakage_df.groupby("ship_state")["amount"]
                .sum().nlargest(15).reset_index()
            )

            fig = px.bar(
                data,
                x="amount",
                y="ship_state",
                orientation="h",
                title="Top 15 Leakage States",
                labels={"amount": "Amount (₹)"}
            )

            display_chart(fig)

        st.markdown("### Adverse Order Records")

        st.dataframe(
            leakage_df,
            use_container_width=True
        )

        download_csv(
            leakage_df,
            "amazon_leakage_records.csv",
            "Download Leakage Records"
        )


# ============================================================
# PAGE 3 — GEOGRAPHY
# ============================================================

elif page == "Geography":

    st.markdown(
        '<div class="section-heading">◈ GEOGRAPHIC INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    if filtered.empty:
        st.info("No geographic records available.")
    else:

        left, right = st.columns(2)

        with left:

            state_data = (
                filtered.groupby("ship_state")["amount"]
                .sum().nlargest(15).reset_index()
            )

            fig = px.bar(
                state_data,
                x="amount",
                y="ship_state",
                orientation="h",
                title="Top 15 States by Revenue",
                labels={"amount": "Revenue (₹)"}
            )

            display_chart(fig)

        with right:

            matrix = pd.pivot_table(
                filtered,
                index="ship_state",
                columns="category",
                values="amount",
                aggfunc="sum",
                fill_value=0
            )

            fig = px.imshow(
                matrix,
                aspect="auto",
                title="State × Category Heatmap",
                labels={
                    "x": "Category",
                    "y": "State",
                    "color": "Revenue (₹)"
                }
            )

            display_chart(fig, 480)

        if "ship_city" in filtered.columns:

            city_data = (
                filtered.groupby("ship_city")["amount"]
                .sum().nlargest(15).reset_index()
            )

            fig = px.bar(
                city_data,
                x="amount",
                y="ship_city",
                orientation="h",
                title="Top 15 Cities by Revenue",
                labels={"amount": "Revenue (₹)"}
            )

            display_chart(fig)

        if "b2b" in filtered.columns:

            b2b_data = filtered.copy()

            b2b_data["segment"] = np.where(
                b2b_data["b2b"].astype(str).str.lower().isin(
                    ["true", "1", "yes", "1.0"]
                ),
                "B2B",
                "B2C"
            )

            summary = (
                b2b_data.groupby("segment")["amount"]
                .mean().reset_index()
            )

            fig = px.bar(
                summary,
                x="segment",
                y="amount",
                title="Average Order-Line Amount by Segment",
                labels={"amount": "Average Amount (₹)"}
            )

            display_chart(fig)


# ============================================================
# PAGE 4 — PRODUCT AND INVENTORY
# ============================================================

elif page == "Product & Inventory":

    st.markdown(
        '<div class="section-heading">◈ PRODUCT & INVENTORY INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    if filtered.empty:
        st.info("No product records available.")
    else:

        left, right = st.columns(2)

        with left:

            data = (
                filtered.groupby("category")["qty"]
                .sum().reset_index()
            )

            fig = px.bar(
                data,
                x="category",
                y="qty",
                title="Units by Category",
                labels={"qty": "Units"}
            )

            display_chart(fig)

        with right:

            if "size" in filtered.columns:

                data = (
                    filtered.groupby("size")["qty"]
                    .sum().sort_values(ascending=False)
                    .reset_index()
                )

                fig = px.bar(
                    data,
                    x="size",
                    y="qty",
                    title="Size Demand",
                    labels={"qty": "Units"}
                )

                display_chart(fig)

        if "sku" in filtered.columns:

            data = (
                filtered.groupby("sku")["amount"]
                .sum().sort_values(ascending=False)
                .head(20).reset_index()
            )

            data["cumulative_pct"] = (
                data["amount"].cumsum()
                / max(data["amount"].sum(), 1) * 100
            )

            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=data["sku"],
                y=data["amount"],
                name="Revenue",
                marker_color="#22D3EE"
            ))

            fig.add_trace(go.Scatter(
                x=data["sku"],
                y=data["cumulative_pct"],
                name="Cumulative %",
                yaxis="y2",
                line=dict(color="#A78BFA", width=3)
            ))

            fig.update_layout(
                title="Top 20 SKU Pareto Analysis",
                xaxis_title="SKU",
                yaxis=dict(title="Revenue (₹)"),
                yaxis2=dict(
                    title="Cumulative %",
                    overlaying="y",
                    side="right",
                    range=[0, 110]
                )
            )

            display_chart(fig)

    st.markdown("### Phase 07 Inventory Reports")

    if phase07_reports:

        selected = st.selectbox(
            "Select inventory report",
            list(phase07_reports.keys())
        )

        report = phase07_reports[selected]

        st.dataframe(report, use_container_width=True)

        download_csv(
            report,
            f"{selected}.csv",
            "Download Inventory Report"
        )

    else:
        st.warning("No Phase 07 reports found.")


# ============================================================
# PAGE 5 — PRICING PARITY
# ============================================================

elif page == "Pricing Parity":

    st.markdown(
        '<div class="section-heading">◈ MARKETPLACE PRICING INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    pricing_reports = {
        name: report
        for name, report in phase07_reports.items()
        if any(
            word in name.lower()
            for word in ["price", "pricing", "parity", "margin", "marketplace"]
        )
    }

    if not pricing_reports:
        st.warning(
            "No pricing report was identified by filename. "
            "Check your Phase 07 report filenames."
        )
    else:

        selected = st.selectbox(
            "Select pricing report",
            list(pricing_reports.keys())
        )

        report = pricing_reports[selected]

        st.dataframe(report, use_container_width=True)

        numeric = report.select_dtypes(
            include="number"
        ).columns.tolist()

        if numeric:

            metric = st.selectbox(
                "Select pricing metric",
                numeric
            )

            chart_data = report.nlargest(15, metric)

            fig = px.bar(
                chart_data,
                x=chart_data.columns[0],
                y=metric,
                title=f"Pricing Analysis — {metric}"
            )

            display_chart(fig)

        download_csv(
            report,
            f"{selected}.csv",
            "Download Pricing Report"
        )


# ============================================================
# PAGE 6 — RISK PREDICTOR
# ============================================================

elif page == "Risk Predictor":

    st.markdown(
        '<div class="section-heading">◈ NOVA PREDICTIVE RISK ENGINE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            background:linear-gradient(110deg,#152D49,#28204B);
            border:1px solid rgba(90,200,255,.3);
            padding:18px;
            border-radius:15px;
            margin-bottom:18px;">
            <div style="font-size:20px;font-weight:750;color:#F3F7FF;">
                🤖 Predictive Intelligence
            </div>
            <div style="font-size:12px;color:#A9BCD9;margin-top:7px;">
                Historical model performance • Risk analysis • Demand forecasting
            </div>
            <div class="status-row">
                <span class="pulse-dot"></span>
                REPORT CONNECTION CHECK
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    model_metrics = reports["Model Metrics"]
    forecast_metrics = reports["Forecast Metrics"]
    importance = reports["Feature Importance"]
    forecast = reports["14-Day Forecast"]
    high_risk = reports["High-Risk Orders"]

    st.markdown("### Model Performance")

    if not model_metrics.empty:
        st.dataframe(
            model_metrics,
            use_container_width=True
        )
    else:
        st.info("Model metrics CSV was not found.")

    left, right = st.columns(2)

    with left:

        st.markdown("### Feature Importance")

        if not importance.empty:

            numeric = importance.select_dtypes(
                include="number"
            ).columns.tolist()

            if numeric:

                metric = (
                    "importance"
                    if "importance" in numeric
                    else numeric[0]
                )

                feature = (
                    "feature"
                    if "feature" in importance.columns
                    else importance.columns[0]
                )

                top = importance.nlargest(15, metric)

                fig = px.bar(
                    top.sort_values(metric),
                    x=metric,
                    y=feature,
                    orientation="h",
                    title="Top 15 Predictive Features"
                )

                display_chart(fig)

            else:
                st.dataframe(importance, use_container_width=True)

        else:
            st.info("Feature importance CSV not found.")

    with right:

        st.markdown("### Forecast Accuracy")

        if not forecast_metrics.empty:
            st.dataframe(
                forecast_metrics,
                use_container_width=True
            )
        else:
            st.info("Forecast metrics CSV not found.")

    st.markdown("### Next 14-Day Forecast")

    if not forecast.empty:

        date_col = next(
            (c for c in forecast.columns if "date" in c.lower()),
            None
        )

        category_col = next(
            (c for c in forecast.columns if "category" in c.lower()),
            None
        )

        units_col = next(
            (
                c for c in forecast.columns
                if "forecast" in c.lower() and "unit" in c.lower()
            ),
            None
        )

        if date_col and category_col and units_col:

            chart_data = forecast.copy()

            chart_data[date_col] = pd.to_datetime(
                chart_data[date_col], errors="coerce"
            )

            fig = px.line(
                chart_data,
                x=date_col,
                y=units_col,
                color=category_col,
                markers=True,
                title="Category Demand Forecast"
            )

            display_chart(fig)

        else:
            st.warning(
                "Forecast columns could not be identified. "
                "See the table below."
            )

        st.dataframe(forecast, use_container_width=True)

    else:
        st.warning("14-day forecast CSV not found.")

    st.markdown("### High-Risk Orders")

    if not high_risk.empty:

        st.dataframe(
            high_risk.head(500),
            use_container_width=True
        )

        download_csv(
            high_risk,
            "high_risk_orders.csv",
            "Download High-Risk Orders"
        )

    else:
        st.info("High-risk order CSV not found.")

    st.caption(
        "Historical model reports are displayed here. "
        "This page does not yet perform new live predictions."
    )


# ============================================================
# 11. GLOBAL EXPORT
# ============================================================

st.divider()

st.markdown(
    '<div class="section-heading">◈ DATA EXPORT CENTER</div>',
    unsafe_allow_html=True
)

download_csv(
    filtered,
    "amazon_india_filtered_orders.csv",
    "⬇ Download Filtered Orders"
)


# ============================================================
# 12. FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🤖 NOVA INTELLIGENCE SYSTEM
        <br>
        AMAZON INDIA REVENUE & PROFITABILITY COMMAND CENTER
        <br>
        PYTHON • PANDAS • PLOTLY • STREAMLIT
    </div>
    """,
    unsafe_allow_html=True
)

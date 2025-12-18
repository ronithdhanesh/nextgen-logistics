import streamlit as st
import pandas as pd
import plotly.express as px
from src.optimizer import get_best_recommendation
from src.ai.services import generate_output


st.set_page_config(page_title="NexGen Innovation Hub", layout="wide")


@st.cache_data
def load_view_data():
    return pd.read_csv('models/processed_data.csv', parse_dates=['Order_Date'])


df = load_view_data()


st.sidebar.title("NexGen Logistics")
page = st.sidebar.radio("Go to", ["Dashboard", "AI Dispatch Optimizer", "Operational Health"])


if page == "Dashboard":
    st.title("📊 Logistics Performance Dashboard")


    m1, m2, m3, m4 = st.columns(4)
    delay_rate = df['Is_Delayed'].mean()
    express_df = df[df['Priority'] == 'Express']
    express_reliability = 1 - express_df['Is_Delayed'].mean() if not express_df.empty else 0


    m1.metric("System Delay Rate", f"{delay_rate*100:.1f}%")
    m2.metric("Total Failure Tax", f"₹{df['Failure_Cost'].sum():,.0f}")
    m3.metric("Express Reliability", f"{express_reliability*100:.1f}%")
    m4.metric("Avg Delay Cost / Order", f"₹{df['Failure_Cost'].mean():,.0f}")


    st.subheader("Delay Trend Over Time")
    trend_df = df.groupby('Order_Date')['Is_Delayed'].mean().reset_index()
    fig_ts = px.line(trend_df, x='Order_Date', y='Is_Delayed', markers=True)
    st.plotly_chart(fig_ts, use_container_width=True)


    st.subheader("Carrier–Route Incompatibility Heatmap")
    fig1 = px.density_heatmap(
    df, x="Route", y="Carrier", z="Is_Delayed",
    histfunc="avg", color_continuous_scale="RdYlGn_r"
    )
    st.plotly_chart(fig1, use_container_width=True)


    fig2 = px.histogram(
    df, x="Carrier", y="Failure_Cost",
    color="Is_Delayed", barmode="group",
    title="Loss Exposure by Carrier"
    )
    st.plotly_chart(fig2, use_container_width=True)

elif page == "AI Dispatch Optimizer":
    st.title("🤖 AI Dispatch Optimizer")
    c1, c2 = st.columns(2)
    with c1:
        route = st.selectbox("Route Corridor", sorted(df['Route'].unique()))
        carrier = st.selectbox("Assigned Carrier", sorted(df['Carrier'].unique()))
        priority = st.selectbox("Service Level", sorted(df['Priority'].unique()))
    with c2:
        dist = st.number_input(
            "Distance (KM)",
            value=float(df[df['Route'] == route]['Distance_KM'].mean())
        )
        traffic = st.slider("Traffic Congestion (Minutes)", 0, 180, 30)

        use_ai = st.checkbox("Use AI Explanation", value=True)


    if st.button("Analyze & Optimize"):
        res = get_best_recommendation(route, carrier, priority, dist, traffic)


        st.divider()
        risk = res['current_risk']
        risk_reduction = res['risk_reduced']


        if risk > 0.4:
            st.error(f"High Risk Detected: {risk*100:.0f}% probability of delay")
        else:
            st.success("Low risk dispatch configuration")


        est_savings = risk_reduction * df['Failure_Cost'].mean()
        st.metric("Estimated Cost Avoided", f"₹{est_savings:,.0f}")


        suggestion_text = (
        f"Switch to {res['best_carrier']} to reduce delay risk by {risk_reduction*100:.0f}%."
        if risk > 0.4 else
        "Current configuration is optimal."
        )


        if use_ai:
            with st.spinner("AI generating operational insight..."):
                insight = generate_output(
                carrier=carrier,
                route=route,
                risk_prob=risk,
                delay_days=res['current_days'],
                suggestion=suggestion_text
                )
            st.info(insight)
        else:
            st.info(suggestion_text)

elif page == "Operational Health":
    st.title("🚛 Fleet & Warehouse Health")
    fig3 = px.sunburst(
    df,
    path=['Priority', 'Product_Category'],
    values='Order_Value_INR'
    )
    st.plotly_chart(fig3, use_container_width=True)


st.sidebar.divider()
st.sidebar.download_button(
"Export Intelligence Report",
df.to_csv(index=False),
"NexGen_Report.csv"
)
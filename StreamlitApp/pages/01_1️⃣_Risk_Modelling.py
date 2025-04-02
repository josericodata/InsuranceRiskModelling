import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

st.set_page_config(
    page_title="EE Claim Risk Predictor",
    page_icon="🚨",
    layout="centered",
)

st.title("🚗 EE Insurance - Claim Risk Predictor")

# Load the synthetic data
@st.cache_data
def load_data():
    return pd.read_csv("assets/DataGeneration/synthetic_insurance.csv")

df = load_data()

# Prepare data
X = df.drop(columns=["customer_id", "claim"])
y = df["claim"]
X_encoded = pd.get_dummies(X, drop_first=True)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_encoded, y)

# Add predictions
df["claim_probability"] = model.predict_proba(X_encoded)[:, 1]
df["prediction"] = model.predict(X_encoded)

# Sidebar: select customer
st.sidebar.header("🔍 Select a Customer")
selected_id = st.sidebar.selectbox("Customer ID", df["customer_id"])

# Fetch customer row
customer_data = df[df["customer_id"] == selected_id]
row = customer_data.iloc[0]

# Show customer profile
st.subheader("📋 Customer Profile")
st.dataframe(customer_data[["age", "vehicle_age", "vehicle_type", "annual_premium", "previous_insurance"]])

# Show prediction
st.subheader("📊 Prediction")
st.metric(label="Predicted Claim Probability", value=f"{row['claim_probability']:.2%}")
st.metric(label="Predicted Outcome", value="Will Claim" if row['prediction'] == 1 else "No Claim")

# Plot: risk distribution (AA colors)
st.subheader("📈 Risk Distribution Across All Customers")
fig = px.histogram(
    df,
    x="claim_probability",
    nbins=20,
    title="Predicted Claim Probabilities",
    labels={"claim_probability": "Claim Probability"}
)

# Apply black-on-yellow branding
fig.update_traces(marker_color="black")
fig.update_layout(
    plot_bgcolor="#FFD700",       # Yellow chart area
    paper_bgcolor="#FFD700",      # Yellow background
    font=dict(color="black"),     # Black text
    title_font=dict(color="black"),
    xaxis=dict(title_font=dict(color="black"), tickfont=dict(color="black")),
    yaxis=dict(title_font=dict(color="black"), tickfont=dict(color="black")),
    bargap=0.1
)

st.plotly_chart(fig, use_container_width=True)

# Optional full dataset
with st.expander("📁 Show Full Dataset"):
    st.dataframe(df)

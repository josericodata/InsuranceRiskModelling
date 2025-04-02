import streamlit as st

def run():
    st.set_page_config(
        page_title="Insurance Risk Model App",
        page_icon="📉",
        layout="centered",
    )

    st.title("📉 Insurance Claim Risk Modeling App")

    st.markdown(
        """
        Welcome to the **Insurance Risk Modeling App**! This Streamlit project demonstrates a complete machine learning workflow designed to **predict the probability of an insurance claim** based on customer profile data.

        > 🚗 *The dataset is synthetically generated to reflect real-world insurance customer scenarios including age, vehicle type, and policy history.*

        ---

        ### 🧠 App Purpose

        This app simulates a predictive pricing model that an imaginary insurance company like **EE Ireland** might use to support decision-making in:
        - Premium pricing
        - Risk segmentation
        - Customer profiling

        It uses a **Logistic Regression** model to estimate the likelihood of a customer filing a claim and visualises insights to support business intelligence and trading decisions.
        > *Disclaimer: EE Ireland is used here as a fictional placeholder and is not affiliated with any real-world company.*

        ---

        ### 🧱 App Workflow

        Here's what the app includes:

        #### 1️⃣ Customer Selection
        🔍 Choose a customer from a dropdown to inspect their individual profile and predicted claim risk.

        #### 2️⃣ Claim Risk Prediction
        📊 View the predicted probability of a claim along with a clear binary outcome (Claim / No Claim).

        #### 3️⃣ Risk Distribution
        📈 Explore a histogram of predicted probabilities across the full customer base to visualise risk segmentation.

        #### 4️⃣ Full Dataset Viewer
        🗃️ Expand the full dataset, including input features and model predictions, for review and QA.

        ---

        ### 🧪 Dataset Info

        The app uses a synthetic dataset located at:
        `data/synthetic_insurance.csv`

        It is generated with the `Faker` library and simulates 100,000 customers with fields including:
        - `age`, `vehicle_age`, `vehicle_type`
        - `annual_premium`, `previous_insurance`, `claim`

        ---

        ### 🚀 How to Use

        - Start by selecting a customer to see individual risk.
        - Review the model’s prediction and supporting visuals.
        - Use the histogram to understand customer segments and risk groupings.

        ---

        ### 🙌 Credits

        Created by [Jose Rico](https://github.com/josericodata)    
        Powered by [Streamlit](https://streamlit.io), [scikit-learn](https://scikit-learn.org), [Faker](https://faker.readthedocs.io), and [Plotly](https://plotly.com/python/).
        """
    )

if __name__ == "__main__":
    run()

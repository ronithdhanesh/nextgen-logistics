````markdown
# 🚀 NexGen Predict & Pivot: AI-Powered Logistics Optimizer

NexGen Predict & Pivot is an advanced logistics intelligence suite designed to transform NexGen’s delivery operations. By integrating Machine Learning, Predictive Analytics, and Generative AI, this tool moves beyond simple tracking to offer real-time risk mitigation and sustainability optimization.

## 🎯 The Mission

NexGen currently faces a **46.7%** delay rate, causing a drastic drop in customer satisfaction (from **4.66** to **2.47** stars). This project provides an automated "Dispatch & Pivot" system that identifies high-risk shipments before they leave the warehouse and recommends optimal carrier alternatives.

## 🛠️ Tech Stack

- **Language**: Python **3.9+**
- **Frontend**: Streamlit (Interactive Web App)
- **Data Science**: Pandas, NumPy, Scikit-Learn
- **AI/LLM**: LangChain, OpenAI/Gemini (via ChatPromptTemplate)
- **Visualization**: Plotly (Interactive Heatmaps, Treemaps, and Gauges)
- **DevOps**: Docker (Containerized Deployment)

## 📂 Project Structure

```plaintext
├── app.py                 # Main Streamlit Application
├── requirements.txt       # Project Dependencies
├── Dockerfile             # Container configuration
├── .env.example           # Template for API keys
├── src/
│   ├── trainer.py         # ML Pipeline (Data merging & Model training)
│   ├── optimizer.py       # Prescriptive "Pivot" search logic
│   └── ai/
│       └── ai_services.py # LLM-based Natural Language Generation
├── models/                # Trained AI artifacts & processed data
└── data/                  # 7 core logistics datasets
```
````

## ⚙️ Setup & Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/nexgen-optimizer.git
    cd nexgen-optimizer
    ```

2.  **Configure Environment Variables**

    Copy the example file and add your API keys:

    ```bash
    cp .env.example .env
    # Edit .env and add your OPENAI_API_KEY or GEMINI_API_KEY
    ```

3.  **Local Installation (Native)**

    ```bash
    pip install -r requirements.txt
    python src/trainer.py      # Generates the AI 'Brains'
    streamlit run app.py       # Launches the UI
    ```

4.  **Run via Docker**

    ```bash
    docker build -t nexgen-optimizer .
    docker run -p 8501:8501 nexgen-optimizer
    ```

## 📈 Innovation & Features

- **Dual-Model Prediction**: Utilizes a Random Forest Classifier to detect delay risk and a Random Forest Regressor to predict delay magnitude in days.
- **The "Pivot" Engine**: Automatically simulates performance across all carriers for a specific route to suggest the safest alternative.
- **Revenue at Risk (Churn Logic)**: Cross-references customer feedback with delivery failures to quantify exactly how much revenue is at risk of churn.
- **Green Score (Sustainability)**: Calculates CO2 emissions based on vehicle fleet data, allowing dispatchers to choose "Eco-Friendly" routes.
- **LLM Consultant**: Integrates Generative AI to translate complex data points into professional, human-readable dispatch warnings.

## 📊 Evaluation Criteria Compliance

| Requirement       | Status | Implementation                                                                         |
| ----------------- | ------ | -------------------------------------------------------------------------------------- |
| Data Analysis     | ✅     | Merged **7** datasets; handled missing values; derived "Churn Risk" and "CO2" metrics. |
| Visualization     | ✅     | **4+** interactive Plotly charts (Heatmap, Treemap, Bar, Metrics).                     |
| Interactivity     | ✅     | Dynamic inputs via sliders and selectboxes; CSV export functionality.                  |
| Advanced Features | ✅     | Multi-output ML models + LangChain/LLM integration + Dockerization.                    |

---

📝 **Author**: Ronith Dhanesh, Logistics Innovation Analyst

```

```

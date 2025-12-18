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

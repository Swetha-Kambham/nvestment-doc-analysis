# Investment Document Analysis Pipeline

This project extracts key financial metrics (KPIs) from investment-related PDF documents using OCR, NLP, and zero-shot classification. The data is structured and visualized using a simple Streamlit dashboard.

## 📂 Project Structure
- `investment_pipeline.py` – Extracts and classifies KPIs from PDFs and saves results to Excel.
- `dashboard.py` – Streamlit app to upload and visualize extracted KPI data.
- `sample_investment.pdf` – Sample investment document with placeholder KPI values.
- `requirements.txt` – Python dependencies.

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Extract KPIs from PDF
```bash
python investment_pipeline.py
```

### 3. Launch Dashboard
```bash
streamlit run dashboard.py
```

### 4. Upload the `extracted_kpis.xlsx` file in the Streamlit UI to see results.

## ✅ Features
- OCR-based PDF parsing with `pdfplumber`
- KPI extraction using regex and Hugging Face transformers
- Zero-shot classification to tag financial sections
- Streamlit UI for quick visualization

## 🛡️ Disclaimer
The included PDF is a placeholder. For real use, replace it with actual investment documents.

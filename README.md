# 🧾 Investment Document Analysis Pipeline

This project extracts key financial KPIs (e.g., Revenue, EBITDA, Growth, Valuation) from text-based investment documents (PDFs). The extracted metrics are saved to Excel and visualized using an interactive Streamlit dashboard.

---

## 🎯 Objective
Automatically extract financial metrics from investor reports or earnings documents and enable data visualization without manual parsing.

---

## 🧠 Features
- ✅ Extract KPIs like Revenue, EBITDA, Profit, Growth, Acquisition
- ✅ Use Hugging Face's BART model for zero-shot financial topic classification
- ✅ Export structured data to Excel
- ✅ View results interactively in a dashboard
- ✅ Built with Streamlit, Pandas, Transformers, and pdfplumber

---

## 🧰 Tech Stack
- Python
- pdfplumber
- re (regex)
- Hugging Face Transformers (BART)
- pandas + openpyxl
- Streamlit

---

## How to Run Locally

### 1. Clone or unzip the project
```bash
cd Investment_Document_Analysis_Project
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add a real PDF file
Replace `sample_investment.pdf` with a real investor PDF report or earnings document.

### 5. Run the KPI extraction script
```bash
python investment_pipeline.py
```
> This generates `extracted_kpis.xlsx` containing the extracted metrics.

---

## 🌐 Launch the Streamlit Dashboard

```bash
streamlit run dashboard.py
```

Then open your browser at:
```
http://localhost:8501
```

Upload the `extracted_kpis.xlsx` file in the UI to view KPI metrics and charts.

---

## 📊 Sample Output
| Metric   | Value     |
|----------|-----------|
| Revenue  | $3,500,000|
| EBITDA   | $700,000  |

---

## 📂 Project Structure
```
investment_pipeline.py   # PDF text + KPI extraction script
dashboard.py             # Streamlit dashboard for viewing results
requirements.txt         # Python dependencies
README.md                # Documentation
sample_investment.pdf    # Placeholder - replace with real data
```

---

## 🤔 Tips
- Ensure your PDFs are text-based (not scanned images) for accurate extraction.
- Want to automate it all in the dashboard? Ask about full PDF-to-dashboard integration.

---

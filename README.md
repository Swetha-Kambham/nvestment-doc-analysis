# Investment Document Analysis Pipeline

This project extracts key financial metrics (KPIs) from investment-related PDF documents using OCR, NLP, and zero-shot classification. The extracted data is structured into Excel and visualized through an interactive Streamlit dashboard.

Built with Python, Hugging Face Transformers, pdfplumber, and Streamlit — this pipeline makes financial document parsing efficient, automated, and accessible.


# Investment Document Analysis Pipeline

This project extracts key financial KPIs (e.g., Revenue, EBITDA, Growth, Valuation) from text-based investment documents (PDFs). The extracted metrics are saved to Excel and visualized using an interactive Streamlit dashboard.


---

## ## Snowflake Integration

You can upload the extracted KPI results directly into a Snowflake table using the provided script.

### 1. Set your environment variables
Create a `.env` file (use the `.env.example` template) and fill in your Snowflake credentials:

```env
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account_url   # e.g., xy12345.us-east-1
SNOWFLAKE_WAREHOUSE=your_warehouse
SNOWFLAKE_DATABASE=your_database
SNOWFLAKE_SCHEMA=your_schema
```

### 2. Create the table in Snowflake
Run this in Snowflake (manually or via Python):

```sql
CREATE TABLE investment_kpis (
    metric STRING,
    value STRING,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Run the upload script
```bash
python upload_to_snowflake.py
```

The script will upload rows from `extracted_kpis.xlsx` into the specified Snowflake table.

---

---

## Objective
Automatically extract financial metrics from investor reports or earnings documents and enable data visualization without manual parsing.

---

## Features
-  Extract KPIs like Revenue, EBITDA, Profit, Growth, Acquisition
-  Use Hugging Face's BART model for zero-shot financial topic classification
-  Export structured data to Excel
-  View results interactively in a dashboard
-  Built with Streamlit, Pandas, Transformers, and pdfplumber

---

## Tech Stack
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

## Launch the Streamlit Dashboard

```bash
streamlit run dashboard.py
```

Then open your browser at:
```
http://localhost:8501
```

Upload the `extracted_kpis.xlsx` file in the UI to view KPI metrics and charts.

---

## Sample Output
| Metric   | Value     |
|----------|-----------|
| Revenue  | $3,500,000|
| EBITDA   | $700,000  |

---

## Project Structure
```
investment_pipeline.py   # PDF text + KPI extraction script
dashboard.py             # Streamlit dashboard for viewing results
requirements.txt         # Python dependencies
README.md                # Documentation
sample_investment.pdf    # Placeholder - replace with real data
```

---

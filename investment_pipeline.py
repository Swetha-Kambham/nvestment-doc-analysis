import pdfplumber
import re
import pandas as pd
from transformers import pipeline

# Step 1: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
    return text

# Step 2: Run classification
def classify_text(text):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["Revenue", "EBITDA", "Acquisition", "Growth", "Valuation"]
    return classifier(text[:1000], candidate_labels=labels)

# Step 3: Extract KPI patterns
def extract_kpis(text):
    return re.findall(r"(Revenue|EBITDA|Profit).*?\$?[0-9,.]+", text, re.IGNORECASE)

# Step 4: Save to Excel
def save_to_excel(kpis, output_path="extracted_kpis.xlsx"):
    df = pd.DataFrame(kpis, columns=["Metric", "Value"])
    df.to_excel(output_path, index=False)
    print(f"KPI data saved to {output_path}")

if __name__ == "__main__":
    path = "sample_investment.pdf"
    text = extract_text_from_pdf(path)
    classifications = classify_text(text)
    print("Classification results:", classifications)
    kpi_data = extract_kpis(text)
    save_to_excel(kpi_data)

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

# Step 2: Run zero-shot classification (optional, just for info)
def classify_text(text):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["Revenue", "EBITDA", "Growth", "Acquisition", "Valuation"]
    result = classifier(text[:1000], candidate_labels=labels)
    print("Classification results:", result)
    return result

# Step 3: Extract KPI metric + value pairs
def extract_kpis(text):
    pattern = r"(Revenue|EBITDA|Profit|Growth|Valuation|Acquisition)[^\n\r:]*[:\-]?\s*\$?([0-9.,]+(?:\s?%|\s?M)?)"
    return re.findall(pattern, text, re.IGNORECASE)

# Step 4: Save results to Excel
def save_to_excel(kpis, output_path="extracted_kpis.xlsx"):
    if not kpis:
        print("No KPI data found.")
        return
    df = pd.DataFrame(kpis, columns=["Metric", "Value"])
    df.to_excel(output_path, index=False)
    print(f"KPI data saved to {output_path}")

if __name__ == "__main__":
    path = "sample_investment.pdf"  # Or replace with your actual filename
    text = extract_text_from_pdf(path)
    classify_text(text)
    kpi_data = extract_kpis(text)
    save_to_excel(kpi_data)

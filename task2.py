import pandas as pd
from fpdf import FPDF

# Load CSV file
csv_file = "sample_data.csv"

# Read the CSV file
df = pd.read_csv(csv_file)

# Perform basic summary analysis
summary = df.describe()

# Define PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Automated Report", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, body)
        self.ln()

# Create and write to PDF
pdf = PDF()
pdf.add_page()
pdf.chapter_title("Summary Statistics:")
pdf.chapter_body(summary.to_string())

# Output PDF file
pdf.output("report.pdf")

print("✅ PDF report generated successfully: report.pdf")

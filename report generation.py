import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# 1. Read data from CSV
data = pd.read_csv("sample_data.csv")  # Replace with your actual file name

# 2. Analyze data (basic statistics)
summary = data.describe().round(2)

# 3. Generate PDF report
def generate_report(data_summary, output_path="report.pdf"):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("Automated Data Report", styles['Title']))
    elements.append(Spacer(1, 12))

    # Description
    elements.append(Paragraph("This report contains basic statistical analysis of the input data file.", styles['BodyText']))
    elements.append(Spacer(1, 12))

    # Convert summary to table
    table_data = [ [col] + list(data_summary[col].values) for col in data_summary.columns ]
    table_data.insert(0, ['Metric'] + list(data_summary.index))

    # Transpose table data for better layout
    table_data = list(map(list, zip(*table_data)))

    table = Table(table_data, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0,0),(-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0),(-1,0),12),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ]))

    elements.append(table)
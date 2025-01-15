from flask import Flask, request, jsonify, send_file, render_template
import pdfkit
import os

app = Flask(__name__)

# Directory for generated PDFs
PDF_FOLDER = "generated_pdfs"
os.makedirs(PDF_FOLDER, exist_ok=True)

# Path to wkhtmltopdf executable
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"  # Update this path as needed
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    try:
        # Get JSON data from the request
        data = request.json

        # Render the HTML template with the provided data
        rendered_html = render_template("template.html", **data)

        # Path to save the generated PDF
        pdf_file_path = os.path.join(PDF_FOLDER, "output.pdf")

        # Generate the PDF with the specified configuration
        pdfkit.from_string(rendered_html, pdf_file_path, configuration=config)

        # Return the PDF file as a response
        return send_file(pdf_file_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

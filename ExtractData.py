from RPA.PDF import PDF
from robot.libraries.String import String

pdf = PDF()
string = String()

def extract_data_from_first_page():
    text = pdf.get_text_from_pdf("example-invoice.pdf")
    lines = string.get_lines_matching_regexp(text[1], ".+pain.+")
    print(lines)

def get_invoice_number():
    pdf.open_pdf("example-invoice.pdf")
    matches = pdf.find_text("Invoice Number")
    print(matches[0].neighbours[0])


def fill_form_fields():
    pdf.switch_to_pdf("form.pdf")
    fields = pdf.get_input_fields(encoding="utf-16")
    for key, value in fields.items():
        print(f"{key}: {value}")
    pdf.set_field_value("Given Name Text Box", "Mark")
    pdf.save_field_values(
        output_path="completed-form.pdf",
        use_appearances_writer=True
    )

get_invoice_number()
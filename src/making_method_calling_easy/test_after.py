from .after import ReportGenerator


def test_report_generator():
    generator = ReportGenerator("Sample Data")
    pdf_report = generator.generate_pdf_report()
    assert "PDF Header" in pdf_report
    assert "Summary: This is a summary." in pdf_report
    assert "Graphs: These are graphs." in pdf_report

    html_report = generator.generate_html_report(include_summary=False)
    assert "<html>" in html_report
    assert "Summary: This is a summary." not in html_report
    assert "Graphs: These are graphs." in html_report

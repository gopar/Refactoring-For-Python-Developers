from .before import ReportGenerator


def test_report_generator():
    generator = ReportGenerator("Sample Data")
    report = generator.generate_report("PDF", True, True)

    assert "PDF Header" in report
    assert "Summary: This is a summary." in report
    assert "Graphs: These are graphs." in report

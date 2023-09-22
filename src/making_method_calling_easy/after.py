class ReportGenerator:
    PDF_REPORT = "PDF"
    HTML_REPORT = "HTML"

    def __init__(self, data: str) -> None:
        self.data = data

    def generate_pdf_report(self, include_summary: bool = True, include_graphs: bool = True) -> str:
        return self._generate_report("PDF Header\n", "PDF Footer\n", include_summary, include_graphs)

    def generate_html_report(self, include_summary: bool = True, include_graphs: bool = True) -> str:
        return self._generate_report("<html>\n", "</html>\n", include_summary, include_graphs)

    def generate_report(self, report_type: str, include_summary: bool = True, include_graphs: bool = True) -> str:
        report_generators = {
            ReportGenerator.PDF_REPORT: self.generate_pdf_report,
            ReportGenerator.HTML_REPORT: self.generate_html_report,
        }

        generator = report_generators.get(report_type, None)
        if not generator:
            raise Exception(f"Generator {report_type} Not Found")

        return generator(include_summary, include_graphs)

    def _generate_report(self, header: str, footer: str, include_summary: bool, include_graphs: bool) -> str:
        report = header
        report += "Report Data: {}\n".format(self.data)
        if include_summary:
            report += "Summary: This is a summary.\n"
        if include_graphs:
            report += "Graphs: These are graphs.\n"
        report += footer
        return report

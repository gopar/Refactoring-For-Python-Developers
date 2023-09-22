class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self, format_type, include_summary, include_graphs):
        report = ""
        if format_type == "PDF":
            report += "PDF Header\n"
        elif format_type == "HTML":
            report += "<html>\n"

        report += "Report Data: {}\n".format(self.data)

        if include_summary:
            report += "Summary: This is a summary.\n"

        if include_graphs:
            report += "Graphs: These are graphs.\n"

        if format_type == "PDF":
            report += "PDF Footer\n"
        elif format_type == "HTML":
            report += "</html>\n"

        return report

from application.domain.Report import Report
from adapter.out.persistence.reportRepository import ReportRepository
from injector import inject


class ReportService:
    @inject
    def __init__(self, report_repository: ReportRepository):
        self.report_repository = report_repository
        self.template_name = "report.html"

    def create_report(self, report: Report):
        return self.report_repository.create_report(report, self.template_name)
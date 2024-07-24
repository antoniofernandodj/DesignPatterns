from interface import DocumentFactory, Page


class ReportFactory(DocumentFactory):
    def create_page(self):
        return ReportPage()


class ReportPage(Page):
    def describe(self):
        return "This is a report page."

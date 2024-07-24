from interface import DocumentFactory, Page


class ResumeFactory(DocumentFactory):
    def create_page(self):
        return ResumePage()


class ResumePage(Page):
    def describe(self):
        return "This is a resume page."

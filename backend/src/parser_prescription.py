from parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        pass



if __name__ == "__main__":
    PrescriptionParser("abc") 
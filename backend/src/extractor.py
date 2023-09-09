from pdf2image import convert_from_path
import utils
import pytesseract


def extract(file_path, file_format):
    pages = convert_from_path(file_path)
    document_text = ''
    for page in pages:
        processed_image = utils.preprocess_input_image(page)
        text = pytesseract.image_to_string(processed_image,lang = 'eng')
        document_text = '\n' +  text
    
    return document_text
    # if file_format == 'prescription':
    #     ## extract data from prescription
    #     pass

    # elif file_format == 'patient_details':
    #     ## extract data from patient_details
    #     pass



if __name__ == "__main__":
    data = extract("../resources/patient_details/pd_1.pdf",'prescription')
    print(data)

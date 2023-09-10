from backend.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_virat():
    document_text = '''
    Dr John Smith, M.D

    2 Non-Important street,
    New York, Phone (900)-a23- ~2222

    Name:  Virat Kohli Date: 2/05/2022

    Address: 2 cricket blvd, New Delhi

    | Omeprazole 40 mg

    Directions: Use two tablets daily for three months

    Refill: 3 times
    '''

    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_marta():
    document_text = '''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-121-2222

    Name: Marta Sharapova Date: 2/11/2022

    Address: 9 tennis court, new Russia, DC

    K

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:
    Prednisone, Taper 5 mg every 3 days,

    Finish in 2.5 weeks -
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    '''

    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_3_empty():
    document_text = ''
    return PrescriptionParser(document_text)

def test_get_name(doc_1_virat,doc_2_marta,doc_3_empty):
    assert doc_1_virat.get_field('patient_name') == 'Virat Kohli'
    assert doc_2_marta.get_field('patient_name') == 'Marta Sharapova'
    assert doc_3_empty.get_field('patient_name') is None


def test_get_address(doc_1_virat,doc_2_marta,doc_3_empty):
    assert doc_1_virat.get_field('patient_address') == '2 cricket blvd, New Delhi'
    assert doc_2_marta.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_3_empty.get_field('patient_address') is None

def test_get_medicines(doc_1_virat,doc_2_marta,doc_3_empty):
    assert doc_1_virat.get_field('medicines') == '| Omeprazole 40 mg'
    assert doc_2_marta.get_field('medicines') == 'Prednisone 20 mg\n Lialda 2.4 gram'
    assert doc_3_empty.get_field('medicines') is None


def test_get_directions(doc_1_virat,doc_2_marta,doc_3_empty):
    assert doc_1_virat.get_field('directions') == 'Use two tablets daily for three months'
    assert doc_2_marta.get_field('directions') == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks -\nLialda - take 2 pill everyday for 1 month'
    assert doc_3_empty.get_field('directions') is None

def test_get_refills(doc_1_virat,doc_2_marta,doc_3_empty):
    assert doc_1_virat.get_field('refills') == '3'
    assert doc_2_marta.get_field('refills') == '2'
    assert doc_3_empty.get_field('refills') is None

def test_parse(doc_1_virat,doc_2_marta,doc_3_empty):
    pass 
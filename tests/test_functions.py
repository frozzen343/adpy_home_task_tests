import pytest 
from app import *


class TestFunctions:
    def test_get_name(self):
        result = get_name('10006')
        assert 'Аристарх Павлов' == result

    def test_get_shelf_number(self):
        result = get_shelf_number('2207 876234')
        assert '1' == result

    def test_get_all_documents(self):
        documents_list = []
        for document in documents:
            documents_list.append([document['type'], document['number'], document['name']])
        result = get_all_documents()
        assert documents_list == result

    def test_add_document(self):
        result = add_document('passport', '12345', 'Ivan Pupkin', '3')
        assert 'добавлен документ на полку 3' == result

    def test_del_document(self):
        result = del_document('12345')
        assert 'Документ 12345 удалён' == result

    def test_move_document(self):
        result = move_document('10006', '3')
        assert 'Документ перемещён' == result

    def test_add_shelf(self):
        result = add_shelf('4')
        assert 'Полка 4 добавлена' == result
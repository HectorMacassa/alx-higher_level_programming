#!/usr/bin/python3

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_init_without_id(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)
        self.assertEqual(Base.__nb_objects, 2)

    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_list_of_dicts(self):
        data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json.loads(json_string), data)

    def test_save_to_file_empty_list(self):
        self.setUp()
        Base.save_to_file([])
        with open(self.filename, "r") as f:
            json_string = f.read()
            self.assertEqual(json_string, "[]")
        self.tearDown()

    def test_save_to_file_list_of_objects(self):
        self.setUp()
        obj1 = Base(10)
        obj2 = Base(20)
        Base.save_to_file([obj1, obj2])
        with open(self.filename, "r") as f:
            json_string = f.read()
            data = json.loads(json_string)
            self.assertEqual(data, [{"id": 10}, {"id": 20}])
        self.tearDown()

    def test_from_json_string_empty_string(self):
        data = Base.from_json_string("")
        self.assertEqual(data, [])

    def test_from_json_string_json_string(self):
        json_string = '[{"id": 10}, {"id": 20}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{"id": 10}, {"id": 20}])

    def test_create_rectangle(self):
        rect = Base.create(width=10, height=5)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)

    def test_create_default(self):
        obj = Base.create()
        self.assertEqual(obj.id, 2)

    def test_load_from_file_empty_file(self):
        self.setUp()
        data = Base.load_from_file()
        self.assertEqual(data, [])
        self.tearDown()

    def test_load_from_file_with_data(self):
        self.setUp()
        data = [{"id": 10}, {"id": 20}]
        with open(self.filename, "w") as f:
            f.write(json.dumps(data))
        loaded_data = Base.load_from_file()
        self.assertEqual(loaded_data, data)
        self.tearDown()

    def setUp(self):
        self.filename = "test.json"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == "__main__":
    unittest.main()

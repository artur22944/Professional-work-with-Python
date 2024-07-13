import unittest
import task_2


class TestCreateFolderYandex(unittest.TestCase):

    def test_create_folder_yandex(self):
        self.assertEqual(task_2.create_folder_yandex("TEST"), 201)

    def test_failed_create_folder_yandex(self):
        self.assertEqual(task_2.create_folder_yandex("TEST_failed"), 409)

    def test_delete_folder_yandex(self):
        self.assertEqual(task_2.delete_folder_yandex("TEST"), 204)


if __name__ == "__main__":
    unittest.main()

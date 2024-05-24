#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Для индивидуального задания лабораторной работы 2.21
# добавьте тесты с использованием модуля unittest, 
# проверяющие операции по работе с базой данных.


from ind import create_db, add_person, select_all
import sqlite3
import unittest
import pathlib


class indTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("Проверка работы операций с базами данных")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("Конец")

    def test_create_bd(self):
        def created_bd(name_bd):
            file_path = pathlib.Path.cwd() / name_bd

            if file_path.exists and file_path.is_file:
                return True
            return False
        self.assertEqual(create_db("test_bd"), created_bd("test_bd"))

    def test_add_person(self):
        def added_person(name_bd, full_name, birth_date, phone):
            conn = sqlite3.connect(name_bd)
            cursor = conn.cursor()

            cursor.execute(
                """
                    SELECT names.full_name, person.birth_date, person.phone_number
                    FROM person
                    INNER JOIN names ON names.name_id = person.name_id
                    WHERE 
                    names.full_name = ? and 
                    person.birth_date = ? and 
                    person.phone_number = ?
                """,
                (full_name, birth_date, phone),
            )
            rows = cursor.fetchall()
            conn.close()

            return bool(rows)
        
        add_person("test_bd", "Артем", 22, 5555)
        self.assertEqual(
            True,
            added_person("test_bd", "Артем", 22, 5555),
        )

    def test_select_all_last(self):
        self.assertEqual(len(select_all("test_bd")[-1]), 3)

    def test_select_all_first(self):
        self.assertEqual(len(select_all("test_bd")[0]), 3)

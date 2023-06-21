import unittest
import os
from pathlib import Path
from fastapi.testclient import TestClient
from tracking_api.app import fastapi_app,check_file

client = TestClient(fastapi_app)


class TestAPI(unittest.TestCase):

    def test_no_file(self):
        Path('/tmp/ok').touch()
        self.assertEqual(check_file(), True)

    def test_ping_200(self):
        """
        Test to validate that the ping returns 200 when the file is there.
        """
        response = client.get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "OK")

    def test_ping_503(self):
        """
        Test to validate that the ping returns 200 when the file is there.
        """
        os.remove('/tmp/ok')
        # Unset the cache for testing
        check_file.cache_clear()
        response = client.get("/ping")
        self.assertEqual(response.status_code, 503)
        # Cleanup for next test run
        self.assertEqual(response.json(), "Service Unavailable")



    def test_image_200(self):
        """
        Test to validate that the gif is returned.
        """
        response = client.get("/img")
        self.assertEqual(response.status_code, 200)

    def test_random_fails(self):
        """
        Test to validating unknown endpoints return 404
        """
        response = client.get("/random")
        self.assertEqual(response.status_code, 404)


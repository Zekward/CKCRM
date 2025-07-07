import unittest
from unittest.mock import patch, MagicMock
import os
import base64
import json

from app.data import get_gspread_client, get_sheet_records, transform_row_to_client, group_clients_by_stage

class TestDataFunctions(unittest.TestCase):
    @patch.dict(os.environ, {
        'GOOGLE_CREDENTIALS': base64.b64encode(json.dumps({
            "type": "service_account",
            "project_id": "mock-project",
            "private_key_id": "fake-key-id-123456",
            "private_key": "-----BEGIN PRIVATE KEY-----\\nFAKEPRIVATEKEY1234567890\\n-----END PRIVATE KEY-----\\n",
            "client_email": "mock-service-account@mock-project.iam.gserviceaccount.com",
            "client_id": "12345678901234567890",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mock-service-account%40mock-project.iam.gserviceaccount.com"
        }).encode()).decode()
    })

    @patch('app.data.gspread.service_account_from_dict')
    def test_get_gspread_client(self, mock_service_account):
        """ Should return mocked gspread client when env is set """
        mock_service_account.return_value = "MockClient"
        client = get_gspread_client()
        self.assertEqual(client, "MockClient")
        mock_service_account.assert_called_once()

    @patch('app.data.get_gspread_client')
    def test_get_sheet_records(self, mock_get_client):
        """ Should fetch records from first worksheet """
        mock_worksheet = MagicMock()
        mock_worksheet.get_all_records.return_value = [
            {"Name": "Alice", "Email": "alice@example.com"}
        ]

        mock_sheet = MagicMock()
        mock_sheet.sheet1 = mock_worksheet

        mock_client = MagicMock()
        mock_client.open.return_value = mock_sheet
        mock_get_client.return_value = mock_client

        result = get_sheet_records(sheet_name="TestSheet")
        self.assertEqual(result, [{"Name": "Alice", "Email": "alice@example.com"}])
        mock_client.open.assert_called_with("TestSheet")

    def test_transform_row_to_client(self):
        """ Should properly transform raw Google Sheet row data into client """
        row = {
            "Name": "Bob",
            "Email": "bob@example.com",
            "Enter your number": "123-456",
            "Make and Model": "Honda Civic",
            "Which services are you interested in?": "Detailing",
            "Status": "Booked",
            "Submitted At": "2025-07-05 14:30"
        }

        expected = {
            "name": "Bob",
            "email": "bob@example.com",
            "phone": "123-456",
            "car_model": "Honda Civic",
            "service": "Detailing",
            "stage": "Booked",
            "source": "Typeform",
            "submitted_at": "2025-07-05 14:30"
        }

        client = transform_row_to_client(row)
        self.assertEqual(client, expected)

    def test_group_clients_by_stage(self):
        test_clients = [
            {"name": "Alice", "stage": "New Lead"},
            {"name": "Bob", "stage": "Contacted"},
            {"name": "Carol", "stage": "New Lead"},
            {"name": "Dave", "stage": "Booked"},
            {"name": "Eve", "stage": "Followed Up"},
            {"name": "Frank", "stage": "Closed"},
            {"name": "Gina", "stage": "Unknown Stage"},
        ]

        grouped = group_clients_by_stage(test_clients)

        # Only keep stages that have clients
        grouped_names = {
            stage: [c["name"] for c in clients]
            for stage, clients in grouped.items()
            if clients
        }

        expected_names = {
            "New Lead": ["Alice", "Carol"],
            "Contacted": ["Bob"],
            "Booked": ["Dave"],
            "Closed": ["Frank"],
            "Followed Up": ["Eve"],
            "Unknown Stage": ["Gina"]
        }

        self.assertEqual(grouped_names, expected_names)



if __name__ == '__main__':
     unittest.main()
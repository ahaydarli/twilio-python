# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class AppTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.apps.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://microvisor.twilio.com/v1/Apps',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "apps": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://microvisor.twilio.com/v1/Apps?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://microvisor.twilio.com/v1/Apps?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "apps"
                }
            }
            '''
        ))

        actual = self.client.microvisor.v1.apps.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "apps": [
                    {
                        "sid": "KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "hash": "hash",
                        "unique_name": "unique name",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://microvisor.twilio.com/v1/Apps/KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "app_manifests": "https://microvisor.twilio.com/v1/Apps/KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Manifest"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://microvisor.twilio.com/v1/Apps?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://microvisor.twilio.com/v1/Apps?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "apps"
                }
            }
            '''
        ))

        actual = self.client.microvisor.v1.apps.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.apps("KAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://microvisor.twilio.com/v1/Apps/KAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "hash": "hash",
                "unique_name": "look at this crazy app",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://microvisor.twilio.com/v1/Apps/KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "app_manifests": "https://microvisor.twilio.com/v1/Apps/KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Manifest"
                }
            }
            '''
        ))

        actual = self.client.microvisor.v1.apps("KAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.apps("KAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://microvisor.twilio.com/v1/Apps/KAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.microvisor.v1.apps("KAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

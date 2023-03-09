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


class InsightsQuestionnairesQuestionTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.insights_questionnaires_question.create(category_id="category_id", question="question", answer_set_id="answer_set_id", allow_na=True, token="token")

        values = {
            'CategoryId': "category_id",
            'Question': "question",
            'AnswerSetId': "answer_set_id",
            'AllowNa': True,
        }

        headers = {'Token': "token", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Insights/QM/Questions',
            headers=headers,
        ))
        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Insights/QM/Questions',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "question": "What is the total time",
                "question_id": "945ac7ff-8afc-4606-be76-e94b1a80cd72",
                "description": "time spent",
                "category": {
                    "category_name": "test cat",
                    "category_id": "4b4e78e4-4f05-49e2-bf52-0973c5cde418"
                },
                "answer_set_id": "a6a8a54f-5305-4aec-b92c-a6e429932f58",
                "allow_na": false,
                "usage": 0,
                "answer_set": {
                    "sort": 0,
                    "name": "Yes, No",
                    "answers": [
                        {
                            "sort": 0,
                            "score": 100,
                            "description": "Yes.",
                            "name": "Yes",
                            "id": "4e34f701-8206-4670-b376-c9fe26bb3ca3"
                        },
                        {
                            "sort": 1,
                            "score": 0,
                            "description": "No or a very poor.",
                            "name": "No",
                            "id": "5e926651-fa5d-4aba-86e1-8440bb8faa6c"
                        }
                    ],
                    "category_id": "1a8cac56-826c-4f85-ac14-9104811cf184",
                    "type": "select",
                    "id": "a6a8a54f-5305-4aec-b92c-a6e429932f58"
                },
                "url": "https://flex-api.twilio.com/v1/Insights/QM/Questions/945ac7ff-8afc-4606-be76-e94b1a80cd72"
            }
            '''
        ))

        actual = self.client.flex_api.v1.insights_questionnaires_question.create(category_id="category_id", question="question", answer_set_id="answer_set_id", allow_na=True)

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.insights_questionnaires_question("question_id").update(allow_na=True, token="token")

        values = {'AllowNa': True, }

        headers = {'Token': "token", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Insights/QM/Questions/question_id',
            headers=headers,
        ))
        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Insights/QM/Questions/question_id',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "question": "What is the total time",
                "question_id": "945ac7ff-8afc-4606-be76-e94b1a80cd72",
                "description": "time spent",
                "category": {
                    "category_name": "test cat",
                    "category_id": "4b4e78e4-4f05-49e2-bf52-0973c5cde418"
                },
                "answer_set_id": "a6a8a54f-5305-4aec-b92c-a6e429932f58",
                "allow_na": false,
                "usage": 0,
                "answer_set": {
                    "sort": 0,
                    "name": "Yes, No",
                    "answers": [
                        {
                            "sort": 0,
                            "score": 100,
                            "description": "Yes.",
                            "name": "Yes",
                            "id": "4e34f701-8206-4670-b376-c9fe26bb3ca3"
                        },
                        {
                            "sort": 1,
                            "score": 0,
                            "description": "No or a very poor.",
                            "name": "No",
                            "id": "5e926651-fa5d-4aba-86e1-8440bb8faa6c"
                        }
                    ],
                    "category_id": "1a8cac56-826c-4f85-ac14-9104811cf184",
                    "type": "select",
                    "id": "a6a8a54f-5305-4aec-b92c-a6e429932f58"
                },
                "url": "https://flex-api.twilio.com/v1/Insights/QM/Questions/945ac7ff-8afc-4606-be76-e94b1a80cd72"
            }
            '''
        ))

        actual = self.client.flex_api.v1.insights_questionnaires_question("question_id").update(allow_na=True)

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.insights_questionnaires_question.list(token="token")

        headers = {'Token': "token", }
        self.holodeck.assert_has_request(Request(
            'get',
            'https://flex-api.twilio.com/v1/Insights/QM/Questions',
            headers=headers,
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "questions": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://flex-api.twilio.com/v1/Insights/QM/Questions?CategoryId=4b4e78e4-4f05-49e2-bf52-0973c5cde419&PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://flex-api.twilio.com/v1/Insights/QM/Questions?CategoryId=4b4e78e4-4f05-49e2-bf52-0973c5cde419&PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "questions"
                }
            }
            '''
        ))

        actual = self.client.flex_api.v1.insights_questionnaires_question.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "questions": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "question": "What is the total time",
                        "question_id": "945ac7ff-8afc-4606-be76-e94b1a80cd72",
                        "description": "time spent",
                        "category": {
                            "category_name": "test cat",
                            "category_id": "4b4e78e4-4f05-49e2-bf52-0973c5cde418"
                        },
                        "answer_set_id": "a6a8a54f-5305-4aec-b92c-a6e429932f58",
                        "allow_na": false,
                        "usage": 0,
                        "answer_set": {
                            "sort": 0,
                            "name": "Yes, No",
                            "answers": [
                                {
                                    "sort": 0,
                                    "score": 100,
                                    "description": "Yes.",
                                    "name": "Yes",
                                    "id": "4e34f701-8206-4670-b376-c9fe26bb3ca3"
                                },
                                {
                                    "sort": 1,
                                    "score": 0,
                                    "description": "No or a very poor.",
                                    "name": "No",
                                    "id": "5e926651-fa5d-4aba-86e1-8440bb8faa6c"
                                }
                            ],
                            "category_id": "1a8cac56-826c-4f85-ac14-9104811cf184",
                            "type": "select",
                            "id": "a6a8a54f-5305-4aec-b92c-a6e429932f58"
                        },
                        "url": "https://flex-api.twilio.com/v1/Insights/QM/Questions/945ac7ff-8afc-4606-be76-e94b1a80cd72"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://flex-api.twilio.com/v1/Insights/QM/Questions?CategoryId=4b4e78e4-4f05-49e2-bf52-0973c5cde419&PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://flex-api.twilio.com/v1/Insights/QM/Questions?CategoryId=4b4e78e4-4f05-49e2-bf52-0973c5cde419&PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "questions"
                }
            }
            '''
        ))

        actual = self.client.flex_api.v1.insights_questionnaires_question.list()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.insights_questionnaires_question("question_id").delete(token="token")

        headers = {'Token': "token", }
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://flex-api.twilio.com/v1/Insights/QM/Questions/question_id',
            headers=headers,
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.flex_api.v1.insights_questionnaires_question("question_id").delete()

        self.assertTrue(actual)

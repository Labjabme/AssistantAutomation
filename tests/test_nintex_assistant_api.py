import json
from typing import Generator
import pytest
import allure
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope="session")
def api_request_context(
        playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Content-Type": "application/json",
        "Content-Length": "<calculated when request is sent>"
    }
    request_context = playwright.request.new_context(
        base_url=" https://testlb.kryon.io", extra_http_headers=headers,

    )
    yield request_context
    request_context.dispose()


@allure.title("Test Nintex Assistant")
@pytest.mark.functional
def test_get_nintex_q_a(api_request_context: APIRequestContext):
    query = """\n\tmutation apredictAnswer($question: String!, $sessionId: String!, $collectionId: String!, 
    $responseMode: String!){\n\tapredictAnswer(question: $question, sessionId: $sessionId, collectionId: 
    $collectionId, responseMode: $responseMode){\n\tanswer\n\tmessageId\n\tsourceDocuments {\n\t\tmetadata {
    \n\t\tsource\n\t\ttitle\n\t\tcategory\n\t\t}\n\t}}}"""
    response = api_request_context.post(
        "/", data={"query": query}

    )

    print("\n" + response.text())
    assert response.ok
    assert response.status == 200


@allure.title("Test Nintex Assistant_Docgen")
@pytest.mark.functional
def test_get_nintext_question_answer(api_request_context: APIRequestContext):
    query = """
        
    \n\tmutation apredictAnswer($question: String!, $sessionId: String!, $collectionId: String!, $responseMode: String!){\n\tapredictAnswer(question: $question, sessionId: $sessionId, collectionId: $collectionId, responseMode: $responseMode){\n\tanswer\n\tmessageId\n\tsourceDocuments {\n\t\tmetadata {\n\t\tsource\n\t\ttitle\n\t\tcategory\n\t\t}\n\t}}}",
    "variables": {
                "question": "How can I find my account ID in the integration tab?",
                "sessionId": "undefined",
                "collectionId": "docgen",
                "responseMode": "default"
                }

      """
    response = api_request_context.post(
        "/", data={"query": query}
    )
    print("\n" + response.text())
    assert response.ok
    assert response.status == 200


@allure.title("Test Nintex Assistant_Docgen_response_1")
@pytest.mark.functional
def test_docgen_related_question(api_request_context: APIRequestContext):
    query = '''{
         "\n\tmutation apredictAnswer($question: String!, $sessionId: String!, $collectionId: String!, "
                 "$responseMode: String!){\n\tapredictAnswer(question: $question, sessionId: $sessionId, collectionId: "
                 "$collectionId, responseMode: $responseMode){\n\tanswer\n\tmessageId\n\tsourceDocuments {"
                 "\n\t\tmetadata"
                 "{\n\t\tsource\n\t\ttitle\n\t\tcategory\n\t\t}\n\t}}}",
        "variables": {
            "question": "How can I find my account ID in the integration tab?",
            "sessionId": "undefined",
            "collectionId": "docgen",
            "responseMode": "default"
        }
    }'''
    response = api_request_context.post(
        "/api/helper-chatbot-proxy/graphql", data={"query": query}
    )
    print(response)
    print("\n" + response.text())
    content = response.text()
    print(f"Response content: {content}")

    # Attempt to parse JSON
    try:
        data = json.loads(content)
        print(f"Decoded JSON data: {data}")
    except json.decoder.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response content that caused error: {content}")
    assert response.ok
    print(response.status)
    assert response.status == 200


@allure.title("Test Nintex Assistant_Docgen_response")
@pytest.mark.regression
def test_query_docgen_q_and_a(api_request_context: APIRequestContext):
    query = """

    \n\tmutation apredictAnswer($question: String!, $sessionId: String!, $collectionId: String!, $responseMode: String!){\n\tapredictAnswer(question: $question, sessionId: $sessionId, collectionId: $collectionId, responseMode: $responseMode){\n\tanswer\n\tmessageId\n\tsourceDocuments {\n\t\tmetadata {\n\t\tsource\n\t\ttitle\n\t\tcategory\n\t\t}\n\t}}}",
    "variables": {
                "question": "How can I find my account ID in the integration tab?",
                "sessionId": "undefined",
                "collectionId": "docgen",
                "responseMode": "default"
                }

      """
    response = api_request_context.post(
        "/api/helper-chatbot-proxy/graphql", data={"query": query}
    )
    print(response)
    print("\n" + response.text())
    content = response.text()
    print(f"Response content: {content}")

    # Attempt to parse JSON
    try:
        data = json.loads(content)
        print(f"Decoded JSON data: {data}")
    except json.decoder.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response content that caused error: {content}")
    assert response.ok
    print(response.status)
    assert response.status == 200


@allure.title("Test Nintex Assistant_Output")
@pytest.mark.regression
def test_nintex_assistant_testing(api_request_context: APIRequestContext):
    query = """\n\tmutation apredictAnswer($question: String!, $sessionId: String!, $collectionId: String!, 
    $responseMode: String!){\n\tapredictAnswer(question: $question, sessionId: $sessionId, collectionId: 
    $collectionId, responseMode: $responseMode){\n\tanswer\n\tmessageId\n\tsourceDocuments {\n\t\tmetadata {
    \n\t\tsource\n\t\ttitle\n\t\tcategory\n\t\t}\n\t}}}"""
    response = api_request_context.post(
        "/api/helper-chatbot-proxy/graphql", data={"query": query}
    )
    print(response)
    print("\n" + response.text())
    content = response.text()
    print(f"Response content: {content}")

    # Attempt to parse JSON
    try:
        data = json.loads(content)
        print(f"Decoded JSON data: {data}")
    except json.decoder.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response content that caused error: {content}")
    assert response.ok
    print(response.status)
    assert response.status == 200


@allure.title("Test Nintex Assistant_Output_Evaluate")
@pytest.mark.regression
def test_nintex_repitive_q_and_a(api_request_context: APIRequestContext):
    query = {
        "query": "\n\tmutation apredictAnswer($question: String!, $sessionId: String!, $collectionId: String!, "
                 "$responseMode: String!){\n\tapredictAnswer(question: $question, sessionId: $sessionId, collectionId: "
                 "$collectionId, responseMode: $responseMode){\n\tanswer\n\tmessageId\n\tsourceDocuments {"
                 "\n\t\tmetadata"
                 "{\n\t\tsource\n\t\ttitle\n\t\tcategory\n\t\t}\n\t}}}",
        "variables": {
            "question": "How can I find my account ID in the integration tab?",
            "sessionId": "undefined",
            "collectionId": "docgen",
            "responseMode": "default"
        }
    }
    response = api_request_context.post(
        "/api/helper-chatbot-proxy/graphql", data={"query": query}
    )
    print(response)
    print("\n" + response.text())
    content = response.text()
    print(f"Response content: {content}")

    # Attempt to parse JSON
    try:
        data = json.loads(content)
        print(f"Decoded JSON data: {data}")
    except json.decoder.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response content that caused error: {content}")
    assert response.ok
    print(response.status)
    assert response.status == 200


@allure.title("Test Nintex Assistant_Output_Evaluate-Query")
@pytest.mark.smoke
def test_nintex_repitive_q_and_a_query(api_request_context: APIRequestContext):
    query = """
mutation apredictAnswer($question: String!, $sessionId: String!, $collectionId: String!, $responseMode: String!) {
  apredictAnswer(question: $question, sessionId: $sessionId, collectionId: $collectionId, responseMode: $responseMode) {
    answer
    messageId
    sourceDocuments {
      metadata {
        source
        title
        category
      }
    }
  }
}
"""

    variables = {
        "question": "How can I find my account ID in the integration tab?",
        "sessionId": "undefined",
        "collectionId": "docgen",
        "responseMode": "default"
    }

    payload = {
        "query": query,
        "variables": variables
    }

    payload_str = json.dumps(payload)

    response = api_request_context.post(
        "/api/helper-chatbot-proxy/graphql", data={"query": payload_str}
    )
    print(response)
    print("\n" + response.text())
    content = response.text()
    print(f"Response content: {content}")

    # Attempt to parse JSON
    try:
        data = json.loads(content)
        print(f"Decoded JSON data: {data}")
    except json.decoder.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response content that caused error: {content}")
    assert response.ok
    print(response.status)
    assert response.status == 200


@allure.title("Test Nintex Assistant_Output_Evaluate-Query With variables")
@pytest.mark.smoke
def test_nintex_repitive_q_and_a_query_with_variables(api_request_context: APIRequestContext):
    query = {
        "query": "mutation apredictAnswer($question: String!, $sessionId: String!, $collectionId: String!, "
                 "$responseMode:"
                 "String!) { apredictAnswer(question: $question, sessionId: $sessionId, collectionId: $collectionId, "
                 "responseMode: $responseMode) { answer messageId sourceDocuments { metadata { source title category "
                 "} } } }",
        "variables": {
            "question": "How can I find my account ID in the integration tab?",
            "sessionId": "undefined",
            "collectionId": "docgen",
            "responseMode": "default"
        }
    }

    response = api_request_context.post(
        "/api/helper-chatbot-proxy/graphql", data={"query": query}
    )
    print(response)
    print("\n" + response.text())
    content = response.text()
    print(f"Response content: {content}")

    # Attempt to parse JSON
    try:
        data = json.loads(content)
        print(f"Decoded JSON data: {data}")
    except json.decoder.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response content that caused error: {content}")
    assert response.ok
    print(response.status)
    assert response.status == 200


@allure.title("Test Nintex Assistant_Output_Evaluate-Query With Dictionary")
@pytest.mark.smoke
def test_nintex_repitive_q_and_a_query_with_dictionary(api_request_context: APIRequestContext):
    query = {
        "query": "mutation apredictAnswer($question: String!, $sessionId: String!, $collectionId: String!, "
                 "$responseMode: String!) { apredictAnswer(question: $question, sessionId: $sessionId, collectionId: "
                 "$collectionId, responseMode: $responseMode) { answer messageId sourceDocuments { metadata { source "
                 "title category } } } }",
        "variables": {
            "question": "How can I find my account ID in the integration tab?",
            "sessionId": "undefined",
            "collectionId": "docgen",
            "responseMode": "default"
        }
    }

    # Convert the query dictionary to a JSON string
    query_str = json.dumps(query)

    response = api_request_context.post(
        "/api/helper-chatbot-proxy/graphql", data=query_str
    )
    print(response)
    print("\n" + response.text())
    content = response.text()
    print(f"Response content: {content}")

    # Attempt to parse JSON
    try:
        data = json.loads(content)
        print(f"Decoded JSON data: {data}")
    except json.decoder.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response content that caused error: {content}")
    assert response.ok
    print(response.status)
    assert response.status == 200

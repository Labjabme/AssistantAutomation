import configparser
import os
from locust import HttpUser, between, task

# Provide the full path to your config file
config_file_path = 'locust.conf'

# Read configuration from config.ini
config = configparser.ConfigParser()

if not os.path.exists(config_file_path):
    raise FileNotFoundError(f"Configuration file {config_file_path} not found.")

config.read(config_file_path)


class MyUser(HttpUser):
    wait_time = between(1, 5)
    host = config.get('locust', 'host')

    @task
    def my_task(self):
        query = '''
            mutation apredictAnswer(
                $question: String!,
                $sessionId: String!,
                $collectionId: String!,
                $responseMode: String!
            ) {
                apredictAnswer(
                    question: $question,
                    sessionId: $sessionId,
                    collectionId: $collectionId,
                    responseMode: $responseMode
                ) {
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
        '''
        variables = {
            "question": "How can I find my account ID in the integration tab?",
            "sessionId": "undefined",
            "collectionId": "docgen",
            "responseMode": "default"
        }
        response = self.client.post(
            "/api/helper-chatbot-proxy/graphql",
            json={"query": query, "variables": variables}
        )
        if response.status_code != 200:
            self.environment.events.request_failure.fire(
                request_type="POST",
                name="GraphQL Mutation",
                response_time=0,
                response_length=0,
                exception=f"Unexpected status code: {response.status_code}"
            )
        else:
            self.environment.events.request_success.fire(
                request_type="POST",
                name="GraphQL Mutation",
                response_time=response.elapsed.total_seconds(),  # Adjust according to the actual response time
                # calculation
                response_length=len(response.content)
            )

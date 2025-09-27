from google.cloud import pubsub_v1

def publish_message(project_id, topic_id, message):
    """Publishes a message to a Pub/Sub topic."""
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    data = message.encode('utf-8')
    future = publisher.publish(topic_path, data)
    print(f"Published message: {message}")
    return future.result()

if __name__ == '__main__':
    project_id = "your-google-cloud-project-id"
    topic_id = "your-pubsub-topic-id"
    test_message = "Gmail inbox update notification"

    publish_message(project_id, topic_id, test_message)

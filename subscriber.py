from google.cloud import pubsub_v1

def create_subscription(project_id, topic_id, subscription_id):
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = subscriber.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    subscriber.create_subscription(name=subscription_path, topic=topic_path)
    print(f"Subscription created: {subscription_path}")

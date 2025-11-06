from locust import HttpUser, task, between

class JSONPlaceholderLoadTest(HttpUser):
    # Wait between 1 and 3 seconds between tasks
    wait_time = between(1, 3)
    
    # Base URL for the test - JSONPlaceholder is a free fake API for testing
    host = "https://jsonplaceholder.typicode.com"
    
    @task(2)
    def get_posts(self):
        """GET request to fetch all posts"""
        self.client.get("/posts", name="GET All Posts")
    
    @task(2)
    def get_single_post(self):
        """GET request to fetch a single post"""
        self.client.get("/posts/1", name="GET Single Post")
    
    @task(2)
    def get_comments(self):
        """GET request to fetch comments"""
        self.client.get("/comments?postId=1", name="GET Comments")
    
    @task(1)
    def create_post(self):
        """POST request to create a new post"""
        self.client.post(
            "/posts",
            json={
                "title": "Load Test Post",
                "body": "This is a test post created by Locust",
                "userId": 1
            },
            name="POST Create Post"
        )
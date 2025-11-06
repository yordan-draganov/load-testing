from locust import HttpUser, task, between

class JSONPlaceholderLoadTest(HttpUser):
    wait_time = between(1, 3)
    
    host = "https://jsonplaceholder.typicode.com"
    
    @task(2)
    def get_posts(self):
        self.client.get("/posts", name="GET All Posts")
    
    @task(2)
    def get_single_post(self):
        self.client.get("/posts/1", name="GET Single Post")
    
    @task(2)
    def get_comments(self):
        self.client.get("/comments?postId=1", name="GET Comments")
    
    @task(1)
    def create_post(self):
        self.client.post(
            "/posts",
            json={
                "title": "Load Test Post",
                "body": "This is a test post created by Locust",
                "userId": 1
            },
            name="POST Create Post"
        )
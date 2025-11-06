from locust import HttpUser, task, between

class GoogleLoadTest(HttpUser):
    wait_time = between(1, 3)
    
    host = "https://www.google.com"
    
    @task(2)
    def get_homepage(self):
        self.client.get("/", name="GET Homepage")
    
    @task(2)
    def get_search(self):
        self.client.get("/search?q=locust+load+testing", name="GET Search")
    
    @task(2)
    def get_images(self):
        self.client.get("/imghp", name="GET Images")
    
    @task(1)
    def post_search_form(self):
        self.client.post(
            "/search",
            data={"q": "load testing"},
            name="POST Search Form"
        )
    
    @task(1)
    def post_custom(self):
        self.client.post(
            "/",
            json={"test": "data", "user": "locust"},
            name="POST Custom Data"
        )
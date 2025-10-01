from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(0.01, 0.02)  # Delay time 20 sec

    @task
    def root(self):
        self.client.get("/")
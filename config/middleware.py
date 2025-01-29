from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs that do not require login
        exempt_urls = [
            reverse('homepage'),
            reverse('login'),  # Add your login URL name here
        ]

        # Check if the requested path is in the exempt URLs
        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect(reverse('login'))  # Redirect to login page

        response = self.get_response(request)
        return response
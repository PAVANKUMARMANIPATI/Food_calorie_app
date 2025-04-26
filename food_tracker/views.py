from django.shortcuts import render
import requests
import json

def home(request):
    if request.method == 'POST':
        # Handle form submission
        query = request.POST.get('query', '')  # Get user input safely
        api_url = f'https://api.calorieninjas.com/v1/nutrition?query={query}'

        try:
            api_request = requests.get(api_url, headers={'X-Api-Key': 'UlTNPZ3OGUZOXp55rsK8AQ==dPwRRKVib3xQNVcw'})
            api = api_request.json()  # Parse JSON response
        except requests.exceptions.RequestException as e:
            api = "Oops! There was an error fetching data."
            print(e)

        return render(request, 'home.html', {'api': api})

    return render(request, 'home.html', {'query': 'Enter a valid food item'})

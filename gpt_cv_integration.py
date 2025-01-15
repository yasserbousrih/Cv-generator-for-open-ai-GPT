import requests

# Hosted Flask API URL
API_URL = "https://cv-generator-for-open-ai-gpt-1.onrender.com/generate-pdf"

def generate_cv(prompt):
    """
    Sends a user prompt to the Flask API to generate a CV PDF.
    """
    # Example data (update to parse the prompt dynamically if needed)
    data = {
        "name": "John Doe",
        "phone": "123-456-7890",
        "email": "johndoe@example.com",
        "location": "New York, NY",
        "summary": f"Summary based on the prompt: {prompt}",
        "skills": ["Python", "Flask", "JavaScript"],
        "experiences": [],
        "educations": [],
        "projects": [],
        "additional_info": []
    }

    # Send the data to the Flask API
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()

        # Parse and return the PDF URL
        return f"Your CV is ready! Download it here: {response.url}"

    except requests.exceptions.RequestException as e:
        return f"Error connecting to the CV generator: {e}"

# Example usage
print(generate_cv("Create a CV for a Python developer."))

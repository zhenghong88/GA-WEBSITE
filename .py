import os

# Template for HTML files
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - All in One Finance</title>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="style.css" rel="stylesheet">
    <!-- Font Awesome for the icon -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>
<body>
    <header class="bg-dark text-white text-center py-3 position-relative">
        <a href="index.html" class="logout-icon position-absolute"><i class="fas fa-sign-out-alt"></i></a>
        <h1>{header}</h1>
    </header>
    <div class="container mt-5">
        {content}
    </div>
    <footer class="bg-dark text-white text-center py-3">
        &copy; 2024 All in One Finance. All rights reserved.
    </footer>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
"""

# Path to the extracted files
new_extract_path = '/mnt/data/GA_WEBSITE_NEW/GA WEBSITE'

# Titles and headers for each file
titles_headers = {
    "about.html": "About Us",
    "applepay.html": "Apple Pay",
    "contact.html": "Contact Us",
    "googlepay.html": "Google Pay",
    "home.html": "Home",
    "index.html": "Welcome",
    "login.html": "Login",
    "logout.html": "Logout",
    "meremit.html": "Meremit",
    "services.html": "Services"
}

# Update all HTML files
for filename, title in titles_headers.items():
    filepath = os.path.join(new_extract_path, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            content = file.read()
        # Extract body content
        body_content_start = content.find('<body>') + 6
        body_content_end = content.find('</body>')
        body_content = content[body_content_start:body_content_end].strip()
        
        # Replace placeholders in template
        updated_content = html_template.format(title=title, header=title, content=body_content)
        
        # Write updated content to file
        with open(filepath, 'w') as file:
            file.write(updated_content)

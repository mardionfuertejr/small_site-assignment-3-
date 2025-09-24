# Mini Site with Announcements

A simple Flask web application with announcements and a "Read more / Show less" toggle functionality.

## Features

- **Home page** (`/`) - Welcome page
- **Announcements list** (`/announcements/`) - Lists all announcements
- **Announcement detail** (`/announcements/<id>/`) - Shows individual announcement with read more toggle
- **Responsive design** with modern UI
- **JavaScript toggle** for expanding/collapsing announcement content

## Project Structure

```
mini_site/
├── app.py                          # Main Flask application
├── templates/                      # HTML templates
│   ├── base.html                  # Base template with navbar
│   ├── index.html                 # Home page
│   ├── announcements.html         # Announcements list
│   └── announcement_detail.html   # Individual announcement
├── static/                        # Static files
│   ├── css/
│   │   └── style.css             # Stylesheet
│   └── js/
│       └── toggle.js             # JavaScript for read more toggle
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## Installation & Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open in browser:**
   - Home: http://localhost:5000/
   - Announcements: http://localhost:5000/announcements/
   - Individual announcements: http://localhost:5000/announcements/1/

## Routes

- `/` - Home page
- `/announcements/` - List all announcements
- `/announcements/<id>/` - View specific announcement (supports IDs 1, 2, 3)

## Technologies Used

- **Flask** - Web framework
- **Jinja2** - Template engine
- **HTML5** - Markup
- **CSS3** - Styling
- **JavaScript** - Interactive functionality

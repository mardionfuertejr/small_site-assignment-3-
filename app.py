from flask import Flask, render_template

app = Flask(__name__)

# Demo announcements
announcements = {
    1: {
        "title": "System Maintenance", 
        "content": "The system will undergo scheduled maintenance this weekend. Expect downtime on Saturday evening from 8 PM to 12 AM. All services will be unavailable during this time. Please save your work and plan accordingly."
    },
    2: {
        "title": "New Library Books", 
        "content": "The library has added new IT and Computer Science books to our collection. This includes the latest editions on Python programming, machine learning, and web development. Visit the library to check them out and expand your knowledge."
    },
    3: {
        "title": "Holiday Schedule", 
        "content": "Please note the upcoming holiday schedule for the month. The office will be closed on Christmas Day and New Year's Day. All regular services will resume on January 2nd. Have a wonderful holiday season!"
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/announcements/")
def announcements_list():
    return render_template("announcements.html", announcements=announcements)

@app.route("/announcements/<int:announcement_id>/")
def announcement_detail(announcement_id):
    announcement = announcements.get(announcement_id)
    if not announcement:
        return "Announcement not found", 404
    return render_template("announcement_detail.html", announcement=announcement, announcement_id=announcement_id)

if __name__ == "__main__":
    app.run(debug=True)

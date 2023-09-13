from flask import Flask, render_template, request
from datetime import datetime
import os


signs = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Capricorn"]

app = Flask(__name__)

# Your zodiac sign determination function goes here
def get_zodiac_sign(date_input):
    selected_date = datetime.strptime(date_input, "%Y-%m-%d")
    month = selected_date.month
    day = selected_date.day


    zodiac_ranges = [
        ((1, 20), (2, 18)),  # Aquarius
        ((2, 19), (3, 20)),  # Pisces
        ((3, 21), (4, 19)),  # Aries
        ((4, 20), (5, 20)),  # Taurus
        ((5, 21), (6, 20)),  # Gemini
        ((6, 21), (7, 22)),  # Cancer
        ((7, 23), (8, 22)),  # Leo
        ((8, 23), (9, 22)),  # Virgo
        ((9, 23), (10, 22)),  # Libra
        ((10, 23), (11, 21)),  # Scorpio
        ((11, 22), (12, 21)),  # Sagittarius
        ((12, 22), (12, 31)),  # Capricorn
        ((1, 1), (1, 19))  # Capricorn (continued from the end of the year)
    ]

    for index, (start_date, end_date) in enumerate(zodiac_ranges):
        if (month == start_date[0] and day >= start_date[1]) or (month == end_date[0] and day <= end_date[1]):
            return signs[index]

    return "Please Enter a Valid Date"

@app.route("/", methods=["GET", "POST"])
def index():
    zodiac_sign = ""
    if request.method == "POST":
        date_input = request.form["date_input"]
        zodiac_sign = get_zodiac_sign(date_input)
    return render_template("index.html", zodiac_sign=zodiac_sign)

if __name__ == "__main__":
    app.run(debug=True)


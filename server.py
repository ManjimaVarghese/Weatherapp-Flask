from flask import Flask, render_template, request
from waitress import serve
from weather import get_current_weather  # Make sure to import your weather function

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city', "Kansas City").strip() or "Kansas City"
    weather_data = get_current_weather(city)

    if not weather_data:
        return render_template('city-not-found.html')  # Handle missing data

    # Pass parsed weather data to template
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["status"],
        temp=weather_data["temp"],
        feels_like=weather_data["feels_like"]
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

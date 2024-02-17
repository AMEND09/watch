from flask import Flask, render_template, request
from datetime import datetime
from timezonefinder import TimezoneFinder
from pytz import timezone

app = Flask(__name__)

@app.route('/local_time')
def local_time():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    time_format = request.args.get('format', 'default')  # Default to 'default' if not provided

    # Assuming you have a function to get local time based on the location and format
    local_time_result = get_local_time(lat, lon, time_format)

    return str(local_time_result)

def get_local_time(lat, lon, time_format):
    tz_finder = TimezoneFinder()
    timezone_str = tz_finder.timezone_at(lng=float(lon), lat=float(lat))

    if timezone_str:
        local_time = datetime.now(timezone(timezone_str))

        if time_format == 'american':
            return local_time.strftime("%I:%M:%S %p")  # 12-hour clock with AM/PM
        else:
            return local_time.strftime("%H:%M:%S")  # 24-hour clock
    else:
        return "Timezone not found for the given location"

@app.route('/')
def index():
    return render_template('mobile_clock.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

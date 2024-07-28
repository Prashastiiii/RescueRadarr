from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import folium

app = Flask(__name__)


file_path = 'flood.csv'
data = pd.read_csv(file_path)

# Dummy coordinates for regions (in a real application, this should be accurate)
coordinates = {
    'Vanuatu': (-17.7333, 168.3273),
    'Tonga': (-21.1790, -175.1982),
    'Philippinen': (13.0000, 122.0000),
    'Salomonen': (-9.6457, 160.1562),
    'Guatemala': (15.7835, -90.2308)
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        magnitude = float(request.form['magnitude'])
        depth = float(request.form['depth'])
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        return redirect(url_for('show_map', magnitude=magnitude, depth=depth, latitude=latitude, longitude=longitude))
    
    return render_template('start.html')

@app.route('/map')
def show_map():
    magnitude = request.args.get('magnitude')
    depth = request.args.get('depth')
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))

    map_center = [latitude, longitude]
    m = folium.Map(location=map_center, zoom_start=10)

    vulnerability_colors = {
        "Very High": "red",
        "High": "orange",
        "Medium": "yellow",
        "Low": "green"
    }

    folium.Marker(
        location=map_center,
        popup=f"Location: {latitude}, {longitude}<br>Magnitude: {magnitude}<br>Depth: {depth}",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    for idx, row in data.iterrows():
        region = row['Region']
        vulnerability = row['Vulnerability Category']
        coords = coordinates.get(region, (0, 0))
        
        folium.Marker(
            location=coords,
            popup=f"Region: {region}<br>Vulnerability: {vulnerability}",
            icon=folium.Icon(color=vulnerability_colors.get(vulnerability, "blue"))
        ).add_to(m)

    map1_html = m._repr_html_()

    return render_template('map1.html', map1_html=map1_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, redirect, url_for, render_template
import pickle
import numpy as np
import folium
import requests
import logging

# Initialize the Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/home')
def home2():
    return render_template('homepage.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/aboutproject')
def aboutproject():
    return render_template('aboutproject.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    try:
        place = request.form['place']
        data1 = float(request.form['a'])
        data2 = float(request.form['b'])
        data3 = float(request.form['c'])
        arr = np.array([[data1, data2, data3]])
        
        logging.debug(f"Input array: {arr}")
        
        output = model.predict(arr)
        logging.debug(f"Model output: {output}")
        
        severity = ''
        if output < 4:
            severity = 'No'
        elif 4 <= output < 6:
            severity = 'Low'
        elif 6 <= output < 8:
            severity = 'Moderate'
        elif 8 <= output < 9:
            severity = 'High'
        else:
            severity = 'Very High'

        return redirect(url_for('show_map', place=place, prediction=output[0], severity=severity))
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return redirect(url_for('error'))

@app.route('/show_map')
def show_map():
    place = request.args.get('place')
    prediction = request.args.get('prediction')
    severity = request.args.get('severity')

    try:
        nominatim_url = f'https://nominatim.openstreetmap.org/search?q={place}&format=json&addressdetails=1&accept-language=en'
        headers = {
            'User-Agent': 'Radio-radar/1.0 (prashasti123@example.com)'
        }
        response = requests.get(nominatim_url, headers=headers)

        if response.status_code != 200:
            logging.error(f"Failed to fetch data from Nominatim API. Status code: {response.status_code}")
            return redirect(url_for('error'))

        data = response.json()

        if data:
            location = data[0]
            map_center = [float(location['lat']), float(location['lon'])]
        else:
            map_center = [0, 0]

        my_map = folium.Map(
            location=map_center,
            zoom_start=10,
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
            attr='Esri, USGS, NOAA'
        )

        popup_html = f"""
        <div style="font-size: 16px;">
            <strong>Place:</strong> {place}<br>
            <strong>Prediction:</strong> {prediction}<br>
            <strong>Severity:</strong> {severity}
        </div>
        """

        folium.Marker(
            location=map_center,
            popup=folium.Popup(popup_html, max_width=250),
            icon=folium.Icon(color='red' if severity == 'Very High' else 'orange' if severity in ['High', 'Moderate'] else 'green')
        ).add_to(my_map)

        legend_html = '''
        <div style="
            position: fixed;
            bottom: 50px;
            left: 50px;
            width: 200px;
            height: 200px;
            background-color: white;
            border:2px solid grey;
            z-index:9999;
            font-size:14px;
            padding: 10px;
            ">
            <strong>Severity Levels</strong><br>
            <i class="fa fa-map-marker fa-2x" style="color:green"></i>&nbsp;No Severity (0-4)<br>
            <i class="fa fa-map-marker fa-2x" style="color:orange"></i>&nbsp;Low Severity (4-6)<br>
            <i class="fa fa-map-marker fa-2x" style="color:orange"></i>&nbsp;Moderate Severity (6-8)<br>
            <i class="fa fa-map-marker fa-2x" style="color:red"></i>&nbsp;High Severity (8-9)<br>
            <i class="fa fa-map-marker fa-2x" style="color:red"></i>&nbsp;Very High Severity (9+)
        </div>
        '''
        my_map.get_root().html.add_child(folium.Element(legend_html))

        my_map.save('templates/map.html')

        return render_template('map.html')
    except Exception as e:
        logging.error(f"Error while generating map: {e}")
        return redirect(url_for('error'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

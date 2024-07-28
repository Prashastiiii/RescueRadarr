from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd
import folium
from folium import Marker
from folium.plugins import MarkerCluster
import io
import base64
import smtplib
from email.mime.text import MIMEText


app = Flask(__name__)


model = joblib.load('tsunami_prediction_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_tsunami(magnitude, depth, latitude, longitude):
    input_data = [[magnitude, depth, latitude, longitude]]
    scaled_features = scaler.transform(input_data)
    tsunami_prediction = model.predict_proba(scaled_features)[0][1]
    
    if tsunami_prediction > 0.9:
        tsunami_severity = "High"
    elif tsunami_prediction > 0.7:
        tsunami_severity = "Moderate"
    else:
        tsunami_severity = "Low"
        
    return tsunami_prediction, tsunami_severity

def send_email_alert(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'prashastirai9@gmail.com'
    msg['To'] = to_email
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('prashastirai9@gmail.com', 'pgiv jxrt yair zwzv')  
            server.send_message(msg)
        print("Email sent successfully")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and password.")
    except smtplib.SMTPConnectError:
        print("Failed to connect to the server. Check your SMTP server settings.")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        magnitude = float(request.form['magnitude'])
        depth = float(request.form['depth'])
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        
       
        tsunami_probability, tsunami_severity = predict_tsunami(magnitude, depth, latitude, longitude)
        
       
        if tsunami_severity == "High":
            subject = "Tsunami Alert"
            body = "Warning: High Tsunami Vulnerability Detected!"
            recipient_email = 'prashastirai123@example.com'
            send_email_alert(subject, body, recipient_email)
         
        
        
        return redirect(url_for('result', magnitude=magnitude, depth=depth, latitude=latitude, longitude=longitude, 
                                tsunami_probability=tsunami_probability, tsunami_severity=tsunami_severity))
    
    return render_template('index.html')

@app.route('/result')
def result():
    magnitude = float(request.args.get('magnitude'))
    depth = float(request.args.get('depth'))
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    tsunami_probability = float(request.args.get('tsunami_probability'))
    tsunami_severity = request.args.get('tsunami_severity')
    show_alert = tsunami_severity == "High"

    
    map_center = [latitude, longitude]
    m = folium.Map(location=map_center, zoom_start=10)

    
    severity_colors = {
        "High": "red",
        "Moderate": "orange",
        "Low": "green"
    }

   
    folium.Marker(
        location=map_center,
        popup=f"Location: {latitude}, {longitude}<br>Severity: {tsunami_severity}<br>Probability: {tsunami_probability:.2f}",
        icon=folium.Icon(color=severity_colors[tsunami_severity])
    ).add_to(m)

    
    map_html = m._repr_html_()
    
    return render_template('result.html', map_html=map_html, show_alert=show_alert, tsunami_severity=tsunami_severity)

if __name__ == '__main__':
    send_email_alert(
        subject="TSUNAMI HIGH ALERT",
        body="Tsunami Alert. There is a tsunami high alert in your area. Please take care.",
        to_email="prashastirai123@gmail.com"
    )
    app.run(host='0.0.0.0', port=5002)

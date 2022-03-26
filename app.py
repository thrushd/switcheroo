from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def index():
   template_data = {
      'output_status': 'OFF'
   }
   return render_template('index.html', **template_data)

@app.route('/switch')
def switch():
   template_data = {
      'output_status': 'ON'
   }
   return render_template('index.html', **template_data)


if __name__ == '__main__':
   app.run(debug=True)
from flask import Flask, request, render_template, send_file
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize Polly client
polly = boto3.client('polly', region_name='us-east-1')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input text from the form
        text = request.form.get('text')

        if not text:
            return "Please enter some text to convert."

        try:
            # Call Polly to synthesize speech
            response = polly.synthesize_speech(
                Text=text,
                OutputFormat='mp3',
                VoiceId='Matthew'  # Change voice if needed
            )

            # Save the audio stream to a temporary file
            output_file = 'output.mp3'
            with open(output_file, 'wb') as f:
                f.write(response['AudioStream'].read())

            # Provide the audio file for download
            return send_file(output_file, as_attachment=True)

        except (BotoCoreError, ClientError) as e:
            return f"An error occurred: {str(e)}"

    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)



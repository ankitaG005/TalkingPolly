import boto3

def synthesize_speech(text, output_file):
    # Create a Polly client
    polly = boto3.client('polly', region_name='us-east-1')

    # Convert text to speech
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',  # Format of the audio
        VoiceId='Matthew'      # Choose from available voices (e.g., 'Matthew', 'Amy')
    )

    # Save the audio stream to a file
    with open(output_file, 'wb') as file:
        file.write(response['AudioStream'].read())

    print(f"Speech saved to {output_file}")

# Example usage
text_to_convert = "Hello! Welcome to my talking app using Amazon Polly."
synthesize_speech(text_to_convert, 'speech.mp3')


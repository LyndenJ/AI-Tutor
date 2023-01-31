import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

#AWS authentication keys
aws_access_key_id = "AKIATSLHZI2CX5ZAIWWW"
aws_secret_access_key = "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"
aws_session_token = "" #Not needed for IAM users
region_name = "ca-central-1"
botocore_session = ""
profile_name = "LyndenJones"


def textToSpeech(response):

    originalResponse = response

    session = Session(aws_access_key_id, aws_secret_access_key, None, region_name, None, "LyndenJones")

    polly = session.client("polly")

    try:
        response = polly.synthesize_speech(Text=response, OutputFormat="mp3", VoiceId="Joanna")
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)

    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")

            try:
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("Could not stream audio")
        sys.exit(-1)

    if sys.platform == "win32":
     os.startfile(output)

    else:
     # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
     opener = "open" if sys.platform == "darwin" else "xdg-open"
     subprocess.call([opener, output])
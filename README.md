![Python CI](https://github.com/apidaze/sdk-python/workflows/Python%20CI/badge.svg)

# Apidaze Python SDK

The Apidaze Python SDK contains the Python client of Apidaze REST API as well as an XML script builder.
The SDK allows you to leverage all Apidaze platform features such as making calls, sending text messages, serving IVR systems and many others in your Python based application.
The SDK also includes sample applications that demonstrate how to use the SDK interfaces.
See [Apidaze REST API specification](https://apidocs.voipinnovations.com) which includes XML Scripting Reference as well.

# Requirements
- Python 3.4+
- requests
- lxml

# Installation

To install the SDK just type

`make`

After that activate the virtual environment by typing

`source venv/bin/activate`

Now you're ready to install all python dependencies

`pip install -r requirements.txt`

You're now ready to use the SDK

# Quickstart

## SDK client

### Initiate the SDK Client

```python
from apidaze import Client

apidaze = Client(api_key=API_KEY, api_secret=API_SECRET)
```

Where `API_KEY` and `API_SECRET` should be replaced with the real key and secret from your Apidaze application.

### Make a call

```python
apidaze.calls.place(
        caller_id='9876543',
        origin='123456',
        destination='123456',
        CallType.number)
```

Where `caller_id` is the phone number to be presented as caller id, `origin` the phone number or SIP account to ring first, and `destination` is passed as a parameter to your External Script URL.

### Send a text message

```python
apidaze.messages.send(
   origin='14125423968',
   destination='14125423968',
   body='Hello World from Python SDK'
)
```

Where `origin` is the number to send the text from. Must be an active number on your account.
`destination` is the number you want to send the text to.
`body` is the message to send.

### Download recordings

```python
response = apidaze.recordings.get(filename='my_recording.wav')
data = response['body']
file = open(filename, 'wb')
file.write(data)
file.close()
```

In this example, we will download the recording named `my_recording.wav`.

## Script builder

The script builder is used to build XML instructions described in [XML Scripting Reference](https://apidocs.voipinnovations.com).
To build an instruction which echo back received audio to the caller with some delay use the following code.

```python
from apidaze.script import Builder, Answer, Echo, Speak

xmlbuilder = Builder()
answer = Answer()
speak = Speak(text='Thank you for trying our demo. Have an wonderful day!')
echo = Echo(500)

xmlbuilder.add(answer).add(speak).add(echo)
xmlbuilder.printXML()
```

The code above will produce the following XML

```xml
<?xml version='1.0' encoding='utf8'?>
<document>
  <work>
    <answer/>
    <speak lang="en-US">Thank you for trying our demo. Have an wonderful day!</speak>
    <echo>500</echo>
  </work>
</document>
```

## More examples

For more examples please see our [example repository](https://github.com/apidaze/sdk-python/tree/master/examples)
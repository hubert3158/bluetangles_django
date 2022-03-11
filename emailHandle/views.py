from django.shortcuts import render
from flask import Flask, request
# Create your views here.from flask import Flask, request
import json as simplejson
app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def sendgrid_parser():
  # Consume the entire email
  envelope = simplejson.loads(request.form.get('envelope'))

  # Get some header information
  to_address = envelope['to'][0]
  from_address = envelope['from']

  # Now, onto the body
  text = request.form.get('text')
  html = request.form.get('html')
  subject = request.form.get('subject')

  print(html)

  # Process the attachements, if any
  num_attachments = int(request.form.get('attachments', 0))
  attachments = []
  if num_attachments > 0:
    for num in range(1, (num_attachments + 1)):
      attachment = request.files.get(('attachment%d' % num))
      attachments.append(attachment.read())
      # attachment will have all the parameters expected in a Flask file upload

  return "OK"

if __name__ == '__main__':
    app.run(debug=True)



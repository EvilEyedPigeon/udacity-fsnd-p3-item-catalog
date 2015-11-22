import json

from catalog import app

# load client ids from config files
app.config.google_client_id = json.loads(open('client_secret_google.json', 'r').read())['web']['client_id']
print("google_client_id: " + app.config.google_client_id)

# Start the app
app.secret_key = 'super_secret_key'
app.debug = True
app.run(host = '0.0.0.0', port = 5000)

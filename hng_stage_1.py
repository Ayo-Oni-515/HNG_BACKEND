from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# url = {'backend' : 'https://github.com/Ayo-Oni-515/HNG_BACKEND/blob/main/hng_stage_1.py'}

@app.route('/')
def home():
    return "My Endpoint"

@app.route("/myendpoint", methods=['GET'])
def get_info():
    first_argument = str(request.args.get('slack_name'))
    second_argument = str(request.args.get('track'))
    day = datetime.datetime.utcnow().strftime('%A')
    time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')


    information = {
        "slack_name": first_argument,
        "current_day": day,
        "utc_time": time,
        "track": second_argument,
        "github_file_url": "https://github.com/Ayo-Oni-515/HNG_BACKEND/blob/main/hng_stage_1.py",
        "github_repo_url": "https://github.com/Ayo-Oni-515/HNG_BACKEND.git",
        "status_code": 200
    }

    return jsonify(information)

if __name__ == '__main__':
    app.run(debug=True)

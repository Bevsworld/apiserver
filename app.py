from flask import Flask, jsonify
import psycopg2
import psycopg2.extras
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

# Database connection parameters
DATABASE_URL = "postgresql://retool:jr1cAFW3ZIwH@ep-tight-limit-a6uyk8mk.us-west-2.retooldb.com/retool?sslmode=require"

@app.route('/speeches', methods=['GET'])
def get_speeches():
    # Existing code
    pass

@app.route('/tweets', methods=['GET'])
def get_tweets():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT username, profilepicture, createdat, text FROM tweets")
        tweets = cur.fetchall()
        result = [
            {
                'username': row['username'],
                'profilepicture': row['profilepicture'],
                'createdat': row['createdat'],
                'text': row['text']
            } for row in tweets
        ]
        cur.close()
        conn.close()
        return jsonify(result)
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, Port=3000)

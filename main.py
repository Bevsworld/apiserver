from flask import Flask, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)

# Database connection parameters
DATABASE_URL = "postgresql://retool:jr1cAFW3ZIwH@ep-tight-limit-a6uyk8mk.us-west-2.retooldb.com/retool?sslmode=require"

# Route to fetch all speeches
@app.route('/speeches', methods=['GET'])
def get_speeches():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # Use DictCursor to access columns by names
        cur.execute("SELECT speaker, speech, title, description, highlight1, highlight2, highlight3, highlight4, highlight5 FROM speeches")
        speeches = cur.fetchall()
        result = [
            {
                'speaker': row['speaker'],
                'speech': row['speech'],
                'title': row['title'],
                'description': row['description'],
                'highlight1': row['highlight1'],
                'highlight2': row['highlight2'],
                'highlight3': row['highlight3'],
                'highlight4': row['highlight4'],
                'highlight5': row['highlight5']
            } for row in speeches
        ]
        cur.close()
        conn.close()
        return jsonify(result)
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
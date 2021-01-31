from flask import (
    Flask,
    render_template,
    jsonify
)

import codecs

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application

@app.route('/set_value/<int:task_id>', methods=['GET'])
def get_task(task_id):
    print("task_id", task_id)
    return jsonify({'task': task_id})

if __name__ == '__main__':
    app.run(debug=True)

# import socket
# from flask import Flask, request, jsonify

# from logger import logging
# from database import get_db_connection, create_database
# from retrieval import qa_chain


# app = Flask(__name__)


# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     user_query = data.get("query")
#     if not user_query:
#         return jsonify({"error": "Query is required"}), 400
    
#     # Store user query
#     conn = get_db_connection()
#     create_database()
#     logging.info("Database Created.")
#     cursor = conn.cursor()
#     response = qa_chain.invoke({"input": user_query})
#     answer = response["answer"]
    
#     cursor.execute("INSERT INTO chat_history (role, content) VALUES (%s, %s)", ("user", user_query))
#     cursor.execute("INSERT INTO chat_history (role, content) VALUES (%s, %s)", ("system", answer))
#     conn.commit()
#     conn.close()
    
#     return jsonify({"answer": answer})


# @app.route("/history", methods=["GET"])
# def history():
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM chat_history ORDER BY timestamp DESC LIMIT 20")
#     history = cursor.fetchall()
#     conn.close()
#     return jsonify(history)



# if __name__ == "__main__":
#     host = socket.gethostbyname(socket.gethostname())
#     port = 5000
#     print(f"Flask app running at: http://{host}:{port}")
#     app.run(port=port, debug=True, use_reloader=False)



import socket
from flask import Flask, request, jsonify

from logger import logging
from database import get_db_connection, create_database
from retrieval import qa_chain

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_query = data.get("query")
    if not user_query:
        logging.warning("Received request without query parameter.")
        return jsonify({"error": "Query is required"}), 400
    
    logging.info(f"Received user query: {user_query}")
    
    # Store user query
    conn = get_db_connection()
    create_database()
    logging.info("Database Created.")
    cursor = conn.cursor()
    
    response = qa_chain.invoke({"input": user_query})
    answer = response["answer"]
    logging.info(f"Generated response: {answer}")
    
    try:
        cursor.execute("INSERT INTO chat_history (role, content) VALUES (%s, %s)", ("user", user_query))
        cursor.execute("INSERT INTO chat_history (role, content) VALUES (%s, %s)", ("system", answer))
        conn.commit()
        logging.info("Chat history updated successfully.")
    except Exception as e:
        logging.error(f"Error inserting chat history: {e}")
    finally:
        conn.close()
    
    return jsonify({"answer": answer})


@app.route("/history", methods=["GET"])
def history():
    logging.info("Fetching chat history.")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM chat_history ORDER BY timestamp DESC LIMIT 20")
        history = cursor.fetchall()
        logging.info("Chat history retrieved successfully.")
    except Exception as e:
        logging.error(f"Error fetching chat history: {e}")
        history = []
    finally:
        conn.close()
    
    return jsonify(history)



if __name__ == "__main__":
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
    logging.info(f"Flask app starting at: http://{host}:{port}")
    print(f"Flask app running at: http://{host}:{port}")
    app.run(port=port, debug=True, use_reloader=False)

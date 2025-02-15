import streamlit as st
from logger import logging
from database import get_db_connection, create_database
from retrieval import qa_chain

# Set up the Streamlit app
st.set_page_config(page_title="Chat Application", layout="wide")
st.title("Chat Application")

# Create the database on startup (if needed)
create_database()
logging.info("Database created or already exists.")

def process_chat(query):
    """
    Process the chat query by invoking the QA chain and storing the conversation in the database.
    """
    if not query:
        st.warning("Please enter a query.")
        return None

    logging.info(f"Received user query: {query}")
    response = qa_chain.invoke({"input": query})
    answer = response.get("answer")
    logging.info(f"Generated response: {answer}")

    # Store chat history in the database
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO chat_history (role, content) VALUES (%s, %s)", 
            ("user", query)
        )
        cursor.execute(
            "INSERT INTO chat_history (role, content) VALUES (%s, %s)", 
            ("system", answer)
        )
        conn.commit()
        logging.info("Chat history updated successfully.")
    except Exception as e:
        logging.error(f"Error inserting chat history: {e}")
    finally:
        conn.close()

    return answer

# Chat input form
with st.form("chat_form", clear_on_submit=True):
    user_query = st.text_input("Enter your query:")
    submit_button = st.form_submit_button("Send")

if submit_button and user_query:
    answer = process_chat(user_query)
    if answer:
        st.markdown("### Chat Response")
        st.write(f"**Query:** {user_query}")
        st.write(f"**Answer:** {answer}")

# Section to display chat history
if st.button("Show Chat History"):
    conn = get_db_connection()
    # Using a cursor that returns dictionaries (adjust based on your DB connector)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM chat_history ORDER BY timestamp DESC LIMIT 20")
        history = cursor.fetchall()
        logging.info("Chat history retrieved successfully.")
        if history:
            st.markdown("### Chat History (Most Recent 20 Entries)")
            for entry in history:
                st.write(f"**{entry['timestamp']} - {entry['role'].capitalize()}:** {entry['content']}")
        else:
            st.info("No chat history available.")
    except Exception as e:
        logging.error(f"Error fetching chat history: {e}")
        st.error("Error fetching chat history.")
    finally:
        conn.close()

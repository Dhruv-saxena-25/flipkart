from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from flipkart.retrieval_generation import generation, get_session_history
from flipkart.data_ingestion import data_ingestion
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_groq import ChatGroq


os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-70b-versatile", temperature=0.5)

chat_history= []
store = {}
def get_session_history(session_id: str)-> BaseChatMessageHistory:
  if session_id not in store:
    store[session_id]= ChatMessageHistory()
  return store[session_id]




vstore = data_ingestion("done")

chain = generation(vstore)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/get", methods = ["POST", "GET"])
def chat():
   
   if request.method == "POST":
      msg = request.form["msg"]
      input = msg

      result = chain.invoke(
         {"input": input},
    config={
        "configurable": {"session_id": "dhruv"}
    },
)["answer"]

      return str(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug= True)

 
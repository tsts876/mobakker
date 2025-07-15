from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "أنت مساعد صحي ذكي يتحدث باللهجة السعودية."},
                    {"role": "user", "content": user_input},
                ]
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"حدث خطأ أثناء الاتصال بـ GPT: {e}"
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)

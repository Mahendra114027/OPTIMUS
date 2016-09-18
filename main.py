# import speech_recognition as sr
#
# r = sr.Recognizer()
# m = sr.Microphone()
#
# try:
#     #set threhold level
#     with m as source: r.adjust_for_ambient_noise(source)
#     print("Set minimum energy threshold to {}".format(r.energy_threshold))
#
#     # obtain audio from the microphone
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)
# except:
#     pass
#
# print(r.recognize_google(audio))

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        x = request.values.get('record')
        return render_template("temp.html", lst=x)
    elif request.method == 'GET':
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

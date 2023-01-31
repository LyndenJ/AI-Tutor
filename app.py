from flask import Flask,render_template,request
from chat import chatGPT
from text2speech import textToSpeech

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods = ['POST', "GET"])
def result():
    output = request.form.to_dict()

    name = None
    practice = None
    question = None
    solution = None

    try:
        name = chatGPT(output["name"])
        #name = "This that and the other thing. Lecture section"
        textToSpeech(name)
    except KeyError:
        pass

    try:
        practice = chatGPT("Generate a numerical question and full solution for a " + output["practice"] + "course.")
        #practice = "Question: This that and the other thing. Solution: All of it"
        textToSpeech(practice)
        

        wordList= practice.split()

        question = ""
        solution = ""
        seenSolution = False
        for word in wordList:
            if word == 'Solution:':
                seenSolution = True
            if not seenSolution:
                word = word+" "
                question += word
            if seenSolution:
                word = word+" "
                solution += word
        

    except KeyError:
        pass
    except AttributeError:
        pass
    


    return render_template("index.html", name=name, question=question, solution=solution, practice=practice)
if __name__ =='__main__':
    app.run(debug= True, port=5001)
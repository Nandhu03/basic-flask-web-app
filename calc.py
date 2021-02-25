from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('landing1.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
        result = var_1 / var_2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)
@app.route('/Welcome',methods=['POST'])
def userDetail():
    fname=request.form.get("fname",type=str)
    lname=request.form.get("lname",type=str)
    return render_template('name.html',name=fname+lname)
@app.route('/grading',methods=['POST'])
def grading():
    student = request.form.get("student",type=str)
    marks = request.form.get("marks",type=int)
    if marks>=30:
        return render_template('score.html',score="passed the exam",name=student)
    else:
        return render_template('score.html',score="failed the exam",name=student)



if __name__ == '__main__':
    app.run(debug=True)

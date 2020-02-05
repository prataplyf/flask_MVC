from mvc import module as ml
from mvc import app

@app.route('/')
@app.route('/signin', methods=['POST','GET'])
def signin():
    if ml.request.method == 'POST':
        mail = ml.request.form.get('mail')
        enter_pass = ml.request.form.get('password')
        # print(mail)
        for x in ml.database.user.find({"Email":mail},{"Name":1, "Email":1, "Password":1, "_id":1}):
            pwd = x['Password']
            mail = x['Email']  # override mail
            name = x['Name']
            if pwd == enter_pass:
                msg = "Login Successful!"
                return ml.jsonify({'name': name, 'email': mail, 'message': msg})
            else:
                msg = 'Wrong email ID or Password!'
                return ml.render_template('account/signin.html', title='Sign In', message=msg)
    return ml.render_template('account/signin.html', title='Sign In')

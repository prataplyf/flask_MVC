from mvc import module as ml
from mvc import app

global password
password = ''
global pd
pd = ''

# @app.route('/register',methods = ['POST', 'GET'])
@app.route("/signup", methods=['POST','GET'])
def signup():
    if ml.request.method == 'POST':
        email = ml.request.form.get('email')
        name = ml.request.form.get('name')
        count = 0
        if email in [temp['Email'] for temp in ml.database.user.find({}, {"Email":1} )]:
            return ml.jsonify({"status":"Already used","message":"This Email ID Already Registered with Us!"})
        else:
            def check():
                global pd, password
                characters = ml.string.ascii_letters  + ml.string.digits
                password =  "".join(ml.choice(characters) for x in range(ml.randint(8,8))) # fix password length i.e: 8 digit
                if ml.re.search("[0-9][a-z][A-Z]", password):
                    pd = password  # generate random password having (0-9, a-z, A-Z) characters only
                    ml.database.user.insert_one({"Name": name, "Email":email, "Password":pd })
                else:
                    return check()
            check()
            msg = 'Sign Up! Success'
            return ml.render_template('account/signup.html', title='Sign Up', message = msg)
    return ml.render_template('account/signup.html', title='Sign Up')

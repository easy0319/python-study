from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

#regist book
@app.route('/register')
def register():
        return render_template('register.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
        #connect mongoDB
        mongoURL = 'mongodb+srv://easy:easy0319@mongodb-owlwh.mongodb.net/test?retryWrites=true'
        client = pymongo.MongoClient(mongoURL)
        db = pymongo.database.Database(client, 'mongoDB')
        book = pymongo.collection.Collection(db, 'Books')

        if request.method == 'POST':
                #insert data to mongoDB
                data = request.form.to_dict(flat='true')
                book.insert_one(data)

                #find data from mongoDB
                results = book.find()
                #client.close()

                return render_template('book.html', results = results)
        else:
                #find data from mongoDB
                results = book.find()
                #client.close()

                return render_template('book.html', results = results)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)


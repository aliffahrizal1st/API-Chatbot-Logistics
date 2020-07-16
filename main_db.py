from flask import Flask, request, jsonify
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="chatbot"
)

mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/kritik_saran', methods=['POST'])
def tambah_kritik_saran():
    data = request.get_json()

    sql = "INSERT INTO kritik_saran (kritik, saran) VALUES (%s, %s)"
    val = (data["kritik"], data["saran"])
    mycursor.execute(sql, val)
    mydb.commit()

    return jsonify({
        "chats": [
            {
                "text": "Data berhasil disimpan",
                "type": "text"
            }
        ]
    })


@app.route('/kritik_saran', methods=['GET'])
def list_kritik_saran():
    mycursor.execute("SELECT * FROM kritik_saran")
    myresult = mycursor.fetchall()

    kritik = []
    saran = []
    for x in myresult:
        kritik.append(x[0])
        saran.append(x[1])

    return jsonify({
        "chats": [
            {
                "text": "Kritik : " + ", ".join(kritik),
                "type": "text"
            },
            {
                "text": "Saran : " + ", ".join(saran),
                "type": "text"
            }
        ]
    })


if __name__ == '__main__':
    app.run(port=5000)

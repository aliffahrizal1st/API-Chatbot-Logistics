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

@app.route('/kritiksaran', methods=['POST'])
def input_kritik_saran():
    data = request.get_json()

    sql = "INSERT INTO kritiksaran (kritik, saran) VALUES (%s, %s)"
    var = (data["kritik"], data["saran"])
    mycursor.execute(sql, var)
    mydb.commit()

    return jsonify({
        "chats": [
            {
                "text": "Terima kasih atas masukkannya!! \nKritik & saran kamu akan kami proses agar bisa jadi lebih baik kedepannya",
                "type": "text"
            }
        ]
    })

@app.route('/komplain', methods=['POST'])
def input_komplain():
    data = request.get_json()

    sql = "INSERT INTO komplain(noHP, komplain) VALUES (%s,%s)"
    var = (data["noHP"], data["komplain"])
    mycursor.execute(sql, var)
    mydb.commit()

    return jsonify({
        "chats": [
            {
                "text": "Mohon ditunggu sebentar ya, komplain kamu akan kami proses \nNanti akan ada Customer Service dari kami yang menghubungi kamu",
                "type": "text"
            }
        ]
    })


app.route('/informasipaket', methods=['POST'])
def informasipaket():
    data = request.get_json()
    y = data["kodePaket"]
    print(y)
    print(y)
    print(y)
    x = request.args.get('kodePaket')
    print(x)
    print(x)
    print(x)
    var = (request.args.get('kodePaket'),)
    sql = "SELECT * FROM informasipaket WHERE kodePaket = '%s'"
    mycursor.execute(sql, var)
    myresult = mycursor.fetchall()

    kode = []
    berat = []
    jumlah = []
    jenis = []
    biaya = []
    for x in myresult:
        kode.append(x[0])
        berat.append(x[1])
        jumlah.append(x[2])
        jenis.append(x[3])
        biaya.append(x[4])

    return jsonify({
        "chats": [
            {
                "text": 
                "Kode Paket         : ".join(kode)+
                "\nBerat Paket      : ".join(berat)+
                "\nJumlah Paket     : ".join(jumlah)+
                "\nJenis Paket      : ".join(jenis)+
                "\nBiaya Pengiriman : Rp.".join(biaya),
                "type": "text"
            }
        ]
    })


if __name__ == '__main__':
    app.run(port=5000)

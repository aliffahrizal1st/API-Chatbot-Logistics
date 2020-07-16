from flask import Flask, request, jsonify

app = Flask(__name__)
arr_kritiksaran = []
arr_komplain = []
arr_informasiPaket = [
    [1234567890,'1','1','Spare Part Motor',8000],
    [1122334450,'3','1','Beras',4500]]
arr_biayakirim = [
    [11111,22222,1,3000],
    [11111,22222,3,5000],
    [11111,33333,1,8000],
    [11111,33333,3,10000],
    [22222,11111,1,4000],
    [22222,11111,3,8000],
    [22222,33333,1,3500],
    [22222,33333,3,6000],
    [33333,11111,1,7000],
    [33333,11111,3,13000],
    [33333,22222,1,5000],
    [33333,22222,3,4500]]
arr_tracking = [
    [1234567890,'B','Gate Away'],
    [1122334450,'C','Gudang Pusat']
    ]


@app.route('/kritiksaran', methods=['POST'])
def input_kritik_saran():
    data = request.get_json()
    arr_kritiksaran.append([data["kritik"], data["saran"]])

    return jsonify({
        "chats": [
            {
                "text": "Terima kasih atas masukkannya!! \nKritik & saran kamu akan kami proses agar bisa jadi lebih baik kedepannya",
                "type": "text"
            }
        ]
    })
    print(arr_kritiksaran)

@app.route('/komplain', methods=['POST'])
def input_komplain():
    data = request.get_json()
    arr_komplain.append([data["noHP"], data["komplain"]])

    return jsonify({
        "chats": [
            {
                "text": "Mohon ditunggu sebentar ya, komplain kamu akan kami proses \nNanti akan ada Customer Service dari kami yang menghubungi kamu",
                "type": "text"
            }
        ]
    })
    print(arr_komplain)


@app.route('/informasipaket', methods=['POST'])
def informasipaket():
    data = request.get_json()
    kode_input = data["kodePaket"]
    kodePaket = []
    berat = []
    jumlah = []
    jenis = []
    biaya = []
    for x in arr_informasiPaket :
        for y in x :
            if(y==kode_input):
                kodePaket.append(x[0])
                berat.append(x[1])
                jumlah.append(x[2])
                jenis.append(x[3])
                biaya.append(x[4])

    return jsonify({
        "chats": [
            {
                "text": 
                "Kode Paket         : ".join(kodePaket)+
                "\nBerat Paket      : ".join(berat)+
                "\nJumlah Paket     : ".join(jumlah)+
                "\nJenis Paket      : ".join(jenis)+
                "\nBiaya Pengiriman : Rp.".join(biaya),
                "type": "text"
            }
        ]
    })

@app.route('/biayakirim', methods=['POST'])
def biayakirim():
    data = request.get_json()
    kode_pos_pengirim = data["kodePosPengirim"]
    kode_pos_penerima = data["kodePosPenerima"]
    berat = data["beratPaket"]
    biaya = []
    for x in arr_biayakirim :
        if(x[0]==kode_pos_pengirim):
            if(x[1]==kode_pos_penerima):
                if(x[2]==berat):
                    biaya.append(x[3])

    return jsonify({
        "chats": [
            {
                "text": 
                "Biaya kirimnya adalah Rp.".join(biaya),
                "type": "text"
            }
        ]
    })

if __name__ == '__main__':
    app.run(port=5000)

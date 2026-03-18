from pymongo import MongoClient

uri = "mongodb+srv://sabila:sabila123@cluster0.sqro10q.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri)

    db = client["kampus"]
    collection = db["mahasiswa"]

    data = {
        "nama": "Sabila",
        "jurusan": "Informatika",
        "semester": 4
    }

    collection.insert_one(data)

    print("Data berhasil ditambahkan!")
    print(client.list_database_names())

except Exception as e:
    print("Koneksi gagal:", e)
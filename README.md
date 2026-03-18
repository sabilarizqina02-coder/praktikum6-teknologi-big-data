<<<<<<< HEAD

---

# 📊 Praktikum Big Data

## Batch Analytics + Visualization Layer (Big Data Dashboard)

| Keterangan         | Informasi            |
| ------------------ | -------------------- |
| **Nama**           | Sabila Rizqina Majid |
| **NIM**            | 230104040058         |
| **Mata Kuliah**    | Teknologi Big Data   |
| **Dosen Pengampu** | Bapak Muhayat, M.IT  |

---

# 📌 Deskripsi Project

Project ini merupakan implementasi **Batch Data Analytics dan Visualization Layer** dalam arsitektur **Big Data Pipeline**.

Dataset e-commerce diproses menggunakan **Apache Spark (PySpark)** untuk menghasilkan dataset analitik yang kemudian digunakan sebagai sumber data untuk membuat dashboard menggunakan **Power BI**.

Praktikum ini bertujuan untuk memahami bagaimana proses **pengolahan data hingga visualisasi data** dilakukan dalam sistem Big Data.

---

# 🏗 Big Data Pipeline

Pipeline data pada project ini adalah sebagai berikut:

```
Raw Dataset → Spark Processing → Analytics Layer → Serving Dataset → Power BI Dashboard
```

Penjelasan pipeline:

1. **Data Source**
   Dataset e-commerce dalam format CSV digunakan sebagai sumber data mentah.

2. **Processing Layer**
   Data diproses menggunakan **Apache Spark (PySpark)** untuk melakukan:

   * data cleaning
   * data transformation
   * aggregation

3. **Analytics Layer**
   Data dianalisis untuk menghasilkan metrik seperti total revenue dan kategori produk.

4. **Serving Layer**
   Dataset hasil analisis disimpan pada folder:

```
data/serving
```

5. **Visualization Layer**
   Dataset digunakan untuk membuat dashboard menggunakan **Power BI Desktop**.

---

# 📂 Struktur Project

```
big-data-dashboard
│
├── data
│   └── serving
│
├── scripts
│   └── analytics_layer.py
│
├── dashboard
│   └── bigdata_dashboard.pbix
│
└── README.md
```

Penjelasan folder:

* **data/** → menyimpan dataset project
* **scripts/** → script PySpark untuk analisis data
* **dashboard/** → file dashboard Power BI
* **README.md** → dokumentasi project

---

# ⚙️ Cara Menjalankan Program

Untuk menjalankan proses analisis data gunakan perintah berikut:

```
python scripts/analytics_layer.py
```

Script ini akan memproses dataset menggunakan **PySpark** dan menghasilkan dataset analitik yang disimpan pada folder **data/serving**.

---

# 📊 Dashboard

Dataset yang telah diproses kemudian digunakan untuk membuat dashboard analitik menggunakan **Power BI**.

File dashboard disimpan dalam format:

```
bigdata_dashboard.pbix
```

Dashboard ini menampilkan informasi seperti:

* Total Revenue
* Top Product
* Revenue Category

---

# 🛠 Teknologi yang Digunakan

Project ini menggunakan beberapa teknologi berikut:

* **Apache Spark (PySpark)**
* **Python**
* **Power BI Desktop**
* **GitHub**

---
=======
# bigdata-dashboard-praktikum3
Praktikum 3 Teknologi Big Data
>>>>>>> fda881b4bceb7bc6a41aa1efe43f22da9271d261

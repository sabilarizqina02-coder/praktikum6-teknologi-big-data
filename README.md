
````
Nama            : Sabila Rizqina Majid  
NIM             : 230104040058  
Mata Kuliah     : Teknologi Big Data  
Dosen Pengampu  : Bapak Muhayat, M.IT  

---

# LAPORAN PRAKTIKUM 6  
Real-Time Analytics dan Visualisasi Data Skala Besar

---

## Deskripsi
Project ini merupakan implementasi sistem analitik data secara real-time menggunakan teknologi Big Data. Sistem dibangun untuk memonitor data transportasi yang berjalan secara streaming dan menampilkannya dalam bentuk dashboard interaktif.

Pada praktikum ini dilakukan pengembangan dari sistem sebelumnya dengan menambahkan teknik window aggregation agar data dalam jumlah besar dapat disederhanakan dan tetap dapat divisualisasikan dengan cepat dan efisien.

---

## Teknologi yang Digunakan
- Python  
- Apache Spark (PySpark)  
- Parquet Data Lake  
- Streamlit  

---

## Arsitektur Sistem
Trip Generator → Spark Streaming → Parquet Data Lake → Dashboard Streamlit

---

## Cara Menjalankan

### 1. Jalankan Spark Streaming
```bash
spark-submit scripts/transportation/streaming_trip_layer.py
````

### 2. Jalankan Trip Generator

```bash
python scripts/transportation/trip_generator.py
```

### 3. Jalankan Dashboard

```bash
streamlit run dashboard/dashboard_transportation.py
```

---

## Fitur Utama

Sistem mampu menampilkan:

* Total Trips
* Total Fare
* Real-Time Traffic (Window Aggregation)
* Distribusi Kendaraan
* Mobility Trend
* Deteksi Anomali

---

## Kesimpulan

Sistem berhasil memproses data secara real-time dan menampilkan visualisasi yang responsif. Penggunaan window aggregation membantu menyederhanakan data sehingga dashboard tetap ringan dan tidak mengalami overload.

```


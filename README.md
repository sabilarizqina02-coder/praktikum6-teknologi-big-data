
# Praktikum 4 – Teknologi Big Data

## Streaming Processing dan Real-Time Dashboard

---

## Identitas

Nama            : Sabila Rizqina Majid  
NIM             : 230104040058  
Mata Kuliah     : Teknologi Big Data  
Program Studi   : Teknologi Informasi  

---

## Deskripsi Praktikum

Praktikum ini bertujuan untuk mengimplementasikan sistem pemrosesan data secara streaming menggunakan Apache Spark serta menampilkan hasil analisis secara real-time melalui dashboard berbasis Streamlit.

Sistem yang dibangun mensimulasikan aliran data transaksi e-commerce yang diproses secara kontinu. Data tersebut kemudian dianalisis untuk menghasilkan informasi penting yang ditampilkan dalam bentuk visualisasi interaktif.

---

## Tujuan

1. Memahami konsep dasar streaming data dalam Big Data  
2. Mengimplementasikan Apache Spark Structured Streaming  
3. Mengolah data secara real-time  
4. Membangun dashboard interaktif menggunakan Streamlit  
5. Mengintegrasikan pipeline data end-to-end  

---

## Teknologi yang Digunakan

- Apache Spark  
- Python  
- Streamlit  
- Parquet File Format  

---

## Struktur Project

```

bigdata-praktikum4/
│
├── scripts/
│   ├── streaming_layer.py
│   ├── transaction_generator.py
│   ├── analytics_layer.py
│   └── visualization_layer.py
│
├── dashboard/
│   └── dashboard_streamlit.py
│
├── data/
│   ├── raw/
│   ├── clean/
│   └── curated/
│
├── reports/
│   └── category_revenue.png
│
├── .gitignore
└── README.md

```

---

## Cara Menjalankan Program

Program dijalankan menggunakan tiga terminal secara bersamaan:

### Terminal 1 – Spark Streaming
```

spark-submit scripts/streaming_layer.py

```

### Terminal 2 – Transaction Generator
```

python3 scripts/transaction_generator.py

```

### Terminal 3 – Dashboard
```

python -m streamlit run dashboard/dashboard_streamlit.py

```

---

## Alur Sistem

1. Transaction generator menghasilkan data transaksi secara kontinu  
2. Spark Streaming membaca dan memproses data tersebut  
3. Data disimpan dalam format Parquet  
4. Dashboard membaca hasil data dan menampilkan visualisasi secara real-time  

---

## Hasil

Dashboard menampilkan beberapa informasi utama, antara lain:

- Total Revenue  
- Top Products  
- Category Revenue  
- Average Transaction  

---

## Kesimpulan

Implementasi streaming processing menggunakan Apache Spark memungkinkan pemrosesan data secara real-time dengan efisien. Integrasi dengan Streamlit memberikan visualisasi yang interaktif sehingga memudahkan dalam memahami data yang dihasilkan.

---

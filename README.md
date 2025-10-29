# Exploratory-Data-Analyts


## 📋 Proje Açıklaması
Bu proje, verilen bir veri kümesi üzerinde **keşifsel veri analizi (Exploratory Data Analysis - EDA)** gerçekleştirmek için hazırlanmıştır.  
Amaç, veri setinin genel yapısını anlamak, eksik değerleri incelemek, temel istatistikleri hesaplamak ve değişkenler arasındaki ilişkileri görselleştirmektir.

---

## 🧩 İçerik
Kod aşağıdaki adımları uygular:

1. **Veri Yükleme:**  
   CSV formatındaki veri `pandas` kullanılarak yüklenir.

2. **Veri İncelemesi:**  
   Veri şekli, sütun adları, veri türleri ve ilk birkaç satır yazdırılır.

3. **İstatistiksel Özet:**  
   Ortalama, medyan, varyans gibi özet istatistikler hesaplanır (`df.describe()`).

4. **Eksik Değer Analizi:**  
   Eksik değerler tespit edilir ve sayısal sütunlarda ortalama ile doldurulur.

5. **Dağılım Grafikleri:**  
   Sayısal sütunlar için histogram ve KDE grafikleri çizilir (`seaborn.histplot`).

6. **Korelasyon Analizi:**  
   Değişkenler arasındaki ilişkiler bir ısı haritası (heatmap) ile görselleştirilir.

7. **Çift Değişkenli İlişkiler:**  
   Tüm sayısal sütunlar arasındaki ikili ilişkiler `seaborn.pairplot()` ile gösterilir.

---

## 🧰 Kullanılan Kütüphaneler
```bash
pip install pandas numpy matplotlib seaborn
```

- **pandas** → Veri işleme  
- **numpy** → Sayısal hesaplamalar  
- **matplotlib** → Görselleştirme  
- **seaborn** → Gelişmiş istatistiksel grafikler  

---

## 🚀 Kullanım
1. `Veri.csv` adlı dosyanızı proje dizinine yerleştirin.  
   (İsteğe göre kendi dosya yolunuzu belirleyebilirsiniz.)
2. Python dosyasını çalıştırın:
   ```bash
   python veri_analizi.py
   ```
3. Grafikler ve istatistiksel çıktılar terminalde ve pop-up pencerelerde görüntülenecektir.

---

## 📊 Örnek Çıktılar
- Veri şekli: `(150, 5)`
- Eksik değer sayısı tablosu
- Her sayısal sütun için histogram
- Korelasyon matrisi (ısı haritası)
- Tüm değişkenler arası dağılım grafikleri (pairplot)

---

## 📁 Dosya Yapısı
```
├── Veri.csv
├── veri_analizi.py
└── README.md
```

---

## 🧩 Notlar
- `Veri.csv` dosyası sayısal sütunlar içermelidir.
- Eksik değer doldurma işlemi yalnızca **sayısal** sütunlar için yapılır.
- Büyük veri setlerinde `pairplot` işlemi zaman alabilir.

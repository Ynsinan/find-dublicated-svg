SVG Duplicate Finder
Bu Python scripti, belirli bir klasördeki SVG dosyalarını tarar ve benzerliklerine göre çiftler halinde çoğaltır. Bu, büyük ölçekteki görsel varlık kütüphanelerini yönetirken yararlı olabilir.

Kullanım
Bu scripti kullanmak için, aşağıdaki adımları izleyin:

Bu repository'yi klonlayın veya indirin.
Terminali açın ve scriptin bulunduğu dizine gidin.
python index.py komutunu çalıştırın.
Script, mevcut çalışma dizinindeki 'icons' adlı bir klasördeki SVG dosyalarını tarar. Bu klasör adını ve konumunu ihtiyaçlarınıza göre değiştirebilirsiniz.

Çalışma Prensibi
Script, aşağıdaki adımları izler:

Belirtilen klasördeki tüm dosyaları listeler.
Her dosya için, dosyanın bir SVG dosyası olup olmadığını kontrol eder.
SVG dosyasını bir PNG dosyasına dönüştürür.
Dönüştürülen PNG dosyasını, klasördeki diğer tüm SVG dosyalarıyla karşılaştırır.
İki görüntü arasındaki benzerlik skorunu hesaplar.
Eğer iki görüntü tamamen aynıysa (benzerlik skoru 1), bu çifti bir çoğaltma olarak kaydeder.
Çıktı
Script, bulunan tüm çoğaltmaları 'duplicate_log.txt' adlı bir dosyaya yazar. Her çizgi, aynı olan iki dosyanın adını ve yolunu içerir.

Bağımlılıklar
Bu scriptin çalışması için aşağıdaki Python kütüphanelerinin kurulu olması gerekmektedir:

cairosvg
os
cv2
skimage
Bu kütüphaneleri pip kullanarak kurabilirsiniz:

image
Notlar
Bu script, büyük ölçekteki görsel varlık kütüphanelerini yönetirken yararlı olabilir. Ancak, çok büyük kütüphanelerle çalışırken performans sorunları yaşayabilirsiniz. Bu durumda, scripti daha küçük alt kümeler üzerinde çalıştırmayı düşünün.

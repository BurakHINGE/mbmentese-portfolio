# Blog: Local RAG Asistanı Bölüm 1 - Amacımız ve Temeller

Bu yazıda Mehmet Burak Menteşe, Microsoft AI Innovators programında geliştirdiği Local RAG asistanının temellerini anlatıyor.
Yapay zeka modellerinin spesifik bilgiler sorulduğunda yalan uydurma eğilimine 'Halüsinasyon' denir.
Bunu çözmek için modeli baştan eğitmek çok maliyetlidir. Bunun yerine RAG (Bulup Getirme, Harmanlama, Üretme) yöntemi kullanılır.
Asistanın bilgileri hatırlaması için kelimeler Vektör denilen sayı dizilerine çevrilir. (Embeddings)
Bu vektörler SQLite veri tabanında saklanır.

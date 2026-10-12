# Proje: Local RAG Asistanı

Bu proje, tamamen cihaz üzerinde (offline/yerel) çalışan ve verilerinizi dışarı aktarmadan size özel belgeler (PDF, notlar vb.) üzerinden sorularınızı yanıtlayan bir yapay zeka (AI) asistanıdır.
Microsoft Foundry Local platformu ve qwen3-embedding-0.6b modeli ile entegre edilmiştir.

Kullanılan Teknolojiler:
- Python
- LLM (Büyük Dil Modeli) & Prompt Engineering
- RAG (Retrieval-Augmented Generation) mimarisi
- Vektör Depolama için SQLite

Amaç: Yapay zekanın 'halüsinasyon' (bilmediği şeyi uydurma) problemini RAG mimarisi ile çözmek. Kullanıcının belgelerini 'chunking' (parçalama) yöntemiyle vektörlere ayırıp, kullanıcının sorusuyla en alakalı kısımları kosinüs benzerliği ile bularak doğru ve kanıta dayalı cevaplar üretmesini sağlamak.

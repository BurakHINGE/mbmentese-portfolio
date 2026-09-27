# Blog: Local RAG Asistanı Bölüm 2 - Veri Parçalama ve Arama Engine

Bu yazıda sisteme PDF veya uzun metin verildiğinde bunun nasıl işlendiği anlatılır.
Bütün metni yapay zekaya tek seferde vermek limitlere takılır (Token limitleri). Bu yüzden 'Chunking' (parçalara ayırma) yöntemi kullanılır.
Kullanıcı bir soru sorduğunda, kullanıcının sorusu da vektöre çevrilir ve SQLite veritabanındaki diğer vektörlerle 'Kosinüs Benzerliği' (Cosine Similarity) kullanılarak en yakın eşleşmeler bulunur.
Son adımda, bulunan bilgi parçacıkları (context) bir Prompt ile yapay zekaya verilir ve sadece o belgelere dayanarak cevap vermesi emredilir.

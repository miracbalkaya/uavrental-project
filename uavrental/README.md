# UAV Rental Project

Bu proje, Python ve Django kullanılarak geliştirilen bir UAV (Unmanned Aerial Vehicle) kiralama uygulamasını içerir. Ayrıca PostgreSQL ve Django Rest Framework kullanılarak geliştirilmiştir.

## Fonksiyonellik & API Endpoint'leri:

- **Üyelik:**
    - Kullanıcıların kayıt olabileceği API curl.
        - curl --location --request POST 'http://127.0.0.1:8000/api/users/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "id": 1,
  "name": "bayraktar",
  "surname": "yok",
  "email": "SIHA",
  "createdDate": "2024-01-07T10.",
  "password": "123"
}
'

- **UAV İşlemleri:**
- UAV özellikleri: Marka, Model, Ağırlık, Kategori vb.
- UAV ekleme serivis: 
    - curl --location --request POST 'http://127.0.0.1:8000/api/uavs/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "brand": "TB3",
  "model": "TB3 v1",
  "weight": 280,
  "category": "SIHA"
}
'
- UAV listeleme serivisi: 
    - curl --location --request GET 'http://127.0.0.1:8000/api/uavs/' \'
- UAV silme serivisi: 
    - curl --location --request DELETE 'http://127.0.0.1:8000/api/uavs/1/' \'
- UAV güncelleme serivis: 
    - curl --location --request PUT 'http://127.0.0.1:8000/api/uavs/2/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "brand": "TB3",
  "model": "TB3 v1",
  "weight": 280,
  "category": "SIHA"
}
- **Üye Kiralama Kayıtları:**
  Kullanıcıların kiralama geçmişini görebilecekleri bir curl.
  - curl --location --request GET 'http://127.0.0.1:8000/api/rentals/?renting_member=1'

- **Kiralanan UAV İşlemleri:**
  - Kiralanan UAV'leri silme, güncelleme, listeleme işlemleri.
  - Kiralama özellikleri: UAV, Tarih ve Zaman Aralıkları, Kiralayan Üye vb.
  - UAV Kiralama: 
  - curl --location --request PUT 'http://127.0.0.1:8000/api/rentals/2/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "start_date": "2024-01-07T20:59:00Z",
    "end_date": "2026-01-07T20:59:00Z",
    "uav": 3,
    "renting_member": 1
}'
- Kiralanan UAV kaydının silinmesi: 
  - curl --location --request DELETE 'http://127.0.0.1:8000/api/rentals/2/'

- Kiralanan UAV kaydının güncelleme:
  - curl --location --request PUT 'http://127.0.0.1:8000/api/rentals/2/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "start_date": "2024-01-07T20:59:00Z",
    "end_date": "2026-01-07T20:59:00Z",
    "uav": 3,
    "renting_member": 1
}'
- Kiralanan UAV kayıtlarının listelemesi
  - curl --location --request GET 'http://127.0.0.1:8000/api/rentals/'
  

- **Tüm Kiralanan UAV kayıtlarının Filtreleme ve Arama Özellikleri:**
  Listeleme sayfalarında filtreleme ve arama özellikleri.
  - curl --location --request GET 'http://127.0.0.1:8000/api/rentals/?renting_member=1&uav=3'

## Kurulum

1. Proje dizininde Django uygulamasını oluşturun:

   ```bash
   django-admin startproject uavrental

2. Gerekli Python paketlerini yükleyin:
python manage.py startapp rentals

3. Veritabanını oluşturun:
python manage.py migrate

4. Geliştirme sunucusunu başlatın:
python manage.py runserver

Proje artık http://127.0.0.1:8000 adresinde çalışmaktadır.


PostgreSQL Bağlantısı:

- Veritabanı Adı: uavrentals
- Kullanıcı Adı: postgres
- Şifre: mirac8478
- Host: localhost
- Port: 5432


## Docker ile çalıştırma komutları 

- Docker build command: 
docker build -t uavrentalv1 .

- Docker run command
docker run -p 8000:8000 mydjangoapp
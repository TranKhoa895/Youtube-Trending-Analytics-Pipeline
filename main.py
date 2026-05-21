'''
DATA EXTRACTION
'''
import os
import json
from datetime import datetime
from googleapiclient.discovery import build 

# 1. Cấu hình các tham số 
API_key = "AIzaSyBEmnJ8wysW0ykBanbyj11VFM8l3FEY-aw"
PROJECT_name = "youtube_trending_pipeline"

def extract_trending_videos():
    # 2. Tạo đối tượng kết nối với Youtube API
    youtube = build('youtube', 'v3', developerKey=API_key)

    # 3. Gọi API lấy top 50 video trending tại Việt Nam 
    request = youtube.videos().list(
        part = "snippet,contentDetails,statistics",
        chart = "mostPopular",
        regionCode = "VN",
        maxResults = 50
    )
    response = request.execute()

    # 4. Bổ sung dữ liệu (metadata) về thời gian chạy pipeline
    execution_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    data_to_save = {
        "extracted_at": execution_time,
        "items": response.get("items", [])
    }

    # 5. Lưu tạm thành file JSON local để kiểm tra
    file_name = f"youtube_trending_{datetime.utcnow().strftime('%Y%m%d')}.json"
    with open(file_name, 'w', encoding='utf-8') as f:
        for item in response.get("items", []):
            record = {
                "extracted_at": execution_time, 
                "video_data": item
            }
            f.write(json.dumps(record, ensure_ascii=False)+"\n")

    print(f"Đã trích xuất thành công {len(data_to_save['items'])} videos và lưu vào file {file_name}")
    return file_name

'''
DATA LOADING
'''
from google.cloud import storage

def upload_to_gcs(local_file_name, bucket_name, gcs_blob_name, key_json_path):
    try:
        #  1. Tra file JSON vào client để xác thực quyền Storage Object Admin 
        storage_client = storage.Client.from_service_account_json(key_json_path)

        # 2. Định vị đúng Bucket mục tiêu trên Cloud 
        bucket = storage_client.bucket(bucket_name)

        # 3. Định nghĩa đường dẫn và tên file trên Cloud 
        blob = bucket.blob(gcs_blob_name)

        # 4. Tiến hành upload file lên Cloud 
        print(f"Đang tải file {local_file_name} lên Cloud Storage")
        blob.upload_from_filename(local_file_name)

        print(f"Thành công! File có tại: gs://{bucket_name}/{gcs_blob_name}")
        return True 
    except Exception as e:
        print(f"Lỗi khi upload lên GCS: {e}")
        return False

if __name__ == "__main__":
    # 1. Trích xuất data từ API về máy local 
    local_file = extract_trending_videos()
    
    # Cấu hình thông số Cloud
    BUCKET_NAME = "youtube-trending-lake-tpk-2026"
    GCS_DESTINATION_PATH = f"raw_data/{local_file}"
    KEY_PATH = "gcp-key.json"

    # 2. Tự động upload file lên Data Lake (Google Cloud Storage)
    upload_to_gcs(local_file, BUCKET_NAME, GCS_DESTINATION_PATH, KEY_PATH)

'''
DATA TRANSFORMATION
'''
# ĐÃ LÀM TRÊN SQL CỦA BIGQUERY Ở GOOGLE CLOUD STORAGE 

'''
DATA VISUALIZATION 
'''
# ĐÃ LÀM Ở DATA STUDIO 

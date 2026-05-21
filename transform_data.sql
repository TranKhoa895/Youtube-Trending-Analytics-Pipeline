CREATE OR REPLACE TABLE `black-skyline-477412-e1.youtube_raw.cleaned_trending_videos` AS
SELECT
  video_data.id AS video_id,
  TRIM(video_data.snippet.title) AS video_title,
  TRIM(video_data.snippet.channelTitle) AS channel_title,
  video_data.snippet.categoryId AS category_id,
  
  CAST(video_data.statistics.viewCount AS INT64) AS view_count,
  CAST(video_data.statistics.likeCount AS INT64) AS like_count,
  CAST(video_data.statistics.commentCount AS INT64) AS comment_count,
  
  extracted_at
FROM
  `black-skyline-477412-e1.youtube_raw.trending_videos_raw`
QUALIFY
  ROW_NUMBER() OVER (
    PARTITION BY video_data.id, extracted_at 
    ORDER BY extracted_at DESC
  ) = 1;
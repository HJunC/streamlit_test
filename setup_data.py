import pandas as pd
import os

def create_data_folder() :
    if not os.path.exists('data') :
        os.makedirs('data')
        print("data 폴더가 생성되었습니다.")
    
    if not os.path.exists('data/users.csv') :
        users_columns = ['user_id', 'username', 'password', 'created_at']
        empty_users = pd.DataFrame(columns = users_columns)
        empty_users.to_scv('data/users.csv', index=False, encoding='utf-8')
        print('data/users.csv 파일이 생성되었습니다.')
    
    if not os.path.exists('data/posts.csv') :
        posts_columns = ['post_id', 'user_id', 'content', 'timestamp']
        empty_posts = pd.DataFrame(columns = posts_columns)
        empty_posts.to_scv('data/posts.csv', index=False, encoding='utf-8')
        print('data/posts.csv 파일이 생성되었습니다.')

    if not os.path.exists('data/likes.csv') :
        likes_columns = ['post_id', 'user_id', 'content', 'timestamp']
        empty_likes = pd.DataFrame(columns = likes_columns)
        empty_likes.to_scv('data/likes.csv', index=False, encoding='utf-8')
        print('data/likes.csv 파일이 생성되었습니다.')

    print('초기설정이 완료되었습니다.')

if __name__ == '__main__' :
    create_data_folder()
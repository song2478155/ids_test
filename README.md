

### 미니콘다 설치
# 1. 다운로드 및 설치
- wget https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-Linux-x86_64.sh
- chmod +x Miniconda3-py38_22.11.1-1-Linux-x86_64.sh
- bash Miniconda3-py38_22.11.1-1-Linux-x86_64.sh

# 2. 환경변수 적용
 - source ~/.bashrc

# 3. 실행 확인
 - conda list
 - conda env list
 
# 4. 콘다 생성
 - conda create --name ids_conda python=3.10

# 4.1 콘다 접속
 - conda activate ids_conda

# 5.1 폴더 이동 및 필수 라이브러리 설치
 - test 폴더에 파일 복사 완료, "/data2/msbaek_dir/0_datasets/CIC-IDS-2017/CSVs/MachineLearningCVE" cicids2017 데이터셋 복사 완료
 - cd ../msbaek/test/
 - pip install -r requirements.txt
 - pip install torch==2.7.1+cu126 torchvision==0.18.1+cu126 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu126


# 5.2 실행
 - cd 0_DeepLearning
 - python 1_change_the_encoding_to_utf8_DL.py

# 6. vscode 연결
 - Remote - SSH 설치
 - F1 혹은 ctrl+shift+p을 눌러 명령어 팔레트(Command Palette)를 열기
 - "Remote-SSH: Add new SSH Host..." 클릭
 - ssh {계정}@{Host 주소} -{port} 입력
   예) etri@129.254.62.184
 - open folder 이용 "/home/msbaek/test/0_DeepLearning/" 으로 이동

 - 
# 콘다 삭제
 - rm -rf ~/miniconda3

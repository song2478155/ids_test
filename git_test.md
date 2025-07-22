
# 1. 콘다 생성 / 활성화
 - conda create --name GNN_IDS python=3.10
 - conda activate GNN_IDS
 - cd /home/msbaek  

# 2. git 다운로드 및 설치
- git clone https://github.com/song2478155/GNN-IDS.git
- cd GNN-IDS/
- chmod -R 777 install.sh
- ./install.sh

# 2. 토치 버전 맞추기
 - pip install torch==2.0.1+cu117 torchvision==0.15.2+cu117 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu117
 - pip install torch-geometric==2.3.1
 - pip install torch-scatter torch-sparse torch-cluster torch-spline-conv -f https://data.pyg.org/whl/torch-2.0.1+cu117.html

# 3. numpy 에러 발생
 - pip install numpy==1.26.4


# 4. 주피터 노트북 설치 / 접속
 - conda install jupyter notebook -y
 - jupyter notebook . --ip='*' --NotebookApp.token='' --NotebookApp.password=''
 - 로컬(윈도우)에서 http://129.254.62.184:8888/ 접속 

# 5. vscode에서도 접속
 - File - open folder - "/home/msbaek/GNN-IDS" - OK
 - 비번
 - src/*.ipynb 실행 - python enviroment를 GNN_IDS로 변경
 - 실행

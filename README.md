

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

# 5. 콘다 삭제
 - rm -rf ~/miniconda3

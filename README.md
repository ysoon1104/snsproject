# 📱 SNS 사용시간이 학생에게 미치는 영향 분석

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)

**당곡고등학교 데이터 분석 프로젝트**

[🌐 웹사이트 바로가기](#) · [📊 데이터 보기](#) · [🐛 오류 신고](#)

</div>

---

## 📌 프로젝트 소개

> SNS(소셜 미디어) 사용시간이 고등학생의 학업, 수면, 스트레스, 집중력에
> 어떤 영향을 미치는지 데이터로 분석하고 시각화한 프로젝트입니다.

### 🎯 분석 목표
- SNS 사용시간과 **학업 성취도**의 상관관계 파악
- SNS 사용시간과 **수면 질**의 상관관계 파악
- SNS 사용시간과 **스트레스 지수**의 상관관계 파악
- SNS 사용시간과 **집중력**의 상관관계 파악

---

## 📊 주요 분석 결과

| SNS 사용시간 | 학업 성취도 | 수면 질 | 스트레스 | 집중력 |
|:----------:|:---------:|:------:|:-------:|:-----:|
| 1시간 이하  | 78점 | 82점 | 30점 | 80점 |
| 1 ~ 2시간  | 75점 | 79점 | 35점 | 77점 |
| 2 ~ 3시간  | 73점 | 76점 | 42점 | 74점 |
| 3 ~ 4시간  | 71점 | 74점 | 50점 | 70점 |
| 4시간 이상  | 68점 | 70점 | 62점 | 65점 |

### 💡 핵심 결론
```
✅ SNS를 하루 4시간 이상 사용하면
   - 학업 성취도 : 최대 10점 감소
   - 수면 질     : 최대 12점 감소
   - 스트레스    : 최대 32점 증가
   - 집중력      : 최대 15점 감소
```

---

## 🛠️ 사용 기술

```
📦 Tech Stack

├── 언어         : Python 3.8+
├── 웹 프레임워크 : Streamlit
├── 시각화        : Matplotlib, Numpy
├── 데이터 처리   : Pandas
└── 배포          : Streamlit Cloud + GitHub
```

---

## 🚀 실행 방법

### 1️⃣ 저장소 클론
```bash
git clone https://github.com/[최여준]/[레포지토리이름].git
cd [레포지토리이름]
```

### 2️⃣ 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 3️⃣ 앱 실행
```bash
streamlit run app.py
```

### 4️⃣ 브라우저에서 확인
```
http://localhost:8501
```

---

## 📁 프로젝트 구조

```
📦 sns-study-impact/
│
├── 📄 app.py                # 메인 Streamlit 앱
├── 📄 requirements.txt      # 필요 라이브러리 목록
├── 📄 README.md             # 프로젝트 설명 (현재 파일)
│
├── 📁 data/
│   └── 📄 sns_data.csv      # 설문조사 데이터
│
├── 📁 pages/
│   ├── 📄 1_그래프분석.py    # 그래프 시각화 페이지
│   ├── 📄 2_데이터보기.py    # 원본 데이터 페이지
│   └── 📄 3_결론.py         # 결론 및 제언 페이지
│
└── 📁 assets/
    └── 🖼️ logo.png          # 로고 이미지
```

---

## 📋 조사 개요

| 항목 | 내용 |
|:----:|:----:|
| 조사 대상 | 당곡고등학교 학생 |
| 조사 방법 | 설문조사 |
| 조사 기간 | 2025년 |
| 표본 크기 | 00명 |
| 분석 도구 | Python, Streamlit |

---

## 👥 팀원

| 이름 | 역할 | GitHub |
|:----:|:----:|:------:|
| 홍길동 | 데이터 수집 & 분석 | [@아이디](#) |
| 김철수 | 시각화 & 개발 | [@아이디](#) |
| 이영희 | 기획 & 발표 | [@아이디](#) |

---

## 📜 라이선스

```
MIT License
Copyright (c) 2025 당곡고등학교
```

---

<div align="center">

**당곡고등학교** · 2025

⭐ 이 프로젝트가 도움이 됐다면 Star를 눌러주세요!

</div>

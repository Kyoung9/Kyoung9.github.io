# jobscraper.github.io
job_scrapper

jobscraper/
├─ app.py                 # Flask 앱 생성, 라우트 등록
├─ config.py              # 환경 설정, 타임아웃, UA 등
├─ routes/
│  └─ search.py           # 요청 검증 + 템플릿 렌더
├─ services/
│  └─ job_search.py       # 통합 검색 로직(병합/정렬/중복제거)
├─ scrapers/
│  ├─ base.py             # 공통 인터페이스/헬퍼
│  ├─ berlinstartupjobs.py
│  ├─ weworkremotely.py
│  └─ web3career.py
├─ models/
│  └─ job.py              # Job 도메인 모델
├─ utils/
│  ├─ http.py             # requests 세션/재시도/타임아웃
│  ├─ normalize.py        # 텍스트 정규화/URL 정리
│  └─ logging.py          # 로깅 설정
├─ templates/
│  ├─ home.html
│  └─ search.html
└─ tests/
   ├─ test_scrapers.py
   └─ test_service.py

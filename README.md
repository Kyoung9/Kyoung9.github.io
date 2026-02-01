# Job Scraper (jobscraper.github.io)

## English
### Overview
A small Flask app that searches multiple job boards by keyword, merges results, removes duplicates, and lets you export the results to a CSV file.

### Features
- Keyword search across multiple sources
- Dedupe by link (or by source/company/title when link is missing)
- CSV export (`/export?keyword=...`) saved under `exports/`
- Simple in-memory cache (TTL 1 hour)

### Data Sources
- Berlin Startup Jobs
- We Work Remotely
- Web3.career

### Tech Stack
- Python 3.11+
- Flask
- requests + BeautifulSoup4
- Pico.css (via CDN)

### Getting Started
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5001` in your browser.

### Usage
1. Enter a keyword on the home page and submit.
2. Review the aggregated results on the search page.
3. Click **Export to file** to download a CSV.

### Project Structure
```
app.py
services/
  job_search.py
  job_export.py
scrapers/
  base.py
  berlinstartupjobs.py
  weworkremotely.py
  web3career.py
models/
  job.py
utils/
  cache.py
  file_export.py
  http.py
  normalize.py
  logging.py
templates/
  home.html
  search.html
tests/
```

### Notes
- Target sites can change their HTML; if a scraper fails, check the selectors in `scrapers/`.
- Exported files are created in the `exports/` directory.

---

## 한국어
### 개요
키워드로 여러 채용 사이트를 검색하고 결과를 합친 뒤 중복을 제거하여 CSV로 내보낼 수 있는 간단한 Flask 앱입니다.

### 주요 기능
- 여러 소스에서 키워드 검색
- 링크 기준 중복 제거(링크가 없으면 source/company/title 조합)
- CSV 내보내기(`/export?keyword=...`) 후 `exports/`에 저장
- 1시간 TTL의 간단한 메모리 캐시

### 데이터 소스
- Berlin Startup Jobs
- We Work Remotely
- Web3.career

### 기술 스택
- Python 3.11+
- Flask
- requests + BeautifulSoup4
- Pico.css (CDN)

### 시작하기
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

브라우저에서 `http://localhost:5001`로 접속하세요.

### 사용 방법
1. 홈 화면에서 키워드를 입력하고 검색합니다.
2. 검색 결과 페이지에서 통합 결과를 확인합니다.
3. **Export to file**을 눌러 CSV를 다운로드합니다.

### 프로젝트 구조
```
app.py
services/
  job_search.py
  job_export.py
scrapers/
  base.py
  berlinstartupjobs.py
  weworkremotely.py
  web3career.py
models/
  job.py
utils/
  cache.py
  file_export.py
  http.py
  normalize.py
  logging.py
templates/
  home.html
  search.html
tests/
```

### 참고
- 대상 사이트의 HTML이 변경되면 스크레이퍼가 실패할 수 있습니다. `scrapers/`의 셀렉터를 확인하세요.
- CSV 파일은 `exports/` 폴더에 생성됩니다.

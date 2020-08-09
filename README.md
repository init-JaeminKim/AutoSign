# AutoSign(오토싸인)
여신금융협회 회원가입을 도와주는 프로그램입니다  
Chromedriver를 통해 필드값 입력 및 클릭을 자동화한 시스템이며  
GUI는 PyQt5로 구현되었습니다

## 설치 방법 (Installation)
* 업로드 된 파일을 압축 파일로 받아 원하는 위치에 압축을 푸십시오 
* 백신 탐지로 프로그램이 삭제 될 경우 백신 프로그램 설정에서  
압축파일이 풀릴 위치를 검사 항목에서 예외처리를 합니다

## 사용 방법 (Usage)
1. setting.exe를 통해 여신금융협회 가입에 필요한 기본정보를 입력합니다 (최초 1회 필요)
2. Verification.exe로 관리자에게 사용인증 요청을 합니다 (최초 1회 필요, 24시간 내에 승인되지 않을 시 문의)
3. 인증을 받은 후 AutoSign.exe로 여신금융협회 회원가입을 시작합니다

## 라이센스 (License)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)    

## 버그들 (Known Bugs)
* Windosws 10을 제외한 운영체제에서 정상작동되지 않을 수 있습니다
* VerificationHelper.exe가 작동중지되거나 응답없은 경우가 발생 (사용인증 요청은 정상처리 됨)
* 컴퓨터에 api-ms-win-crt-runtime-l1-1-0.dll이(가) 없어 프로그램을 시작할 수 없습니다 ([운영체제에 맞는 패키지를 설치하여 해결](https://support.microsoft.com/ko-kr/help/2999226/update-for-universal-c-runtime-in-windows))

## FAQ (Frequently Asked Qustions)
* 크롬 브라우저와 크롬 드라이버의 버전이 일치해야 합니다
* [크롬드라이버 다운로드](https://chromedriver.chromium.org/downloads)
* [크롬브라우저 버전 확인방법](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=ko)
* [카카오톡 오픈채팅 고객지원](https://open.kakao.com/o/sn3nzpnc)
* 아이디는 k + '사업자등록번호' 입니다

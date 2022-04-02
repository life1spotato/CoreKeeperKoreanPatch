## Core Keeper 한국어화 / 한글패치

## [최신 공지](https://gall.dcinside.com/corekeeper/1659) | [최신 릴리즈](https://github.com/life1spotato/CoreKeeperKoreanPatch/releases) 

[![GitHub issues](https://img.shields.io/github/issues/life1spotato/CoreKeeperKoreanPatch?logo=GitHub)](https://github.com/life1spotato/CoreKeeperKoreanPatch/issues)

## 사용 툴

- UABEA
https://github.com/nesrak1/UABEA

- Il2CppDumper
https://github.com/Perfare/Il2CppDumper

## dll 추출

1. `Il2CppDumper.exe` 실행
2. `Core Keeper\GameAssembly.dll` 선택 (IlCpp binary file)
3. `Core Keeper\CoreKeeper_Data\il2cpp_data\Metadata\global-metadata.dat` 선택 (global-metadata)
4. `Il2CppDumper` 설치 폴더에 `DummyDll` 폴더 생성됨 (1~2분 소요)
5. 잘라내어 `Core Keeper\CoreKeeper_Data` 폴더에 `Managed`로 이름 바꾸어 붙여넣기

## 패치 과정

### 업데이트 확인

1. `UABEAvalonia.exe` 실행
2. `File → Open`
3. `Core Keeper\CoreKeeper_Data\data.unity3d` 열기
4. 알림창 `File → 파일로 압축 해제`, `Memory → 메모리에 압축 해제`
5. `Core Keeper\CoreKeeper_Data\` 폴더에 `Export All`
6. `resources.assets` 를 `_resources.assets` 로 이름 바꾸고 열기
7. `I2Languages`, `ThaiFont`, `TextManager` 항목 `Export Dump` (raw = raw 데이터, dump = txt 또는 Json으로 dump)
<br> &nbsp;7-1. 파일 형식 `UABEA json dump`로 지정해주어야 함.
<br> &nbsp;7-2. `View → Search by name`에 이름 전체로 검색 (부분 검색 안됨)
8. `python json2tsv.py --version {version} --dir {json file dir}`
9. `python migration.py --ov {old_version} --nv {new_version} --dir {tsv file dir}`
10. 과정 9 결과를 번역용 구글스프레드시트에 추가
<br> &nbsp;10-1. `파일 → 가져오기 → new.tsv, update.tsv 선택 → '탭으로 구분' → 새 시트로 가져오기` (자동화 예정)
<br> &nbsp;10-2. 알아서 잘 업데이트 (자동화 예정)
11. 번역 진행

### 패치 제작
1. 번역 다운로드 `버전 페이지 → 파일 → 다운로드 → 탭으로 구분된 값` (자동화 예정)
2. 폰트 값 병합 `python mergefont.py --dir {json file dir} [--reuse]`
3. 텍스트 매니저 변환 `python cvttextmgr.py --dir {json file dir} [--reuse]`
4. 번역 데이터 적용 `python applydata.py --ogv {old_game_version} --ngv {new_game_version} --kt {korean_tag} --jd {json_dir} --td {tsv_dir} [--reuse]`
5. `UABEA` 로 `_resources.assets` 열기
6. `I2Languages, ThaiFont, TextManager` json import
7. `File → Save` `resources.assets` 저장
8. `data.unity3d` 를 `_data.unity3d` 로 바꾸고 `File → Open` 열기
9. `Import → resources.assets`
10. `File → Save` `_1data.unity3d` 저장
11. `File → Open` `_1data.unity3d` 열기
12. `File → Compress` `data.unity3d` 을 `LZ4` 로 압축
13. `data.unity3d` zip으로 압축하여 배포

## 폰트 출처
[갈무리 폰트](https://galmuri.quiple.dev/)


# 七項驗證錯誤修復 · 2026-10-31

基線為 `a23a87e62d6c44b1fe296d67a7c66f153480ba6c`。本次檢查原有七項報錯，修正驗證器的入口選擇及引用範圍，再修復真正失效的正文路徑。採用明確的根目錄布局，結果為 **0 項錯誤、1 項可選警告**。這是結構與連結檢查，不是新的來源覆蓋或人格辨識。

## 原有七項錯誤

| 檢查 | 原報錯 | 原因與處理 |
| --- | --- | --- |
| S1 | 找不到唯一技能入口 | 舊程式只查 `.agents/skills/`；現有安裝刻意使用根目錄入口。新增明確的 `--layout root`，不恢復已移除的 discovery 目錄。 |
| S2 | 缺少 SKILL.md | 跟隨錯誤入口去找不存在的位置；根目錄檔案實際存在。根目錄模式直接讀取該檔。 |
| S3 | 缺少 references、voice、frameworks | 同一入口錯位造成的連帶報錯；三者實際存在。 |
| C1 | name 或 description 為空 | 未讀到真正的核心檔，並非現有 frontmatter 缺欄位。 |
| C1b | name 與目錄名不符 | 比較的是空名稱與內部佔位符。根目錄模式核對宣告名稱及任何存在的 discovery 別名，倉庫名稱可不同。 |
| C2 | description 為空或帶評測用語 | 未讀到真正的描述；正確讀取後通過，沒有刪改原描述。 |
| C6 | c01–c12 無法解析 | 入口錯位使已知模組集合為空；另外全倉 Markdown 掃描把歷史 c09–c12 也當作當前引用。改為只檢查核心與實際 references；歷史記錄保持。 |

前六項是同一入口問題的連帶結果。第七項同時涉及入口與歷史記錄的邊界。新版預設仍要求 discovery 布局，新交付的原有打包規則不變；這次使用的是明確選定的既有根目錄安裝模式。

## 真正失效的三處路徑

讀到正文後，C5 額外找出以下錯誤。初次七項報錯時沒有讀到這些正文，因而未能發現。

| 位置 | 修正前 | 修正後 |
| --- | --- | --- |
| frameworks 的核心指引 | SKILL.md | ../SKILL.md |
| voice 的核心指引 | SKILL.md | ../SKILL.md |
| C06 的聲音指引 | voice.md | ../voice.md |

這三處是全部 runtime 改動，逐項差異見 [edits.json](edits.json)。其餘正文、段落、來源代碼與 C 引用保持不變。provenance 第 117–118 行的英文命令式措辭也改成已完成編輯的事實記錄，消除 L1 警告。

## 驗證與限制

驗證器為 Persona-Distiller 的 [4e9263a](https://github.com/ariel-lee-1023/Persona-Distiller/commit/4e9263a337d3b2c02fa7010c6620e202d02b2683)。在該工具倉庫執行 `python3 scripts/validate_package.py ../liu-zhongjing-perspective --layout root` 可重現檢查；這不是不帶參數的 discovery 驗證通過。

新增 9 項入口、別名及引用範圍回歸測試，驗證器專項共 16 項通過；補齊工具已聲明的 jsonschema 依賴後，完整 114 項測試通過。依賴只安裝在臨時環境。真缺核心、缺 references、名稱不符、重複副本、懸空別名、壞連結與當前失效 C 引用仍會報錯。版本和雜湊見 [validator.json](validator.json)。

唯一剩餘警告為可選的 transworld-identity/episodic.md 不存在；沒有為了消除警告新增空白或虛構的經驗記錄。C3 未提供語言特定標題錨點，因此仍明確跳過。未執行嚴格研究驗收，未新增原書閱讀、來源覆蓋或機器辨識；Candidate 狀態保持。

使用者 AGENTS.md 的既有未提交修改完整保留，不納入本次提交。歷史評測與舊版本的報錯記錄保留原來範圍。前後結果見 [原七項報錯](package-before.json)、[定位正文後的路徑報錯](package-before-link-repair.json)、[修復後檢查](package-after.json)；內容完整性見 [checks.json](checks.json)。

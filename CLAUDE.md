# 呱呱大腦 — 好年企業專案記憶

## 關於主人
- **公司**：好年企業有限公司
- **負責人**：謝豐安
- **Email**：phoneann@gmail.com
- **地址**：台南市永康區中山路101巷2號
- **電話**：06-2324880

## 目前專案
- **名稱**：報價單產生器（haonian-quotation）
- **GitHub**：`phoneann/haonian-quotation`
- **技術**：Python + Streamlit
- **已部署**：Streamlit Cloud（share.streamlit.io，帳號 phoneann）
- **主程式**：`app.py`
- **PDF產生**：`pdf_generator.py`

## 與「呱呱大腦」母體（Google Drive Vault）的關係
- 主人在 Google Drive 有一套更完整、更成熟的個人／公司AI協作系統，叫「呱呱的大腦」，底下依部門（CEO戰略、CMO行銷、COO營運、CFO財務、CBO商務拓展…）跟專案（BNI億金分會、曦安科技、有情天、台南喵團隊、網站接案服務等）分資料夾，有自己的路由表、「AI共同工作看板」、「每日回顧」、「收工/開工」觸發字機制，Claude／Codex／Antigravity 都要遵守
- **這個repo（haonian-quotation報價單App）目前還沒被登記進母體的路由表**，所以桌機在那個Drive vault環境裡工作的紀錄，不會自動出現在這裡；反過來，這裡發生的事也不會自動出現在母體
- 這份 `CLAUDE.md` 只服務「有人直接在這個repo資料夾工作」的情境，是輕量版的專案記憶，**不是**完整的呱呱大腦，內容也不會跟Drive那份同步——重複資訊只會造成兩邊兜不起來，所以不把母體內容整份搬過來
- 母體CLAUDE.md路由表要補一行指到這個repo，才能真正打通（見下方待辦）
- **真正能跨裝置同步的捷徑**：母體的「每日回顧」（`~/guagua-brain/每日回顧.md`）不是放在沒有版本控制的Drive資料夾裡，它本身就是獨立的git repo `phoneann/guagua-brain`，桌機每天23:30自動push。任何一個Claude Code session（不管手機還是桌機）只要用 `add_repo` 把 `phoneann/guagua-brain` 接進來，就能直接讀寫這份每日回顧，看到彼此真正做過的事——這比土法煉鋼複製貼上、或指望路由表可靠得多。如果又碰到「手機看不到桌機在做什麼」，先試這條路

## 主人的習慣與狀況
- 常用手機跟我對話
- 有桌機（NB），但不一定開著
- 不太熟技術操作，需要一步一步引導
- 習慣叫我「呱呱」

## 手機上能做的事（呱呱幫你做）
| 任務 | 可以嗎 |
|---|---|
| 叫呱呱改程式碼 | ✅ |
| 叫呱呱 push / merge | ✅ |
| 叫呱呱新增功能 | ✅ |
| 打開報價單 App 使用 | ✅（Streamlit Cloud 有網址） |
| 跑本機指令 | ❌（需要桌機） |

## 手機上能做的事（自己做）
| 任務 | 可以嗎 |
|---|---|
| 跟呱呱對話下指令 | ✅ |
| 開報價單 App 填資料 | ✅（有網址後） |
| 下載 PDF / Excel | ✅ |
| 看 GitHub | ✅ |

## 首要目標（2026/07）
- **BNI 億金分會成會** — 目前13人，目標20人，還差7個
- 每天花1小時執行KPI：聯繫3個潛在成員、追13位成員訪客、清1件待辦、回報李孟蓉
- 核心動力：不是為了分會本身，是為了願意跟進來的那些成員

## BNI 億金分會狀況
- 從2025年10月開始籌備
- 啟動大會：2026/07/07 已完成
- 聯絡窗口：李孟蓉（0922-543072）— 籌備顧問
- 主人心態：成熟，知道情緒在哪但不讓它擋路，專注把事情做完

## 臉書內容方向
- 商業洞察系列（已發一篇：AI時代懂商業者的黃金年代）
- 個人標籤：#謝豐安觀點

## 今日行程（2026/07/22）
- 09:30 BNI 億金籌備會議（主持）
- 10:30 有情天會議（性質待補充）

## 待辦 / 尚未完成
- [ ] 確認 Streamlit Cloud 網址並記錄在這裡
- [ ] BNI：找2-3人組核心小組（會務・來賓・活動）
- [ ] BNI：列出10個潛在成員名單
- [ ] BNI：傳進度給李孟蓉（每天一則）
- [ ] 補充「有情天」是什麼會議，記錄進大腦
- [ ] 在Drive「呱呱大腦」母體CLAUDE.md的路由表補一行，指到這個GitHub repo（文字已準備好，見上方「與呱呱大腦母體的關係」段落說明，貼上即可）：
      `| **報價單**、報價單產生器、haonian-quotation、quotation | GitHub repo \`phoneann/haonian-quotation\`（Streamlit報價單App，部署在Streamlit Cloud） |`

## AI協作日誌（跨工具同步，手機/桌機、Claude/Codex/Gemini 共用）
> 這份日誌是所有AI工具的共同記憶。不管主人用手機還是桌機、叫的是 Claude、Codex 還是 Gemini，只要是在這個repo裡工作，都要讀這裡拿最新狀況，也都要往這裡寫。
> 格式：`- YYYY-MM-DD HH:MM [工具/裝置] 做了什麼`

- 2026-08-03 [Claude/手機] 討論跨工具（Claude/Codex/Gemini）同步記憶的機制，建立本日誌區塊 + AGENTS.md / GEMINI.md 指向檔
- 2026-08-03 [Claude/手機] 主人分享Drive「呱呱的大腦」母體CLAUDE.md內容，確認這是更完整的桌機端多AI協作系統（獨立於這個repo），本repo尚未登記進母體路由表；補上「與母體的關係」說明段落，並把待辦改成請主人去母體路由表補登這個repo
- 2026-08-03 [Claude/手機] 找到真正同步路徑：`~/guagua-brain`（每日回顧）本身就是獨立git repo並自動push GitHub，跟Drive大腦資料夾是兩回事；已用add_repo接進本session，直接寫回一筆今天的每日回顧，手機端第一次真正打通桌機記錄，並把這個捷徑記進CLAUDE.md

## 重要提醒（所有AI工具都要遵守，不只Claude）
- 程式碼改完一定要 push 到 `main`，Streamlit Cloud 才會自動更新
- 每次進新 session，開工前一定要先讀這份 CLAUDE.md（Codex/Gemini 是透過 AGENTS.md / GEMINI.md 被導引過來讀這份），快速回到狀況
- **每次進新session（不管手機還是桌機），開工時要主動用 `add_repo` 把 `phoneann/guagua-brain` 接進來，讀最新的「每日回顧.md」，才能真的知道桌機/其他工具最近做過什麼——不用等主人問「你知道我做了什麼嗎」才做**。這是Claude Code專屬能力（透過 `add_repo`/`register_repo_root`），如果所在的工具沒有這個能力，至少要提醒主人這條路徑存在
- **每次工作session結束前，不用主人開口提醒，AI要主動在上面「AI協作日誌」新增一行紀錄，然後commit + push**。這是預設行為，不是主人要求才做的事
- 如果這次對話沒有實際commit/push任何東西（純聊天、討論），也要照樣在日誌補一行文字紀錄「聊了什麼」，這樣手機/桌機才不會互相看不到彼此做過的事
- 提醒主人：AGENTS.md、GEMINI.md 只是指向這份檔案的入口，實際內容只維護這一份 CLAUDE.md，避免三份資料兜不起來

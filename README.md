# 劉仲敬

A distilled **perspective skill** for LLM agents: analyse history, politics, civilisation, current affairs, and even ordinary life questions the way Liu Zhongjing (劉仲敬, b. 1974) does — translate the question into one about *order being produced or consumed*, about heredity and class position, about genealogical placement — then answer coldly, and withhold reassurance exactly where the reader most wants it.

The skill is written in Traditional Chinese and defaults to Traditional Chinese output unless the user explicitly requests another language or script. Its technical identifier remains `liu-zhongjing-perspective`. It is written in the first person, as a voice rather than a set of instructions about a voice. It is designed to be dropped into any agent that supports file-based skills, or pasted in as a system prompt.

---

## 新增參考類別：文明譜系與地方憲制

[文明譜系與地方憲制——從兩河到東亞](references/clusters/c09-civilizational-genealogy-constitutions.md)把《美索不達米亞》與《東亞史.md》合輯接成一條線：祭司、商路與武裝集團如何帶入制度，地方共同體又怎樣分配財產、司法、代表權和戰爭責任。它涵蓋吳越與江淮、巴蜀與滇黔、晉燕齊、上海及滿洲，並保留作者對同化、行政國家和文明循環所作的條件區分。

**可以這樣開始：**「上海與兩河城邦的比較，能幫我們分清財富、自治和軍事保護之間的關係嗎？」技能會先追查實際承擔這些工作的團體，再談制度名稱。這是建議提問，不是保存的測試回答。

本次是有界主題蒸餾：已盤點全部章節，按主題選讀原文及問答，沒有逐段全書精讀，也沒有獨立核實考古與歷史主張。新簇為 **Candidate**，已作來源定位及連結檢查，尚未進行人格辨識評測；原有評測不能自動延伸到本簇。詳見[範圍記錄](transworld-identity/scope.md)與[本次驗證結果](transworld-identity/validation.json)。

---

## Repository layout

```
liu-zhongjing-perspective/
├── SKILL.md                        # core reasoning and judgement; read with frameworks.md and voice.md
├── references/
│   ├── clusters/
│   │   ├── c01-ayi-life-advice.md     # anti-self-help life advice; the "machine off" warm register
│   │   ├── c02-premodern-order.md     # order structure + classical/pre-modern constitutions, epigraphy
│   │   ├── c03-wadi-psychology.md     # Chinese collective psychology — pathology
│   │   ├── c04-civilization-theory.md # last man, 守先待後, the Great Flood mechanism
│   │   ├── c05-jingxuan-lectures.md   # contemporary application: news items, 2020s topics,
│   │   │                              #   global capitalism, family, class instinct
│   │   ├── c06-figures.md             # character studies, two registers: written studies + lecture-mode
│   │   ├── c07-nation-invention.md    # comparative nation-invention: Poland, Russia, 中華民族
│   │   ├── c08-minguo-wenyan.md       # Republican chronicle + the classical-Chinese register
│   │   └── c09-civilizational-genealogy-constitutions.md # civilisation transmission + local constitutions
│   ├── frameworks.md               # concepts, reasoning methods and established judgements; required reading
│   └── voice.md                    # expressive system — required even for short answers
├── fidelity-ledger/
│   ├── provenance.md               # honesty ledger: element → source → score → gate status;
│   │                                    #   human-facing, never loaded by the host agent
│   └── episodic.md                 # attested one-off happenings not used as cluster anchors
├── transworld-identity/            # scoped c09 evidence, coverage and current validation
├── CHANGELOG.md
├── LICENSE
├── NOTICE.md
└── README.md
```

**Before the first substantive response in this persona, read `SKILL.md`, `references/frameworks.md`, and `references/voice.md` in full, even for a short answer.** The core supplies the overall reasoning posture and judgements; `frameworks.md` supplies concept definitions, reasoning methods, and established judgements; `voice.md` governs the sentences actually written. All three are required regardless of topic or answer length. Keep them available throughout the conversation. If any is lost through context compaction, reload that file before continuing; do not reread material already fully available in context.

The core's style sketch does not replace the expressive system. `voice.md` supplies constructions, an avoid-list, modulation rules, and three register families with nine measured subregisters. Apply the selected register from the first sentence and check the draft against it before sending. Short answers retain the voice; the measured baselines guide calibration, not word or phrase quotas.

Consult the already loaded `references/frameworks.md` for precise concepts and established judgements about particular people, regimes, institutions, or nations, and load relevant files in `references/clusters/` for the subject and register. These files supply substantive material as well as expressive detail; follow the retrieval rules at the bottom of `SKILL.md` rather than treating them as optional refinements based on answer length.

---

## Usage

### As a Claude / Agent Skill

Clone the repository into your skills directory. The repository name already matches the skill name, so `SKILL.md` lands at the root of a correctly named folder:

```bash
git clone https://github.com/ariel-lee-1023/liu-zhongjing-perspective.git \
  ~/.claude/skills/liu-zhongjing-perspective
```

The agent reads the YAML frontmatter in `SKILL.md` to decide when to trigger. Once triggered, it reads the full core, `references/frameworks.md`, and `references/voice.md` before answering, then loads relevant clusters as the question requires.

### As a plain system prompt

Paste the body of `SKILL.md` (everything after the frontmatter) together with the full `references/frameworks.md` and `references/voice.md` as your system prompt. Include relevant cluster material when the question requires it. Do not paste `fidelity-ledger/provenance.md` or `fidelity-ledger/episodic.md` into the prompt — they are metadata about the distillation, and putting them in context degrades the voice.

---

## Design notes

Three constraints shaped this version, and they are worth knowing before you edit it.

**Frameworks are background, not content.** The named models — 秩序輸入/輸出, 費拉化, 末人, 瓦房店化, 民族發明學 — live in `references/frameworks.md` and are deliberately kept *out* of the core. The core carries only the concrete judgements those models produce. The main failure mode of earlier versions was reciting definitions at the reader instead of using them.

**Jargon is modulated by register, not sprayed.** Measured density runs ~13 per 10k characters in the life-advice register versus ~35 in theoretical monologue, and back down to ~17 in the written character studies. Flagship terms (瓦房店化, 末人, 編戶齊民, 做題家) are near-absent when the subject is a person's life — across all 35 character studies: 瓦房店 0, 末人 0, 做題家 2. Piling up jargon is the most common way an imitation goes wrong.

**The registers are the fingerprint, not the averages.** Measured across 3.21M characters of firsthand material, question marks run 4.6 per 10k in the academic-historical register and 38 in the life-advice Q&A; connectives run 0.7 in the classical-Chinese chronicle and 14 in the Q&A; second-person reference runs 3.6% in written prose and 23% in lectures. Any imitation that hits the means but flattens those gaps is not this voice. The full table is in `references/voice.md`.

**Refusals carry the identity.** The section 我不讓步 is the centre of gravity: nine positions the persona holds at a cost — refusing to comfort the bereaved with philosophy, refusing national identity, refusing a way out to someone structurally locked in, refusing to concede that its own system is *correct* rather than merely dominant. A copy that keeps the vocabulary and drops the refusals is not this persona.

**One modulation must survive.** In the face of real grief, the whole analytical machine shuts off: short sentences, plain words, warmth. This is not an inconsistency in the character; it is the single place the character permits.

### Knowledge-base priority & factual cutoff

**the companion knowledge base** https://github.com/ariel-lee-1023/LiuZhongjing-Thoughts (under `content/LZJT/`). Matching material is authoritative and must be used. If nothing matches, the agent stays strictly in character and never admits the gap.

The reasoning posture itself is time-independent. The *facts* are not. Q&A material clusters in 2018–2019; lecture and interview material extends to 2025; the books span 2011–2018. Anything more recent — the last year or two of events, election and conflict outcomes, current policy and market data — is outside the corpus.

Host agents should **retrieve current facts first, then let the persona digest them through its frameworks.** The voice is confident and fond of pronouncement, so this guard matters more here than it would for a neutral assistant.

---

## Provenance and honesty

`fidelity-ledger/provenance.md` is an audit trail rather than documentation: every element in the core is logged with its source cluster, its composite score, and whether it passed the projection and cost gates. It also records what was *demoted* and why. If you fold new material in, extend that ledger — the point of keeping it is that the distillation stays checkable.

Source material was supplied by the commissioning party, who declared the right to use it. The corpus itself is not included in this repository and is excluded by `.gitignore`.

## Contributing

Issues and pull requests are welcome, particularly for: coverage gaps (the female first-person register remains thin), post-2025 fold-ins with fresh source clusters, and translations of the skill into other languages. Please update `CHANGELOG.md` and `fidelity-ledger/provenance.md` alongside any change to `SKILL.md`.

---

## 簡介（繁體中文）

技能顯示名稱為「劉仲敬」，技術識別符保留為 `liu-zhongjing-perspective`。預設以繁體中文輸出；使用者明確要求其他語言或字體時，依其指定範圍切換。

這是一個供 LLM 代理加載的**技能**：以劉仲敬的方式分析歷史、政治、文明、時事、人物乃至具體人生問題——先把問題翻譯成一個關於秩序生產還是消耗、遺傳與階級位置、譜系定位的問題，再冷靜給出結論，且在讀者最想要安慰、認同、出路的地方偏偏不給。

首次以此人格作實質回答前，必須完整讀取 `SKILL.md`、`references/frameworks.md` 與 `references/voice.md`，短答也不例外：核心管整體分析與判斷，框架提供概念定義、推理方法與既有定判，聲音文件管實際寫出的句子。三份文件不依題材或篇幅決定是否載入；已完整保留在上下文中時不必重讀，壓縮後丟失哪份就先補讀哪份。已載入的框架按具體概念與對象查閱，相關簇按題材和語域加載；它們承載具體論述與定判，並非僅供長文潤色。命名框架的定義仍留在框架文件中，不在回答裡機械複述。

**具體事實的覆蓋以 2018–2025 語料為界，更新的事實需由宿主代理先行檢索。

---

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

This license covers the original text in this repository. It does not extend to any referenced source books, which remain the property of their respective copyright holders.

# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **Third cluster merge: `c02-neiya-order` + `c08-premodern-order` → `c02-premodern-order.md`**
  (3,032 + 2,033 → 5,282 est. tokens). Same reasoning skeleton — constitutional position before
  name, order import/export, an armed band plus one bargain — split only by acquisition source
  (the *China Lowland* 29-question appendix vs. the *Scripture and History* essays and lectures).
  `c09-minguo-wenyan` renumbers to `c08-minguo-wenyan`; nine clusters become eight.
- **The register gap in this merge is the widest of the three, and is again not averaged.**
  Group A: 47 question marks per 10k Han characters (corpus maximum). Group B: 4.6 (corpus
  minimum). The head of the file and §eleven both state the two sets separately and forbid
  pooling them.
- Updated references: the load list in `SKILL.md`, five 〔cNN〕 provenance tags in
  `frameworks.md`, the tree in `README.md`, and the cluster pointers in `provenance.md`.
  Batch 4b's `c09`/`c10` are left as the numbering of their time.

### Fixed

- Removed the core-only and answer-length shortcuts from the current loading instructions.
  `SKILL.md` and `references/voice.md` must both be read in full before the first substantive
  persona response, including short answers, and restored if lost through context compaction.
  Aligned the README's English and Chinese guidance, installation and system-prompt usage,
  and the voice module; clarified topic-based framework/cluster retrieval and draft checks.
  Removed the current guidance's “~20% style” claim; historical release notes retain the old design.
- **Removed "狼性" (wolf nature) as a diagnostic label the persona owns.** `c03` and
  `frameworks.md` both closed the Leninist-personality entry with a distiller-written aphorism —
  "that is the truth of 狼性: not strength, but the regression left after the boundary is broken
  through". He never uses the word to name a personality. All ten corpus occurrences are in one
  book: two are his own, and both point at a term already loose in the world ("Huawei's wolf
  culture is the Party's rectification-campaign SM course"); the equation of 狼性 with the
  Leninist personality comes from an **editor-supplied chapter heading**, not from him. Replaced
  with the attested material: the label is something he identifies, not something he uses.
  Three compounding causes are logged in `provenance.md` batch 8 — an editorial-text trap the
  existing source-genre warning did not cover, a correct signature construction ("not X, but Y")
  shielding an unlicensed coinage, and the sentence being quotable enough that a host would lift
  it verbatim. Proposed fix upstream: a Stage 4 gate that counts literal corpus occurrences of
  every term the pack uses as a diagnostic label.
- **`fidelity-ledger/episodic.md` had drifted into a second provenance file.** Against the
  persona-distiller admission test — *could a reader point to it as an event, something that
  happened, was said, or was decided on a specific occasion?* — none of its four sections
  qualified: three were regularities and judgements carrying composite scores, one was a
  disposal note, one was a source-genre warning. All three kinds moved to `provenance.md`
  (batch 6), where they belong. `episodic.md` was rewritten with the admission test and its two
  exclusions (no concepts, no expression) at the head, and now holds only qualifying items.
- The truncated sentence in `episodic.md` §three (subject lost in an earlier manual web edit)
  is restored, in `provenance.md`.
- `SKILL.md` no longer points the host at `episodic.md`. A never-loaded human-facing file has no
  business being named in the embodiment context.

### Known gaps

- `episodic.md` is now short and honestly so. The corpus's concrete incidents are almost all
  already cluster anchors, which the admission test excludes; what remains in scope is the
  "he talks about himself, uncited by any cluster" class, and no dedicated pass has been run
  for it.


## [5.0.0] - 2026-08-15

Nothing new was distilled in this release. Everything here comes from running the assembled
package against live questions and rebuilding what the failures exposed. The measured coverage
this release reports is much worse than the previous two, and the reason is in the method: the
earlier scores were produced on question sets chosen by the distiller.

### Changed — `references/frameworks.md` rebuilt around a method layer (10 sections → 8)

- **New §一 "how to read a question"**, which the package previously had nowhere: false-premise
  diagnosis, the four-step search for the explanatory layer, 格局—路径—节点 plus the
  counterfactual-substitution test, "material is subordinate to the configuration", and the
  read-the-compliment-backwards rule.
- **New §七 "argumentative moves"**, consolidating the opening four-way choice, ventriloquism with
  its density table, the six-step counterfactual baseline, **digression redefined as isomorphic-case
  retrieval** (on topic = another run of the same subsystem, even two millennia and two
  civilisations away; off topic = a different subsystem under the same topic heading, even if every
  document is from the case at hand), and autobiographical material admitted only when it carries
  an argument.
- The old `§史料与记录` section was dissolved and its contents folded into the sections whose
  reasoning they serve. §三 promotes 德性 from a definition to a causal node. Two deliberate
  downgrades paid for the additions: `§个人层面` and `§守先待后` merged into an index of names with
  definitions pointing back to `c01`/`c04`, and island-extrapolation merged with rattlesnake
  lock-in in §二. **No judgement was lost; what was lost is quoted wording recoverable from the
  clusters.** 4,834 → 5,999 est. tokens.
- **No standing-positions library as a separate part.** The recurring concrete judgements are
  inlined as `**定判**：` entries inside the relevant sections, with one 「常备定判」 entry at the
  end of §六.

### Changed — `SKILL.md` compressed, three gates added

Compression only; the structure and all eleven parallel items are intact. 6,480 → 5,997 est.
tokens. Three new gates: the first move on receiving a question is to check whether it presupposes
a freedom of choice the speaker does not have; a pointer into `frameworks.md` §一 for the
configuration/path/node test; and **look up the standing judgement before reasoning about a
concrete object** — if one exists, follow it and do not re-derive on the spot.

### Changed — `references/voice.md`

- **A new prohibition on mid-course signposting**, listed separately from the existing one on
  closing cushions: "我先动一下你这个提法", "讲到这儿我岔一段", "所以回到你的问题". Metadiscourse
  markers measure 0 across the corpus. Forbidding closing cushions does not catch these.
- Four fingerprints added to §一.3 (line-register for ventriloquised speech, pseudo-precision,
  forced concretisation, mid-sentence self-correction); the cutting-down close added to §七; the
  proper-name rule in §四 rewritten as **omnivory** — the old entry listed names that all fell
  inside medieval/Inner-Asian history, which was overfitting, and the only stable rule is "not the
  standard textbook for this question"; the metaphor stock widened from four wells to five with an
  everyday/workplace well.
- Two items were **reclassified out of voice and into framework**: substituting a concrete position
  of interest for a moral judgement, and digression-as-isomorphic-retrieval. Autobiographical
  material likewise belongs to framework.

### Changed — clusters consolidated from ten to nine

- **Merged `c06-figures-written` and `c07-figures-lectures` into a single `c06-figures.md`.**
  The two files cover the same subject — how a person is read: lineage, micro-environment,
  ecological niche, power base, bargain — on the same cast of figures. They were split by source
  batch (written monograph series vs. lecture series), not by subject, and each was among the
  smallest modules in the package (2,138 and 2,177 tokens). The merged module is 4,323 tokens,
  still under the 6,000 ceiling.
- **The merged module keeps the two registers apart rather than averaging them.** A warning at the
  head of the file forbids pooling the statistics: 甲组 (written studies) runs at 6 question marks
  and 3.6% second person per 10k Chinese characters with flagship jargon near zero; 乙组 (lecture
  mode) runs at 14–24 question marks with high second-person density and "对不对？" present. Each
  group is loaded on its own; §十一 states the difference explicitly.
- **Renumbered the modules after the merge**: `c08-nation-invention` → `c07`,
  `c09-premodern-order` → `c08`, `c10-minguo-wenyan` → `c09`. All cross-references updated in
  `SKILL.md`, `references/frameworks.md` (the 〔cNN〕 provenance tags), `fidelity-ledger/episodic.md`
  and `README.md`.

### Fidelity — five live tests, measured coverage 0.22 ± 0.02

The measurement method changed. Batches 1–4 used post-hoc holdout with probes written by the
distiller *after* reading the ground truth, which batch 4b had already logged as the leading
defect. This release used **live tests**: the user supplies a real external question (mostly the
actual questions put to him on a given programme), the package answers first, and the answer is
then scored against his real reply. The ground truth exists independently before the answer is
written, which closes the probe-from-truth channel.

| Round | Domain | Score |
|---|---|---|
| 1 | current affairs + a concrete institution (defence industry, a Poly-group-type object) | 6/18 ≈ 0.33 |
| 2 | birthright citizenship, the Fourteenth Amendment, the retreat from jus soli | 7/20 = 0.35 |
| 3 | why civilisations without a new frontier decay; high-variance populations | 4/20 = 0.20 |
| 4 | the direction of technical progress, longevity and AI, Harari's useless class | 5/23 ≈ 0.22 |
| 5 | Confucius Institutes, overseas united-front work, the logic of agents | 4.5/19 ≈ 0.24 |

**The last three rounds sit at 0.22 ± 0.02 across three unrelated domains.** That stability is the
finding: it rules out "that question was hard" and points at a coverage ceiling. These numbers are
**not** comparable with batch 3's 0.75 or batch 4b's 0.65 — those question sets were chosen by the
distiller and skewed systematically towards historical and structural questions, never once
towards a concrete institution, so both were probably inflated by selection.

**Two metrics had been hidden under one number.** Round 4 read as the best round by eye while
scoring 0.22, essentially level with round 3's 0.20. The reason is that *item coverage* (how many
judgements in the ground truth were hit) and *trunk-hit rate* (whether the main line of the
argument was hit) had been reported as a single figure. Round 4 hit three trunk items, round 3 hit
none. The second metric is the meaningful one and will be reported separately from now on. The
table above is item coverage.

**One distiller attractor logged, not written into the package.** "Rights are exchanged for
military service; universal suffrage arrives with total war" was used twice in five rounds and
appears **zero** times in the corresponding ground truths. On re-checking the corpus it is **half
true**: welfare-as-the-conquering-warrior's-pension and sovereignty-from-force-not-labour are solid
and attested in `c02`, `c09` and the core; the extension to "European suffrage came out of total
mobilisation — you can be conscripted to die, therefore you have a vote" **has no basis in the
corpus** and was added by the distiller. His actual proposition is that those trained by war become
the future rulers, which is reproduction of 德性, not a contractual exchange.

**A defect traced to another persona file — a first for this project.** The session that produced
this release had the user's own `liu-zhongjing-persona` skill loaded, and that skill explicitly
instructs the agent to "pull back to the main thread with 回到刚才的问题" and to say 好了，讲到这里.
Both are mid-course signposts; the corpus has none. The signposting drift observed across all five
rounds traces directly to that instruction, and the new prohibition in `voice.md` §五 exists
because of it.

**Ten method defects are itemised in `fidelity-ledger/provenance.md`** (batch 5, §五), eight
inherited. The two most consequential: no cross-corpus consistency check has ever been run, so a
"ground truth" window may be contradicted elsewhere in his own work; and the question-type
distribution has always been chosen by the distiller and is systematically skewed.

### Known gaps

- **Nothing was re-measured after the changes.** The 0.22 band is the score *before* this
  release's edits. Two consecutive batches now carry unretested changes.
- `SKILL.md`, `frameworks.md` and `voice.md` all sit between 5,996 and 5,999 against a 6,000
  ceiling. All three are at the cap simultaneously: nothing can be added without deleting first.

### Changed — clusters consolidated from twelve to ten

- **Merged `c05-jingxuan-lectures`, `c06-interviews` and `c12-class-instinct` into a single
  `c05-jingxuan-lectures`** ("contemporary application"). The three were one domain split across
  three files by batch accident, not by subject: all three answer a present-day question — a news
  item, a 2020s topic, or something from the reader's own life — by putting it back into a
  structure. `c06` was also the smallest module in the package (1,226 tokens), too thin to justify
  a separate load.
- **The merged module keeps the two registers apart rather than averaging them.** The interview
  material is dialogue (A3: frequent question marks, spoken connectives); the lecture and
  monograph material is monologue (A2). A warning at the head of the file forbids pooling the two
  sets of statistics and points at `voice.md` §八 rows A2/A3.
- **Compressed to fit.** Raw concatenation came to ~7,480 est. tokens, over the 6,000 hard ceiling.
  Cut to **5,993** by tightening quotations and dropping duplicated framing; no judgement, no
  worked example and no quantified claim was removed.
- **Renumbered the rest**: `c07`→`c06`, `c08`→`c07`, `c09`→`c08`, `c10`→`c09`, `c11`→`c10`. Every
  cross-reference was updated — the loading map in `SKILL.md`, the eleven provenance tags in
  `frameworks.md`, the sibling references inside `c07`/`c08`/`c10`, `episodic.md`, and the tree in
  `README.md`. Two internal section pointers into `c05` were re-aimed at their new section numbers.
  Historical batch records in `fidelity-ledger/provenance.md` and in the entries below keep the
  numbering they were written with.

### Added — projection re-test on `c04` and the re-curation it forced

- **Ran a held-out projection test on `c04` (post-hoc variant).** Batch 4 resized three clusters
  without re-running any fidelity gate; this closes that gap for `c04`. Because the module was
  already assembled, the item pool was restricted to Q&A turns from the source book that `c04`
  does **not** use (374 turns → 50 qualifying unused turns after length filters and an 8-gram
  overlap check with OpenCC script normalization), so the answers are provably absent from the
  module. `holdout_split.py --seed 1023 --frac 0.20` masked 10 items. Prediction was done by an
  isolated subagent given only `SKILL.md` + `frameworks.md` + `voice.md` + `c04`, forbidden from
  reading the source corpus. **Score: 13/20 = 0.65** — clears the 0.50 gate, below the 0.70 solid
  line. By domain: order theory and forward projection 6/6, concrete ancient-history structural
  judgements 3/6, out-of-domain (nation-invention / Qing, which belong to `c09`/`c10`) 2/4.
  Full item-by-item scoring in `fidelity-ledger/provenance.md` batch 4b.

### Fixed — three failure modes the test located

- **"Push back" was over-fit into a default reflex.** `c04` §一 opened with "袁 throws a frame,
  刘 pushes it back" plus six push-back techniques, and the blind predictor concluded every
  question must be pushed back — on the one item where 刘 simply agrees ("基本上是这样") the
  prediction inverted his stance. Added a meta-rule: he pushes back on sentiment, hope, universal
  laws and moral frames, not on every question.
- **The "inversion" move was never encoded as callable.** Three of the ten items failed for the
  same reason: the module supplies the mechanism library but never says that each answer should
  land on a point that reverses the questioner's intuition. Added §一 "每答一题，找一次翻转"
  with three attested samples (conquering the oldest civilization is the conqueror's misfortune;
  "the Roman Empire" does not exist as an entity; the biggest losers of the Manchu conquest were
  the tribal elders, not the Ming).
- **Genuinely missing construct: 收割者 / the civilization ceiling.** `c04` had "evolution cannot
  climb back up a slope" but not "bureaucracy and state-building are the most dangerous harvesters
  — the civilization freezes at the height it had when they appeared", nor the 树高根深 inference
  rule. Added to `c04` §三 and defined in `frameworks.md` under 秩序生产与消耗.
- The Machiavellian target-selection meta-rule was already present but buried and unillustrated;
  rewritten as a callable item with its attested example.

### Changed — budget recovery to absorb the additions

- The additions cost ~780 est tokens against a cluster with no headroom, so: 36 long verbatim
  quotes compressed with ellipses, the whole "比喻专名库" section removed (every name in it already
  occurs in place in the body — it was a redundant index), and three duplicated bullets deleted.
  `c04` 6,719 → **5,941** est tokens, still above its 4,457 soft budget and below the 6,000 ceiling.
  `frameworks.md` 4,612 → 4,835.

### Changed — fold-in batch 4: three clusters resized to budget, voice.md re-partitioned by register

- **`c01-ayi-life-advice.md`, `c03-wadi-psychology.md`, and `c04-civilization-theory.md` extended from
  well under the per-cluster soft budget to deliberately *above* soft budget and below the hard ceiling**
  (c01 5,775 · c03 5,888 · c04 5,931 est. tokens; soft budgets ≈4,44x, hard ceiling 6,000). Their source
  books (《阿姨我不想努力了》/《洼地与韭菜》/《文明更迭的源代码》) carry long causal chains rather than
  loose opinion lists, and the budget formula saturates near 4,775 words, which is a conservative lower
  bound for material of this density. The trade-off and its cost (no headroom left for future additions
  without equivalent cuts) are logged in `fidelity-ledger/provenance.md` batch 4.
- **`c04` no longer draws only on 第八章.** Chapters 一–七 are now represented: the Darwinian
  epistemology (孤岛外推／火车头喷蒸汽, 响尾蛇式锁定, 观相术随脉象改药), the attrition model
  (组织资源不可再生, 普遍进步＝既有积累的毁灭, 决断＝分娩, 霸主＝补丁), the seed-bank clauses
  (黑匣子, 拉比阶级的重税, 压缩胶囊), order-as-growth (舞伴默契, 罗马法的阶段截面, 普通法可逆),
  the six-step noun-dismantling template built on 绝对主义, and the nation-state consequences.
- **`frameworks.md` extended with the new named constructs**, each tagged with its home cluster, plus two
  new sections: 个人层面的可投射动作 (c01) and 守先待后的运作条款 (c04). Definitions stay solely in
  frameworks; clusters carry usage only.
- **`voice.md` rewritten around a three-way register partition (BREAKING for anyone quoting the old
  baseline table).** The previous version averaged incommensurable distributions: a single "均值 32–38 汉字"
  across all registers, a "全部著作（9 部）" weighted-average row, and one combined cell for
  《民国纪事本末》＋《数卷残编》. The corpus is now split into **nine mutually exclusive register
  directories** and measured separately with no cross-group weighting. 人物评传 is treated as a
  spoken/written continuum and split per-file at 你/万汉字 < 10; the four oral-Q&A books are also measured
  individually. Headline spreads per 10k 汉字: 你 0.22 → 150.95 (~680×), 连接词 0 → 13.4, hedge 1.4 → 46.5,
  疑问号 4.6 → 38.4, 句长均 28.0 → 46.0.
- **New explicit default rule in both `voice.md` and `SKILL.md`: the persona defaults to register family A
  (oral Q&A, calibrated on 《洼地与韭菜》), switching to C (文言, with 《民国纪事本末》 as the extreme end)
  only on explicit user request and to B (written 评传／史论) only for written-essay tasks.** Registers must
  never be averaged, and rhetorical devices must not be generalized across them.
- **Quantitative guardrails expanded from three to five and split by register family** (second person,
  flagship jargon, hedge floor, connective words as a register switch, sentence length).
- **Measurement caveat logged**: `zh_metrics.py`'s person-percentage columns are unreliable on 文言 (之/其
  are counted as pronouns, producing a spurious 82.2% "first person" for 《民国纪事本末》). Classical-Chinese
  register is now calibrated on absolute per-10k rates only.

### Changed
- **`provenance.md` moved out of `references/` into a new top-level `fidelity-ledger/` folder.**
  `references/` is loaded by the host agent at runtime, so the honesty ledger now lives at
  `fidelity-ledger/provenance.md`, a sibling of `references/` rather than a member of it —
  structurally out of reach during embodiment, not just documented as off-limits. Content
  unchanged; only the path moved. `README.md` updated to point at the new location.
- **`episodic.md` moved out of `references/` into `fidelity-ledger/`, alongside `provenance.md`.**
  Low-scoring but attested corroborating material is not reasoning the host agent should load
  mid-embodiment, so it belongs with the honesty ledger rather than the host-agent-facing package.
  Content unchanged; only the path moved, to `fidelity-ledger/episodic.md`. `SKILL.md` and
  `README.md` (including the repository-layout tree) updated to point at the new location.
- **"Facts and framework handled separately" (事实与框架分开处理) rewritten to name the SOURCE OF
  TRUTH distinction and the no-narration distinction explicitly.** The paragraph already required
  retrieving current external facts before letting the persona digest them, but did not say that
  this is a *different mechanism* from the knowledge-base priority retrieval directly above it
  (which stays inside the LiuZhongjing-Thoughts repository by design), and this repo had no
  existing "don't narrate the retrieval" rule to conflict with, so the paragraph now states the
  distinction on its own terms: 不叙述≠不检索 (not narrating the search is not the same as not doing
  it) — the retrieval itself can never be skipped.

### Added — fold-in batch 3: full knowledge base, distilled under persona-distiller 2.0.0

Re-run against the whole of [LiuZhongjing-Thoughts](https://github.com/ariel-lee-1023/LiuZhongjing-Thoughts) @ `793c4c1` (131 files, 3.21M Chinese characters). The first two batches were built entirely from dialogue and lecture material; this one adds the three genres that were missing, and the two structural pieces persona-distiller 2.0.0 requires.

- **`references/voice.md` — the standing expressive-system module, co-equal with `frameworks.md`.** The core carries at most ~20% style by design, which is enough to *frame* an answer in the voice and not enough to *write* one at length; the rest of the system now has a home. It holds favoured constructions with attested fragments, the **avoid-list** (综上所述, 需要指出的是, 笔者, 客观地说, 总的来说 … — near-zero hits across 3.21M characters, and as diagnostic as the favoured terms), modulation rules as trigger→shift pairs, a seven-row register range, the lexical fingerprint and proper-name inventory, the measured baselines, and anti-drift pairs. The core's loading block now tells host agents to load it before any sustained prose.
- **Six new cluster modules**, covering genres no earlier batch touched: `c07-figures-written` (35 written character studies — the corpus's highest written register), `c08-figures-lectures` (诸夏十大罪人, Kissinger, Zhou Enlai, Chen Jiongming), `c09-nation-invention` (Poland, Czech, Hungary, Italy, Korea; the four-type taxonomy), `c10-premodern-order` (《经与史》《从华夏到中国》, Rome, 河朔三镇, 三星堆, the origin of writing), `c11-minguo-wenyan` (《民国纪事本末》《数卷残编》 — the only classical-Chinese register in the corpus), `c12-class-instinct` (class instinct, upbringing, entertainment, fragility).
- **Seven new elements in the core**, all diagnostic classes, no style padding: two cost-bearing refusals (giving a dead failure neither martyrdom nor betrayal; turning the knife on the writing class *including himself*), five projectible regularities (a record's credibility comes from the conditions of its making; a figure is judged by his net effect on *his own* polity; lineage and micro-environment co-evolve; every regime is a power base plus a bargain; re-feudalisation and the "Holy-Roman-Empire-isation" of public services), and two interactional moves (ironic restatement in the target's own propaganda voice; playing an opponent's first-person monologue before stepping back to judge).
- A Chinese-language `zh_metrics` counterpart to persona-distiller's `style_metrics.py` (the shipped script tokenises on `[A-Za-z]` and returns zeros on this corpus). Every number in `voice.md` comes from an actual run of it.

### Changed
- **Core size is now a computed budget, not a fixed cap.** supply = 6,140 tokens (9 cost-refusals capped at 6, 12 regularities capped at 7, 7 interactional capped at 5, 4 modulation); ceiling 6,500 (large multi-period corpus); the assembled core measures ≈6,141 tokens against a ±10% tolerance. It was ≈4,170 before this batch. Formula, ceiling row, and measured size are recorded in `references/provenance.md`.
- **`references/episodic.md` no longer holds expression or modulation material.** Under 2.0.0 those belong in `voice.md`; the measured style tables, the proper-name inventory, and the demoted expression items moved there. `episodic.md` keeps demoted non-expression elements and the disposal notes.
- `references/frameworks.md` gained the constructs this batch surfaced: the four-type nation-invention taxonomy, 班底与交易, the CCP faction taxonomy (干部党/匪谍系/工运系/梁山系), 逆淘汰定律, 血酬/费厄泼赖, 自守之贼, 水蜘蛛 with 价值界一神论/多神论, micro-environment co-evolution, and the sovereign-less state.
- OCR artefacts inherited from the PDF-converted corpus (口→又 substitutions) normalised in shipped quotations.

### Fidelity
- **Pre-assembly projection gate 0.80** (seed 1023, 5 masked passages from the new clusters, blind-predicted then scored). Two misses shared one cause and forced one re-curation round — which is where "power base plus bargain" entered the core.
- **Stage 5 re-check 0.75** overall (9/12 across 6 items). The added contemporary-affairs item scored 1/2 — direction and most mechanisms hit, the landing ("re-feudalisation") missed — and that miss is why it too is now in the core.
- **Cost/presence assertion: pass.** 11 divergences inventoried, 9 in the final core, 2 logged out with reasons, 0 missing unlogged.
- **Style-match** run on the shipping configuration (core + `voice.md`) across three samples including a contested prompt and an 833-character long-form: `avoid_list_violations = 0`, modulation reproduced, sentence-length delta ≈0.03. Two real deviations surfaced — generated prose under-hedges badly (delta ≈0.53) and over-uses second person in long form — and both are now written into `voice.md` as quantified guard-rails.

### Fixed
- Corrected knowledge-base repository name from `LiuZhongjing-Thought` to the actual repo `LiuZhongjing-Thoughts` (plural) in `SKILL.md`, `README.md`. Host agents can now locate `content/LZJT/` without 404.

### Added
- `.gitignore`, which the 4.1.0 notes listed as delivered but which was never actually present. `README.md` states that the source corpus is excluded by it; until now nothing enforced that, and a `git add -A` run from a directory holding the source books would have published copyrighted material. Ignores source formats (`*.pdf`, `*.epub`, `*.docx`, …), corpus directories, persona-distiller run artifacts, and local agent/editor state.
- Knowledge-base priority retrieval rule: host agents must first search https://github.com/ariel-lee-1023/LiuZhongjing-Thoughts (content/LZJT/) before answering. Matching content is treated as authoritative; absence of a match must never break character or be admitted.

### Changed
- Repository reorganised into the layout required by [persona-distiller](https://github.com/ariel-lee-1023/persona-distiller): `SKILL.md` at the root, reference material under `references/`, and the six source clusters under `references/clusters/` as `c01`–`c06`. Cluster numbering follows the order the core already assigns them in its loading hints. The move itself changed no text.
- On-demand reference loading paths in `SKILL.md` updated to the `references/` layout, superseding the earlier correction to a flat root layout. Path references in `README.md` and the cross-references between cluster files updated to match.
- Repository renamed from `liu-zhongjing` to `liu-zhongjing-perspective`, matching the skill name in the `SKILL.md` frontmatter and the persona-distiller `<slug>-perspective` convention. GitHub redirects the old URL; existing clones should run `git remote set-url origin https://github.com/ariel-lee-1023/liu-zhongjing-perspective.git`.

### Known gaps
- Female first-person register remains thin; the source corpus frames questions from a predominantly male viewpoint.
- Specific facts from roughly the last one to two years are outside the corpus. Host agents must retrieve current facts before the persona reasons over them.

---

## [4.1.0] - 2026-07-23

First public release. Packaged for GitHub with license, changelog, and repository conventions.

### Added
- `interviews.md` cluster listed in the on-demand loading hints in `SKILL.md`; the file shipped with the reference set but was not previously referenced from the core.
- `README.md`, `LICENSE` (MIT), `.gitignore`, and this changelog.

### Changed
- Skill frontmatter `name` set to `liu-zhongjing-perspective` to match the repository and skill directory name (previously `liu-zhongjing-persona-v4`).
- Reference files reorganised into `references/` with cluster files under `references/clusters/`, matching the paths already cited in `SKILL.md`.

---

## [4.1.0-fold.2] - Batch 2 fold-in

Folded in 23 lectures plus 5 topical talks from 《刘仲敬访谈精选》 (2020–2025), narrowing the post-2019 factual gap. Scoring weights unchanged; new material scored on the same scale as existing elements.

### Added
- **Anti-\"new\" recognition move** promoted into the core (composite 0.62): a thing presented as unprecedented is first identified as which recurrence of an old state it is. This is the engine that keeps the persona from fumbling 2020s topics.
- New domains in `jingxuan-lectures.md`: global capitalism and financial empire, cognitive warfare, knowledge and nihilism, ideological genealogy, family and fertility as order structure.

### Changed
- **Capital-flow / global-capitalism placement** promoted from `references/` back into the core (composite 0.61). It had been demoted for overlapping with order input/output; batch 2 supplied independent multi-cluster evidence.
- Post-2019 factual coverage reclassified from \"weak\" to \"partially filled\".

### Fixed
- Off-home-turf projection score upgraded from an estimate of ~0.6 to a measured 0.75, clearing the 0.70 robustness line. The one miss (t19, on the \"useless class\") is what prompted the anti-\"new\" rule to enter the core.

---

## [4.0.0] - Rewrite from v3

A full re-distillation, not an edit. Four failure modes in v3 were targeted directly.

### Changed
- Named frameworks moved out of the core into `references/frameworks.md`. The core now carries only the concrete judgements those frameworks produce, with an explicit instruction not to recite definitions. v3 front-loaded the entire framework set as expository content.
- Jargon rewritten as a register-modulated voice rule backed by measured density (~13 per 10k characters in conversational and life registers, ~35 in theoretical monologue), replacing v3's large glossary, which invited pile-up. Flagship terms now near-absent from the core.
- The core rewritten entirely in the first person and inside the voice. v3 was largely meta-instruction *about* imitating the subject.

### Added
- **Cost-refusal made the highest-priority pass.** Seven positions held at a cost were extracted and made the centre of gravity of the core (`我不让步`), replacing v3's success criteria, which measured only surface style — catchphrases, sentence length, proper-noun density, term frequency.
- The grief modulation: the analytical machine shuts off in the face of real bereavement, with short, plain, warm sentences.
- The recoverable-versus-locked distinction governing \"what should I do\" answers.
- `references/provenance.md` as an honesty ledger, and `references/episodic.md` for measured style figures and demoted evidence.

### Removed
- v3's demonstration answers. They were model-written simulations rather than genuine source material and are excluded from the evidence base; they may serve as application examples but must not be quoted as the subject's own words.

[Unreleased]: https://github.com/ariel-lee-1023/liu-zhongjing-perspective/compare/v4.1.0...HEAD
[4.1.0]: https://github.com/ariel-lee-1023/liu-zhongjing-perspective/releases/tag/v4.1.0

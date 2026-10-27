import {
  BarChart,
  Callout,
  Card,
  CardBody,
  CardHeader,
  CollapsibleSection,
  Grid,
  H1,
  H2,
  H3,
  Link,
  Row,
  Stack,
  Stat,
  Table,
  Text,
  UsageBar,
} from "cursor/canvas";

const QUERY_ID = "6d4459e7-42f4-431d-9e54-68566fed49aa";
const ADO = "https://dev.azure.com/tieto-si/360/_workitems/edit";
const ADO_QUERY = `https://dev.azure.com/tieto-si/360/_queries/query-edit/${QUERY_ID}/`;
const LAST_ADO_CHECK = "18 Aug 2026, 16:51 CET";
const FOUNDATION_EPIC_TITLE = "PnB Baseline for the Danish Market";
const FOUNDATION_EPIC_ID = 434005;
const FOUNDATION_DAYS = "200 days";
const RELEASE_PLANNING_ID = 434336;
const QUERY_ITEM_COUNT = 27;
const PORTFOLIO_COUNT = 25;
const PLACEHOLDER_ID = 429990;
const BUILD_WINDOW_MONTHS = 10;
const TIMELINE_STATUS = "ukendt";
const PLANNING_BAND = "~10 mo (bid assumption)";
const NET_EFFORT_MONTHS = "30–55 months";
const AVG_FTE = "3–6 FTE";
const PEAK_FTE = "6–10 FTE";
const ROADMAP_SOURCE = "Public 360° roadmap PPT (Q1 2026–Q2 2027)";

type RoadmapSummary = {
  status: string;
  count: number;
  meaning: string;
  dgImplication: string;
};

const ROADMAP_SUMMARY: RoadmapSummary[] = [
  {
    status: "A — On roadmap, aligns with KK delivery",
    count: 5,
    meaning: "Existing roadmap item(s) that align well with a credible bid timeline",
    dgImplication: "Reference existing roadmap in bid narrative",
  },
  {
    status: "B — On roadmap, needs acceleration",
    count: 6,
    meaning: "Existing roadmap item(s) that must be delivered faster than currently targeted",
    dgImplication: "Core investment conflict — BRE, search, Flow/servicemål pulled forward",
  },
  {
    status: "C — Off roadmap, strategically relevant",
    count: 11,
    meaning: "New scope not on the roadmap but strategically relevant if we bid",
    dgImplication: "Net-new product bets beyond current roadmap",
  },
  {
    status: "D — Off roadmap, low priority",
    count: 3,
    meaning: "New scope not on the roadmap and would otherwise not be prioritized",
    dgImplication: "Small or hygiene items; low standalone priority",
  },
];

type ClusterBrief = {
  name: string;
  magnitude: string;
  risk: "High" | "Medium" | "Low";
  pfrCount: number;
  effortBand: string;
  gateQuestion: string;
  pfrIds: number[];
};

const CLUSTERS: ClusterBrief[] = [
  {
    name: "Case UX / search / tagging",
    magnitude: "L + M",
    risk: "High",
    pfrCount: 5,
    effortBand: "12–22 months",
    gateQuestion: "Is 435480 (tagging module) in scope or challenged via Q&A?",
    pfrIds: [435480, 435481, 435482, 435483, 435485],
  },
  {
    name: "Process control & templates",
    magnitude: "M + L",
    risk: "Medium",
    pfrCount: 2,
    effortBand: "6–12 months",
    gateQuestion: "Milestone timeline + case templates: config-only or product commits?",
    pfrIds: [435484, 435488],
  },
  {
    name: "BOM + BRE integration",
    magnitude: "L",
    risk: "High",
    pfrCount: 2,
    effortBand: "10–16 months",
    gateQuestion: "B2-03 BRE write-back to BOM — is BRE pilot ready for KK MK?",
    pfrIds: [435486, 435487],
  },
  {
    name: "Servicemål / deadlines",
    magnitude: "XL",
    risk: "High",
    pfrCount: 3,
    effortBand: "12–20 months",
    gateQuestion: "Danish servicemål model + dashboard at Overtagelsesdag — Flow program commit?",
    pfrIds: [434878, 434881, 435490],
  },
  {
    name: "Time registration",
    magnitude: "L",
    risk: "Medium",
    pfrCount: 1,
    effortBand: "4–8 months",
    gateQuestion: "B2-14: reuse eDoc patterns or net-new product work?",
    pfrIds: [435491],
  },
  {
    name: "FilArkiv archive",
    magnitude: "L",
    risk: "Medium",
    pfrCount: 1,
    effortBand: "6–12 months",
    gateQuestion: "P&B → FilArkiv merge project — in bid baseline?",
    pfrIds: [435489],
  },
  {
    name: "Integration spine",
    magnitude: "XL + L + M",
    risk: "High",
    pfrCount: 7,
    effortBand: "18–32 months",
    gateQuestion: "All nine grunddata registers live at Overtagelsesdag? Options (435502/435503) in baseline?",
    pfrIds: [435495, 435496, 435497, 435498, 435499, 435502, 435503],
  },
  {
    name: "Security / logging / SIEM",
    magnitude: "L",
    risk: "High",
    pfrCount: 3,
    effortBand: "6–12 months",
    gateQuestion: "LogPoint + log integrity: build, partner, or no-bid?",
    pfrIds: [434352, 435493, 435501],
  },
  {
    name: "Point fix",
    magnitude: "S",
    risk: "Low",
    pfrCount: 1,
    effortBand: "<1 month",
    gateQuestion: "Low risk — include in baseline bid narrative.",
    pfrIds: [435492],
  },
];

const TEAM_ROLLUP: { team: string; modules: string; pfrs: number; xl: number; fteBand: string }[] = [
  { team: "Plan & Build / Process Platform", modules: "Flow, servicemål, BOM, templates, process control", pfrs: 8, xl: 2, fteBand: "3–5 FTE" },
  { team: "Core Integration", modules: "BOM, grunddata, deep links, Digital Post, debtor, AI Assist", pfrs: 7, xl: 1, fteBand: "2–4 FTE" },
  { team: "Core UI / Search", modules: "Search, tagging, case UX", pfrs: 4, xl: 0, fteBand: "1–3 FTE" },
  { team: "Tech Platform / CloudOps", modules: "Logs, SIEM, data delimitation", pfrs: 3, xl: 0, fteBand: "1–2 FTE" },
  { team: "Core BL / Archive", modules: "FilArkiv, time registration", pfrs: 2, xl: 0, fteBand: "1–2 FTE" },
];

const DECISION_PATHS = [
  {
    title: "A — Strategic yes (market + product merge)",
    body: "Yes to Q1 and Q2: approve epic #434005 (200 man-days, Approach 1 — P&B as P360 module on Flow). Bid KK with foundation + managed PFR delta. Accept 30–55 months tender effort on top. Propose credible implementation plan (4.1.1) and staff 3–6 FTE average (6–10 FTE peak). Proceed with release planning (#434336).",
  },
  {
    title: "B — Market yes, product narrow",
    body: "Yes to Q1, no or partial on Q2: bid with Approach 2 (141 days) or eDoc/Flow-heavy story without full P&B merge. Challenge SIEM, tagging, and log integrity via ordregiver Q&A. Weaker on full byggesag portfolio.",
  },
  {
    title: "C — No-bid or low-effort",
    body: "No to Q1: decline KK or minimal compliance. Defer Danish P&B module; continue eDoc migration track (#376382) only.",
  },
];

const FOUNDATION_BREAKDOWN: { block: string; days: number; contents: string }[] = [
  { block: "Integrations", days: 77, contents: "BOM (15), fee (8), BBR (10), FilArkiv (10), GIS conflict (15), GIS neighbor (15), GIS localization (4)" },
  { block: "Process models", days: 40, contents: "360 Flow process modelling basis" },
  { block: "UI & database", days: 53, contents: "P&B case types — BIF + FIB + DB" },
  { block: "Testing", days: 30, contents: "Six case-type families (building, supervision, illegality, complaint, estate dividing, request)" },
];

const QUERY_PORTFOLIO: { id: number; layer: string; note: string }[] = [
  { id: 434005, layer: "Foundation epic", note: "PnB Baseline — 200 days; not counted in PFR delta" },
  { id: 429990, layer: "Placeholder", note: "Suggestion for Improvement — exclude from gate" },
  { id: 434352, layer: "Tender PFR delta", note: "Data delimitation" },
  { id: 434878, layer: "Tender PFR delta", note: "Servicemålstid — superseded by 435490" },
  { id: 434881, layer: "Tender PFR delta", note: "Sagsbehandlingstid — superseded by 435490" },
  { id: 435480, layer: "Tender PFR delta", note: "Tagging" },
  { id: 435481, layer: "Tender PFR delta", note: "Conflict resolution" },
  { id: 435482, layer: "Tender PFR delta", note: "Journalisation" },
  { id: 435483, layer: "Tender PFR delta", note: "Search / export" },
  { id: 435484, layer: "Tender PFR delta", note: "Process control" },
  { id: 435485, layer: "Tender PFR delta", note: "Handling received information" },
  { id: 435486, layer: "Tender PFR delta", note: "BRE write-back to BOM" },
  { id: 435487, layer: "Tender PFR delta", note: "BOM search criteria" },
  { id: 435488, layer: "Tender PFR delta", note: "Case templates" },
  { id: 435489, layer: "Tender PFR delta", note: "FilArkiv transfer" },
  { id: 435490, layer: "Tender PFR delta", note: "Servicemål consolidated (B2-12+)" },
  { id: 435491, layer: "Tender PFR delta", note: "Time registration" },
  { id: 435492, layer: "Tender PFR delta", note: "Error texts" },
  { id: 435493, layer: "Tender PFR delta", note: "Log integrity — Not met" },
  { id: 435495, layer: "Tender PFR delta", note: "Integration landscape" },
  { id: 435496, layer: "Tender PFR delta", note: "Grunddata registers" },
  { id: 435497, layer: "Tender PFR delta", note: "Deep links" },
  { id: 435498, layer: "Tender PFR delta", note: "Remote print SF1601" },
  { id: 435499, layer: "Tender PFR delta", note: "MeMo Digital Post — Not met" },
  { id: 435501, layer: "Tender PFR delta", note: "SIEM LogPoint — Not met" },
  { id: 435502, layer: "Tender PFR delta", note: "Debtor system (option)" },
  { id: 435503, layer: "Tender PFR delta", note: "AI Assist (option)" },
];

const STRATEGIC_QUESTIONS = [
  { q: "Q1 — Danish market", body: "Commit to Denmark with KK as beachhead? LT decision awaited via #434336 by end Aug 2026." },
  { q: "Q2 — P&B → P360 module", body: "Approve Approach 1 in epic #434005 (200 man-days): merge P&B into Public 360° on 360 Flow, including fee, GIS, BOM, FilArkiv." },
  { q: "Q3 — Tender PFR delta", body: "Given yes/yes: which of the 25 query PFRs are in bid baseline vs Q&A narrow? SIEM (435501), tagging (435480), servicemål polish." },
];

type ClusterScan = {
  cluster: string;
  lead: string;
  gapStance: string;
  complexity: string;
  magnitude: string;
  risk: string;
  gateNote: string;
  signOff: string;
};

const CLUSTER_SCANS: ClusterScan[] = [
  {
    cluster: "Case UX / search / tagging",
    lead: "Bjørn Henrik / Anita / Arve",
    gapStance: "3 Partial (435480/482/483/485/481), 2 TBD",
    complexity: "Tagging now partly met in tool (435480); search/export rated partial; conflict resolution partial",
    magnitude: "L + M · 12–22 months",
    risk: "High — 435480 still evaluation-weighted despite partial rating",
    gateNote: "435480 downgraded to Partial in tender tool — confirm commitment wording vs Q&A.",
    signOff: "Pending — Core UI + P&B leads",
  },
  {
    cluster: "Servicemål / deadlines",
    lead: "Bjørn Henrik / Morten",
    gapStance: "1 Partial consolidated PFR (435490), 2 Partial overlap (434878/434881)",
    complexity: "435490 now bundles B2-12 + 5.2.11.2 + 5.2.11.3 + 5.2.16.3; overlaps child #434006",
    magnitude: "XL · 12–20 months",
    risk: "High — MK minimum B2-12",
    gateNote: "Dedupe 434878/434881 into consolidated 435490 before commitment wording.",
    signOff: "Pending — Plan & Build program owner",
  },
  {
    cluster: "Security / logging / SIEM",
    lead: "Jarle / CloudOps",
    gapStance: "2 Not met (435493, 435501), 1 Partial (434352)",
    complexity: "LogPoint delivery + manual log deletion not supported; data delimitation partly met",
    magnitude: "L · 6–12 months",
    risk: "High — explicit MK blockers",
    gateNote: "435501 and 435493 both rated Not able to meet in tender tool.",
    signOff: "Pending — Tech Platform + CloudOps",
  },
  {
    cluster: "Integration spine",
    lead: "Olga / Jarle / Morten",
    gapStance: "1 Not met (435499 MeMo), 5 Partial, 1 TBD (435497)",
    complexity: "B2-18 landscape; grunddata partial; options 435502/435503 partial; MeMo Not met",
    magnitude: "XL + L + M · 18–32 months",
    risk: "High — 435499 regression + integration breadth",
    gateNote: "435499 MeMo rated Not met — was in flight; 435496/435497 still need assignee.",
    signOff: "Pending — Core Integration",
  },
  {
    cluster: "BOM + BRE integration",
    lead: "Arve / Claus",
    gapStance: "2 Partial — B2-03 MK Verify",
    complexity: "Business-rule triggered BOM write-back; BOM searchable metadata",
    magnitude: "L · 10–16 months",
    risk: "High — MK minimum on B2-03",
    gateNote: "435486 depends on BRE pilot maturity (~55% per BRE assessment).",
    signOff: "Pending — BRE + BOM integration leads",
  },
  {
    cluster: "FilArkiv archive",
    lead: "Arve / Axel",
    gapStance: "Partial — merge project noted in tool",
    complexity: "Decision Panel, protected person warning, per-document transfer status",
    magnitude: "L · 6–12 months",
    risk: "Medium — P&B specific",
    gateNote: "435489 bundles 5 requirement IDs; confirm eDoc/FilArkiv baseline.",
    signOff: "Pending — Archive lead",
  },
  {
    cluster: "Process control & templates",
    lead: "Morten / Axel / Jarle",
    gapStance: "2 Partial",
    complexity: "Milestone timeline, mandatory steps, validation warnings, case templates",
    magnitude: "M + L · 6–12 months",
    risk: "Medium",
    gateNote: "435484 spans three requirement sections — confirm MK vs IK mix.",
    signOff: "Pending — Flow + P&B",
  },
  {
    cluster: "Time registration",
    lead: "Bjørn Henrik",
    gapStance: "TBD — check eDoc (435491 unassigned in tool)",
    complexity: "B2-14 MK + five 5.2.17.x sub-requirements",
    magnitude: "L · 4–8 months",
    risk: "Medium",
    gateNote: "Distinct from servicemål days — do not conflate with 435490.",
    signOff: "Pending — P&B",
  },
  {
    cluster: "Point fix",
    lead: "Morten",
    gapStance: "Partial (IK)",
    complexity: "Configurable error texts — admin/config scope",
    magnitude: "S · <1 month",
    risk: "Low",
    gateNote: "Include in baseline; no gate blocker.",
    signOff: "Pending — confirm IK-only",
  },
];

export default function KkManagementGate() {
  const highRiskClusters = CLUSTERS.filter((c) => c.risk === "High").length;
  const totalPfrs = CLUSTERS.reduce((n, c) => n + c.pfrIds.length, 0);

  const queryPortfolioRows = QUERY_PORTFOLIO.map((item) => [
    <Link href={`${ADO}/${item.id}`}>{item.id}</Link>,
    item.layer,
    item.note,
  ]);

  const gapSegments = [
    { id: "not-met", value: 3, color: "red" as const },
    { id: "partial", value: 19, color: "orange" as const },
    { id: "in-flight", value: 1, color: "green" as const },
    { id: "tbd", value: 2, color: "gray" as const },
  ];

  const roadmapSegments = [
    { id: "a-aligns", value: 5, color: "green" as const },
    { id: "b-accelerate", value: 6, color: "orange" as const },
    { id: "c-strategic", value: 11, color: "red" as const },
    { id: "d-low", value: 3, color: "gray" as const },
  ];

  const roadmapRows = ROADMAP_SUMMARY.map((r) => [r.status, String(r.count), r.meaning, r.dgImplication]);

  const clusterRows = CLUSTERS.map((c) => [
    c.name,
    c.pfrIds.length,
    c.magnitude,
    c.effortBand,
    c.risk,
    c.gateQuestion,
    c.pfrIds.join(", "),
  ]);

  const teamRows = TEAM_ROLLUP.map((t) => [t.team, String(t.pfrs), t.fteBand, String(t.xl), t.modules]);

  const scanRows = CLUSTER_SCANS.map((s) => [s.cluster, s.lead, s.gapStance, s.magnitude, s.risk, s.gateNote, s.signOff]);

  return (
    <Stack gap={24} style={{ padding: 20, maxWidth: 1100 }}>
      <Stack gap={8}>
        <H1>Københavns Kommune — management go/no-go brief</H1>
        <Text tone="secondary">
          Decision gate prep · ADO query{" "}
          <Link href={ADO_QUERY}>{QUERY_ITEM_COUNT} items</Link> ({PORTFOLIO_COUNT} PFR delta + foundation #{FOUNDATION_EPIC_ID} + placeholder #{PLACEHOLDER_ID}) · verified {LAST_ADO_CHECK}
        </Text>
      </Stack>

      <Grid columns={5} gap={12}>
        <Stat value={FOUNDATION_DAYS} label="Foundation epic #434005" tone="warning" />
        <Stat value={String(QUERY_ITEM_COUNT)} label="ADO query items" />
        <Stat value={String(totalPfrs)} label="Tender PFR delta (in clusters)" />
        <Stat value={NET_EFFORT_MONTHS} label="PFR delta only (excl. 200 d foundation)" tone="warning" />
        <Stat value={AVG_FTE} label={`Avg team · ${BUILD_WINDOW_MONTHS} mo window`} tone="warning" />
        <Stat value={TIMELINE_STATUS} label="Go-live in tender (Timeline sheet)" tone="warning" />
        <Stat value={PLANNING_BAND} label={`Internal planning · ${BUILD_WINDOW_MONTHS} mo band`} />
      </Grid>

      <Grid columns={3} gap={12}>
        {STRATEGIC_QUESTIONS.map((item) => (
          <Callout key={item.q} tone="info" title={item.q}>
            {item.body}
          </Callout>
        ))}
      </Grid>

      <Callout tone="danger" title="Primary gate questions (Q1 + Q2)">
        (1) Open the Danish market with KK as beachhead? (2) Approve P&B → Public 360° module merge — epic{" "}
        <Link href={`${ADO}/${FOUNDATION_EPIC_ID}`}>#{FOUNDATION_EPIC_ID}</Link> ({FOUNDATION_DAYS}, Approach 1)?
      </Callout>

      <Callout tone="warning" title="Tactical bid blockers (Q3 — only if yes/yes)">
        SIEM LogPoint (<Link href={`${ADO}/435501`}>435501</Link>), log integrity (<Link href={`${ADO}/435493`}>435493</Link>), MeMo Digital Post (<Link href={`${ADO}/435499`}>435499</Link>). Tagging (<Link href={`${ADO}/435480`}>435480</Link>) now Partial in tool — confirm commitment. Servicemål (<Link href={`${ADO}/435490`}>435490</Link>) consolidates 434878/434881; overlaps foundation child #434006.
      </Callout>

      <Card>
        <CardHeader>
          Foundation investment — Epic #{FOUNDATION_EPIC_ID} ({FOUNDATION_DAYS}) · {FOUNDATION_EPIC_TITLE}
        </CardHeader>
        <CardBody>
          <Text size="small" style={{ marginBottom: 10 }}>
            ADO title: Copenhagen Bid - Master Commitment – {FOUNDATION_EPIC_TITLE}. Assigned Bjørn Henrik · Impacted Module Plan&amp;Build · Effort 200. Child #434006 (servicemål/deadlines). Related #434009 (time registration). Release planning{" "}
            <Link href={`${ADO}/${RELEASE_PLANNING_ID}`}>#{RELEASE_PLANNING_ID}</Link> awaiting LT decision end Aug 2026.
          </Text>
          <Table
            headers={["Block", "Days", "Contents"]}
            rows={FOUNDATION_BREAKDOWN.map((r) => [r.block, String(r.days), r.contents])}
            striped
          />
          <Text tone="tertiary" size="small" style={{ marginTop: 10 }}>
            Total 200 man-days (Approach 1). Approach 2 (P&B subset on P360 DAN) = 141 days. Several query PFRs map to foundation scope; SIEM/tagging are tender delta only.
          </Text>
        </CardBody>
      </Card>

      <Callout tone="info" title="Implementation timeline — no fixed go-live">
        Tender Timeline sheet: award and go-live both <strong>{TIMELINE_STATUS}</strong>. Supplier proposes Overtagelsesdag in bid (4.1.1 Implementeringsplan, 15% weight; Bilag 1 §5.1). Penalties bind to our proposed plan. Freeze: all July, 24 Dec–1 Jan. Driftsprøve: 30 days after Overtagelsesprøve. Koncern IT risk review: up to 3 months.
      </Callout>

      <Callout tone="warning" title="Team size vs bid timeline">
        Internal planning band: ~{BUILD_WINDOW_MONTHS} months from award (assumption only — not a tender commitment). **30–55 months is PFR delta only** — foundation ({FOUNDATION_DAYS}) is separate (~10 person-months). Some PFRs overlap foundation scope (BOM, FilArkiv, servicemål). Program needs {AVG_FTE} sustained, {PEAK_FTE} peak when integration spine and servicemål run together.
      </Callout>

      <Callout tone="info" title="ADO portfolio check">
        Verified {LAST_ADO_CHECK}: query returns 27 items (25 PFR delta + #434005 foundation + #429990 placeholder). All PFRs New. Impacted Module unset on 22/25 PFRs (only 434352/434878/434881 = Plan&amp;Build).
      </Callout>

      <Grid columns={3} gap={12}>
        {DECISION_PATHS.map((path) => (
          <Card key={path.title}>
            <CardHeader>{path.title}</CardHeader>
            <CardBody>
              <Text size="small">{path.body}</Text>
            </CardBody>
          </Card>
        ))}
      </Grid>

      <Card>
        <CardHeader>Portfolio gap profile ({PORTFOLIO_COUNT} Features)</CardHeader>
        <CardBody>
          <UsageBar
            total={25}
            topLeftLabel="Tender-tool gap ratings"
            topRightLabel="3 Not met · 19 Partial · 1 In flight · 2 TBD"
            segments={gapSegments}
          />
          <Text tone="tertiary" size="small" style={{ marginTop: 10 }}>
            Source: KK Tender tool internal ratings. TBD = not yet rated in tool (most IK/MK Verify items).
          </Text>
        </CardBody>
      </Card>

      <Card>
        <CardHeader>Roadmap alignment vs KK delivery ({PORTFOLIO_COUNT} Features)</CardHeader>
        <CardBody>
          <UsageBar
            total={25}
            topLeftLabel={ROADMAP_SOURCE}
            topRightLabel="A 5 · B 6 · C 11 · D 3"
            segments={roadmapSegments}
          />
          <Table
            headers={["Status", "PFRs", "Meaning", "DG implication"]}
            rows={roadmapRows}
            rowTone={["success", "warning", "danger", "neutral"]}
            striped
            style={{ marginTop: 12 }}
          />
          <Text tone="tertiary" size="small" style={{ marginTop: 10 }}>
            ~24% on roadmap but needs acceleration (B). ~44% strategically relevant but not on roadmap (C). Cluster-owner validation pending.
          </Text>
        </CardBody>
      </Card>

      <CollapsibleSection title={`ADO query portfolio — all ${QUERY_ITEM_COUNT} items`} defaultOpen>
        <Text size="small" tone="secondary" style={{ marginBottom: 8 }}>
          Query returns {QUERY_ITEM_COUNT} work items. Gate analysis covers {PORTFOLIO_COUNT} tender PFRs plus foundation epic #{FOUNDATION_EPIC_ID} ({FOUNDATION_DAYS}). #{PLACEHOLDER_ID} excluded.
        </Text>
        <Table
          headers={["ID", "Layer", "Note"]}
          rows={queryPortfolioRows}
          rowTone={QUERY_PORTFOLIO.map((item) =>
            item.layer === "Tender PFR delta" ? "warning" : item.layer === "Foundation epic" ? "danger" : "neutral",
          )}
          striped
          stickyHeader
        />
      </CollapsibleSection>

      <Stack gap={10}>
        <H2>Commitment clusters — complexity, magnitude, risk ({totalPfrs} PFRs)</H2>
        <Table
          headers={["Cluster", "PFRs", "Size", "Effort (months)", "Risk", "Gate question", "IDs"]}
          rows={clusterRows}
          rowTone={CLUSTERS.map((c) => (c.risk === "High" ? "danger" : c.risk === "Medium" ? "warning" : "success"))}
          striped
          stickyHeader
        />
      </Stack>

      <Grid columns={2} gap={16}>
        <Stack gap={8}>
          <H3>PFR count by magnitude tier</H3>
          <BarChart
            categories={["XL", "L", "M", "S"]}
            series={[{ name: "PFRs", data: [3, 10, 11, 1], tone: "warning" }]}
            showValues
            height={160}
          />
        </Stack>
        <Stack gap={8}>
          <H3>High-risk cluster share</H3>
          <BarChart
            categories={["High risk", "Other clusters"]}
            series={[{ name: "Clusters", data: [highRiskClusters, CLUSTERS.length - highRiskClusters], tone: "danger" }]}
            showValues
            height={160}
          />
        </Stack>
      </Grid>

      <Stack gap={10}>
        <H3>Roadmap alignment share</H3>
        <Table
          headers={["Status", "PFRs"]}
          rows={ROADMAP_SUMMARY.map((r) => [r.status, String(r.count)])}
          rowTone={["success", "warning", "danger", "neutral"]}
          striped
        />
        <BarChart
          horizontal
          categories={["A · Aligns", "B · Accelerate", "C · Strategic", "D · Low priority"]}
          series={[{ name: "PFRs", data: ROADMAP_SUMMARY.map((r) => r.count), tone: "warning" }]}
          showValues
          height={220}
        />
        <Text tone="tertiary" size="small">
          KK pulls BRE, search, and Flow/servicemål forward and adds SIEM, tagging, and archive scope not on the roadmap.
        </Text>
      </Stack>

      <CollapsibleSection title="Cluster light scans — owner sign-off (pre-meeting)" defaultOpen>
        <Table
          headers={["Cluster", "Lead", "Gap stance", "Magnitude", "Risk", "Gate note", "Sign-off"]}
          rows={scanRows}
          striped
          stickyHeader
        />
      </CollapsibleSection>

      <CollapsibleSection title="Product team demand rollup" defaultOpen={false}>
        <Table headers={["Team", "PFRs", "FTE band (10 mo)", "XL", "Modules"]} rows={teamRows} striped />
        <Text tone="tertiary" size="small" style={{ marginTop: 8 }}>
          Bands overlap — not additive headcount. Plan & Build + Integration dominate peak load.
        </Text>
      </CollapsibleSection>

      <Row gap={12}>
        <Link href={`${ADO}/${FOUNDATION_EPIC_ID}`}>Foundation epic #{FOUNDATION_EPIC_ID}</Link>
        <Link href={`${ADO}/${RELEASE_PLANNING_ID}`}>Release planning #{RELEASE_PLANNING_ID}</Link>
        <Link href={`${ADO}/435501`}>SIEM blocker 435501</Link>
        <Link href="/docs/tender-reference/KK-management-gate-brief.md">Markdown brief</Link>
      </Row>
    </Stack>
  );
}

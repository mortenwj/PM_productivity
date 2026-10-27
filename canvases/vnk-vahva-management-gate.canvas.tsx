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

const PARENT_ID = 436815;
const ADO = "https://dev.azure.com/tieto-si/360/_workitems/edit";
const LAST_ADO_CHECK = "4 Sep 2026, 00:10 CET";
const PORTFOLIO_COUNT = 9;
const LINKED_COUNT = 8;
const ORPHAN_ID = 430291;
const TENDER_FUNCTIONAL_REQS = 487;
const TENDER_MANDATORY = 416;
const BUILD_WINDOW_MONTHS = 18;
const NET_EFFORT_MONTHS = "55–90 months";
const FULL_TENDER_EFFORT = "120–200+ months";
const AVG_FTE = "4–6 FTE";
const PEAK_FTE = "8–12 FTE";
const ROADMAP_SOURCE = "Public 360° roadmap PPT (Q1 2026–Q2 2027)";
const TIMELINE_STATUS = "Supplier proposes (PoC → Rakentamisvaihe 1)";

type RoadmapSummary = {
  status: string;
  count: number;
  meaning: string;
  dgImplication: string;
};

const ROADMAP_SUMMARY: RoadmapSummary[] = [
  {
    status: "A — On roadmap, aligns with VN Asia delivery",
    count: 1,
    meaning: "Existing roadmap item(s) that align well with expected delivery",
    dgImplication: "Reference existing roadmap in PoC / bid narrative",
  },
  {
    status: "B — On roadmap, needs acceleration",
    count: 4,
    meaning: "Existing roadmap item(s) that must be delivered faster than currently targeted",
    dgImplication: "Core investment conflict — metadata, mass ops, search, templates",
  },
  {
    status: "C — Off roadmap, strategically relevant",
    count: 4,
    meaning: "New scope not on the roadmap but strategically relevant if we bid",
    dgImplication: "Net-new bets — especially API-first (#437273)",
  },
  {
    status: "D — Off roadmap, low priority",
    count: 0,
    meaning: "New scope not on the roadmap and would otherwise not be prioritized",
    dgImplication: "—",
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
    name: "API / integration platform",
    magnitude: "XL",
    risk: "High",
    pfrCount: 1,
    effortBand: "35–55 months",
    gateQuestion: "Is #437273 (API-first / new SIF) in or out?",
    pfrIds: [437273],
  },
  {
    name: "Metadata / TOS",
    magnitude: "L",
    risk: "High",
    pfrCount: 1,
    effortBand: "12–22 months",
    gateQuestion: "Does #430281 cover F-section (111 reqs) or only RFI subset?",
    pfrIds: [430281],
  },
  {
    name: "Mass operations",
    magnitude: "L",
    risk: "Medium",
    pfrCount: 1,
    effortBand: "8–14 months",
    gateQuestion: "Mass metadata + bulk export — product commit or services?",
    pfrIds: [433271],
  },
  {
    name: "Search / FFUI",
    magnitude: "L",
    risk: "Medium",
    pfrCount: 1,
    effortBand: "8–14 months",
    gateQuestion: "Single wildcard + cross-org saved-search share?",
    pfrIds: [434693],
  },
  {
    name: "Dispatch / notifications",
    magnitude: "L + M",
    risk: "Medium",
    pfrCount: 3,
    effortBand: "10–18 months",
    gateQuestion: "Redispatch model + merge #430291 / #432904?",
    pfrIds: [430271, 432904, 430291],
  },
  {
    name: "Templates / document UX",
    magnitude: "M",
    risk: "Low",
    pfrCount: 1,
    effortBand: "3–6 months",
    gateQuestion: "FI subsetup template filter — config-only sufficient?",
    pfrIds: [433354],
  },
  {
    name: "Archiving / disposal",
    magnitude: "M",
    risk: "Medium",
    pfrCount: 1,
    effortBand: "4–8 months",
    gateQuestion: "Generic draft disposal vs FI-only customization?",
    pfrIds: [433356],
  },
];

const TEAM_ROLLUP: { team: string; modules: string; pfrs: number; xl: number; fteBand: string }[] = [
  { team: "Core Integration / API", modules: "SIF, NG API, webhooks, SIEM, async jobs", pfrs: 1, xl: 1, fteBand: "3–5 FTE" },
  { team: "Core BL / metadata", modules: "Custom fields, TOS, inheritance, infosec warnings", pfrs: 2, xl: 0, fteBand: "2–4 FTE" },
  { team: "Core UI / Search", modules: "Search, FFUI, templates", pfrs: 2, xl: 0, fteBand: "2–3 FTE" },
  { team: "Dispatch / Office", modules: "Dispatch, notifications, Outlook", pfrs: 3, xl: 0, fteBand: "1–3 FTE" },
  { team: "Archive / retention", modules: "Draft disposal, retention", pfrs: 1, xl: 0, fteBand: "1–2 FTE" },
];

const DECISION_PATHS = [
  {
    title: "A — Strategic bid",
    body: "Yes to Q1+Q2: commit to API-first (#437273) and deliver 9 PFRs through PoC → Rakentamisvaihe 1. Accept 55–90 months PFR effort; staff 4–6 FTE avg (8–12 peak). Register PFRs for Suomi.fi, eIDAS, multi-org before final tender.",
  },
  {
    title: "B — Bid with Q&A / PoC narrow",
    body: "Negotiate; prove standard product on PoC subset. Challenge API breadth, eIDAS, Suomi.fi via Q&A. Phase #437273. Merge #430291 into #432904. Disclose Product Backlog per Liite 3.1.",
  },
  {
    title: "C — No-bid or low-effort",
    body: "Decline or minimal compliance if API spine and mandatory A15/C21 cannot be credibly committed before final tarjouspyyntö.",
  },
];

const UNREGISTERED_GAPS = [
  { domain: "Suomi.fi (A15 Pakollinen)", refs: "A15", pfr: "—", risk: "High" },
  { domain: "eIDAS advanced signing", refs: "C21, C27", pfr: "—", risk: "High" },
  { domain: "Multi-org case model", refs: "A2–A7, A36", pfr: "—", risk: "High" },
  { domain: "Workflow / process engine", refs: "D, P", pfr: "—", risk: "Medium" },
  { domain: "Security matrix", refs: "Liite 2.6", pfr: "—", risk: "High" },
  { domain: "Hierarchical picklists", refs: "F16–F17", pfr: "Slide 14", risk: "Medium" },
  { domain: "Full Flex UI documents", refs: "—", pfr: "Slide 14", risk: "Medium" },
];

const TENDER_SECTIONS = [
  { sec: "A", name: "Case mgmt (multi-org)", reqs: 36 },
  { sec: "B", name: "Documents", reqs: 89 },
  { sec: "C", name: "eIDAS signing", reqs: 27 },
  { sec: "D", name: "Workflows", reqs: 16 },
  { sec: "E", name: "Dispatch / notify", reqs: 65 },
  { sec: "F", name: "Metadata / TOS", reqs: 111 },
  { sec: "G–P", name: "Archive, search, admin…", reqs: 143 },
];

const STRATEGIC_QUESTIONS = [
  { q: "Q1 — Finnish government market", body: "Commit to VN Asia (VNK + Valtori)? TLIV, Katakri PoC audit, SÄHKE2, EU/NATO segregation." },
  { q: "Q2 — API-first platform", body: "Approve #437273 as integration spine (REST, webhooks, SIEM, Elasticsearch) — not a single Feature." },
  { q: "Q3 — RFI PFR delta + unregistered", body: "Given yes/yes: which of 9 PFRs + 7 unregistered domains are in baseline vs PoC backlog?" },
];

const PORTFOLIO_ROWS: { id: number; link: string; title: string; note: string }[] = [
  { id: 437273, link: "Related", title: "360° API requirements", note: "Post–Innovation Board; XL" },
  { id: 430281, link: "Related", title: "Metadata requirements", note: "F-section partial" },
  { id: 433271, link: "Related", title: "Mass functions", note: "B/E mass ops" },
  { id: 434693, link: "Related", title: "Search enhancements", note: "I-section partial" },
  { id: 430271, link: "Related", title: "Enhanced dispatch", note: "Redispatch model" },
  { id: 432904, link: "Related", title: "Email notifications", note: "Metadata in subject/body" },
  { id: 430291, link: "Orphan", title: "Email configurability", note: "Not on epic — overlaps #432904" },
  { id: 433354, link: "Child", title: "Template filtering FI/SV", note: "Only formal child" },
  { id: 433356, link: "Related", title: "Draft file disposal", note: "B66 / H" },
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
    cluster: "API / integration platform",
    lead: "Mika / Tero / Integration",
    gapStance: "1 Partial (#437273)",
    complexity: "API-first, webhooks, async, SIEM, ES — >> current SIF",
    magnitude: "XL · 35–55 months",
    risk: "High — primary gate question",
    gateNote: "FI API brief delivered summer 2026; not in Innovation Board deck.",
    signOff: "Pending — Core Integration",
  },
  {
    cluster: "Metadata / TOS",
    lead: "Willy Koch",
    gapStance: "1 Partial (#430281)",
    complexity: "FI/SV/EN fields, length, inheritance; infosec warning on record-type change",
    magnitude: "L · 12–22 months",
    risk: "High — F-section has 111 reqs",
    gateNote: "B50/F21 overlap with slide 9 infosec story — bid blocker if silent.",
    signOff: "Pending — Core BL",
  },
  {
    cluster: "Dispatch / notifications",
    lead: "Olga / Jarle",
    gapStance: "3 Partial; orphan #430291",
    complexity: "Redispatch as new doc; configurable notification metadata",
    magnitude: "L+M · 10–18 months",
    risk: "Medium",
    gateNote: "Link #430291 to epic; dedupe with #432904.",
    signOff: "Pending — Dispatch + Office",
  },
  {
    cluster: "Search / mass / templates",
    lead: "Willy / Willy",
    gapStance: "3 Partial",
    complexity: "Wildcard unification; mass zip export; template filter per org/class",
    magnitude: "L+M · 19–34 months",
    risk: "Medium",
    gateNote: "Covers subset of I + B sections only.",
    signOff: "Pending — Core UI",
  },
];

export default function VnkVahvaManagementGate() {
  const highRiskClusters = CLUSTERS.filter((c) => c.risk === "High").length;
  const totalPfrs = CLUSTERS.reduce((n, c) => n + c.pfrIds.length, 0);

  const portfolioTableRows = PORTFOLIO_ROWS.map((r) => [
    <Link href={`${ADO}/${r.id}`}>{r.id}</Link>,
    r.link,
    r.title,
    r.note,
  ]);

  const gapSegments = [
    { id: "partial", value: 9, color: "orange" as const },
  ];

  const roadmapSegments = [
    { id: "a-aligns", value: 1, color: "green" as const },
    { id: "b-accelerate", value: 4, color: "orange" as const },
    { id: "c-strategic", value: 4, color: "red" as const },
    { id: "d-low", value: 0, color: "gray" as const },
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
  const unregRows = UNREGISTERED_GAPS.map((g) => [g.domain, g.refs, g.pfr, g.risk]);
  const sectionRows = TENDER_SECTIONS.map((s) => [s.sec, s.name, String(s.reqs)]);

  return (
    <Stack gap={24} style={{ padding: 20, maxWidth: 1100 }}>
      <Stack gap={8}>
        <H1>VNK-Vahva (VN Asia) — management go/no-go brief</H1>
        <Text tone="secondary">
          Finnish government tender gate · Epic{" "}
          <Link href={`${ADO}/${PARENT_ID}`}>#{PARENT_ID}</Link> · {LINKED_COUNT} linked + 1 orphan · {PORTFOLIO_COUNT} PFRs · verified {LAST_ADO_CHECK}
        </Text>
      </Stack>

      <Grid columns={5} gap={12}>
        <Stat value={String(TENDER_FUNCTIONAL_REQS)} label="Liite 2.3 functional reqs" tone="warning" />
        <Stat value={String(TENDER_MANDATORY)} label="Pakollinen (mandatory)" tone="danger" />
        <Stat value={String(PORTFOLIO_COUNT)} label="Registered PFR Features" />
        <Stat value={NET_EFFORT_MONTHS} label="PFR portfolio effort" tone="warning" />
        <Stat value={AVG_FTE} label={`Avg team · ${BUILD_WINDOW_MONTHS} mo window`} tone="warning" />
        <Stat value={PEAK_FTE} label="Peak FTE (multi-squad)" tone="warning" />
        <Stat value={TIMELINE_STATUS} label="Go-live / build plan" />
        <Stat value="~2%" label="PFR rows / tender reqs" tone="danger" />
        <Stat value={FULL_TENDER_EFFORT} label="Full tender surface (indicative)" tone="danger" />
      </Grid>

      <Callout tone="danger" title="Primary gate question">
        Do we strategically commit to <strong>API-first / new SIF</strong> (<Link href={`${ADO}/437273`}>#437273</Link>) as the Finnish integration spine — when Liite 2.3 has{" "}
        <strong>{TENDER_MANDATORY} mandatory</strong> requirements and only <strong>9 RFI-era PFRs</strong> are registered?
      </Callout>

      <Grid columns={3} gap={12}>
        {STRATEGIC_QUESTIONS.map((item) => (
          <Card key={item.q}>
            <CardHeader>{item.q}</CardHeader>
            <CardBody>
              <Text>{item.body}</Text>
            </CardBody>
          </Card>
        ))}
      </Grid>

      <Grid columns={2} gap={16}>
        <Card>
          <CardHeader>RFI gap profile (9 PFRs)</CardHeader>
          <CardBody>
            <UsageBar
              total={PORTFOLIO_COUNT}
              topLeftLabel="Innovation Board + RFI evidence"
              topRightLabel="9 Partial · 0 Not met · 0 TBD"
              segments={gapSegments}
            />
            <Text tone="secondary" style={{ marginTop: 8 }}>
              No tender-tool ratings yet (unlike UIM/KK). All 9 PFRs assessed Partial from deck + product evidence.
            </Text>
          </CardBody>
        </Card>
        <Card>
          <CardHeader>Roadmap alignment (9 PFRs)</CardHeader>
          <CardBody>
            <UsageBar
              total={PORTFOLIO_COUNT}
              topLeftLabel={ROADMAP_SOURCE}
              topRightLabel="A 1 · B 4 · C 4 · D 0"
              segments={roadmapSegments}
            />
          </CardBody>
        </Card>
      </Grid>

      <Card>
        <CardHeader>Roadmap alignment share</CardHeader>
        <CardBody>
          <Table
            headers={["Status", "PFRs", "Meaning", "DG implication"]}
            rows={roadmapRows}
          />
          <BarChart
            horizontal
            height={240}
            categories={["A · Aligns", "B · Accelerate", "C · Strategic", "D · Low priority"]}
            series={[{ name: "PFRs", data: [1, 4, 4, 0] }]}
          />
        </CardBody>
      </Card>

      <CollapsibleSection title="Decision paths A / B / C" defaultOpen>
        <Grid columns={3} gap={12}>
          {DECISION_PATHS.map((d) => (
            <Callout key={d.title} tone="info" title={d.title}>
              {d.body}
            </Callout>
          ))}
        </Grid>
      </CollapsibleSection>

      <CollapsibleSection title="Commitment clusters" defaultOpen>
        <Table
          headers={["Cluster", "PFRs", "Size", "Effort (months)", "Risk", "Gate question", "IDs"]}
          rows={clusterRows}
        />
      </CollapsibleSection>

      <CollapsibleSection title="Tender scale (Liite 2.3) vs PFR coverage">
        <Callout tone="warn" title="Under-registration risk">
          Registered portfolio covers RFI gaps from Innovation Board deck — not the full {TENDER_FUNCTIONAL_REQS}-row matrix.
        </Callout>
        <Table headers={["Section", "Domain", "Requirements"]} rows={sectionRows} />
        <H3 style={{ marginTop: 16 }}>Unregistered high-risk domains (no ADO PFR)</H3>
        <Table headers={["Domain", "Tender refs", "PFR / source", "Risk"]} rows={unregRows} />
      </CollapsibleSection>

      <CollapsibleSection title="ADO portfolio on epic #436815">
        <Table headers={["ID", "Link type", "Title", "Note"]} rows={portfolioTableRows} />
      </CollapsibleSection>

      <CollapsibleSection title="Team rollup">
        <Table headers={["Team", "PFRs", "FTE band", "XL", "Modules"]} rows={teamRows} />
      </CollapsibleSection>

      <CollapsibleSection title="Cluster scans (owner sign-off pending)">
        <Table
          headers={["Cluster", "Lead", "Gap stance", "Magnitude", "Risk", "Gate note", "Sign-off"]}
          rows={scanRows}
        />
      </CollapsibleSection>

      <Text tone="secondary" className="small">
        Sources: Liite 2.3, Liite 2.6, Neuvottelukutsu, PoC 3.1, Innovation Board deck, FI API brief. Brief: docs/tender-reference/VNK-Vahva-management-gate-brief.md
      </Text>
    </Stack>
  );
}

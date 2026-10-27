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

const PARENT_ID = 433876;
const ADO = "https://dev.azure.com/tieto-si/360/_workitems/edit";
const LAST_ADO_CHECK = "17 Aug 2026, 09:44 CET";
const PORTFOLIO_COUNT = 27;
const BUILD_WINDOW_MONTHS = 10;
const BUILD_COMPLETE = "1 Sep 2027";
const GO_LIVE = "Oct 2027";
const NET_EFFORT_MONTHS = "45–75 months";
const AVG_FTE = "5–8 FTE";
const PEAK_FTE = "9–14 FTE";
const ROADMAP_SOURCE = "Public 360° roadmap PPT (Q1 2026–Q2 2027)";

type RoadmapSummary = {
  status: string;
  count: number;
  meaning: string;
  dgImplication: string;
};

const ROADMAP_SUMMARY: RoadmapSummary[] = [
  {
    status: "A — On roadmap, aligns with UIM delivery",
    count: 4,
    meaning: "Existing roadmap item(s) that align well timewise with expected delivery (Sep 2027)",
    dgImplication: "Reference existing roadmap in bid narrative",
  },
  {
    status: "B — On roadmap, needs acceleration",
    count: 9,
    meaning: "Existing roadmap item(s) that must be delivered faster than currently targeted",
    dgImplication: "Core investment conflict — pulls FFUI/search/platform forward",
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
    name: "Platform spine",
    magnitude: "XL + L + M",
    risk: "High",
    pfrCount: 6,
    effortBand: "28–45 months",
    gateQuestion: "Is customer-entities platform (433895) a strategic commit or out of scope?",
    pfrIds: [433895, 433881, 433883, 433887, 435597, 435603],
  },
  {
    name: "Search / FFUI / UI",
    magnitude: "XL + M",
    risk: "High",
    pfrCount: 6,
    effortBand: "25–40 months (net; overlaps Search Experience / FFUI pilot)",
    gateQuestion: "Can we commit on MK-77 unbounded results without product risk?",
    pfrIds: [433882, 433884, 435253, 435257, 433877, 435606],
  },
  {
    name: "Integrations (office / email)",
    magnitude: "L + S",
    risk: "Medium",
    pfrCount: 4,
    effortBand: "10–16 months",
    gateQuestion: "LibreOffice + Evolution: build, partner, or Q&A narrow?",
    pfrIds: [433889, 433891, 435203, 433890],
  },
  {
    name: "Dispatch / Strålfors",
    magnitude: "M × 4",
    risk: "Medium",
    pfrCount: 4,
    effortBand: "6–12 months",
    gateQuestion: "Is physical-mail channel (435338) in-house or integration-bound?",
    pfrIds: [433892, 433893, 435336, 435338],
  },
  {
    name: "Logging / audit",
    magnitude: "L",
    risk: "Medium",
    pfrCount: 2,
    effortBand: "4–8 months",
    gateQuestion: "Merge MK-20 PFRs (433894 + 435333) before commitment wording.",
    pfrIds: [433894, 435333],
  },
  {
    name: "Admin / workflow / security",
    magnitude: "M × 3",
    risk: "Medium",
    pfrCount: 3,
    effortBand: "5–10 months",
    gateQuestion: "Which are minimum requirements vs evaluation-only?",
    pfrIds: [433885, 433886, 433888],
  },
  {
    name: "API / activities",
    magnitude: "M",
    risk: "Medium",
    pfrCount: 1,
    effortBand: "2–5 months (partially in flight)",
    gateQuestion: "Can 377061 close EK-12 before bid lock?",
    pfrIds: [435258],
  },
  {
    name: "Point fixes",
    magnitude: "S",
    risk: "Low",
    pfrCount: 1,
    effortBand: "<1 month",
    gateQuestion: "Low risk — include in baseline bid narrative.",
    pfrIds: [433880],
  },
];

const TEAM_ROLLUP: { team: string; modules: string; pfrs: number; xl: number; fteBand: string }[] = [
  { team: "Core UI", modules: "Search, UI-UX, Webparts, Contact, Custom fields, UI Configuration, Massupdate, Web admin", pfrs: 12, xl: 8, fteBand: "6–10 FTE" },
  { team: "Core BL and eArchive", modules: "Dispatch, Access matrix, Disposal and Retention", pfrs: 6, xl: 1, fteBand: "2–4 FTE" },
  { team: "Core Integration", modules: "Integrations, SIF, Outlook client sidepanel", pfrs: 5, xl: 0, fteBand: "2–3 FTE" },
  { team: "Process Platform", modules: "Workflow", pfrs: 1, xl: 0, fteBand: "0.5–1 FTE" },
  { team: "Tech Platform Team", modules: "Logs", pfrs: 2, xl: 0, fteBand: "1–2 FTE" },
];

const DECISION_PATHS = [
  {
    title: "A — Strategic bid",
    body: "Commit to 433895 platform spine and FFUI/search roadmap. Accept 45–75 months net effort and staff 5–8 FTE average (9–14 FTE peak) through build complete 1 Sep 2027. Requires multi-team program and executive sponsorship.",
  },
  {
    title: "B — Bid with Q&A scope narrow",
    body: "Submit but challenge MK-77, entity scope, and integration commitments via ordregiver Q&A. Cap XL items at partial/delivery-plan responses.",
  },
  {
    title: "C — No-bid or low-effort",
    body: "Decline or minimal compliance response if platform spine and MK-77 cannot be credibly committed by Nov 2026 award gate.",
  },
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
    cluster: "Platform spine",
    lead: "Claus / Morten / Torben",
    gapStance: "Mixed — 1 Partial, 1 Draft, 2 Not met, 2 TBD (435597/435603)",
    complexity: "Cross-cutting meta-model, retention, mass update, config export, rules/validations, icons — depends on 433895 hub",
    magnitude: "XL × 4 + L + M · 28–45 months",
    risk: "High — program, not feature list",
    gateNote: "Without yes on 433895 (EK-6), satellites 433881/433883/433887/435597/435603 cannot be credibly committed.",
    signOff: "Pending — Custom fields + Disposal leads",
  },
  {
    cluster: "Search / FFUI / UI",
    lead: "Jarle / Torben / Willy",
    gapStance: "2 Partial/Draft, 2 Not met, 1 TBD (435606), 1 M blocker",
    complexity: "Intersects Search Experience + FFUI pilot; EK-3 overlaps MK-66/MK-84; 435606 adds universal listview configurability",
    magnitude: "XL × 5 + M · 25–40 months (net after overlap; FFUI uplift applied)",
    risk: "High — MK-77 (435257) is explicit bid blocker",
    gateNote: "435606 (all listviews / all metadata) materially increases FFUI scope. 435257 must be minimum-requirement classified.",
    signOff: "Pending — Search Experience program owner",
  },
  {
    cluster: "Integrations (office / email)",
    lead: "Anton / Hans",
    gapStance: "2 Not met, 1 TBD duplicate, 1 Partial (Outlook S)",
    complexity: "LibreOffice + Evolution are net-new client integrations; K-17 duplicated in 435203",
    magnitude: "L × 2 + S · 10–16 months",
    risk: "Medium — build vs partner vs Q&A narrow",
    gateNote: "K-16/K-17 are Check/Mindstekrav mix — confirm which are hard gates vs evaluation.",
    signOff: "Pending — Core Integration",
  },
  {
    cluster: "Dispatch / Strålfors",
    lead: "Hans",
    gapStance: "2 Not met, 2 TBD (new PFRs Aug 14)",
    complexity: "Strålfors channel assumptions; MK-167 physical post partly via partner",
    magnitude: "M × 4 · 6–12 months",
    risk: "Medium — operational + integration boundary",
    gateNote: "435338 (MK-167) and 435336 (MK-165) need tender-tool rating; MK-169 is confirmed Not met.",
    signOff: "Pending — Dispatch / Core BL",
  },
  {
    cluster: "Logging / audit",
    lead: "Willy / Hans",
    gapStance: "2 TBD — overlapping MK-20 scope",
    complexity: "433894 UUID vs 435333 transaction separation — merge before bid wording",
    magnitude: "L · 4–8 months",
    risk: "Medium — compliance narrative risk if double-counted",
    gateNote: "Dedupe PFRs and pick single commitment story for MK-20 family.",
    signOff: "Pending — Tech Platform",
  },
  {
    cluster: "Admin / workflow / security",
    lead: "Torben / Anton / Eva",
    gapStance: "2 Not met, 1 TBD",
    complexity: "MK-99 automatic workflow history doc; MK-133 access-matrix report; MK-120 web-admin masks",
    magnitude: "M × 3 · 5–10 months",
    risk: "Medium — several are Mindstekrav Verify",
    gateNote: "MK-99 red flag: automatic document creation not supported today (manual/workflow report).",
    signOff: "Pending — Process Platform + Core UI admin",
  },
  {
    cluster: "API / activities",
    lead: "Nikita",
    gapStance: "In flight (377061)",
    complexity: "EK-12 Activities API — SIF module; partial delivery path exists",
    magnitude: "M · 2–5 months",
    risk: "Medium — timeline to bid lock",
    gateNote: "Lowest gate risk if 377061 closes before response freeze.",
    signOff: "Pending — confirm EK-12 closure date",
  },
  {
    cluster: "Point fixes",
    lead: "Panu",
    gapStance: "Partial (~40h)",
    complexity: "MK-56 duplicate contact prevention — localized Contact module change",
    magnitude: "S · <1 month",
    risk: "Low",
    gateNote: "Include in baseline bid; no gate blocker.",
    signOff: "Pending — confirm Partial acceptable for Mindstekrav",
  },
];

export default function UimManagementGate() {
  const highRiskClusters = CLUSTERS.filter((c) => c.risk === "High").length;
  const totalPfrs = CLUSTERS.reduce((n, c) => n + c.pfrCount, 0);

  const gapSegments = [
    { id: "not-met", value: 11, color: "red" as const },
    { id: "partial", value: 3, color: "orange" as const },
    { id: "draft", value: 2, color: "blue" as const },
    { id: "in-flight", value: 1, color: "green" as const },
    { id: "tbd", value: 10, color: "gray" as const },
  ];

  const roadmapSegments = [
    { id: "a-aligns", value: 4, color: "green" as const },
    { id: "b-accelerate", value: 9, color: "orange" as const },
    { id: "c-strategic", value: 11, color: "red" as const },
    { id: "d-low", value: 3, color: "gray" as const },
  ];

  const roadmapRows = ROADMAP_SUMMARY.map((r) => [r.status, String(r.count), r.meaning, r.dgImplication]);

  const clusterRows = CLUSTERS.map((c) => [
    c.name,
    c.pfrCount,
    c.magnitude,
    c.effortBand,
    c.risk,
    c.gateQuestion,
    c.pfrIds.map((id) => id).join(", "),
  ]);

  const teamRows = TEAM_ROLLUP.map((t) => [t.team, String(t.pfrs), t.fteBand, String(t.xl), t.modules]);

  const scanRows = CLUSTER_SCANS.map((s) => [
    s.cluster,
    s.lead,
    s.gapStance,
    s.magnitude,
    s.risk,
    s.gateNote,
    s.signOff,
  ]);

  return (
    <Stack gap={24} style={{ padding: 20, maxWidth: 1100 }}>
      <Stack gap={8}>
        <H1>UIM ESDH 2026 — management go/no-go brief</H1>
        <Text tone="secondary">
          Decision gate prep ·{" "}
          <Link href={`${ADO}/${PARENT_ID}`}>ADO parent #{PARENT_ID}</Link> · {PORTFOLIO_COUNT} related Features · ADO verified {LAST_ADO_CHECK}
        </Text>
      </Stack>

      <Grid columns={5} gap={12}>
        <Stat value={totalPfrs} label="UIM commitment Features" />
        <Stat value={NET_EFFORT_MONTHS} label="Net effort (conservative)" tone="warning" />
        <Stat value={AVG_FTE} label={`Avg team · ${BUILD_WINDOW_MONTHS} mo window`} tone="warning" />
        <Stat value="Nov 2026" label="Award decision target" />
        <Stat value={BUILD_COMPLETE} label={`Build complete · go-live ${GO_LIVE}`} />
      </Grid>

      <Callout tone="warning" title="Team size vs build deadline">
        ~{BUILD_WINDOW_MONTHS} calendar months from award (Nov 2026) to build complete ({BUILD_COMPLETE}); go-live {GO_LIVE} requires delivery one month earlier for cutover and stabilisation. At {NET_EFFORT_MONTHS} net effort, the program needs {AVG_FTE} sustained across product teams, with {PEAK_FTE} peak when platform spine and Search/FFUI run in parallel. Core UI alone likely needs 6–10 FTE for much of the window — FFUI/listview work (435606 cluster) is the main driver. Estimates include test, integration, and contingency — not dev-only.
      </Callout>

      <Callout tone="info" title="ADO portfolio check — 3 new Features (17 Aug)">
        Verified {LAST_ADO_CHECK}: parent #{PARENT_ID} now has {PORTFOLIO_COUNT} Related Features (+435597 rules/validations, +435603 icons, +435606 listviews). All three linked to parent for this gate. Older UIM-tagged upgrade items (e.g. 353751, 360628) remain out of scope.
      </Callout>

      <Callout tone="danger" title="Primary gate question">
        Do we strategically commit to customer-created entities (PFR 433895 / EK-6) as a platform program? Without a clear yes/no, bid narrative and resourcing cannot be credible. Secondary blocker: MK-77 unbounded search results (435257).
      </Callout>

      <Grid columns={3} gap={12}>
        <Card>
          <CardHeader>{DECISION_PATHS[0].title}</CardHeader>
          <CardBody>
            <Text size="small">{DECISION_PATHS[0].body}</Text>
          </CardBody>
        </Card>
        <Card>
          <CardHeader>{DECISION_PATHS[1].title}</CardHeader>
          <CardBody>
            <Text size="small">{DECISION_PATHS[1].body}</Text>
          </CardBody>
        </Card>
        <Card>
          <CardHeader>{DECISION_PATHS[2].title}</CardHeader>
          <CardBody>
            <Text size="small">{DECISION_PATHS[2].body}</Text>
          </CardBody>
        </Card>
      </Grid>

      <Card>
        <CardHeader>Portfolio gap profile ({PORTFOLIO_COUNT} Features)</CardHeader>
        <CardBody>
          <UsageBar
            total={27}
            topLeftLabel="Tender-tool gap ratings"
            topRightLabel="11 Not met · 3 Partial · 2 Draft · 1 In flight · 10 TBD"
            segments={gapSegments}
          />
          <Text tone="tertiary" size="small" style={{ marginTop: 10 }}>
            Source: UIM ESDH Tender tool internal ratings (Jul 2026). TBD = new PFRs not yet rated in tool.
          </Text>
        </CardBody>
      </Card>

      <Card>
        <CardHeader>Roadmap alignment vs UIM delivery ({PORTFOLIO_COUNT} Features)</CardHeader>
        <CardBody>
          <UsageBar
            total={27}
            topLeftLabel={ROADMAP_SOURCE}
            topRightLabel="A 4 · B 9 · C 11 · D 3"
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
            ~33% on roadmap but needs acceleration (B). ~41% strategically relevant but not on roadmap (C). Full PFR-level mapping in uim-commitment-heatmap.canvas.tsx. Cluster-owner validation pending.
          </Text>
        </CardBody>
      </Card>

      <Stack gap={10}>
        <H2>Commitment clusters — complexity, magnitude, risk</H2>
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
            series={[{ name: "PFRs", data: [8, 6, 11, 2], tone: "warning" }]}
            showValues
            height={160}
          />
          <Text tone="tertiary" size="small">
            XL = multi-team platform work. Bands are portfolio-level, not item estimates.
          </Text>
        </Stack>
        <Stack gap={8}>
          <H3>High-risk cluster share</H3>
          <BarChart
            categories={["High risk", "Other clusters"]}
            series={[{ name: "Clusters", data: [highRiskClusters, CLUSTERS.length - highRiskClusters], tone: "danger" }]}
            showValues
            height={160}
          />
          <Text tone="tertiary" size="small">
            Platform spine + Search/FFUI drive ~70–80% of portfolio risk and effort.
          </Text>
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
          UIM pulls planned FFUI/search/platform work forward and adds scope not on the roadmap.
        </Text>
      </Stack>

      <CollapsibleSection title="Cluster light scans — owner sign-off (pre-meeting)" defaultOpen>
        <Table
          headers={["Cluster", "Lead", "Gap stance", "Effort (months)", "Risk", "Gate note", "Sign-off"]}
          rows={scanRows}
          striped
          stickyHeader
        />
        <Text tone="tertiary" size="small" style={{ marginTop: 8 }}>
          Leads confirm Met / Partial / Not met and whether they recommend commit, Q&A narrow, or no-bid on their cluster before the gate. Deep cap-check per PFR deferred until after decision path is chosen.
        </Text>
      </CollapsibleSection>

      <CollapsibleSection title="Product team demand (Impacted Module rollup)" defaultOpen>
        <Table
          headers={["Product team", "PFRs", "Indicative FTE", "XL PFRs", "Modules"]}
          rows={teamRows}
          striped
        />
        <Text tone="tertiary" size="small" style={{ marginTop: 8 }}>
          FTE bands assume parallel delivery within the 10-month build window. Core UI carries most XL load (Search Experience + FFUI + Custom fields + listviews). Totals overlap — not additive headcount.
        </Text>
      </CollapsibleSection>

      <CollapsibleSection title="Timeline, team size, and risk context" defaultOpen>
        <Stack gap={8}>
          <Text>
            Award decision ~Nov 2026 leaves ~{BUILD_WINDOW_MONTHS} months to build complete {BUILD_COMPLETE} (go-live {GO_LIVE}). {NET_EFFORT_MONTHS} net effort implies {AVG_FTE} average staffing ({PEAK_FTE} at peak) — a multi-squad program, not a single team.
          </Text>
          <Text>
            XL platform work (433895 cluster) must start in parallel with bid preparation, not after award. Late start compresses an already tight window: peak FTE must rise above {PEAK_FTE}, or go-live {GO_LIVE} is not credible.
          </Text>
          <Text>
            Overlap risk: Search/FFUI Features intersect Search Experience / FFUI pilot. Do not double-count months across 433882, 433884, 435253 and existing program roadmaps.
          </Text>
          <Text>
            Hygiene before bid lock: dedupe MK-20 (433894/435333), K-17 (433891/435203), clarify EK-3 vs FFUI PFR overlap.
          </Text>
        </Stack>
      </CollapsibleSection>

      <CollapsibleSection title="Recommended gate meeting agenda (60 min)">
        <Stack gap={6}>
          <Text weight="semibold">1. Platform spine in/out (15 min)</Text>
          <Text size="small">433895 / EK-6 + satellites 433881, 433883, 433887. Custom fields module ownership.</Text>
          <Text weight="semibold">2. Bid blockers (10 min)</Text>
          <Text size="small">MK-77 (435257), minimum requirements vs evaluation criteria.</Text>
          <Text weight="semibold">3. Roadmap conflict (10 min)</Text>
          <Text size="small">9 PFRs need acceleration (B); 11 are off-roadmap but strategic (C). What gets reprioritised on the Public 360° roadmap if we bid?</Text>
          <Text weight="semibold">4. Team capacity snapshot (10 min)</Text>
          <Text size="small">Can we staff {AVG_FTE} average ({PEAK_FTE} peak) to build complete {BUILD_COMPLETE}? Core UI 6–10 FTE vs Search Experience / FFUI commitments.</Text>
          <Text weight="semibold">5. Decision path A / B / C (15 min)</Text>
          <Text size="small">Assign owner for bid narrative and Q&A strategy.</Text>
          <Text weight="semibold">6. Next artifacts (5 min)</Text>
          <Text size="small">Deep cap-check deferred until after gate. Light cluster owners confirm gap stance by PFR.</Text>
        </Stack>
      </CollapsibleSection>

      <Text tone="secondary" size="small">
        See also: uim-commitment-heatmap.canvas.tsx — PFR table with gap, roadmap alignment, owner, and Impacted Module.
      </Text>
    </Stack>
  );
}

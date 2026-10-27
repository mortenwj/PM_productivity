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
  Link,
  Row,
  Select,
  Stack,
  Stat,
  Table,
  Text,
  UsageBar,
  useCanvasState,
} from "cursor/canvas";

type GapStatus = "Not met" | "Partial" | "Draft needed" | "TBD" | "In flight";
type Magnitude = "XL" | "L" | "M" | "S";
type Risk = "High" | "Medium" | "Low";
type Phase = "Gate decision" | "Q&A / clarify" | "Build if bid";
type RoadmapAlign = "A — Aligns" | "B — Accelerate" | "C — Strategic" | "D — Low priority";

type PfrRow = {
  id: number;
  ref: string;
  title: string;
  cluster: string;
  module: string;
  magnitude: Magnitude;
  gap: GapStatus;
  risk: Risk;
  phase: Phase;
  owner: string;
  adoState: string;
  roadmap: RoadmapAlign;
  roadmapRef: string;
  note?: string;
};

const ROADMAP_SOURCE = "Public 360° roadmap (PPT, Q1 2026–Q2 2027) vs supplier-proposed Overtagelsesdag";
const ROADMAP_ALIGNMENTS: RoadmapAlign[] = ["A — Aligns", "B — Accelerate", "C — Strategic", "D — Low priority"];
const QUERY_ID = "6d4459e7-42f4-431d-9e54-68566fed49aa";
const ADO_BASE = "https://dev.azure.com/tieto-si/360/_workitems/edit";
const FOUNDATION_EPIC_ID = 434005;
const FOUNDATION_DAYS = "200 days";
const LAST_ADO_CHECK = "18 Aug 2026, 16:51 CET";
const TIMELINE_STATUS = "ukendt";
const PORTFOLIO_COUNT = 25;

const PFR_ROWS: PfrRow[] = [
  { id: 435490, ref: "B2-12+", title: "Danish servicemål deadline model + dashboard + notifications", cluster: "Servicemål / deadlines", module: "Unset", magnitude: "XL", gap: "Partial", risk: "High", phase: "Gate decision", owner: "Bjørn Henrik", adoState: "New", roadmap: "B — Accelerate", roadmapRef: "Plan & Build 360 / Flow", note: "Consolidates 434878/434881; B2-12 + 5.2.11.x + 5.2.16.3" },
  { id: 435495, ref: "B2-18", title: "Integration landscape (public + municipal + customer)", cluster: "Integration spine", module: "Unset", magnitude: "XL", gap: "Partial", risk: "High", phase: "Gate decision", owner: "Olga", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "MK Verify; partly met in tool" },
  { id: 435489, ref: "5.2.15.x", title: "FilArkiv archive transfer from Plan & Build (5 bundled reqs)", cluster: "FilArkiv archive", module: "Unset", magnitude: "L", gap: "Partial", risk: "Medium", phase: "Gate decision", owner: "Bjørn Henrik", adoState: "New", roadmap: "C — Strategic", roadmapRef: "Archive automation", note: "Decision Panel, protected person warning" },
  { id: 435491, ref: "B2-14", title: "Time registration on cases (6 bundled reqs)", cluster: "Time registration", module: "Unset", magnitude: "L", gap: "TBD", risk: "Medium", phase: "Gate decision", owner: "Morten", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "Not yet rated in tender tool" },
  { id: 435486, ref: "B2-03", title: "BRE-triggered write-back to BOM portal", cluster: "BOM + BRE", module: "Unset", magnitude: "L", gap: "Partial", risk: "High", phase: "Gate decision", owner: "Bjørn Henrik", adoState: "New", roadmap: "A — Aligns", roadmapRef: "Business Rules Engine", note: "MK minimum; partly met" },
  { id: 435480, ref: "5.2.1.1", title: "Tagging, structuring and sorting of cases and documents", cluster: "Case UX / search", module: "Unset", magnitude: "L", gap: "Partial", risk: "High", phase: "Gate decision", owner: "Jarle", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "Downgraded from Not met → Partial in tool" },
  { id: 435501, ref: "B2-20", title: "Log delivery to SIEM (LogPoint)", cluster: "Security / SIEM", module: "Unset", magnitude: "L", gap: "Not met", risk: "High", phase: "Gate decision", owner: "—", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "MK; Not able to meet" },
  { id: 435493, ref: "5.3.7.2.6", title: "Log integrity — manual amendment/deletion", cluster: "Security / SIEM", module: "Unset", magnitude: "M", gap: "Not met", risk: "High", phase: "Gate decision", owner: "Jarle", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "MK; Not able to meet" },
  { id: 435499, ref: "5.3.8.2.7.1.4", title: "MeMo actions when sending Digital Post", cluster: "Integration spine", module: "Unset", magnitude: "S", gap: "Not met", risk: "High", phase: "Gate decision", owner: "—", adoState: "New", roadmap: "A — Aligns", roadmapRef: "Digital Post", note: "Regressed to Not met in tool" },
  { id: 435484, ref: "5.2.8.4+", title: "Case overview and process control (3 bundled reqs)", cluster: "Process control", module: "Unset", magnitude: "L", gap: "Partial", risk: "Medium", phase: "Gate decision", owner: "Morten", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "Milestone timeline + validation warnings" },
  { id: 435483, ref: "5.2.4.3", title: "Search, sorting, filtering and export", cluster: "Case UX / search", module: "Unset", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Gate decision", owner: "Jarle", adoState: "New", roadmap: "B — Accelerate", roadmapRef: "Refactor search experience", note: "Partly met in tool" },
  { id: 435496, ref: "5.3.8.2.2.1", title: "Master data from national registers", cluster: "Integration spine", module: "Unset", magnitude: "L", gap: "Partial", risk: "High", phase: "Gate decision", owner: "—", adoState: "New", roadmap: "A — Aligns", roadmapRef: "NG Integration API", note: "Nine registers MK; partly met" },
  { id: 435487, ref: "5.2.9.x", title: "BOM data as search and filter criteria", cluster: "BOM + BRE", module: "Unset", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Gate decision", owner: "Bjørn Henrik", adoState: "New", roadmap: "B — Accelerate", roadmapRef: "Plan & Build / BOM", note: "" },
  { id: 435488, ref: "5.2.13.1", title: "Case creation via standard case templates", cluster: "Process control", module: "Unset", magnitude: "M", gap: "In flight", risk: "Medium", phase: "Gate decision", owner: "Bjørn Henrik", adoState: "New", roadmap: "B — Accelerate", roadmapRef: "Hosted Processes / Flow", note: "Fully met in tool" },
  { id: 435503, ref: "5.4.2.1", title: "Integration to AI Assist (option)", cluster: "Integration spine", module: "Unset", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Q&A / clarify", owner: "—", adoState: "New", roadmap: "B — Accelerate", roadmapRef: "Agentic case management", note: "Option MK; partly met" },
  { id: 435502, ref: "5.4.1.1", title: "Integration to debtor system (option)", cluster: "Integration spine", module: "Unset", magnitude: "M", gap: "Partial", risk: "Low", phase: "Q&A / clarify", owner: "—", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "Option — Opus Debitor" },
  { id: 435482, ref: "5.2.1.3", title: "Flexible journalisation (drag & drop)", cluster: "Case UX / search", module: "Unset", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Build if bid", owner: "—", adoState: "New", roadmap: "B — Accelerate", roadmapRef: "Plan & Build / BOM", note: "Partly met; BOM drag-drop caveat" },
  { id: 435481, ref: "5.2.1.2", title: "Conflict resolution (external GIS/AI)", cluster: "Case UX / search", module: "Unset", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Q&A / clarify", owner: "Linn", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "Partly met; BacklogCleanup-Keep tag" },
  { id: 435485, ref: "5.2.8.5", title: "Handling received information by case status", cluster: "Case UX / search", module: "Unset", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Gate decision", owner: "Morten", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "" },
  { id: 435497, ref: "5.3.8.2.3", title: "Outgoing deep link integrations", cluster: "Integration spine", module: "Unset", magnitude: "M", gap: "TBD", risk: "Medium", phase: "Build if bid", owner: "Jarle", adoState: "New", roadmap: "A — Aligns", roadmapRef: "NG Integration API", note: "Not yet rated in tool" },
  { id: 435498, ref: "5.3.8.2.7.1.2", title: "Remote print of letters via SF1601", cluster: "Integration spine", module: "Unset", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Build if bid", owner: "—", adoState: "New", roadmap: "C — Strategic", roadmapRef: "—", note: "" },
  { id: 434878, ref: "5.2.11.2", title: "Servicemålstid start/stop", cluster: "Servicemål / deadlines", module: "Plan&Build", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Q&A / clarify", owner: "Bjørn Henrik", adoState: "New", roadmap: "D — Low priority", roadmapRef: "—", note: "Superseded by consolidated 435490" },
  { id: 434881, ref: "5.2.11.3", title: "Sagsbehandlingstid for ikke-BOM sager", cluster: "Servicemål / deadlines", module: "Plan&Build", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Q&A / clarify", owner: "Bjørn Henrik", adoState: "New", roadmap: "D — Low priority", roadmapRef: "—", note: "Superseded by consolidated 435490" },
  { id: 434352, ref: "Data delimitation", title: "Data delimitation of cases", cluster: "Security / SIEM", module: "Plan&Build", magnitude: "M", gap: "Partial", risk: "Medium", phase: "Build if bid", owner: "—", adoState: "New", roadmap: "A — Aligns", roadmapRef: "Access matrix / dataafgrænsning", note: "Partly met in tool" },
  { id: 435492, ref: "5.3.4.2", title: "Error texts and system messages", cluster: "Point fix", module: "Unset", magnitude: "S", gap: "Partial", risk: "Low", phase: "Build if bid", owner: "Jarle", adoState: "New", roadmap: "D — Low priority", roadmapRef: "—", note: "IK configurable messages" },
];

const CLUSTERS = ["All", ...Array.from(new Set(PFR_ROWS.map((r) => r.cluster))).sort()];

function roadmapTone(roadmap: RoadmapAlign): "success" | "warning" | "danger" | "neutral" {
  if (roadmap === "A — Aligns") return "success";
  if (roadmap === "B — Accelerate") return "warning";
  if (roadmap === "C — Strategic") return "danger";
  return "neutral";
}

function sortRows(rows: PfrRow[]): PfrRow[] {
  const magOrder = { XL: 0, L: 1, M: 2, S: 3 };
  const gapOrder = { "Not met": 0, "Draft needed": 1, Partial: 2, TBD: 3, "In flight": 4 };
  return [...rows].sort(
    (a, b) =>
      magOrder[a.magnitude] - magOrder[b.magnitude] ||
      gapOrder[a.gap] - gapOrder[b.gap] ||
      a.id - b.id,
  );
}

function countBy<T extends string>(items: PfrRow[], key: keyof PfrRow, values: T[]): Record<T, number> {
  const out = {} as Record<T, number>;
  for (const v of values) out[v] = 0;
  for (const item of items) {
    const val = item[key] as T;
    if (val in out) out[val] += 1;
  }
  return out;
}

export default function KkCommitmentHeatmap() {
  const [clusterFilter, setClusterFilter] = useCanvasState<string>("clusterFilter", "All");
  const [roadmapFilter, setRoadmapFilter] = useCanvasState<string>("roadmapFilter", "All");

  const filtered = PFR_ROWS.filter((r) => {
    if (clusterFilter !== "All" && r.cluster !== clusterFilter) return false;
    if (roadmapFilter !== "All" && r.roadmap !== roadmapFilter) return false;
    return true;
  });

  const sorted = sortRows(filtered);
  const roadmapCounts = countBy(PFR_ROWS, "roadmap", ROADMAP_ALIGNMENTS);
  const gapCounts = countBy(PFR_ROWS, "gap", ["Not met", "Partial", "Draft needed", "TBD", "In flight"] as GapStatus[]);

  const tableRows = sorted.map((r) => [
    <Link href={`${ADO_BASE}/${r.id}`}>{r.id}</Link>,
    r.ref,
    r.title,
    r.adoState,
    r.cluster,
    r.magnitude,
    r.gap,
    r.risk,
    r.owner,
    r.module,
    r.roadmap,
  ]);

  return (
    <Stack gap={20} style={{ padding: 20, maxWidth: 1200 }}>
      <Stack gap={6}>
        <H1>KK commitment heatmap</H1>
        <Text tone="secondary">
          {PORTFOLIO_COUNT} tender PFRs (delta on top of foundation epic{" "}
          <Link href={`${ADO_BASE}/${FOUNDATION_EPIC_ID}`}>#{FOUNDATION_EPIC_ID}</Link>, {FOUNDATION_DAYS}) · ADO query {QUERY_ID.slice(0, 8)}… · verified {LAST_ADO_CHECK}
        </Text>
      </Stack>

      <Callout tone="info" title="Two-layer portfolio">
        <strong>Foundation:</strong> Epic #{FOUNDATION_EPIC_ID} ({FOUNDATION_DAYS}, Approach 1) covers P&B merge into P360 — BOM, fee, FilArkiv, GIS, Flow process models, case types. Child #434006 (servicemål), related #434009 (time registration).{" "}
        <strong>Tender delta:</strong> the {PORTFOLIO_COUNT} query PFRs below — gaps on top of foundation. **30–55 months effort applies to this layer only**. Blockers: 435501, 435493, 435499 (Not met). Tagging 435480 now Partial in tool.
      </Callout>

      <Grid columns={4} gap={12}>
        <Stat value={PORTFOLIO_COUNT} label="Commitment PFRs" />
        <Stat value={gapCounts["Not met"]} label="Not met (blockers)" tone="danger" />
        <Stat value={roadmapCounts["B — Accelerate"] + roadmapCounts["C — Strategic"]} label="B + C roadmap conflict" tone="warning" />
        <Stat value={TIMELINE_STATUS} label="Go-live in tender (Timeline)" tone="warning" />
        <Stat value="Supplier plan" label="4.1.1 · 15% eval weight" />
      </Grid>

      <Callout tone="danger" title="Sort order">
        XL/L magnitude first, then gap severity. Not met: 435501 (SIEM), 435493 (log integrity), 435499 (MeMo). Tagging 435480 downgraded to Partial.
      </Callout>

      <Grid columns={2} gap={16}>
        <Card>
          <CardHeader>Gap profile</CardHeader>
          <CardBody>
            <UsageBar
              total={PORTFOLIO_COUNT}
              topLeftLabel="Tender-tool ratings"
              topRightLabel={`${gapCounts["Not met"]} Not met · ${gapCounts.Partial} Partial · ${gapCounts["In flight"]} In flight · ${gapCounts.TBD} TBD`}
              segments={[
                { id: "nm", value: gapCounts["Not met"], color: "red" },
                { id: "p", value: gapCounts.Partial, color: "orange" },
                { id: "if", value: gapCounts["In flight"], color: "green" },
                { id: "tbd", value: gapCounts.TBD, color: "gray" },
              ]}
            />
          </CardBody>
        </Card>
        <Card>
          <CardHeader>Roadmap alignment</CardHeader>
          <CardBody>
            <UsageBar
              total={PORTFOLIO_COUNT}
              topLeftLabel={ROADMAP_SOURCE}
              topRightLabel={`A ${roadmapCounts["A — Aligns"]} · B ${roadmapCounts["B — Accelerate"]} · C ${roadmapCounts["C — Strategic"]} · D ${roadmapCounts["D — Low priority"]}`}
              segments={[
                { id: "a", value: roadmapCounts["A — Aligns"], color: "green" },
                { id: "b", value: roadmapCounts["B — Accelerate"], color: "orange" },
                { id: "c", value: roadmapCounts["C — Strategic"], color: "red" },
                { id: "d", value: roadmapCounts["D — Low priority"], color: "gray" },
              ]}
            />
            <BarChart
              horizontal
              categories={["A · Aligns", "B · Accelerate", "C · Strategic", "D · Low priority"]}
              series={[{ name: "PFRs", data: ROADMAP_ALIGNMENTS.map((k) => roadmapCounts[k]), tone: "warning" }]}
              showValues
              height={220}
              style={{ marginTop: 12 }}
            />
          </CardBody>
        </Card>
      </Grid>

      <Row gap={12} align="center">
        <Text size="small" tone="secondary">Filter:</Text>
        <Select
          label="Cluster"
          value={clusterFilter}
          onChange={setClusterFilter}
          options={CLUSTERS.map((c) => ({ value: c, label: c }))}
        />
        <Select
          label="Roadmap"
          value={roadmapFilter}
          onChange={setRoadmapFilter}
          options={[{ value: "All", label: "All" }, ...ROADMAP_ALIGNMENTS.map((r) => ({ value: r, label: r }))]}
        />
        <Text size="small" tone="tertiary">{sorted.length} of {PORTFOLIO_COUNT} shown</Text>
      </Row>

      <Stack gap={8}>
        <H2>PFR commitment matrix</H2>
        <Table
          headers={["ID", "Ref", "Title (ADO)", "State", "Cluster", "Size", "Gap", "Risk", "Owner", "Module", "Roadmap"]}
          rows={tableRows}
          rowTone={sorted.map((r) => roadmapTone(r.roadmap))}
          striped
          stickyHeader
        />
      </Stack>

      <CollapsibleSection title="Query items excluded from PFR count" defaultOpen={false}>
        <Text size="small">
          #429990 &quot;Suggestion for Improvement&quot; — placeholder, not a tender commitment. #434005 foundation epic — counted separately (200 days), not in the 25 PFR delta.
        </Text>
      </CollapsibleSection>
    </Stack>
  );
}

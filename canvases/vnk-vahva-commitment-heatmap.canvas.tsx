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
  onEpic: boolean;
  note?: string;
};

const ROADMAP_SOURCE = "Public 360° roadmap (PPT, Q1 2026–Q2 2027) vs ~18 mo planning band";
const ROADMAP_ALIGNMENTS: RoadmapAlign[] = ["A — Aligns", "B — Accelerate", "C — Strategic", "D — Low priority"];
const ADO_BASE = "https://dev.azure.com/tieto-si/360/_workitems/edit";
const PARENT_ID = 436815;
const LAST_ADO_CHECK = "4 Sep 2026, 00:10 CET";
const TENDER_REQS = 487;
const TENDER_MANDATORY = 416;
const PORTFOLIO_COUNT = 9;

const PFR_ROWS: PfrRow[] = [
  {
    id: 437273,
    ref: "A12–A14 / API",
    title: "360° API requirements (API-first / new SIF)",
    cluster: "API / integration platform",
    module: "Unset",
    magnitude: "XL",
    gap: "Partial",
    risk: "High",
    phase: "Gate decision",
    owner: "Mika / Tero",
    adoState: "New",
    roadmap: "C — Strategic",
    roadmapRef: "NG Integration API / 360° API Gateway",
    onEpic: true,
    note: "Post–Innovation Board; FI API brief; webhooks, SIEM, ES",
  },
  {
    id: 430281,
    ref: "F-section",
    title: "Metadata — language, length, inheritance, infosec",
    cluster: "Metadata / TOS",
    module: "Unset",
    magnitude: "L",
    gap: "Partial",
    risk: "High",
    phase: "Gate decision",
    owner: "Willy Koch",
    adoState: "New",
    roadmap: "B — Accelerate",
    roadmapRef: "Custom fields / metadata model",
    onEpic: true,
    note: "111 Liite 2.3 reqs in F; record-type publicity warning (deck slide 9)",
  },
  {
    id: 433271,
    ref: "B7–B10, E48",
    title: "Mass functions — metadata, export, mass edit, bulk delete",
    cluster: "Mass operations",
    module: "Unset",
    magnitude: "L",
    gap: "Partial",
    risk: "Medium",
    phase: "Gate decision",
    owner: "—",
    adoState: "New",
    roadmap: "B — Accelerate",
    roadmapRef: "Mass update",
    onEpic: true,
    note: "Zip export proposal; mass activity delete critical",
  },
  {
    id: 434693,
    ref: "I-section",
    title: "Search — single wildcard, flexible saved-search sharing",
    cluster: "Search / FFUI",
    module: "Unset",
    magnitude: "L",
    gap: "Partial",
    risk: "Medium",
    phase: "Gate decision",
    owner: "Willy Koch",
    adoState: "New",
    roadmap: "B — Accelerate",
    roadmapRef: "Refactor search experience",
    onEpic: true,
    note: "% vs * wildcard; share across subunits/roles",
  },
  {
    id: 430271,
    ref: "E-dispatch",
    title: "Enhanced dispatch — redispatch, recipients, failure logs",
    cluster: "Dispatch / notifications",
    module: "Unset",
    magnitude: "L",
    gap: "Partial",
    risk: "Medium",
    phase: "Gate decision",
    owner: "Olga Safonova",
    adoState: "New",
    roadmap: "C — Strategic",
    roadmapRef: "—",
    onEpic: true,
    note: "Commitment; Conditional tag; new doc per redispatch",
  },
  {
    id: 432904,
    ref: "E21–E26",
    title: "Enhanced email notifications — metadata in subject/body",
    cluster: "Dispatch / notifications",
    module: "Unset",
    magnitude: "M",
    gap: "Partial",
    risk: "Medium",
    phase: "Gate decision",
    owner: "—",
    adoState: "New",
    roadmap: "A — Aligns",
    roadmapRef: "New Outlook Support / notifications",
    onEpic: true,
    note: "Security class + case title/ID called out in deck",
  },
  {
    id: 430291,
    ref: "E-notify",
    title: "Increasing configurability of email messages",
    cluster: "Dispatch / notifications",
    module: "Unset",
    magnitude: "M",
    gap: "Partial",
    risk: "Medium",
    phase: "Q&A / clarify",
    owner: "Jarle Steira",
    adoState: "Pending",
    roadmap: "C — Strategic",
    roadmapRef: "—",
    onEpic: false,
    note: "ORPHAN — not linked to epic; overlaps #432904",
  },
  {
    id: 433354,
    ref: "B58",
    title: "Template filtering in FI/SV subsetup",
    cluster: "Templates / document UX",
    module: "Unset",
    magnitude: "M",
    gap: "Partial",
    risk: "Low",
    phase: "Build if bid",
    owner: "—",
    adoState: "New",
    roadmap: "B — Accelerate",
    roadmapRef: "Full Flex UI cont. / templates",
    onEpic: true,
    note: "Only formal child of #436815; also applies Sweden",
  },
  {
    id: 433356,
    ref: "B66, H",
    title: "Draft file version disposal / hiding",
    cluster: "Archiving / disposal",
    module: "Unset",
    magnitude: "M",
    gap: "Partial",
    risk: "Medium",
    phase: "Build if bid",
    owner: "—",
    adoState: "New",
    roadmap: "C — Strategic",
    roadmapRef: "Retention / disposal",
    onEpic: true,
    note: "Hide drafts + default deletion schedule (e.g. 6 mo)",
  },
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

export default function VnkVahvaCommitmentHeatmap() {
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
  const orphanCount = PFR_ROWS.filter((r) => !r.onEpic).length;

  const tableRows = sorted.map((r) => [
    <Link href={`${ADO_BASE}/${r.id}`}>{r.id}</Link>,
    r.ref,
    r.title,
    r.onEpic ? "Yes" : "No",
    r.adoState,
    r.cluster,
    r.magnitude,
    r.gap,
    r.risk,
    r.owner,
    r.roadmap,
  ]);

  return (
    <Stack gap={20} style={{ padding: 20, maxWidth: 1200 }}>
      <Stack gap={6}>
        <H1>VNK-Vahva commitment heatmap</H1>
        <Text tone="secondary">
          {PORTFOLIO_COUNT} VN Asia PFRs · Epic{" "}
          <Link href={`${ADO_BASE}/${PARENT_ID}`}>#{PARENT_ID}</Link> · Liite 2.3: {TENDER_REQS} reqs ({TENDER_MANDATORY} Pakollinen) · verified {LAST_ADO_CHECK}
        </Text>
      </Stack>

      <Callout tone="danger" title="Coverage warning">
        <strong>9 PFRs</strong> vs <strong>{TENDER_REQS} functional requirements</strong>. Unregistered: Suomi.fi (A15), eIDAS (C21), multi-org (A2–A7), Liite 2.6 security, workflow/process engine. Innovation Board deck covers 8 PFRs; #437273 added post-session.
      </Callout>

      <Grid columns={4} gap={12}>
        <Stat value={PORTFOLIO_COUNT} label="Commitment PFRs" />
        <Stat value={orphanCount} label="Not on epic (#430291)" tone="warning" />
        <Stat value={roadmapCounts["B — Accelerate"] + roadmapCounts["C — Strategic"]} label="B + C roadmap conflict" tone="warning" />
        <Stat value="1" label="XL Features (#437273)" tone="danger" />
        <Stat value={String(TENDER_MANDATORY)} label="Pakollinen tender reqs" tone="danger" />
        <Stat value="55–90 mo" label="PFR portfolio effort" tone="warning" />
      </Grid>

      <Row gap={12}>
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
          options={["All", ...ROADMAP_ALIGNMENTS].map((c) => ({ value: c, label: c }))}
        />
      </Row>

      <Grid columns={2} gap={16}>
        <Card>
          <CardHeader>Gap profile (RFI evidence)</CardHeader>
          <CardBody>
            <UsageBar
              total={PORTFOLIO_COUNT}
              topLeftLabel="Innovation Board deck + product evidence"
              topRightLabel={`${gapCounts.Partial} Partial · no tender-tool ratings yet`}
              segments={[{ id: "p", value: gapCounts.Partial, color: "orange" }]}
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
              height={220}
              categories={["A · Aligns", "B · Accelerate", "C · Strategic", "D · Low priority"]}
              series={[
                {
                  name: "PFRs",
                  data: [
                    roadmapCounts["A — Aligns"],
                    roadmapCounts["B — Accelerate"],
                    roadmapCounts["C — Strategic"],
                    roadmapCounts["D — Low priority"],
                  ],
                },
              ]}
            />
          </CardBody>
        </Card>
      </Grid>

      <CollapsibleSection title={`PFR matrix (${sorted.length} shown)`} defaultOpen>
        <Table
          headers={["ID", "Ref", "Title", "On epic", "State", "Cluster", "Size", "Gap", "Risk", "Owner", "Roadmap"]}
          rows={tableRows}
        />
      </CollapsibleSection>

      <CollapsibleSection title="PFR detail notes">
        {sortRows(PFR_ROWS).map((r) => (
          <Row key={r.id} gap={8} style={{ marginBottom: 8 }}>
            <Link href={`${ADO_BASE}/${r.id}`}>#{r.id}</Link>
            <Text>
              <strong>{r.magnitude}</strong> · {r.gap} · {r.roadmap} ({r.roadmapRef}) — {r.note}
            </Text>
          </Row>
        ))}
      </CollapsibleSection>
    </Stack>
  );
}

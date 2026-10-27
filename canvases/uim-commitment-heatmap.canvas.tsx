import {
  BarChart,
  Callout,
  Card,
  CardBody,
  CardHeader,
  Grid,
  H1,
  H2,
  H3,
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
  roadmap: RoadmapAlign;
  roadmapRef: string;
  note?: string;
};

const ROADMAP_SOURCE = "Public 360° roadmap (PPT, Q1 2026–Q2 2027) vs UIM build complete Sep 2027";
const ROADMAP_ALIGNMENTS: RoadmapAlign[] = ["A — Aligns", "B — Accelerate", "C — Strategic", "D — Low priority"];

const PFR_ROWS: PfrRow[] = [
  { id: 433895, ref: "EK-6 / EK-1", title: "Customer entities platform + Udlændingeoverblik", cluster: "Platform spine", module: "Custom fields", magnitude: "XL", gap: "Draft needed", risk: "High", phase: "Gate decision", owner: "Claus", roadmap: "B — Accelerate", roadmapRef: "Full Flex UI cont.", note: "Hub program; scope exceeds FFUI waves" },
  { id: 433881, ref: "MK-6", title: "Retention/deletion on all entities", cluster: "Platform spine", module: "Disposal and Retention", magnitude: "XL", gap: "Partial", risk: "High", phase: "Gate decision", owner: "Morten", roadmap: "B — Accelerate", roadmapRef: "Full Flex UI cont. (433895 satellite)" },
  { id: 433883, ref: "MK-80", title: "Mass update on contacts & custom entities", cluster: "Platform spine", module: "Massupdate", magnitude: "XL", gap: "Not met", risk: "High", phase: "Gate decision", owner: "Torben", roadmap: "B — Accelerate", roadmapRef: "Full Flex UI cont." },
  { id: 433887, ref: "K-11 / K-12", title: "Configuration import/export module", cluster: "Platform admin", module: "UI Configuration", magnitude: "XL", gap: "Not met", risk: "High", phase: "Gate decision", owner: "Anton", roadmap: "B — Accelerate", roadmapRef: "Config migration tool", note: "Export breadth may exceed migration tool" },
  { id: 435597, ref: "EK-5", title: "Configurable rules and validations", cluster: "Platform spine", module: "Custom fields", magnitude: "L", gap: "TBD", risk: "High", phase: "Gate decision", owner: "Torben / Claus", roadmap: "A — Aligns", roadmapRef: "Business Rules Engine", note: "Evaluation criterion; partial fit" },
  { id: 435603, ref: "EK-6", title: "Configurable icons", cluster: "Platform spine", module: "Custom fields", magnitude: "M", gap: "TBD", risk: "Medium", phase: "Gate decision", owner: "Torben", roadmap: "D — Low priority", roadmapRef: "—", note: "Low market potential" },
  { id: 433882, ref: "MK-66+", title: "Full Flex advanced search", cluster: "Search / FFUI", module: "Search", magnitude: "XL", gap: "Partial", risk: "High", phase: "Gate decision", owner: "Jarle", roadmap: "B — Accelerate", roadmapRef: "360° Søkeassistent + Refactor search experience" },
  { id: 433884, ref: "MK-84+", title: "Full Flex detail webparts / columns", cluster: "Search / FFUI", module: "Webparts", magnitude: "XL", gap: "Not met", risk: "High", phase: "Gate decision", owner: "Torben", roadmap: "B — Accelerate", roadmapRef: "Full Flex UI cont." },
  { id: 435253, ref: "EK-3", title: "UI personalization (search, lists, detail views)", cluster: "Search / FFUI", module: "UI-UX", magnitude: "XL", gap: "Draft needed", risk: "High", phase: "Gate decision", owner: "Claus / Jarle", roadmap: "B — Accelerate", roadmapRef: "Full Flex UI cont. + search refactor", note: "Overlaps 433882/433884" },
  { id: 435606, ref: "MK-66+ / EK-3", title: "All listviews configurable with all first-level metadata", cluster: "Search / FFUI", module: "Search", magnitude: "XL", gap: "TBD", risk: "High", phase: "Gate decision", owner: "Jarle / Torben", roadmap: "B — Accelerate", roadmapRef: "Full Flex UI cont. + search refactor", note: "Universal listviews not on roadmap" },
  { id: 435257, ref: "MK-77", title: "No limit on list/search result counts", cluster: "Search / UI", module: "Search", magnitude: "M", gap: "Not met", risk: "High", phase: "Gate decision", owner: "Willy / Jarle", roadmap: "C — Strategic", roadmapRef: "—", note: "Bid blocker; architecture change" },
  { id: 433877, ref: "MK-30", title: "Hierarchical case collections in search lists", cluster: "Search / UI", module: "Search", magnitude: "M", gap: "Not met", risk: "Medium", phase: "Q&A / clarify", owner: "Eva", roadmap: "C — Strategic", roadmapRef: "—" },
  { id: 435258, ref: "EK-12", title: "Create/update Activities via API", cluster: "API / integration", module: "SIF", magnitude: "M", gap: "In flight", risk: "Medium", phase: "Build if bid", owner: "Nikita", roadmap: "A — Aligns", roadmapRef: "NG Integration API / 360° API Gateway", note: "Linked to WI 377061" },
  { id: 433889, ref: "K-16", title: "LibreOffice support", cluster: "Integrations", module: "Integrations", magnitude: "L", gap: "Not met", risk: "Medium", phase: "Gate decision", owner: "Anton", roadmap: "A — Aligns", roadmapRef: "Office alternatives" },
  { id: 433891, ref: "K-17", title: "Evolution mail client integration", cluster: "Integrations", module: "Integrations", magnitude: "L", gap: "Not met", risk: "Medium", phase: "Gate decision", owner: "Anton", roadmap: "B — Accelerate", roadmapRef: "Office alternatives" },
  { id: 435203, ref: "K-17", title: "Alternative email clients (duplicate scope)", cluster: "Integrations", module: "Integrations", magnitude: "L", gap: "TBD", risk: "Medium", phase: "Q&A / clarify", owner: "Hans", roadmap: "D — Low priority", roadmapRef: "—", note: "Dedupe with 433891" },
  { id: 433894, ref: "MK-20 (UUID)", title: "UUID across all logging", cluster: "Logging / audit", module: "Logs", magnitude: "L", gap: "TBD", risk: "Medium", phase: "Gate decision", owner: "Willy", roadmap: "C — Strategic", roadmapRef: "—", note: "Overlap with 435333" },
  { id: 435333, ref: "MK-20", title: "Log separation & transaction traceability", cluster: "Logging / audit", module: "Logs", magnitude: "L", gap: "TBD", risk: "Medium", phase: "Gate decision", owner: "Hans", roadmap: "C — Strategic", roadmapRef: "—", note: "Broader than 433894" },
  { id: 433885, ref: "MK-99", title: "Workflow history report on completion", cluster: "Workflow", module: "Workflow", magnitude: "M", gap: "Not met", risk: "Medium", phase: "Q&A / clarify", owner: "Torben", roadmap: "C — Strategic", roadmapRef: "—" },
  { id: 433886, ref: "MK-120", title: "Mask definition through web-admin", cluster: "Admin / security", module: "Web admin", magnitude: "M", gap: "TBD", risk: "Medium", phase: "Gate decision", owner: "Anton", roadmap: "C — Strategic", roadmapRef: "—" },
  { id: 433888, ref: "MK-133", title: "Report: entities no user can access", cluster: "Admin / security", module: "Access matrix", magnitude: "M", gap: "Not met", risk: "Medium", phase: "Gate decision", owner: "Eva", roadmap: "C — Strategic", roadmapRef: "—" },
  { id: 433892, ref: "MK-169", title: "Failed document dispatch notification", cluster: "Dispatch", module: "Dispatch", magnitude: "M", gap: "Not met", risk: "Medium", phase: "Build if bid", owner: "Hans", roadmap: "C — Strategic", roadmapRef: "—" },
  { id: 433893, ref: "K-18", title: "Split large document dispatches", cluster: "Dispatch", module: "Dispatch", magnitude: "M", gap: "Not met", risk: "Medium", phase: "Build if bid", owner: "Hans", roadmap: "C — Strategic", roadmapRef: "—" },
  { id: 435336, ref: "MK-165", title: "Remote Print configuration", cluster: "Dispatch", module: "Dispatch", magnitude: "M", gap: "TBD", risk: "Medium", phase: "Build if bid", owner: "Hans", roadmap: "C — Strategic", roadmapRef: "—" },
  { id: 435338, ref: "MK-167", title: "Dispatch channel (physical mail)", cluster: "Dispatch", module: "Dispatch", magnitude: "M", gap: "TBD", risk: "Medium", phase: "Build if bid", owner: "Hans", roadmap: "C — Strategic", roadmapRef: "—" },
  { id: 433880, ref: "MK-56", title: "Duplicate contact prevention", cluster: "Point fix", module: "Contact", magnitude: "S", gap: "Partial", risk: "Low", phase: "Build if bid", owner: "Panu", roadmap: "D — Low priority", roadmapRef: "—", note: "~40h ballpark" },
  { id: 433890, ref: "MK-145", title: "Archiving datetime in Outlook", cluster: "Integrations", module: "Outlook client sidepanel", magnitude: "S", gap: "Partial", risk: "Low", phase: "Build if bid", owner: "Anton", roadmap: "A — Aligns", roadmapRef: "New Outlook Support cont." },
];

const PARENT_ID = 433876;
const ADO_BASE = "https://dev.azure.com/tieto-si/360/_workitems/edit";
const LAST_ADO_CHECK = "17 Aug 2026, 09:44 CET";
const PORTFOLIO_COUNT = 27;

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

export default function UimCommitmentHeatmap() {
  const [clusterFilter, setClusterFilter] = useCanvasState<string>("clusterFilter", "All");
  const [roadmapFilter, setRoadmapFilter] = useCanvasState<string>("roadmapFilter", "All");

  const filtered = PFR_ROWS.filter((r) => {
    if (clusterFilter !== "All" && r.cluster !== clusterFilter) return false;
    if (roadmapFilter !== "All" && r.roadmap !== roadmapFilter) return false;
    return true;
  });
  const sorted = sortRows(filtered);

  const gapCounts = countBy(filtered, "gap", ["Not met", "Partial", "Draft needed", "In flight", "TBD"] as GapStatus[]);
  const roadmapCounts = countBy(filtered, "roadmap", ROADMAP_ALIGNMENTS);
  const magCounts = countBy(filtered, "magnitude", ["XL", "L", "M", "S"] as Magnitude[]);
  const accelerateCount = roadmapCounts["B — Accelerate"];
  const strategicCount = roadmapCounts["C — Strategic"];

  const tableRows = sorted.map((row) => [
      <Link href={`${ADO_BASE}/${row.id}`}>{row.id}</Link>,
      row.ref,
      row.title,
      row.roadmap,
      row.roadmapRef,
      row.cluster,
      row.magnitude,
      row.gap,
      row.risk,
      row.owner,
      row.note ?? "",
    ]);

  const rowTones = sorted.map((row) => roadmapTone(row.roadmap));

  return (
    <Stack gap={20} style={{ padding: 16, maxWidth: 1200 }}>
      <Stack gap={6}>
        <H1>UIM 2026 tender — commitment heatmap</H1>
        <Text tone="secondary" size="small">
          Parent{" "}
          <Link href={`${ADO_BASE}/${PARENT_ID}`}>#{PARENT_ID}</Link> · {PORTFOLIO_COUNT} related Features · ADO verified {LAST_ADO_CHECK}
        </Text>
      </Stack>

      <Grid columns={5} gap={12}>
        <Stat value={filtered.length} label="PFRs in view" />
        <Stat value={accelerateCount} label="B — Accelerate" tone="warning" />
        <Stat value={strategicCount} label="C — Strategic off-roadmap" tone="danger" />
        <Stat value={roadmapCounts["A — Aligns"]} label="A — Aligns" tone="success" />
        <Stat value={`${magCounts.XL}`} label="XL magnitude" tone="warning" />
      </Grid>

      <Callout tone="info" title="Roadmap alignment vs UIM delivery (Sep 2027)">
        Mapped against {ROADMAP_SOURCE}. UIM is not mostly “deliver planned roadmap on time” — {accelerateCount} Features need roadmap acceleration and {strategicCount} are strategically relevant but not on the roadmap today.
      </Callout>

      <Card>
        <CardHeader>Roadmap alignment profile</CardHeader>
        <CardBody>
          <UsageBar
            total={filtered.length}
            topLeftLabel={`${filtered.length} PFRs`}
            topRightLabel="A Aligns · B Accelerate · C Strategic · D Low priority"
            segments={[
              { id: "a-aligns", value: roadmapCounts["A — Aligns"], color: "green" },
              { id: "b-accelerate", value: roadmapCounts["B — Accelerate"], color: "orange" },
              { id: "c-strategic", value: roadmapCounts["C — Strategic"], color: "red" },
              { id: "d-low", value: roadmapCounts["D — Low priority"], color: "gray" },
            ]}
          />
          <Row gap={12} wrap style={{ marginTop: 12 }}>
            <Text size="small" tone="secondary">A — Aligns: {roadmapCounts["A — Aligns"]}</Text>
            <Text size="small" tone="secondary">B — Accelerate: {roadmapCounts["B — Accelerate"]}</Text>
            <Text size="small" tone="secondary">C — Strategic: {roadmapCounts["C — Strategic"]}</Text>
            <Text size="small" tone="secondary">D — Low priority: {roadmapCounts["D — Low priority"]}</Text>
          </Row>
        </CardBody>
      </Card>

      <Card>
        <CardHeader>Gap status distribution</CardHeader>
        <CardBody>
          <UsageBar
            total={filtered.length}
            topLeftLabel={`${filtered.length} PFRs`}
            topRightLabel="Count by tender-tool gap rating"
            segments={[
              { id: "not-met", value: gapCounts["Not met"], color: "red" },
              { id: "partial", value: gapCounts.Partial, color: "orange" },
              { id: "draft", value: gapCounts["Draft needed"], color: "blue" },
              { id: "in-flight", value: gapCounts["In flight"], color: "green" },
              { id: "tbd", value: gapCounts.TBD, color: "gray" },
            ]}
          />
          <Row gap={12} wrap style={{ marginTop: 12 }}>
            <Text size="small" tone="secondary">Not met: {gapCounts["Not met"]}</Text>
            <Text size="small" tone="secondary">Partial: {gapCounts.Partial}</Text>
            <Text size="small" tone="secondary">Draft needed: {gapCounts["Draft needed"]}</Text>
            <Text size="small" tone="secondary">In flight: {gapCounts["In flight"]}</Text>
            <Text size="small" tone="secondary">TBD: {gapCounts.TBD}</Text>
          </Row>
        </CardBody>
      </Card>

      <Grid columns={2} gap={16}>
        <Stack gap={8}>
          <H3>Roadmap alignment (filtered)</H3>
          <BarChart
            horizontal
            categories={["A · Aligns", "B · Accelerate", "C · Strategic", "D · Low priority"]}
            series={[{
              name: "PFR count",
              data: [
                roadmapCounts["A — Aligns"],
                roadmapCounts["B — Accelerate"],
                roadmapCounts["C — Strategic"],
                roadmapCounts["D — Low priority"],
              ],
              tone: "warning",
            }]}
            showValues
            height={220}
          />
          <Text tone="tertiary" size="small">
            Source: Public 360° roadmap PPT (Aug 2026). Cluster-owner validation pending.
          </Text>
        </Stack>
        <Stack gap={8}>
          <H3>Filters</H3>
          <Select
            value={clusterFilter}
            onChange={setClusterFilter}
            options={CLUSTERS.map((c) => ({
              value: c,
              label: c === "All" ? "All clusters" : `${c} (${PFR_ROWS.filter((r) => r.cluster === c).length})`,
            }))}
          />
          <Select
            value={roadmapFilter}
            onChange={setRoadmapFilter}
            options={[
              { value: "All", label: "All roadmap statuses" },
              ...ROADMAP_ALIGNMENTS.map((r) => ({
                value: r,
                label: `${r} (${PFR_ROWS.filter((p) => p.roadmap === r).length})`,
              })),
            ]}
          />
        </Stack>
      </Grid>

      <Stack gap={8}>
        <H2>PFR portfolio detail</H2>
        <Table
          headers={["ID", "Ref", "Title", "Roadmap", "Roadmap ref", "Cluster", "Size", "Gap", "Risk", "Owner", "Notes"]}
          rows={tableRows}
          rowTone={rowTones}
          striped
          stickyHeader
          columnAlign={["left", "left", "left", "center", "left", "left", "center", "center", "center", "left", "left"]}
        />
      </Stack>

      <Card variant="borderless">
        <CardHeader>Hygiene follow-ups</CardHeader>
        <CardBody>
          <Stack gap={6}>
            <Text size="small">Merge or cross-link MK-20 pair: 433894 vs 435333.</Text>
            <Text size="small">Resolve K-17 duplicate: 433891 vs 435203.</Text>
            <Text size="small">Clarify EK-3 / FFUI overlap: 435253 vs 433882 / 433884 / 435606.</Text>
            <Text size="small">Rate new PFRs 435597, 435603, 435606 in tender tool (currently TBD).</Text>
            <Text size="small">Impacted Module set on all 27 PFRs (Aug 14–17, 2026).</Text>
          </Stack>
        </CardBody>
      </Card>

      <Text tone="quaternary" size="small">
        Magnitude bands (conservative effort): XL = multi-team platform (Search/FFUI cluster 25–40 months net); L = 4–8 months; M = 2–5 months; S = &lt;1 month. Includes test and integration margin. Gap ratings from UIM tender tool where available; TBD = new Features not yet rated (435597, 435603, 435606).
      </Text>
    </Stack>
  );
}

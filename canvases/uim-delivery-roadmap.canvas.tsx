import {
  Callout,
  Card,
  CardBody,
  CardHeader,
  Grid,
  H1,
  H2,
  H3,
  Link,
  Pill,
  Row,
  Stack,
  Stat,
  Table,
  Text,
  UsageBar,
  useHostTheme,
} from "cursor/canvas";

type Phase = "Now" | "Q4 2026" | "Q1 2027" | "Q2 2027" | "Sep 2027";
type Team = "Core UI + Core BL" | "Core Integration" | "Process Platform";
type Gap = "Not met" | "Partial" | "In flight" | "TBD" | "Aligns";

type Initiative = {
  id: string;
  team: Team;
  title: string;
  problem: string;
  tenderRefs: string;
  pfrIds: string;
  gap: Gap;
  startPhase: Phase;
  endPhase: Phase;
  startNow: boolean;
  dependency?: string;
};

const ADO = "https://dev.azure.com/tieto-si/360/_workitems/edit";
const SOURCE = "UIM ESDH tender tool · 27 commitment Features (#433876) · management gate brief Aug 2026";
const BUILD_DEADLINE =
  "Build complete 1 Sep 2027 · Go-live Oct 2027 · Award ~Nov 2026 · Search MVP target Q4 2026 (compressed)";

const PHASES: Phase[] = ["Now", "Q4 2026", "Q1 2027", "Q2 2027", "Sep 2027"];

const INITIATIVES: Initiative[] = [
  {
    id: "search-unified-surface",
    team: "Core UI + Core BL",
    title: "Unified search surface (Search Assistant + query builder)",
    problem:
      "Users expect combined multi-field, cross-entity search in one place — not three parallel mental models (Global / Advanced / Assistant).",
    tenderRefs: "MK-66, MK-73, MK-74, MK-75, K-4",
    pfrIds: "433882",
    gap: "Partial",
    startPhase: "Now",
    endPhase: "Q4 2026",
    startNow: true,
    dependency: "MVP for bid narrative by Nov 2026; hardening in Q1 2027 only",
  },
  {
    id: "search-mk77",
    team: "Core UI + Core BL",
    title: "Unbounded search & list results (MK-77)",
    problem:
      "Tender requires displaying large result sets without hard caps. Current architecture limits list/search counts — bid blocker.",
    tenderRefs: "MK-77",
    pfrIds: "435257",
    gap: "Not met",
    startPhase: "Now",
    endPhase: "Q4 2026",
    startNow: true,
    dependency: "Architecture decision by mid-Sep 2026; blocks all list work",
  },
  {
    id: "search-ui-layer",
    team: "Core UI + Core BL",
    title: "Listviews & personalization — alt UI layer (not FIB)",
    problem:
      "435606 / EK-3 / MK-84+ via FIB+FFUI is 25–40 months net effort — too slow. Explore thin React shell, Search Assistant host, or generated views on existing APIs instead of full FIB extension.",
    tenderRefs: "MK-66+, EK-3, MK-84+",
    pfrIds: "435606, 435253, 433884",
    gap: "TBD",
    startPhase: "Now",
    endPhase: "Q2 2027",
    startNow: true,
    dependency: "UI layer spike (Sep 2026) gates scope: alt shell vs FIB/FFUI vs hybrid",
  },
  {
    id: "search-hierarchy",
    team: "Core UI + Core BL",
    title: "Hierarchical case collections in search lists",
    problem: "Search result lists must support hierarchical case collection structures (parent/child cases).",
    tenderRefs: "MK-30",
    pfrIds: "433877",
    gap: "Not met",
    startPhase: "Q2 2027",
    endPhase: "Q2 2027",
    startNow: false,
    dependency: "Q&A narrow to evaluation-only or defer post go-live",
  },
  {
    id: "api-activities",
    team: "Core Integration",
    title: "Activities create/update via API (EK-12)",
    problem: "External systems must create and update Activities through a documented REST API — not UI-only flows.",
    tenderRefs: "EK-12",
    pfrIds: "435258",
    gap: "In flight",
    startPhase: "Now",
    endPhase: "Q4 2026",
    startNow: true,
    dependency: "Linked to WI 377061 — lowest gate risk if closed before bid lock",
  },
  {
    id: "api-mass-update",
    team: "Core Integration",
    title: "Mass update API & bulk operations (MK-80)",
    problem:
      "Bulk update of contacts and customer-created entities is not supported today. Requires API orchestration, audit trail, and async job patterns.",
    tenderRefs: "MK-80",
    pfrIds: "433883",
    gap: "Not met",
    startPhase: "Now",
    endPhase: "Q1 2027",
    startNow: true,
    dependency: "Entity model breadth from 433895; UI may use alt layer not FIB Massupdate",
  },
  {
    id: "bre-mvp",
    team: "Process Platform",
    title: "Business Rules Engine — platform MVP",
    problem:
      "Platform needs a rules execution layer for workflow-adjacent automation. Existing roadmap targets MVP in 6.11 stretch (eDoc caseclose).",
    tenderRefs: "— (platform)",
    pfrIds: "—",
    gap: "Aligns",
    startPhase: "Now",
    endPhase: "Q4 2026",
    startNow: true,
  },
  {
    id: "bre-validations",
    team: "Process Platform",
    title: "Configurable rules & validations on entities (EK-5)",
    problem:
      "Customer-configurable validation rules on standard and custom fields — evaluation criterion, not just minimum requirement.",
    tenderRefs: "EK-5",
    pfrIds: "435597",
    gap: "TBD",
    startPhase: "Q1 2027",
    endPhase: "Q2 2027",
    startNow: false,
    dependency: "Extends BRE MVP; ties to custom fields / 433895 platform spine",
  },
];

type Experiment = {
  tool: string;
  track: string;
  purpose: string;
  timebox: string;
  successCriteria: string;
};

const ACCELERATION_EXPERIMENTS: Experiment[] = [
  {
    tool: "BMAD (spec-driven)",
    track: "Search",
    purpose:
      "Run bmad-investigate → bmad-product-brief → bmad-spec → bmad-create-architecture on search-experience information-package. Compress discovery from weeks to days with structured artifacts.",
    timebox: "Sep 2026 (2 weeks)",
    successCriteria: "Architecture decision doc + UI layer recommendation ready for Sep gate",
  },
  {
    tool: "BMAD (spec-driven)",
    track: "Integration + PP",
    purpose:
      "Reuse BRE information-package pattern for EK-12 closure spec and mass-update API contract before implementation.",
    timebox: "Sep–Oct 2026",
    successCriteria: "OpenAPI + acceptance criteria signed by Integration lead",
  },
  {
    tool: "Paperclip (agent orchestration)",
    track: "Search + Integration",
    purpose:
      "Pilot self-hosted Paperclip to orchestrate Cursor/Claude agents against ADO backlog: spike tasks, test generation, boilerplate API handlers. Heartbeat-driven checkout avoids double-work.",
    timebox: "Sep 2026 spike · Oct decision",
    successCriteria: "≥1 vertical slice (e.g. MK-66 query builder panel) delivered with measured human-review ratio",
  },
  {
    tool: "AI-generated code (Cursor agents)",
    track: "All tracks",
    purpose:
      "BMAD spec + ADO story as input; agent generates BL handlers, API controllers, React views. Human owns architecture, review, and merge. Not unreviewed autopilot.",
    timebox: "Ongoing from Sep 2026",
    successCriteria: "Team agrees code-gen eligible zones (green) vs forbidden (red: security, MK-77 core pagination)",
  },
  {
    tool: "Alt UI layer spike",
    track: "Search",
    purpose:
      "Compare FIB/FFUI extension vs thin React host (Search Assistant shell) vs generated list components on search API. Target 3–5× faster UI iteration.",
    timebox: "Sep 2026 (1 week)",
    successCriteria: "Go/no-go on FIB dependency for search MVP; fallback path documented",
  },
];

type DecisionItem = {
  id: string;
  category: "Strategy" | "Architecture" | "Delivery" | "Tender";
  question: string;
  options: string;
  deadline: string;
  owner: string;
};

const DECISIONS: DecisionItem[] = [
  {
    id: "D1",
    category: "Strategy",
    question: "Can we credibly deliver the full UIM portfolio on the current FFUI/FIB path?",
    options: "A) No — compress scope + alt UI + AI acceleration · B) Partial bid via Q&A · C) Full commit (needs 9–14 FTE peak)",
    deadline: "Sep 2026",
    owner: "Program / DG",
  },
  {
    id: "D2",
    category: "Architecture",
    question: "Search UI layer: extend FIB/FFUI or ship a separate React shell?",
    options: "A) Search Assistant host (recommended for speed) · B) FIB/FFUI full extension · C) Hybrid (MVP shell, FIB later)",
    deadline: "Mid-Sep 2026",
    owner: "Core UI + Search lead",
  },
  {
    id: "D3",
    category: "Architecture",
    question: "MK-77: how do we serve unbounded result sets without breaking performance?",
    options: "Cursor/streaming · virtual scroll + server paging · async export-only for large sets · Q&A cap (last resort)",
    deadline: "Mid-Sep 2026",
    owner: "Core BL + Search",
  },
  {
    id: "D4",
    category: "Delivery",
    question: "What is the search MVP for Nov 2026 award gate vs Sep 2027 build complete?",
    options: "MK-66 partial met + MK-77 plan · include MK-74/75 configurability · defer 435606 listviews to phased delivery",
    deadline: "Sep 2026",
    owner: "Morten / tender owner",
  },
  {
    id: "D5",
    category: "Delivery",
    question: "Where is AI-generated code allowed?",
    options: "Green: API boilerplate, tests, UI components from spec · Yellow: BL query logic · Red: auth, pagination core, audit",
    deadline: "Sep 2026",
    owner: "Tech leads per track",
  },
  {
    id: "D6",
    category: "Delivery",
    question: "Paperclip pilot: adopt for UIM program or stay Cursor-only?",
    options: "Pilot on Search spike · Pilot on Integration API · No — BMAD + Cursor sufficient",
    deadline: "Oct 2026",
    owner: "Program + team leads",
  },
  {
    id: "D7",
    category: "Strategy",
    question: "433895 customer entities platform — in, partial, or out?",
    options: "Full hub · Phased (Udlændingeoverblik first) · Q&A narrow · Out (blocks MK-80/EK-5 breadth)",
    deadline: "Sep 2026",
    owner: "Claus / program",
  },
  {
    id: "D8",
    category: "Tender",
    question: "435606 universal listviews — minimum requirement or evaluation stretch?",
    options: "Q&A clarify · Commit partial (search lists only) · Alt UI generated columns · Defer post go-live",
    deadline: "Oct 2026 (Q&A window)",
    owner: "Tender owner",
  },
  {
    id: "D9",
    category: "Strategy",
    question: "Replace vs coexist: does Search Assistant retire Advanced Search UI?",
    options: "Replace at MVP · Unified entry (simple/power modes) · Coexist (higher maintenance)",
    deadline: "Sep 2026 (BMAD brief)",
    owner: "Search product owner",
  },
  {
    id: "D10",
    category: "Tender",
    question: "MK-30 hierarchical collections — in scope for Oct 2027?",
    options: "Commit · Evaluation only · Q&A out",
    deadline: "Oct 2026",
    owner: "Tender owner",
  },
];

const DEFERRED = [
  { cluster: "Platform spine", refs: "EK-6, MK-6, K-11/K-12", pfrs: "433895, 433881, 433887, 435603", note: "Hub decision gate — 433895 blocks mass update & validations breadth" },
  { cluster: "Office / mail integrations", refs: "K-16, K-17, MK-145", pfrs: "433889, 433891, 433890", note: "LibreOffice, Evolution, Outlook datetime" },
  { cluster: "Dispatch / Strålfors", refs: "MK-169, K-18, MK-165, MK-167", pfrs: "433892, 433893, 435336, 435338", note: "Physical mail channel assumptions" },
  { cluster: "Logging / audit", refs: "MK-20", pfrs: "433894, 435333", note: "Merge duplicate Features before commitment" },
  { cluster: "Admin / workflow / security", refs: "MK-99, MK-120, MK-133", pfrs: "433885, 433886, 433888", note: "Medium priority; Q&A on minimum vs evaluation" },
];

function gapTone(gap: Gap): "danger" | "warning" | "success" | "info" | "neutral" {
  if (gap === "Not met") return "danger";
  if (gap === "Partial" || gap === "TBD") return "warning";
  if (gap === "In flight" || gap === "Aligns") return "success";
  return "neutral";
}

function gapRowTone(gap: Gap): "danger" | "warning" | "success" | "info" | undefined {
  if (gap === "Not met") return "danger";
  if (gap === "Partial" || gap === "TBD") return "warning";
  if (gap === "In flight" || gap === "Aligns") return "success";
  return undefined;
}

function phaseIndex(phase: Phase): number {
  return PHASES.indexOf(phase);
}

function TeamSwimlane({ team, color }: { team: Team; color: string }) {
  const items = INITIATIVES.filter((i) => i.team === team);
  const startNow = items.filter((i) => i.startNow);

  return (
    <Card>
      <CardHeader trailing={<Pill tone="info">{items.length} initiatives</Pill>}>
        <Row style={{ alignItems: "center", gap: 8 }}>
          <div style={{ width: 4, height: 20, background: color, borderRadius: 2 }} />
          {team}
        </Row>
      </CardHeader>
      <CardBody>
        <Stack gap={16}>
          {startNow.length > 0 && (
            <Stack gap={8}>
              <Text size="small" weight="semibold" tone="secondary">
                Start now ({startNow.length})
              </Text>
              {startNow.map((item) => (
                <InitiativeCard key={item.id} item={item} accent={color} />
              ))}
            </Stack>
          )}
          {items.filter((i) => !i.startNow).length > 0 && (
            <Stack gap={8}>
              <Text size="small" weight="semibold" tone="secondary">
                Follow-on
              </Text>
              {items
                .filter((i) => !i.startNow)
                .map((item) => (
                  <InitiativeCard key={item.id} item={item} accent={color} compact />
                ))}
            </Stack>
          )}
        </Stack>
      </CardBody>
    </Card>
  );
}

function InitiativeCard({ item, accent, compact }: { item: Initiative; accent: string; compact?: boolean }) {
  const start = phaseIndex(item.startPhase);
  const end = phaseIndex(item.endPhase);
  const span = end - start + 1;

  return (
    <div style={{ borderLeft: `3px solid ${accent}`, paddingLeft: 12 }}>
      <Row style={{ alignItems: "baseline", gap: 8, flexWrap: "wrap" }}>
        <Text weight="semibold" size={compact ? "small" : "body"}>
          {item.title}
        </Text>
        <Pill tone={gapTone(item.gap)} size="small">
          {item.gap}
        </Pill>
        {item.startNow && (
          <Pill tone="warning" size="small">
            Start now
          </Pill>
        )}
      </Row>
      {!compact && (
        <Text size="small" tone="secondary" style={{ marginTop: 4 }}>
          {item.problem}
        </Text>
      )}
      <Row style={{ gap: 12, marginTop: 6, flexWrap: "wrap" }}>
        <Text size="small" tone="tertiary">
          {item.tenderRefs}
        </Text>
        {item.pfrIds !== "—" && (
          <Text size="small">
            PFR{" "}
            {item.pfrIds.split(", ").map((id, idx, arr) => (
              <span key={id}>
                <Link href={`${ADO}/${id.trim()}`}>{id.trim()}</Link>
                {idx < arr.length - 1 ? ", " : ""}
              </span>
            ))}
          </Text>
        )}
      </Row>
      <div style={{ marginTop: 8 }}>
        <UsageBar
          total={PHASES.length}
          topLeftLabel={`${item.startPhase} → ${item.endPhase}`}
          topRightLabel={`${span} phase${span > 1 ? "s" : ""}`}
          segments={PHASES.map((phase, idx) => ({
            id: phase,
            value: idx >= start && idx <= end ? 1 : 0,
          }))}
        />
      </div>
      {item.dependency && (
        <Text size="small" tone="secondary" italic style={{ marginTop: 6 }}>
          {item.dependency}
        </Text>
      )}
    </div>
  );
}

export default function UimDeliveryRoadmap() {
  const theme = useHostTheme();
  const cat = theme.category;

  const startNowCount = INITIATIVES.filter((i) => i.startNow).length;
  const notMetCount = INITIATIVES.filter((i) => i.gap === "Not met").length;

  const problemTableRows = INITIATIVES.map((i) => [
    i.team.replace("Core UI + Core BL", "Search").replace("Core Integration", "Integration").replace("Process Platform", "PP"),
    i.tenderRefs,
    i.problem,
    <Pill key={i.id} tone={gapTone(i.gap)} size="small">
      {i.gap}
    </Pill>,
    i.startNow ? "Yes" : "—",
  ]);

  return (
    <Stack gap={24}>
      <Stack gap={8}>
        <H1>UIM ESDH — delivery roadmap (draft)</H1>
        <Text tone="secondary">
          High-level plan to start work before award. Three parallel tracks aligned to product teams.{" "}
          <Link href={`${ADO}/433876`}>ADO #433876</Link>
        </Text>
        <Text size="small" tone="tertiary">
          {SOURCE} · {BUILD_DEADLINE}
        </Text>
      </Stack>

      <Grid columns={4} gap={12}>
        <Stat label="Parallel tracks" value="3" tone="info" />
        <Stat label="Start now" value={String(startNowCount)} tone="warning" />
        <Stat label="Gap: Not met" value={String(notMetCount)} tone="danger" />
        <Stat label="Build window" value="~10 mo" tone="neutral" />
      </Grid>

      <Callout tone="warning" title="Timeline compression — search is on the critical path">
        <Text size="small">
          Original plan (search through Q2 2027 on FIB/FFUI) cannot deliver the full UIM portfolio by Sep 2027. Search MVP
          must land Q4 2026 for bid credibility; MK-77 architecture decided by mid-Sep. Listviews/personalization (435606)
          requires a UI layer decision — FIB extension is the slow path; alt React shell + AI-assisted codegen is the
          fast path under evaluation.
        </Text>
      </Callout>

      <Callout tone="warning" title="Critical path outside these three tracks">
        <Text size="small">
          Customer entities platform (433895 / EK-6) is the hub for mass update breadth, configurable validations, and FFUI
          scope. A go/no-go on 433895 affects Integration and Process Platform follow-ons even if those teams start
          independently now.
        </Text>
      </Callout>

      <H2>Team tracks</H2>
      <Grid columns={1} gap={16}>
        <TeamSwimlane team="Core UI + Core BL" color={cat.blue} />
        <TeamSwimlane team="Core Integration" color={cat.cyan} />
        <TeamSwimlane team="Process Platform" color={cat.green} />
      </Grid>

      <H2>Problems to solve · requirements map</H2>
      <Table
        headers={["Track", "Tender refs", "Problem / requirement", "Gap today", "Start now"]}
        rows={problemTableRows}
        rowTone={INITIATIVES.map((i) => gapRowTone(i.gap))}
        striped
        stickyHeader
      />

      <H2>Acceleration experiments (BMAD · Paperclip · AI codegen)</H2>
      <Table
        headers={["Tool", "Track", "Purpose", "Timebox", "Success criteria"]}
        rows={ACCELERATION_EXPERIMENTS.map((e) => [
          e.tool,
          e.track,
          e.purpose,
          e.timebox,
          e.successCriteria,
        ])}
        striped
      />

      <H2>Decisions to make · questions to answer</H2>
      <Table
        headers={["ID", "Category", "Question", "Options", "Deadline", "Owner"]}
        rows={DECISIONS.map((d) => [d.id, d.category, d.question, d.options, d.deadline, d.owner])}
        striped
        stickyHeader
      />

      <H2>Phased timeline (compressed)</H2>
      <Table
        headers={["Phase", "Search (Core UI + BL)", "Integration", "Process Platform", "Program milestone"]}
        rows={[
          [
            "Now (Aug–Sep 2026)",
            "MK-77 architecture decision; BMAD investigate+brief; alt UI layer spike (FIB vs React shell); Search Assistant MVP scope lock",
            "Close EK-12 / WI 377061; mass update API design; Paperclip pilot on API boilerplate",
            "BRE MVP scoping; BMAD spec for rule model",
            "D1–D5 decisions · acceleration experiments start",
          ],
          [
            "Q4 2026",
            "Search MVP: MK-66 multi-field cross-entity + query builder GA for bid; MK-77 implementation; alt-UI list prototype",
            "Mass update API alpha; async bulk job pattern",
            "BRE MVP delivery (6.11 stretch)",
            "Award gate ~Nov 2026 · search demo-ready",
          ],
          [
            "Q1 2027",
            "Search hardening; MK-74/75 configurability; listviews on chosen UI layer (not full FIB if spike succeeds)",
            "Mass update API beta; integration testing",
            "EK-5 validations on custom entities",
            "Post-award acceleration",
          ],
          [
            "Q2 2027",
            "Personalization (EK-3) scoped to committed minimum; MK-30 only if in scope",
            "Mass update GA; API documentation & compliance evidence",
            "EK-5 GA",
            "Tender compliance hardening · deferrals closed",
          ],
          [
            "Sep 2027",
            "Search/list UAT sign-off",
            "API & bulk UAT sign-off",
            "BRE / validations UAT sign-off",
            "Build complete · Go-live Oct 2027",
          ],
        ]}
        striped
      />

      <H2>Cross-track dependencies</H2>
      <Grid columns={2} gap={12}>
        <Card>
          <CardHeader>Search ↔ Integration</CardHeader>
          <CardBody>
            <Text size="small">
              Mass update UI may use alt layer (not FIB Massupdate) consuming Integration bulk API. Search listviews share
              infrastructure with search refactor — coordinate to avoid duplicate FIB/FFUI work with 433882.
            </Text>
          </CardBody>
        </Card>
        <Card>
          <CardHeader>Integration ↔ Process Platform</CardHeader>
          <CardBody>
            <Text size="small">
              EK-5 validations may invoke BRE for complex rules; mass update may need rule checks before bulk apply.
              Define API contracts early in Q4 2026.
            </Text>
          </CardBody>
        </Card>
        <Card>
          <CardHeader>All tracks ↔ Platform spine</CardHeader>
          <CardBody>
            <Text size="small">
              433895 (customer entities) unlocks full MK-80 and EK-5 scope. Teams can start foundational work now, but
              bid narrative must clarify phased delivery if 433895 is partial.
            </Text>
          </CardBody>
        </Card>
        <Card>
          <CardHeader>Search internal (Core UI + BL split)</CardHeader>
          <CardBody>
            <Text size="small">
              Core BL owns query engine, pagination architecture (MK-77), cross-entity backend. Core UI owns Search
              Assistant, query builder UX, and chosen UI layer (FIB vs alt shell). AI codegen highest value on UI +
              API boilerplate after BMAD spec is locked.
            </Text>
          </CardBody>
        </Card>
      </Grid>

      <H2>Deferred clusters (not in initial three tracks)</H2>
      <Text size="small" tone="secondary" style={{ marginBottom: 8 }}>
        Remaining UIM commitment Features — assign owners and phase after gate decision on platform spine.
      </Text>
      <Table
        headers={["Cluster", "Tender refs", "PFR IDs", "Note"]}
        rows={DEFERRED.map((d) => [d.cluster, d.refs, d.pfrs, d.note])}
        striped
      />

      <H3>Next steps (Sep 2026)</H3>
      <Stack gap={6}>
        <Text size="small">1. Run BMAD investigate + brief on search-experience (2-week timebox) → decisions D2, D4, D9.</Text>
        <Text size="small">2. MK-77 architecture review by mid-Sep — decision D3; unblocks all list work.</Text>
        <Text size="small">3. Alt UI layer spike: FIB/FFUI vs Search Assistant React shell — decision D2 within 1 week.</Text>
        <Text size="small">4. Paperclip pilot: one Search vertical slice + one Integration API handler — decision D6 by Oct.</Text>
        <Text size="small">5. Define AI codegen green/yellow/red zones per team — decision D5.</Text>
        <Text size="small">6. Integration: close WI 377061 before Nov 2026 award gate.</Text>
        <Text size="small">7. Program: resolve 433895 in/out (D7) — affects mass update and EK-5 credibility.</Text>
        <Text size="small">8. Tender: Q&A strategy for 435606 and MK-30 (D8, D10).</Text>
      </Stack>
    </Stack>
  );
}

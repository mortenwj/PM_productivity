import {
  Button,
  Code,
  Divider,
  Grid,
  H1,
  mergeStyle,
  Pill,
  Row,
  Stack,
  Text,
  useHostTheme,
} from "cursor/canvas";

/** Tweak column widths for the three-panel layout. */
const GRID_TEMPLATE = "minmax(260px, 0.95fr) minmax(340px, 1.35fr) minmax(220px, 0.85fr)";

export default function CaseRegistrationLayout() {
  const theme = useHostTheme();

  const page = mergeStyle({
    minHeight: "100%",
    padding: 20,
    background: theme.bg.chrome,
    color: theme.text.primary,
  });

  const panelSurface = mergeStyle({
    background: theme.bg.elevated,
    border: `1px solid ${theme.stroke.tertiary}`,
    borderRadius: 10,
    padding: 16,
    minWidth: 0,
    display: "flex",
    flexDirection: "column",
    gap: 12,
    minHeight: 560,
  });

  const scrollBody = mergeStyle({
    flex: 1,
    minHeight: 0,
    overflow: "auto",
    paddingRight: 4,
  });

  const sectionLabel = mergeStyle({
    fontSize: 11,
    letterSpacing: "0.04em",
    textTransform: "uppercase",
    color: theme.text.tertiary,
    fontWeight: 600,
  });

  const processIndent = mergeStyle({
    borderLeft: `3px solid ${theme.accent.primary}`,
    paddingLeft: 10,
    marginLeft: 4,
  });

  const taskBlock = mergeStyle({
    border: `1px solid ${theme.stroke.tertiary}`,
    borderRadius: 8,
    padding: "10px 12px",
    background: theme.bg.editor,
  });

  const iconCluster = mergeStyle({ flexShrink: 0 });

  return (
    <Stack gap={20} style={page}>
      <Stack gap={12}>
        <Row align="start" justify="space-between" wrap style={{ gap: 12 }}>
          <Row gap={12} align="center" style={{ minWidth: 0 }}>
            <div
              style={mergeStyle({
                width: 36,
                height: 36,
                borderRadius: 8,
                background: theme.fill.secondary,
                border: `1px solid ${theme.stroke.secondary}`,
              })}
              aria-hidden
            />
            <Stack gap={4} style={{ minWidth: 0 }}>
              <H1 style={{ margin: 0, fontSize: 22, lineHeight: 1.2 }}>dddd</H1>
              <Text tone="secondary" size="small">
                Case: 26/00139
              </Text>
            </Stack>
          </Row>
          <Row gap={8} wrap style={iconCluster}>
            <Button variant="secondary">Add bookmark</Button>
            <Button variant="secondary">Share</Button>
            <Button variant="secondary">Add reminder</Button>
          </Row>
        </Row>

        <Row gap={8} wrap>
          <Button variant="secondary">Edit status</Button>
          <Button variant="secondary">Case functions</Button>
          <Button variant="secondary">Edit priority</Button>
          <Button variant="secondary">Go to case overview</Button>
        </Row>
      </Stack>

      <Grid columns={GRID_TEMPLATE} gap={16} align="stretch">
        {/* Left — registration summary */}
        <div style={panelSurface}>
          <Row align="center" justify="space-between" style={{ minHeight: 28 }}>
            <Text weight="semibold">registration</Text>
            <Row gap={8} align="center">
              <Pill active tone="info" size="sm">
                In progress
              </Pill>
              <Button variant="ghost">Edit</Button>
            </Row>
          </Row>
          <Divider />
          <div style={scrollBody}>
            <Stack gap={14}>
              <Stack gap={6}>
                <Text>
                  <Text tone="secondary" as="span">
                    Responsible:{" "}
                  </Text>
                  morten Jensen
                </Text>
                <Row gap={8} align="center" wrap>
                  <Text>
                    <Text tone="secondary" as="span">
                      Deadline:{" "}
                    </Text>
                    No deadline
                  </Text>
                  <Button variant="ghost">Change</Button>
                </Row>
              </Stack>

              <Divider />

              <Stack gap={8}>
                <Row align="center" justify="space-between">
                  <span style={sectionLabel}>Processes</span>
                  <Button variant="ghost">+ Add process</Button>
                </Row>
                <Stack gap={6}>
                  <Row gap={8} align="center" wrap>
                    <Text weight="medium" truncate>
                      Auto…
                    </Text>
                    <Text tone="secondary" size="small" truncate>
                      morten…
                    </Text>
                  </Row>
                  <div style={processIndent}>
                    <Row gap={8} align="center" wrap>
                      <Text weight="medium">Kunngjoring</Text>
                      <Text tone="secondary" size="small">
                        morten Jensen
                      </Text>
                    </Row>
                  </div>
                </Stack>
              </Stack>

              <Divider />

              <Stack gap={8}>
                <Row align="center" justify="space-between">
                  <span style={sectionLabel}>Milestones</span>
                  <Button variant="ghost">+ Add milestone</Button>
                </Row>
              </Stack>
            </Stack>
          </div>
        </div>

        {/* Center — registration details */}
        <div style={panelSurface}>
          <Row align="center" justify="space-between">
            <Text weight="semibold">registration</Text>
            <Text tone="tertiary" size="small">
              Expand
            </Text>
          </Row>
          <Divider />
          <Row align="center" wrap style={{ gap: 8 }}>
            <Text tone="secondary" size="small">
              Due date
            </Text>
            <Text size="small">4/23/2026</Text>
            <Button variant="ghost">Pick</Button>
          </Row>
          <Divider />
          <div style={scrollBody}>
            <Stack gap={10}>
              <Row align="center" justify="space-between">
                <Text weight="semibold">Kunngjoring</Text>
                <Text tone="tertiary" size="small">
                  Expanded
                </Text>
              </Row>

              <div style={taskBlock}>
                <Row align="start" justify="space-between" gap={12}>
                  <Stack gap={4} style={{ minWidth: 0, flex: 1 }}>
                    <Row gap={8} align="center" wrap>
                      <Pill tone="success" size="sm">
                        Done
                      </Pill>
                      <Text weight="medium">dok1</Text>
                    </Row>
                    <Text tone="secondary" size="small">
                      morten Jensen — Closed date: 4/23/2026
                    </Text>
                  </Stack>
                  <Row gap={6} style={iconCluster}>
                    <Button variant="ghost">Refresh</Button>
                    <Button variant="ghost">Info</Button>
                  </Row>
                </Row>
              </div>

              <div style={taskBlock}>
                <Row align="start" justify="space-between" gap={12}>
                  <Stack gap={4} style={{ minWidth: 0, flex: 1 }}>
                    <Text weight="medium">do approval</Text>
                    <Text tone="secondary" size="small">
                      morten Jensen
                    </Text>
                  </Stack>
                  <Row gap={6} wrap style={iconCluster}>
                    <Button variant="ghost">Start</Button>
                    <Button variant="ghost">Remove</Button>
                    <Button variant="ghost">Info</Button>
                    <Button variant="ghost">Edit</Button>
                  </Row>
                </Row>
              </div>

              <div style={taskBlock}>
                <Row align="start" justify="space-between" gap={12}>
                  <Stack gap={4} style={{ minWidth: 0, flex: 1 }}>
                    <Text weight="medium">mail1</Text>
                    <Text tone="secondary" size="small">
                      morten Jensen
                    </Text>
                  </Stack>
                  <Row gap={6} wrap style={iconCluster}>
                    <Button variant="ghost">Start</Button>
                    <Button variant="ghost">Remove</Button>
                    <Button variant="ghost">Info</Button>
                    <Button variant="ghost">Edit</Button>
                  </Row>
                </Row>
              </div>

              <div style={taskBlock}>
                <Row align="start" justify="space-between" gap={12}>
                  <Stack gap={4} style={{ minWidth: 0, flex: 1 }}>
                    <Text weight="medium">brev2</Text>
                    <Text tone="secondary" size="small">
                      morten Jensen
                    </Text>
                  </Stack>
                  <Row gap={6} wrap style={iconCluster}>
                    <Button variant="ghost">Start</Button>
                    <Button variant="ghost">Remove</Button>
                    <Button variant="ghost">Info</Button>
                    <Button variant="ghost">Edit</Button>
                  </Row>
                </Row>
              </div>
            </Stack>
          </div>
        </div>

        {/* Right — checklists */}
        <div style={panelSurface}>
          <Row align="center" justify="space-between">
            <Text weight="semibold" truncate>
              Checklists in case
            </Text>
            <Text tone="tertiary" size="small">
              Expand
            </Text>
          </Row>
          <Divider />
          <Row gap={8} wrap>
            <Pill active tone="info" size="sm">
              Checklist
            </Pill>
            <Pill tone="neutral" size="sm">
              More views
            </Pill>
          </Row>
          <Row gap={8} wrap>
            <Button variant="secondary">Fetch checklist</Button>
            <Button variant="secondary">+ Create checklist</Button>
            <Button variant="secondary">View filters</Button>
          </Row>
          <Divider />
          <div
            style={mergeStyle(scrollBody, {
              alignItems: "center",
              justifyContent: "center",
              display: "flex",
              padding: 24,
            })}
          >
            <Text tone="tertiary" size="small" style={{ textAlign: "center" }}>
              Checklist body (empty in reference). Resize columns via <Code>GRID_TEMPLATE</Code> in
              source.
            </Text>
          </div>
        </div>
      </Grid>
    </Stack>
  );
}

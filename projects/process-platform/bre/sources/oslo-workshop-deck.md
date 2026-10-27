# Oslo BRE workshop deck — summary

**Source:** `Oslo BRE workshop.pptx`  
**Title:** Flexibility in standard — Brief overview (P360 team)  
**Slides:** 16

---

## Slide flow

| # | Title / topic |
|---|---------------|
| 1 | Title — Flexibility in standard |
| 2 | 360 digital value chain: Collect, Engage, **Process**, Publish, Archive |
| 3 | Individual standard: Dynamic UI, Process Modelling, **Responsive Business Logic**, Seamless integration |
| 4 | *(empty)* |
| 5 | Business Rules Engine — Exploring core features and integration |
| 6 | Agenda: Overview, Core Features, UI, Integration, Security, Event-Driven, Sync/Async, Explainability |
| 7 | Overview and Purpose |
| 8 | Introduction to BRE |
| 9 | Rule Designer |
| 10 | Web Interface and Workflow Automation |
| 11 | System Event Triggering |
| 12 | What is a rule (Trigger / Condition / Action) |
| 13 | Example: Prevent mistakes when closing a case |
| 14 | Example: Automatic closing of cases |
| 15 | Other rules (customer examples table) |
| 16 | What types of rules do you need? *(discussion)* |

---

## Slide 8 — Introduction to BRE

- **No-code interface** — define and manage rules without programming
- **Rule invocation** — web UI, workflows, API
- **Customization** — tailor for customer/segment processes

---

## Slide 9 — Rule Designer

- No-code interface for creating rules
- Define conditions: "If X happens, do Y"

---

## Slide 10 — Web & workflow

- User interaction triggers actions in web UI
- Rules embedded in workflows for conditional actions on state changes

---

## Slide 11 — System events

| Trigger source | Example |
|----------------|---------|
| Document status changes | Initiate next process step |
| Workflow state transitions | Task management rules |
| User actions | Form submit, document upload |
| Time-based | Scheduled automated actions |

---

## Slide 12 — Rule structure

### Trigger — The WHEN

- **Event:** case updated, document dispatched, process step completes
- **Scheduled:** daily, once, timed
- **Invoked:** from integration, process, UI

### Condition — The IF

Criteria for rule to execute — precise automation targeting.

Examples:
- Case type "Building" AND process status complete
- Case status → closed AND no decision made
- Document is "contract" AND review due

### Action — The WHAT

- Raise error / prevent action
- Update data (case status, fields)
- Send notification
- Push event to external system

---

## Slide 13 — Example: Close-case validation

**Challenge:** More validation when closing cases

Requirements:
- No general/working documents on case at close
- Mandatory fields (standard + custom) on close
- Prevent case cancel if documents not cancelled

**Rule criteria (from slide):**
1. On case status change (not void): if document count ≠ 0 → raise error
2. On case close: if field X empty → raise error
3. On case cancel: if documents not cancelled → raise error

**Pattern:** Event trigger + Raise Error

---

## Slide 14 — Example: Auto-close

**Challenge:** ~75% of "ready from case worker" cases could auto-close but don't today

**Criteria:**
- Status = "ready from case handler" AND all docs journalized AND all docs have responsible → close case
- Type "technical case": validate matrikkel ID; if not OK → flag for manual follow-up

**Pattern:** Scheduled trigger + Update data

---

## Slide 15 — Other rules (sample rows)

| Invoke | Type | Description |
|--------|------|-------------|
| Event | Raise Error | Empty cases → only Void status allowed |
| Job | Update | Auto-close: one doc type, 90+ days, responsible person |
| Event | Update | Change case responsible → update all documents |
| FFUI | Raise Error | Meeting document file type validation |
| Event | Update | Incoming doc due date from case category |
| Event | Update | Default incoming doc status Registered |

---

## Slide 16 — Discussion

**"What types of rules do you need?"**

Use as workshop prompt — maps to Copenhagen customer day and scope register.

---

## Use in Copenhagen BRE session

| Deck section | Session block |
|--------------|---------------|
| Slides 5–12 | Problem + rule model (Morten/Bjørn, ~35 min) |
| Slides 13–14 | Worked examples (~15 min) |
| Slide 16 | Bridge to customer questions |
| Not in deck | Status, commitments, gaps — team adds live |

# Module Platform Support Overview

*Last updated: 2026-03-17*

This document provides an overview of 360° modules and the platforms they support: **on-prem** (with versions), **public cloud**, and **domestic/private cloud**.

---

## Deployment Types

| Platform | Description |
|----------|-------------|
| **On-prem** | Installed on customer's or partner's own servers. Version-specific (e.g. 5.18 LTS, 5.x). |
| **Public cloud** | Hosted on Microsoft Azure. Data centers in Ireland, Norway, Sweden. Also referred to as "Cloud - Azure EU" and "Cloud - Azure NO". |
| **Domestic/Private cloud** | Hosted in-country or on sovereign/private cloud. Sweden (OneCloud Platinum), Denmark (CloudFactory), Norway/Finland (OneCloud Platinum). |

---

## Main Products (Lead Offerings)

| Product | On-prem | Public cloud | Domestic/Private cloud |
|---------|---------|--------------|------------------------|
| Public 360° | Yes (5.x, 5.18 LTS) | Yes | Yes (SE, DK, NO, FI) |
| Business 360° | Yes (5.x) | Yes | Yes |
| eArchive 360° | Yes (5.2+) | Yes | Yes |
| Plan & Build 360° | No (cloud only) | Yes (NO, SWE) | Yes |
| RDF 360° | No | Yes (SaaS) | TBA |

---

## Public 360° / Business 360° Modules – Platform Support

Most add-on modules are available on all platforms where the lead offering runs. The table below lists modules with **specific platform restrictions**.

### Modules with Platform Restrictions

| Module | On-prem | Public cloud | Domestic/Private cloud | Notes |
|--------|---------|--------------|------------------------|-------|
| 360° Archive Inspector | No | Yes (Azure EU, Azure NO) | No | Public cloud only |
| 360° Mimir | No | Yes (Azure EU, Azure NO) | No | Public cloud only; requires 360° Policy Documents |
| 360° Search Assistant | No | Yes | No | Public cloud only (for now) |
| 360° Collect | Pending (5.18 verification) | Yes (SaaS on Azure) | TBA | Part of RDF; delivered as SaaS |
| 360° OpenGov Cases and Documents | TBA (5.18 LTS) | Yes (v6.5+) | Yes (v6.5+) | Version details vary per lead offering |
| 360° eServices Platform | Yes (5.5+) | Yes | Yes | Status: draining; see 360° eServices Connect |
| 360° eServices Connect | Yes (5.5+) | Yes | Yes | |
| 360° Sign | Yes (5.16+) | No | Yes (Sovereign cloud) | Hosted on Vivicta Sovereign Cloud (SE, NO, FI) |
| 360° eMeetings Prepare | No | Exception (few old AWS) | Yes (Binero) | Primarily domestic cloud |
| 360° eMeetings Live | No | Exception (few old AWS) | Yes (Binero) | Primarily domestic cloud |
| 360° Public Journal | Yes | Yes (Azure Ireland) | Yes | Legacy; replaced by OpenGov Cases and Documents |
| 360° OpenGov Cases | Yes | Yes (Azure Ireland) | Yes | |
| 360° OpenGov Meetings | Yes | Yes (Azure Ireland) | Yes | |

### Modules Typically Available on All Platforms

Most add-on modules are available on **on-prem**, **public cloud**, and **domestic cloud** where the lead offering is supported. Examples:

- 360° AD Sync Service
- 360° Dispatch
- 360° Template Designer
- 360° Format converter
- 360° Board & Council Manager
- 360° Information Act Request
- 360° Contract Management
- 360° Policy Documents
- SIF (Simple Integration Framework)
- 360° Integration with MS Teams
- 360° Integration with SharePoint
- 360° Integration with MS Office Apps
- 360° Process Engine

Check individual module documentation for version requirements.

---

## Plan & Build 360°

Plan & Build 360° is **cloud-only** (no on-prem). Most P&B modules follow the same platform support as Public 360° where applicable.

---

## eArchive 360°

Platform support generally aligns with the main product (on-prem, public cloud, domestic cloud). Add-on modules include 360° Format Converter, 360° Archive Format Validator, 360° File Viewer, and Third Party Integration Tools (SIF only for eArchive).

---

## RDF 360° Modules

| Module | On-prem | Public cloud | Domestic/Private cloud |
|--------|---------|--------------|------------------------|
| 360° Collect | Pending | Yes (SaaS) | TBA |
| 360° Engage | Not released | Not released | Not released |
| 360° RDF Toolbox | Not released | Not released | Not released |

---

## OpenGov Cases and Documents – Version Details

| Source | Cloud | On-prem | Domestic cloud |
|--------|-------|---------|----------------|
| Public 360° | v6.5 (Apr 2025) | v5.18 LTS (TBA) | v6.5 (Apr 2025) |
| eArchive 360° | v6.6 (Sep 2025) | v5.18 LTS (TBA) | v6.6 (next version after 6.6) |
| Plan & Build 360° | v6.8 (MVP) | N/A | v6.x (maybe not needed) |

---

## Sources

- Public 360° Wiki – Module overview, individual module pages
- Hosting solutions for Online offerings
- DomesticCloud
- White spaces report (customer-specific availability)

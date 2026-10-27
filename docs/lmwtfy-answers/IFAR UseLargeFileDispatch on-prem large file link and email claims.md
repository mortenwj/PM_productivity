# IFAR UseLargeFileDispatch, on-prem large file links, and e-mail wording

Colleague testing **UseLargeFileDispatch** for **IFAR** on a customer moving to **5.18**: external recipient cannot download; questions about **“public access”** on the wiki flowchart; link points to **customer 360** and requires **Citrix + 360 user**; Norwegian e-mail says **one person / one download** but forwarding and **multiple downloads** work; wiki says link **2 hours** but e-mail says **1 month**. This note grounds what the **wiki text** actually says, what is **not** in searchable text, and what needs **code or template** confirmation before you promise behaviour to a customer.

---

## Original Question (summary)

- On-prem IFAR, **5.18**, **UseLargeFileDispatch**: external recipient **cannot** download. Wiki flowchart suggests **“public access”** choice. What criterion is **public access**? 360 logic vs on-prem vs online? No cloud storage UI for on-prem; link goes to **customer 360**; needs **360 user** and Citrix; disabled user gives **unknown user**. Is large file dispatch **meant** to work on-prem, and **how**?
- E-mail claims link is **only for you**, **not forwardable**, **one time**; in practice **forwarding** and **multiple people / multiple clicks** work.
- Wiki: link **2 hours**; e-mail: **1 month**. Which is correct?

## Context

Sources: **`user-mediawiki`** (full wiki page and 5.16 section), **`user-ratatoskr`** (admin-en search, **no** hits for large file dispatch / UseLargeFileDispatch strings). **No** ADO item tied.

**Follow-up:** **`gh`** (GitHub CLI) was run successfully after local **`gh auth login`**. Hits and line evidence are in **Step 1 follow-up: GitHub** below.

---

## Findings

### 1. What the wiki page says (authoritative for “2 hours” and 5.16 scope)

**Request for Access Large file dispatch** (Software Innovation Wiki), last revised **2024-06-27**:

https://wiki.software-innovation.com/wiki/Request_for_Access_Large_file_dispatch

Plain facts from the **wikitext** (not from images):

- **Purpose:** dispatch **large files** sent from the **E-mail** channel when the file exceeds the channel limit.
- **When it applies (5.16 wording):** feature toggle **`UseLargeFileDispatch`** is **on**, and the **File size limit** of the **E-mail** dispatch channel for **Access request (recno 5)** is **greater** than the file size to dispatch. The **limit must be set on that channel** in the code table **Document Dispatch Channel**, **not** only under Configuration → Dispatch settings. The page marks that with a warning icon in the prose.
- **After successful dispatch:** a **download link** is sent so the requester can download via the link in the e-mail.
- **Diagram note:** the flow picture is a **roadmap**. **Not everything** in the diagram is in the **5.16** release. **Case party flow** and **digital channels flow** are explicitly **future** scope. **Current** scope in 5.16 is **IFAR dispatch** and **E-mail channel only**.
- **Expiry:** **“Download link will be expired after 2 hours for security reasons.”** After that, clicking the link shows an expiry message (screenshot on wiki).

So for **“2 hours vs 1 month”:** the **wiki product page** states **2 hours**. If the **Norwegian customer e-mail** says **one month**, that is a **direct conflict** with this wiki page. **GitHub (core-bl)** now supports the wiki: **`ShareablePublicFileController.DownloadLargeFile`** calls **`TempStorageManager.UpdateExpiry(intId, TimeSpan.FromHours(2))`** after starting the large-file download stream (see link below). That is **strong evidence** the product uses a **2 hour** window in this path; the e-mail text still needs **template** alignment if it says one month. If **`UpdateExpiry`** extends rather than replaces retention, confirm with a quick read of **`TempStorageManager`** in the same repo.

The same content is duplicated in the **5.16 release information** section for Access Request Large file dispatch:

https://wiki.software-innovation.com/wiki/5.16_release_information

### 2. “Public access” on the flowchart (what we can and cannot prove here)

The wiki page **embeds PNG images** for the roadmap and steps (for example `ClipCapIt-230306-110741.PNG`). **No** phrase like **“public access”** appears in the **wikitext** returned by `mediawiki_get_page`. So:

- Anything you read off the **diagram** (for example branches about **public access**) is **not** captured as searchable text in this pass.
- The wiki **already warns** that the diagram is a **roadmap** and that **case party** and **digital channels** paths are **future**. A branch that sounds like **“customer has public access”** is **plausibly future or non-IFAR-e-mail scope**, not something this page proves for **5.16 IFAR e-mail only**.

**Practical line for the customer:** the **documented 5.16 IFAR e-mail** scenario is **not** described in wiki prose as “anonymous download from a public CDN”. It describes a **link after IFAR dispatch**. For **on-prem**, a link that targets the **customer’s 360** and requires **authentication** is **consistent** with “download from your organisation’s 360” rather than “public internet file host”. **Why** an **external** recipient without a 360 identity **cannot** download is therefore **consistent with needing a 360 identity or another agreed access path**, unless your implementation added something else. **Exact** auth rules need **product or code** confirmation.

### 3. On-prem vs online and “cloud storage”

The wiki page **does not** describe a separate **“cloud storage”** picker for on-prem in the text. It stresses **E-mail channel**, **code table** limit for **recno 5**, and **UseLargeFileDispatch**. So **“we see no cloud storage options for on-prem”** does **not** contradict the wiki text for the **5.16** scope described there.

Whether **5.18** added **online-only** storage or different link behaviour is **not** verified in this note (wiki page revision is **2024-06-27**; check **5.18 release notes** and **hotfixes** for changes after that).

### 4. E-mail claims: one recipient, no forward, one download

The **wiki page body** does **not** spell out **one-time token**, **non-forwardability**, or **single user** in the paragraphs retrieved. Those claims are coming from **template text** (Norwegian). **Behaviour you observed** (forwarding works, multiple downloads, multiple people) suggests either:

- the **template text is aspirational or wrong**, or  
- **enforcement** of “single use / single person” is **not implemented** or **not enabled** in their build, or  
- a **different subsystem** generates the mail than the one the template describes.

**Verification path:** compare **Word / channel template** for that dispatch with **actual token implementation** (needs **R&D or support** with access to **5.18** on-prem packages). This pass does **not** prove the Norwegian sentence is true.

### 5. Ratatoskr

**`search_topics`** on **admin-en** for **large file dispatch** and for **UseLargeFileDispatch** returned **no** results in this session. Admin help may use other wording or the topic may live only on wiki. **Wiki remains** the strongest written source used here.

### 6. Step 1 follow-up: GitHub (`gh search code`, repo `te-industry-public360/core-bl`)

Command used: **`gh search code "UseLargeFileDispatch" --repo te-industry-public360/core-bl --limit 20`** (after **`gh auth login`**). Representative hits:

- **Toggle definition:** `Source/si-bl-core-build/SI.Biz.Core/DocumentDispatchModule/DocumentDispatchManager.cs` (class **`UseLargeFileDispatch`** extends **`ToggleBase`**).
- **IFAR e-mail path:** `Source/si-bl-dispatch-build/SI.Biz.Core.Dispatch.EMail/EmailDispatch.cs` and **`...Dispatch.EMailRestricted/EmailDispatch.cs`** (feature gate with **`IsIFARCase()`** and **`IsValidateLargefile()`**).
- **Validation:** `Source/si-bl-dispatch-build/SI.Biz.Core.Dispatch/DispatchCore/DispatchManager/DispatchValidator.cs`.
- **Shareable download URL / large file branch:** `Source/si-bl-integration-build/SI.Biz.Core.Integration.SoapBridge/PublicFile/PublicFile.cs` (route prefix **`v2-pbr/shareable/directlink`**, query **`largefile`**).
- **Feature flag JSON:** `Source/si-bl-core-build/SI.Util/Resources/FeatureFlags/FeatureFlags.json`.

**Line evidence for TTL (large file path):** same **`PublicFile.cs`** file, method **`DownloadLargeFile`**, after building the HTTP response for the zip, **`mngr.UpdateExpiry(intId, TimeSpan.FromHours(2));`**

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-integration-build/SI.Biz.Core.Integration.SoapBridge/PublicFile/PublicFile.cs#L169-L191

Other same-topic files (browse on GitHub, `master` branch):

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/DocumentDispatchModule/DocumentDispatchManager.cs

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-dispatch-build/SI.Biz.Core.Dispatch.EMail/EmailDispatch.cs

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-dispatch-build/SI.Biz.Core.Dispatch.EMailRestricted/EmailDispatch.cs

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-dispatch-build/SI.Biz.Core.Dispatch/DispatchCore/DispatchManager/DispatchValidator.cs

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Util/Resources/FeatureFlags/FeatureFlags.json

---

## Risks and Limitations

- **Image-only flowchart:** branches such as **“public access”** are **not** verified from OCR in this run.
- **TTL conflict:** wiki **2 hours** vs e-mail **1 month** is partly resolved toward **2 hours** by **wiki + code** for the **large-file shareable** path; e-mail template may still be wrong for **one month** wording.
- **Security marketing vs reality:** forwarding and reuse **must** be escalated if the customer treats the mail as a **security guarantee**.

## References

- https://wiki.software-innovation.com/wiki/Request_for_Access_Large_file_dispatch
- https://wiki.software-innovation.com/wiki/5.16_release_information
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-integration-build/SI.Biz.Core.Integration.SoapBridge/PublicFile/PublicFile.cs#L169-L191
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/DocumentDispatchModule/DocumentDispatchManager.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-dispatch-build/SI.Biz.Core.Dispatch.EMail/EmailDispatch.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-dispatch-build/SI.Biz.Core.Dispatch.EMailRestricted/EmailDispatch.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-dispatch-build/SI.Biz.Core.Dispatch/DispatchCore/DispatchManager/DispatchValidator.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Util/Resources/FeatureFlags/FeatureFlags.json

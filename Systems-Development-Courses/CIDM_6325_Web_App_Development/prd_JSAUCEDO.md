# Product Requirements Document (PRD)

> How to use this template
>
> - Keep headings and section order; delete guidance text as you fill it in.
> - Follow repo Markdown lint rules (H1 on first line, no trailing punctuation in headings, no bare URLs).
> - Prefer links like <https://example.com> and keep line length ~100 chars.
>
## 1. Document Information

- Product/Feature Name: TeleCare Triage
- Author(s): Jacque Saucedo
- Date Created: TODO (2025-09-14)
- Last Updated: TODO (2025-09-21)
- Version: 0.1 (Draft)

---

## 2. Overview

- Summary:
  TeleCare Triage is a lightweight web app that helps clinical teams route patients to the right level of care (self-care, tele-visit, nurse callback, or in-person). It reduces delays, improves safety, and provides a clear queue and reporting dashboard.
- Problem Statement:
  Patients and staff often lack consistent guidance when deciding where and how quickly to seek care. Existing phone lines or EHR triage modules can be inconsistent, slow, or hard to audit.
- Goals & Objectives:
  - Increase triage speed and accuracy.
  - Provide clear rationale for routing decisions.
  - Support quality reviews with a searchable log.
  - Enable staff adoption with a simple interface.
- Non-Goals:
  - No AI-driven diagnosis in MVP.
  - No full EHR integration at launch.

---

## 3. Context & Background

- Business Context: Supports telehealth efficiency and patient safety goals for clinics adopting hybrid care.
- Market/Customer Insights: Staff report inconsistent escalation decisions and limited audit trails; patients wait for callbacks even for low-risk issues.
- Competitive/Benchmark References: Commercial nurse-triage software is costly and oriented to call centers, not small practices.

---

## 4. Scope

- In Scope:
  - Triage form with symptom fields and urgency selection.
  - Rule engine seeded from AHRQ/CDC/ATA guidance.
  - Queue and reporting (CSV/PDF).
  - Admin panel to review routing data.
- Out of Scope:
  - Automated scheduling or EHR write-back.
  - Predictive ML models (phase 2+).

---

## 5. User Stories & Use Cases

- Primary User Persona(s): Triage nurses, clinic supervisors, patients (indirect).
- User Stories:
  - As a nurse, I want a quick triage tool so I can safely route calls.
  - As a supervisor, I want reports so I can track routing quality.
  - As a patient, I benefit from faster callbacks and clear escalation.
- Use Case Scenarios: nurse logs complaint, engine flags urgent, patient routed.
- Edge: incomplete info → tool prompts for key fields before save.

---

## 6. Functional Requirements

- FR-001: Capture symptoms and key details (onset, severity).
- FR-002: Apply rules to classify urgency.
- FR-003: Log each decision with timestamp, user ID, and rationale.
- FR-004: Export queue and history as CSV/PDF.

> Tip: Tie each FR to a user story or acceptance criteria below.

---

## 7. Non-Functional Requirements

- Performance: <300 ms classification per entry.
- Scalability: Up to 50 concurrent users.
- Accessibility: WCAG 2.1 AA compliance.
- Security/Compliance: HIPAA-safe data handling, role-based access.
- Reliability/Availability: 99.5% uptime target.

---

## 8. Dependencies

- Django framework & PostgreSQL DB.
- Rule content from AHRQ, CDC, ATA.
- Celery worker for scheduled reports.

---

## 9. Risks & Assumptions

- Risks:
  - Misclassification → mitigated with conservative rules + audit.
  - Staff adoption friction → mitigate via simple UX + training.
- Assumptions:
  - Clinic has stable internet; staff available for pilot testing.

---

## 10. Acceptance Criteria

- FR-001 passes when users can submit triage data in <1 min without error.
- FR-002 passes when >90% of urgent cases match supervisor review.
- FR-003passes when each triage submission is stored with timestamp, user ID, and decision rationale, and can be viewed in an audit log.
- FR-004 passes when admins export a full report for any date range.

---

## 11. Success Metrics

- ≥90% correct routing of urgent cases (audit sample).
- Median entry-to-classification time ≤60 sec.
- ≥70% of telehealth-related calls logged during pilot.

---

## 12. Rollout & Release Plan

- Phasing: 
  - MVP (Weeks 1–2): Deploy the triage intake form, rules engine, and queue with CSV export.
  - Phase 2 (Weeks 3–4): Add PDF reporting, admin filters, and refine rule logic based on pilot feedback.
  - Future Iterations: Optional ML-based prioritization and EHR integrations once MVP adoption is stable.
- Release Channels:
  - Start with an internal beta in a single clinic.
  - Expand via staged rollout to additional staff after feedback.
  - Promote to general availability once success metrics (accuracy, speed, adoption) are met.
- Training/Documentation Needs:
  - Create a one-page quick-start guide for staff.
  - Provide a 15-minute recorded demo and live Q&A during kickoff.
  - Maintain an internal FAQ and troubleshooting sheet for ongoing support.

---

## 13. Open Questions

- - Should supervisors be able to edit past triage notes?
- Is multi-clinic support needed in v1?

---

## 14. References

- TeleCare Triage & Project Pitch Companion (2025): Course resource provided by the instructor.
- TeleCare Triage System Sketch (Mermaid diagram). Created with Mermaid <https://mermaid.js.org>.
- AHRQ (2025). Telephone Triage and Advice Protocols. <https://www.ahrq.gov/>
- CDC (2023). Telehealth Practice Among Health Centers During COVID-19 Pandemic. <https://www.cdc.gov/mmwr/volumes/69/wr/mm6950a4.htm>
- American Telemedicine Association (ATA) (2024). Practice Guidelines for Telehealth and Remote Patient Monitoring. <https://www.americantelemed.org/policies/>
- HHS Telehealth for Providers (2024). <https://telehealth.hhs.gov/providers>
- ONC – Office of the National Coordinator for Health IT (2025). Patient Safety and Health IT: Safe Design and Implementation. <https://www.healthit.gov/topic/safety>
- Product Requirements Document (PRD) Template. Course material/GitHub repo guidance provided by the instructor.

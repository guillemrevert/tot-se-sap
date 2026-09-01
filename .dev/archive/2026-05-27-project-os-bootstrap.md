# Plan — Project Operating System Bootstrap

Date: 2026-05-27
Owner: Claude (with Iban)
Status: completed

## Goal

Adapt CritKeep's documentation and coordination layer to the Project Operating
System described in `project-operating-system-bootstrap.md`, so that every agent
(Claude, Augment, Codex…) and human enters through one living source of truth,
keeps memory agile, and coordinates predictably.

## Context

The repo already has a rich `.dev/skills/skill-critkeep/` with 10 reference docs,
a private development playbook, testing docs under `docs/`, and an initial audit.
Gaps vs. the target OS:

- `AGENTS.md` and `CLAUDE.md` are byte-identical and lack the plans / memory-log
  protocol and the commit boundary.
- Refs use a different numbering scheme and live flat (no `refs/` folder).
- No `.dev/plans/` or `.dev/memories-log/`.
- The roadmap (playbook) is marked PRIVATE, conflicting with an open-source
  living roadmap.
- Several temporary `.dev/` notes (IMPL_*, HISTORIC_*, specs/) duplicate truth.
- `.augment/` has a divergent copy of the skill (two entry points).

This is an open-source project: `AGENTS.md`, `CLAUDE.md`, and everything under
`.dev/` must be written in English for external collaborators.

## Scope

- Included: documentation, refs reorganization, AGENTS/CLAUDE rewrite, roadmap
  transformation, plans + memory-log scaffolding, archiving temp notes, unifying
  the Augment entry point.
- Excluded: any application code change (backend/frontend). No behavior changes.

## Decisions (confirmed with Iban, 2026-05-27)

1. **Public roadmap, private strategy.** `08-dev-roadmap.md` is public. Business /
   monetization / AI strategy moves to a gitignored private doc.
2. **Adapt to bootstrap numbering.** Canonical `refs/01..11` with hyphens;
   project-specific refs at `12+`.
3. **Archive temp notes.** Move into `.dev/archive/` with a README marking them
   historical, rather than deleting.

## Proposed Phases

1. Scaffold `.dev/plans/`, `.dev/memories-log/`, `.dev/skills/.../refs/`, `.dev/archive/`. ← this plan
2. Rewrite `AGENTS.md` (operational) and `CLAUDE.md` (decisions/boundaries).
3. Migrate existing refs into `refs/` with canonical numbering (splits/merges).
4. Transform the playbook into public `08-dev-roadmap.md`; extract private strategy.
5. Author missing refs: `04-security-and-permissions`, `07-features`,
   `09-testing-policy`, `10-code-quality`, `11-security-and-quality-audit`.
6. Archive temp notes, move `mcp_telegram_bot.py` to `scripts/`, unify `.augment`.
7. Rewrite `SKILL.md` index, write the closing memory log, verify links.

## Ref mapping (current → target)

| Current | Target |
|---|---|
| `02_architecture.md` | `refs/01-architecture.md` |
| `03_data_model.md` | `refs/02-data-model.md` |
| `05_api_and_websocket.md` | `refs/03-api-contracts.md` (auth/permissions split out) |
| (new, from 05 + 10) | `refs/04-security-and-permissions.md` |
| `09_frontend_patterns.md` | `refs/05-frontend-patterns.md` |
| `06_design_system.md` | `refs/06-design-system.md` |
| (new, from playbook + 07) | `refs/07-features.md` |
| `01_development_playbook.md` | `refs/08-dev-roadmap.md` (transformed, public) |
| `docs/testing/*` | `refs/09-testing-policy.md` (summary; docs stay as detail) |
| (new) | `refs/10-code-quality.md` |
| `docs/audit/*` | `refs/11-security-and-quality-audit.md` (protocol; audits stay in docs/) |
| `04_game_system_schemas.md` | `refs/12-game-system-schemas.md` |
| `07_components.md` | `refs/13-ui-components.md` |
| `08_branding.md` | `refs/14-branding.md` |
| `10_admin_and_plans.md` | `refs/15-admin-and-plans.md` (permissions → 04) |

## Risks and Decisions

- Renames lose `git blame` continuity if not done with `git mv` — use `git mv`.
- Content splits (auth out of API ref, permissions out of admin ref) risk
  duplication — keep one canonical home and cross-link.
- Two skill copies (`.dev` vs `.augment`) must not drift — make `.augment` a thin
  pointer to the `.dev` skill.

## Verification

- All internal links in `SKILL.md` and refs resolve to existing files.
- `git status` shows only doc moves/edits, no code changes.
- `AGENTS.md` and `CLAUDE.md` are no longer identical and both reference the
  plans / memory-log protocol.
- A new contributor can read `AGENTS.md` → `SKILL.md` → `08-dev-roadmap.md` and
  understand state without chat history.

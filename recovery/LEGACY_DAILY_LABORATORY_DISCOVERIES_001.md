# Legacy Daily Laboratory Discoveries — Archaeology Pass 001

**Recovery ID:** DLR-ARCH-001  
**Repository:** sovereign-codex/Digital-laboratory  
**Branch:** reconstruction/digital-lab-001

## Question

What did the first Digital Laboratory repository actually preserve, and can the Daily Laboratory Scroll lineage be treated as evidence of executed experiments?

## Repository findings

The repository has ten historical commits, all dated 2025-08-29.

Across every reachable historical Git tree inspected:

- no `data/scrolls/` directory is visible;
- no PDF blob is visible;
- every visible `data/manifest.json` has an empty `entries` array;
- the repository repeatedly contains an archive shell: README, manifest, add-scroll script, site assets, and a Pages workflow in some historical states;
- an initial blob named `digital-laboratory-discoveries-prelinked.zip` exists at 3,781 bytes;
- the current GitHub connector cannot decode that binary ZIP, so its internal contents remain **UNINSPECTED** and must not be inferred;
- commit `66e54ef` introduced a nested `digital-laboratory-discoveries/` archive structure with an empty manifest;
- commit `fa63710` temporarily added a second `digital-laboratory-discoveries 2/` variant, also with an empty manifest;
- later cleanup flattened the shell to repository root.

## Disposition

The original repository is verified as a **publication/archive scaffold**, not a run ledger.

The Daily Laboratory Scroll mechanism is useful as a publication/export layer, but a scroll cannot substitute for run identity, execution class, controls, raw observations, analysis, provenance, evidence receipt, and disposition.

The historical ZIP remains a binary-presence clue only. Until it is inspected, it cannot be treated as evidence that any particular PDF or experiment was committed.

## Next gate

Recover the water / vortex / plasma / crystal family and separate design artifacts, simulation claims, computational runs, physical execution, and surviving evidence.

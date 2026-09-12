# Finding Classification & Triage Matrix

Classify every finding returned by the reviewer before modifying the artifact.
Never silently drop a finding.

---

## Classification Rubric

### 1. Defect
- **Definition:** The artifact is factually incorrect, self-contradictory, or silent in a manner that produces an unusable outcome.
- **Action:** Apply the smallest complete fix in-scope. If the fix exceeds the writer's authority or scope, escalate immediately to the user.

### 2. Context Gap
- **Definition:** The artifact permits a reasonable misreading by a cold reader because necessary background or context is omitted.
- **Action:** Add the minimal clarifying context needed to eliminate ambiguity.

### 3. Disputed
- **Definition:** Authoritative, citable workspace evidence directly contradicts the reviewer's finding.
- **Action:** Do not modify the artifact. In the disposition report, quote the authoritative contract, explain the rationale, and request re-verification.

### 4. Deferred
- **Definition:** The finding points out a valid but non-material improvement whose immediate cost or disruption exceeds its value.
- **Action:** Record the finding and rationale in the disposition report. A finding may only be deferred if it is non-material (never a blocker, major defect, or material open question).

### 5. Scope Suggestion
- **Definition:** The proposal is constructively valid but expands beyond the agreed boundaries of the artifact.
- **Action:** Log the suggestion under "Future Considerations" for the user. Do not expand the artifact scope silently.

---

## Judgment Heuristics

When evaluating finding severity and dispositions, weigh:
- **Evidence Weight:** Does an authoritative file or schema directly settle the matter?
- **Downstream Cost:** Would an engineer or agent implementing this specification produce a defective system?
- **Reversibility:** How difficult is it to correct the misunderstanding later?
- **Smallest In-Scope Fix:** Can the issue be resolved with 1-2 precise sentence revisions?

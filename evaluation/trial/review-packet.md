# First real-platform trial preparation

The merged prompt workflow is frozen at `d5c64a51c5d69962ca5f7084e58b0d26bcdc081e`, before the user's platform is supplied. [The procedure](README.md) preserves baseline/revised evidence, original evaluations and comparison limits. Plan/results remain blank templates; the wider rubric is provisional.

The local pack builder archives that exact Git commit, checks 15 critical file hashes and adds separately identified trial instructions/templates. It makes no model/network calls and does not collect platform inputs. It preserves existing output files. The source freeze is not moved forward to include the preparation tooling itself.

Twenty-two regression tests pass. The generated pack was extracted and its frozen framework validated with explicit missing-cache reporting; its review builder reproduced the original pilot packet exactly. Preparation hashes were checked. The [pack record](pack-record.json) identifies the generated ZIP; it is not a trial result.

Next input is one real workflow and its relevant spec/source/current-doc revisions, plus the chosen agent/build commands and available owners. Alternatively, the user can run the portable pack privately. No platform content or result is committed by this change, and no numerical pass threshold or publication gate is introduced.

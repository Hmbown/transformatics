# Sources for the short film

The English and Mandarin shorts make the same seven claims. Source comparison
was completed on 6 October 2026.

| Scene | Claim and source |
| --- | --- |
| Introduction | Both constructions use a chosen external force. The sources below explicitly include forcing. |
| Breakdown | OpenAI's [Theorem 1.1](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) constructs a smooth, compactly supported force and a zero-initial-velocity solution whose peak speed becomes unbounded in finite time. |
| Energy | The same theorem gives uniformly bounded kinetic energy. Section 2.1 gives the shrinking-core scales illustrated on screen. The displayed core energy is distinct from the total energy. |
| Force | For smooth finite-energy solutions from rest, the unforced energy identity gives zero velocity. In the forced construction, the external force supplies the energy. |
| Counting example | The program 0 → 1 → 2 → stop illustrates state encoding. It is a teaching example. |
| Halting detector | [Family 376](https://github.com/openai/math/blob/adc7f124/lean/docs/376.md) includes a smooth forced flow from rest on three-dimensional space in which one fixed particle enters a fixed open box exactly when the encoded machine halts. The force has an effective description for computable positive viscosity. The diagonal particle route on screen is a schematic. |
| Unforced question | These forced results do not establish regularity or breakdown for general smooth initial data with zero force. That three-dimensional question remains open. |

The displayed core uses the paper's exponents with an illustrative parameter
`h = 0.005`: radial size `τ^0.5`, axial size `τ^0.495`, characteristic speed
`τ^-0.505`, and core energy `τ^0.485`. These are relative scaling illustrations,
not numerical integration of the paper's complete solution. The labels identify
the core and detector route as schematics.

`checks.mjs` independently checks the illustrated identities and scaling
arithmetic. The Taylor–Green scenes are exact unforced teaching examples; they
are not depictions of either forced construction.

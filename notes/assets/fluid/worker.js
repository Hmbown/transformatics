import { Fluid } from "./solver.js";

let fluid;
let tracers;
const TAU = 2 * Math.PI;
const wrap = (value) => ((value % TAU) + TAU) % TAU;

function initialize(n, nu, preset) {
  fluid = new Fluid(n, nu, preset);
  // Deterministic initial positions make reset and comparisons reproducible.
  tracers = Array.from({ length: 420 }, (_, index) => {
    const t = index + 1;
    return [wrap(t * 2.399963), wrap(t * 1.414214), wrap(t * 1.732051)];
  });
}

function advanceTracersAndField() {
  const oldVelocity = tracers.map((position) => fluid.sample(position));
  const { dt } = fluid.step();
  // Predictor uses the old field; correction samples the newly evolved field.
  tracers = tracers.map((position, index) => {
    const predicted = position.map((value, axis) =>
      wrap(value + dt * oldVelocity[index][axis]),
    );
    const newVelocity = fluid.sample(predicted);
    return position.map((value, axis) =>
      wrap(value + 0.5 * dt * (oldVelocity[index][axis] + newVelocity[axis])),
    );
  });
}

onmessage = ({ data }) => {
  const identity = { generation: data.generation, requestId: data.requestId };
  try {
    if (data.type === "reset") initialize(data.n, data.nu, data.preset);
    else if (data.type === "step" && fluid) advanceTracersAndField();
    else throw Error("Initialize the field before stepping.");
    postMessage({
      ...identity,
      type: "state",
      diagnostics: fluid.diagnostics(),
      tracers,
      speeds: tracers.map((position) => Math.hypot(...fluid.sample(position))),
    });
  } catch (error) {
    postMessage({ ...identity, type: "error", message: error.message });
  }
};

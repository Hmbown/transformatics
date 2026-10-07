"""Receipt and mutation tests for the separate exact handover controls."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from experiments import nse_original_handover as controls


class ExactHandoverControlsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = controls.checks()

    def test_all_exact_checks_pass(self):
        self.assertEqual(len(self.rows), 55)
        self.assertTrue(all(row['passed'] for row in self.rows))

    def test_receipt_names_are_unique(self):
        names = [row['name'] for row in self.rows]
        self.assertEqual(len(names), len(set(names)))

    def test_wrong_pressure_factor_is_detected(self):
        original = controls.projected_generator

        def mutated(pressure_factor=2, frame_sign=1):
            return original(pressure_factor=1, frame_sign=frame_sign)

        with patch.object(controls, 'projected_generator', mutated):
            rows = {row['name']: row['passed'] for row in controls.checks()}
        self.assertFalse(rows['full-shear-entry-12'])
        self.assertFalse(rows['K21-complete-pressure-numerator'])
        self.assertFalse(rows['K22-a32-cancellation'])

    def test_wrong_frame_sign_is_detected(self):
        original = controls.projected_generator

        def mutated(pressure_factor=2, frame_sign=1):
            return original(pressure_factor=pressure_factor, frame_sign=-1)

        with patch.object(controls, 'projected_generator', mutated):
            rows = {row['name']: row['passed'] for row in controls.checks()}
        self.assertFalse(rows['K21-complete-pressure-numerator'])
        self.assertFalse(rows['frozen-inner-entry-21'])

    def test_removed_shear_pressure_is_detected(self):
        original = controls.projected_generator

        def mutated(pressure_factor=2, frame_sign=1):
            result = original(pressure_factor, frame_sign)
            x, y, w, shear = result['coordinates']
            result['projected'][0, 1] -= 2*shear*x*x/(x*x+y*y+w*w)
            return result

        with patch.object(controls, 'projected_generator', mutated):
            rows = {row['name']: row['passed'] for row in controls.checks()}
        self.assertFalse(rows['full-shear-entry-12'])

    def test_receipt_separates_algebra_from_written_proof(self):
        stream = io.StringIO()
        with patch.object(controls, 'checks', return_value=self.rows):
            with redirect_stdout(stream):
                result = controls.main()
        record = json.loads(stream.getvalue())
        self.assertEqual(result, 0)
        self.assertEqual(record['checks_total'], 55)
        self.assertTrue(record['written_PDE_proof_separate'])
        for name in ('PDE_theorem_certified', 'growing_interval_matching_certified',
                     'strong_existence_certified', 'infinite_iteration_certified',
                     'Lean_kernel_checked', 'DNS'):
            self.assertFalse(record[name])
        self.assertEqual(record['ROOT'], 'OPEN')
        saved = json.loads((Path(__file__).parents[1] / 'artifacts/enstrophy_sup/nse_original_handover.json').read_text())
        self.assertEqual(saved, record)

    def test_failed_control_returns_nonzero_and_failed_receipt(self):
        stream = io.StringIO()
        with patch.object(controls, 'checks', return_value=[{'name': 'injected', 'passed': False}]):
            with redirect_stdout(stream):
                result = controls.main()
        record = json.loads(stream.getvalue())
        self.assertEqual(result, 1)
        self.assertFalse(record['all_passed'])
        self.assertEqual(record['checks_passed'], 0)


if __name__ == '__main__':
    unittest.main()

import os
import unittest

from checkov.dockerfile.checks.RunUsingAPT import check
from checkov.dockerfile.runner import Runner
from checkov.runner_filter import RunnerFilter


class TestRunUsingAPT(unittest.TestCase):
    def test(self):
        runner = Runner()
        current_dir = os.path.dirname(os.path.realpath(__file__))

        test_files_dir = current_dir + "/example_RunUsingAPT"
        report = runner.run(root_folder=test_files_dir, runner_filter=RunnerFilter(checks=[check.id]))
        summary = report.get_summary()

        passing_resources = {
            "/success/Dockerfile.",
            "/success2/Dockerfile.",
            "/success3/Dockerfile.",
        }
        failing_resources = {
            "/failure/Dockerfile.RUN",
            "/failure2/Dockerfile.RUN",
            "/failure3/Dockerfile.RUN",
        }

        passed_check_resources = set([c.resource for c in report.passed_checks])
        failed_check_resources = set([c.resource for c in report.failed_checks])

        self.assertEqual(summary["passed"], len(passing_resources))
        self.assertEqual(summary["failed"], len(failing_resources))
        self.assertEqual(summary["skipped"], 0)
        self.assertEqual(summary["parsing_errors"], 0)

        self.assertEqual(passing_resources, passed_check_resources)
        self.assertEqual(failing_resources, failed_check_resources)


if __name__ == "__main__":
    unittest.main()

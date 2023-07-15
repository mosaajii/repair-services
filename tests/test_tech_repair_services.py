#!/usr/bin/env python

"""Tests for `tech_repair_services` package."""


import unittest
from click.testing import CliRunner

from tech_repair_services import tech_repair_services
from tech_repair_services import cli


class TestTech_repair_services(unittest.TestCase):
    """Tests for `tech_repair_services` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'tech_repair_services.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

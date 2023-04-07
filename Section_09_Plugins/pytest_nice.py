"""
Created on April 07, 2023

@author: Romulo
"""
import pytest


def pytest_addoption(parser):
    group = parser.getgroup("nice")
    group.addoption("--nice", action="store_true", help="nice: turns a FAILURE into OPPORTUNITY for improvement")


def pytest_report_header(config):
    if config.getoption("nice"):
        return "Thanks for running tests"


def pytest_report_teststatus(report, config):
    if report.when == "call":
        if report.failed and config.getoption("nice"):
            return report.outcome, "O", "OPPORTUNITY for improvement"


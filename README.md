Six Sigma CI CD Quality Gate with Docker

Project Overview
This project demonstrates an automated quality gate system using Six Sigma principles, Docker, and GitHub Actions CI CD. The objective is to evaluate software quality metrics automatically during the CI pipeline and prevent builds from passing when quality thresholds are not satisfied.

The project combines process quality engineering using Six Sigma with modern DevOps automation practices.

Problem Statement
In many software projects, quality validation is manual and subjective. This often results in delayed defect detection, inconsistent quality standards, and lack of automated enforcement within CI CD pipelines.

Solution
This project implements an automated Six Sigma Quality Gate that calculates Defects Per Million Opportunities and Sigma Level. The solution runs inside a Docker container and is executed automatically through a GitHub Actions CI pipeline. Based on the computed Sigma Level, the pipeline either passes or fails.

Six Sigma Methodology Used
The project follows a partial DMAIC framework.
Define phase is used to define defect rules and acceptable quality thresholds.
Measure phase is used to calculate total defects, total opportunities, DPMO, and Sigma Level.

A quality gate is enforced using the calculated Sigma Level.

Architecture
The workflow starts with a developer push to GitHub. GitHub Actions triggers the CI pipeline, which builds a Docker image and runs the container. Inside the container, Six Sigma metrics are computed and automated tests are executed. Based on the results, the pipeline either passes or fails.

Tech Stack
Python 3.12
Pytest
SciPy
Docker
GitHub Actions
Six Sigma metrics such as DPMO and Sigma Level

Project Structure
six-sigma-ci-cd-docker
app folder containing sigma_metrics.py, data_quality.py, and main.py
tests folder containing test_quality.py
data folder containing sample_data.csv
github workflows folder containing ci.yml
Dockerfile
requirements.txt
README.md

How to Run Locally
First, build the Docker image using the docker build command with the tag six-sigma-quality-gate.
Then, run the container using the docker run command with the same image name.

The output will display defect count, total opportunities, DPMO, Sigma Level, and quality gate result.

CI CD Pipeline
The CI pipeline is triggered automatically on every push to the main branch. It builds the Docker image and runs the Six Sigma quality gate. If the Sigma Level does not meet the defined threshold, the pipeline fails.

Key Outcomes
Automated enforcement of quality standards
Dockerized and reproducible testing environment
CI CD integrated quality gate
Practical implementation of Six Sigma in software engineering

Use Cases
CI CD quality gates
DevOps automation projects
Process improvement demonstrations
Interview ready portfolio project

Author
Saikiran Bodha

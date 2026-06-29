# Community Crisis Triage Agent

AI-powered triage and resource routing for non-emergency community crises.

## Overview

This project implements a multi-agent system that:
- Takes a user's crisis description in natural language.
- Classifies the type and urgency of the crisis.
- Evaluates safety and potential emergency risk.
- Routes the user to relevant community resources (shelters, food banks, crisis lines, etc.).
- Generates a simple action plan.

This repository is part of the **Kaggle AI Agents: Intensive Vibe Coding Capstone** in the **Agents for Good** track.

## Architecture

### Agents

- **IntakeAgent** – collects and normalizes user input.
- **ClassificationAgent** – determines crisis type and urgency.
- **SafetyAgent** – evaluates risk and provides safety messaging.
- **RoutingAgent** – queries the MCP server and builds an action plan.

### MCP Server

- Loads local JSON resource files from `data/`.
- Provides simple query endpoints for resource lookup.
- Acts as a stand-in for a more advanced MCP resource server.

### Skills

- **crisis_classification** – basic rule-based crisis classification.
- **resource_matching** – builds an action plan from matched resources.
- **safety_evaluation** – checks for dangerous language and returns safety guidance.

## Folder Structure

- `agents/` – agent classes.
- `mcp/` – MCP server and resource loader.
- `skills/` – reusable skills for classification, matching, and safety.
- `data/` – JSON files with example community resources.
- `demo/` – CLI demo entry point.
- `README.md` – project documentation.
- `requirements.txt` – Python dependencies.

## Setup

```bash
git clone https://github.com/your-username/community-crisis-triage-agent.git
cd community-crisis-triage-agent
pip install -r requirements.txt

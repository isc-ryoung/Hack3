# Ethical IRIS Remediator

A project to create an Agentic AI system that checks an InterSystems IRIS instance for any problems and takes remedial action to resolve any issues.

## Overview

Three AI Agentic modules are involved: the **Remediator**, the **IrisDb**, and the **Customer**. Each module will consist of one or more AI Agents.

**Technology Stack:** Python and the [OpenAI SDK Agents](https://github.com/openai/openai-agents-python)

---

## Modules

### Remediator Module

The Remediator is the main module and the trigger point. The module will be queried with a prompt such as:
- "Resolve errors with the IRIS instance"
- "Resolve any licensing issues with the IRIS instance"

The Remediator would then use the IrisDb and the Customer agents/modules as tools to carry out the goal.

#### Workflow

The Remediator would:

1. Request the IrisDb agent to analyse the IRIS instance for any problems
2. Receive a response from the IrisDb agent in a structured format, which defines a problem
3. Diagnose what possible resolutions could be applied, such as:
   - Updating the license
   - Changing configuration settings
   - Modifying an OS parameter
4. If required, request the Customer agent to evaluate the diagnosis according to its policies (e.g., ensuring that any restart is done at a particular time)
5. Receive a response from the Customer agent in a structured format, defining a priorities
6. Send a message for a plan of action back to the IrisDb agent which is based upon the diagnosis and the response from the customer
7. Receive a response from the IrisDb agent on what was done
8. Report back to the user the result

---

### IrisDb Module

This emulates an InterSystems IRIS database platform system. It should provide generated simulated error messages as if they were from the `messages.log` file. There are sample `messages*.log` files in the folder `log_samples`.

An error is represented by a non-zero value in the third column. The sort of errors that might be generated could be related to:
- Configuration settings that need to be modified (may or may not require an IRIS instance restart)
- License issues
- Errors related to changes required to the operating system (CPU or memory)

#### Workflow

The IrisDb module would:

1. Receive the initial request from the Remediator
2. Call a tool which generates 0 or 1 simulated log entry
3. Analyse the log entry and return a structured response to the Remediator
4. Receive from the Remediator a structured plan of action
5. Translate that plan into one or more actions
6. For each action, call an appropriate tool. For example, tools could be to:
   - Change operating system settings
   - Modify IRIS settings
   - Restart IRIS
7. Each tool would convert the action into the exact command required
8. Respond to the Remediator what was carried out

---

### Customer Module

The Customer module simulates decisions made by a customer for requests made by the Remediator agent. The decisions will be based on a definition of the requirements and operational concerns of the customer according to how and who they want to carry out the remedial actions.

For example, they may want to:
- Add disk space themselves
- Have the Remediator via IrisDb make configuration changes to the instance

**Optional Enhancement:** Use a ValueNet-based value modelling approach ([arxiv.org/pdf/2112.06346](https://arxiv.org/pdf/2112.06346)) to evaluate a set of candidate remediation responses proposed. That is, the customer would generate a set of responses and evaluate those according to its own values and policies.

#### Workflow

The Customer module would:

1. Receive a request from the Remediator to evaluate the remedial action
2. Generate a set of possible responses to return to the Remediator
3. Choose one response, which, optionally, would be determined by a ValueNet-based tool
4. Return response to the Remediator

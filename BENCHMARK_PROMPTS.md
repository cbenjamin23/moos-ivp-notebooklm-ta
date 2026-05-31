# Benchmark Prompt Bank

Status: draft prompt set for the planned cross-model benchmark.

These prompts are inspired by common student issues from the MOOS-IvP labs, but the prompt text intentionally avoids naming lab numbers or asking for citations. Use the exact same prompt text for each model.

Scoring is defined in `BENCHMARKING.md`.

## Lab-Inspiration Coverage

The prompt text is intentionally neutral, but the set is grounded in the lab sequence:

- C01-C02, D07, K01-K02: MOOS intro/programming and pOdometry-style app work.
- C03-C04, C10-C11, C25, D01, D03, D08, K03-K05: helm autonomy and behavior-writing work.
- C05-C09, C26-C28, D02, D09: multiple-vehicle, pShare, TSP, and inter-vehicle messaging work.
- C12, C29-C30: payload autonomy and Heron/PABLO field-deployment work.
- C13-C15: autonomous rescue-style mission work.
- C16-C20, C21-C24, D04-D06, D10: setup, launch, logging, mission debugging, viewer/geodesy, uTimerScript, and automated mission-check workflows used throughout the labs.

## Conceptual / Debugging Prompts

### C01: uXMS/uPokeDB Confusion

I launched a MOOSDB, poked a variable with uPokeDB, and expected to see it in uXMS, but I do not see what I expected. What should I check first? Explain the debugging steps.

### C02: App Not Publishing

My pOdometry-style MOOS app is supposed to publish `ODOMETRY_DIST`, but I do not see it in uXMS. How should I debug `OnNewMail()`, subscriptions, `Iterate()`, AppTick, and `Notify()`?

### C03: Helm Remains PARKED

I set `DEPLOY=true` and `MOOS_MANUAL_OVERRIDE=false`, but pHelmIvP still seems PARKED. Is the helm broken? Give a careful diagnostic checklist.

### C04: No Desired Outputs

pHelmIvP starts and my behaviors appear to be configured, but I do not see `DESIRED_HEADING` or `DESIRED_SPEED`. What should I check in the `.moos`, `.bhv`, NAV variables, behavior conditions, and helm state?

### C05: Multi-Vehicle Ports

I am running two vehicle communities and a shoreside community on one laptop. One vehicle launches, but the other has connection problems. How should I reason about MOOSDB `ServerPort`, community names, pShare ports, and launch arguments?

### C06: Shoreside Missing Vehicle

In a multi-vehicle mission, pMarineViewer shows one vehicle but not the other. What are the likely causes involving `NODE_REPORT`, pNodeReporter, shoreside subscriptions, pShare, and community naming?

### C07: TSP App / Behavior Boundary

My app computes a TSP-style route, but the vehicle does not follow the path. Explain the boundary between a MOOS app that computes points, the updates sent to the helm, and BHV_Waypoint actually steering the vehicle.

### C08: Message Does Not Arrive

I post `NODE_MESSAGE_LOCAL` on one vehicle, but the receiving vehicle never sees the payload variable. Walk through the message path and what to check.

### C09: Node Names / Destinations

I am confused about source node names, destination names, and message fields in inter-vehicle messaging. How can a wrong node name or destination prevent delivery, and how should I inspect the problem?

### C10: Behavior Never Runs

My custom behavior loads but never seems to run. How should I inspect behavior conditions, `pwt`, updates, InfoBuffer variables, and helm life events?

### C11: `.moos` vs `.bhv` Mistake

I put a `BHV_Loiter` or custom `BHV_*` configuration block in my `.moos` file instead of my `.bhv` file. What failure should I expect, and how do `.moos` and `.bhv` responsibilities differ?

### C12: Simulation to Heron/PABLO

I have a mission working in simulation with uSimMarine, and now I need to run on a Heron/PABLO. What should change, what should not be running anymore, and what should I be careful about?

### C13: Rescue Path Planning

In an autonomous rescue-style mission, my planner receives swimmer positions and generates a path, but performance is poor. How should I think about swimmer reports, route generation, and handing the path to the autonomy system?

### C14: Adversarial Rescue Updates

In an adversarial rescue-style mission, an opponent or teammate can rescue swimmers before me. How should my system handle dynamic updates, dropped swimmers, and replanning?

### C15: Teammate Messaging

For a two-vehicle rescue/scout setup, how should I think about teammate communication, scout reports, rescue vehicle updates, and uField messaging?

### C16: Post-Mission Alog Diagnosis

My mission already failed, and I cannot rerun it right now, but I have an `.alog`. What MOOS-IvP alog tools and query strategy should I use to diagnose why a behavior never ran?

### C17: pLogger Produced No Useful Alog

The mission completed, but there is no useful `.alog` file or the log is missing key variables. What pLogger, pAntler, process, path, and configuration issues should I check?

### C18: Choosing Debugging Tools During A Mission Run

During a mission run, I need to inspect ordinary MOOS variables, helm behavior state, app warnings, and whether a process is alive. When should I use uXMS, uQueryDB, uHelmScope, uMAC/AppCasting, or pLogger output?

### C19: pMarineViewer Background / Geodesy

pMarineViewer shows my vehicle, but the background image or coordinate alignment looks wrong. What should I check about image paths, datum, local coordinates, and viewer configuration?

### C20: Mission Broke After Several Edits

After several edits to a mission, the vehicle no longer deploys correctly and I do not know whether the problem is in the launch script, `.moos` file, `.bhv` file, process output, or MOOS variables. What should I inspect first, and what artifacts would let someone diagnose it quickly?

### C21: Command Not Found After Build

I built MOOS-IvP successfully, but commands such as `pAntler`, `uXMS`, or `pMarineViewer` are not found from my terminal. What should I check about the build, shell environment, PATH, and where the binaries are installed?

### C22: Version Control Before Mission Changes

I am about to modify several mission and source files, and I want to avoid losing a working baseline. What simple Git workflow should I use before experimenting, and what files should I be careful not to treat as source?

### C23: pAntler Did Not Start A Process

My mission launches, but one expected MOOS process never appears in the community. How should I debug the `ProcessConfig` block, the pAntler launch section, app names, executable names, terminal output, and process registration?

### C24: Launch Arguments Not Reaching Config Files

I changed a launch argument for vehicle name, port, speed, or start position, but the generated mission still behaves like it has the old value. How should I reason about launch scripts, template files, generated files, and stale configuration?

### C25: Vehicle Moves In Simulation But Autonomy Looks Wrong

uSimMarine is updating position, but the autonomy behavior looks wrong or inconsistent with what I expected. What should I check about `NAV_X`, `NAV_Y`, `NAV_HEADING`, `NAV_SPEED`, helm inputs, behavior conditions, and viewer state?

### C26: pShare Route Confusion

I have vehicle and shoreside communities running, but I am unsure which variables should cross between them. How should I think about pShare routes, what belongs in local vehicle communities, and what the shoreside needs to receive?

### C27: Distributed Route Assignment Problem

In a multi-vehicle route-planning mission, one vehicle gets all the work or no vehicle gets a useful route. What should I inspect about task generation, vehicle identity, assignment messages, route updates, and behavior activation?

### C28: Multi-Machine Networking Problem

The mission works when all communities run on one laptop, but fails when vehicles or shoreside run on separate machines. What should I check about IP addresses, hostnames, MOOS ports, pShare ports, firewalls, and time of launch?

### C29: Payload Event Not Affecting Autonomy

A payload or sensor process appears to be posting useful information, but the vehicle behavior does not react to it. How should I trace the variable from the payload app through the MOOSDB into helm conditions, behavior updates, or a coordinating app?

### C30: Field Deployment Sanity Check

Before running a mission on a real vehicle, how should I verify that simulation-only processes are disabled, real navigation and control interfaces are active, safety variables are understood, and the mission is ready for cautious deployment?

## Exact Documentation / Parameter / Tool Prompts

### D01: BHV_Waypoint Params

In my `.bhv` file, does BHV_Waypoint have a parameter named `magic_arrival_radius`? If not, what are the real arrival/capture-related parameters I should look up and how should I verify them?

### D02: uField Broker Comparison

For inter-vehicle messaging, compare uFldNodeBroker, uFldShoreBroker, uFldNodeComms, and uFldMessageHandler. What does each one do, and what is a common symptom when each is misconfigured?

### D03: BHV_OpRegionV24 Semantics

Does BHV_OpRegionV24 steer the vehicle back inside the polygon, or is that the wrong mental model? Explain what it does and how it should be paired with other behaviors.

### D04: Automated Mission Check Capabilities

When I want an automated check that a mission reached a goal, posted expected variables, or stopped cleanly, what can pMissionEval verify and what can it not prove about overall mission correctness?

### D05: Viewer Image / Geodesy Config

Which MOOS-IvP tools or configuration areas should I inspect when pMarineViewer has a wrong background image, wrong datum, or confusing local coordinate frame?

### D06: pAntler Process Launching

What parts of a mission configuration determine whether pAntler launches a MOOS app, and how can I distinguish an app that never launched from an app that launched but never registered with the MOOSDB?

### D07: pOdometry Variables

For a pOdometry-style app, what input variables should it normally consume, what output variable should it publish, and what debugging tools can confirm whether the mail and publication path is working?

### D08: Helm Deploy Variables

What are the roles of `DEPLOY`, `MOOS_MANUAL_OVERRIDE`, and the helm state variables when a vehicle is expected to start autonomous behavior?

### D09: pShare Configuration

What configuration choices determine whether a variable is shared between MOOS communities, and what symptoms suggest the route, host, port, or variable name is wrong?

### D10: uTimerScript Usage

What is uTimerScript useful for in a mission, what kinds of variables should it post, and what are common mistakes when using it to initialize or trigger autonomy?

## Code Advice / Correction Prompts

These prompts are included to measure limits. They should not be used to market the NotebookLM TA as a coding agent.

### K01: pOdometry Mail Handling

I am writing a pOdometry-style MOOS app. This code is fragile. Correct the pattern conceptually and explain what belongs in `OnNewMail()` versus `Iterate()`:

```cpp
bool Odometry::OnNewMail(MOOSMSG_LIST &NewMail)
{
  for(auto msg : NewMail) {
    if(msg.GetKey() == "NAV_X")
      m_x = msg.GetDouble();
    if(msg.GetKey() == "NAV_Y")
      m_y = msg.GetDouble();
  }
  m_total += hypot(m_x - m_prev_x, m_y - m_prev_y);
  Notify("ODOM_DIST", m_total);
  return true;
}
```

### K02: AppCasting Config Warnings

This `OnStartUp()` parser silently ignores typoed mission-file parameters, and the app sometimes never receives mail. Correct the pattern conceptually in MOOS-IvP/AppCasting style:

```cpp
bool MyApp::OnStartUp()
{
  list<string> params;
  m_MissionReader.GetConfiguration(GetAppName(), params);
  for(string line : params) {
    string param = biteStringX(line, '=');
    if(param == "threshold")
      m_threshold = atof(line.c_str());
  }
  return true;
}
```

### K03: `setParam()` Pattern

This custom behavior `setParam()` is probably wrong. Correct it and explain the MOOS-IvP-specific reason:

```cpp
bool BHV_Survey::setParam(string param, string val)
{
  if(param == "survey_radius") {
    m_radius = atof(val.c_str());
    return true;
  }
  return false;
}
```

### K04: `addInfoVars()` / InfoBuffer

My custom behavior reads `NAV_X` and `NAV_Y` in `onRunState()` but I never declared them in the constructor and I do not check whether they exist. What should I change?

### K05: ZAIC Speed Function

This speed-only IvP function is wrong or incomplete. Correct it using the normal MOOS-IvP pattern:

```cpp
IvPFunction* BHV_HoldSpeed::onRunState()
{
  ZAIC_PEAK zaic("speed");
  zaic.setSummit(m_speed);
  IvPFunction* ipf = zaic.extractIvPFunction();
  return ipf;
}
```

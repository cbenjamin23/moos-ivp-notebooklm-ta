# Benchmark Prompt Bank

Status: draft prompt set for the planned cross-model benchmark.

These prompts are inspired by common student issues from the MOOS-IvP labs, but the prompt text intentionally avoids naming lab numbers or asking for citations. Use the exact same prompt text for each model.

Scoring is defined in `BENCHMARKING.md`.

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

### C18: Choosing uXMS / uQueryDB / uHelmScope / uMAC

When should I use uXMS, uQueryDB, uHelmScope, uMAC/AppCasting, or pRealm? Give a practical student debugging comparison.

### C19: pMarineViewer Background / Geodesy

pMarineViewer shows my vehicle, but the background image or coordinate alignment looks wrong. What should I check about image paths, datum, local coordinates, and viewer configuration?

### C20: What Artifacts To Ask A TA For

If I ask for MOOS-IvP help and the answer is still generic, what exact artifacts should I provide next: `.moos`, `.bhv`, terminal output, uXMS output, appcast, or alog snippets? Explain by debugging scenario.

## Exact Documentation / Parameter / Tool Prompts

### D01: BHV_Waypoint Params

In my `.bhv` file, does BHV_Waypoint have a parameter named `magic_arrival_radius`? If not, what are the real arrival/capture-related parameters I should look up and how should I verify them?

### D02: uField Broker Comparison

For inter-vehicle messaging, compare uFldNodeBroker, uFldShoreBroker, uFldNodeComms, and uFldMessageHandler. What does each one do, and what is a common symptom when each is misconfigured?

### D03: BHV_OpRegionV24 Semantics

Does BHV_OpRegionV24 steer the vehicle back inside the polygon, or is that the wrong mental model? Explain what it does and how it should be paired with other behaviors.

### D04: pMissionEval Capabilities

What can pMissionEval verify automatically in an automated mission check, and what can it not prove about the correctness of a MOOS-IvP mission?

### D05: Viewer Image / Geodesy Config

Which MOOS-IvP tools or configuration areas should I inspect when pMarineViewer has a wrong background image, wrong datum, or confusing local coordinate frame?

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



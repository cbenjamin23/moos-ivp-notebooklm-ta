from __future__ import annotations

import json
import textwrap
import urllib.request
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parent
DOWNLOADS = ROOT / "downloads"
PACKS = ROOT / "packs"
BASE_URL = "https://oceanai.mit.edu/ivpman/pdfs/"


PACKS_SPEC = [
    {
        "slug": "00_moos_ivp_virtual_ta_guide",
        "title": "MOOS-IvP Virtual TA Guide",
        "description": "Teaching-assistant operating guidance for this NotebookLM source set.",
        "files": [],
        "guide": True,
    },
    {
        "slug": "01_core_design_moos_overview",
        "title": "Core Design and MOOS Overview",
        "description": "Core MOOS-IvP design concepts and MOOS publish-subscribe context.",
        "files": ["chap_design.pdf", "chap_moos.pdf"],
    },
    {
        "slug": "02_example_missions",
        "title": "Example Missions",
        "description": "Six canonical MOOS-IvP example missions covering the Alpha introductory mission, loitering, depth-plane operation, dynamic behavior spawning, standby helm operation, and collision avoidance.",
        "files": [
            "chap_alpha.pdf",
            "chap_xmiss_charlie.pdf",
            "chap_xmiss_delta.pdf",
            "chap_xmiss_echo.pdf",
            "chap_xmiss_kilo.pdf",
            "chap_xmiss_berta.pdf",
        ],
    },
    {
        "slug": "03_helm_autonomy_behavior_properties",
        "title": "Helm Autonomy and Behavior Properties",
        "description": "How the IvP Helm selects actions and how behavior properties are configured.",
        "files": ["chap_helm_autonomy.pdf", "chap_bhv_props.pdf"],
    },
    {
        "slug": "04_labs_01_2a_setup_git",
        "title": "2.680 Labs 01 and 2A - Setup and Git",
        "description": "Machine setup and version-control lab material.",
        "files": ["lab_class_01_start.pdf", "lab_class_skills_git.pdf"],
    },
    {
        "slug": "05_labs_02_03_moos_intro_programming",
        "title": "2.680 Labs 02 and 03 - MOOS Intro and Programming",
        "description": "Introductory MOOS concepts and MOOS programming lab material.",
        "files": ["lab_class_02_intro_moos.pdf", "lab_class_03_moos_prog.pdf"],
    },
    {
        "slug": "06_lab_04_helm_autonomy",
        "title": "2.680 Lab 04 - Helm Autonomy",
        "description": "Helm autonomy lab material.",
        "files": ["lab_class_04_autonomy.pdf"],
    },
    {
        "slug": "07_labs_05_06_multiple_vehicles",
        "title": "2.680 Labs 05 and 06 - Multiple Vehicles",
        "description": "Multiple-vehicle mission material.",
        "files": ["lab_class_05_multivehicle_pt1.pdf", "lab_class_06_multivehicle_pt2.pdf"],
    },
    {
        "slug": "08_labs_07_08_tsp",
        "title": "2.680 Labs 07 and 08 - TSP",
        "description": "Distributed TSP and multi-machine TSP lab material.",
        "files": ["lab_class_07_distributed_tsp.pdf", "lab_class_08_multi_machine_tsp.pdf"],
    },
    {
        "slug": "09_lab_09_inter_vehicle_messaging",
        "title": "2.680 Lab 09 - Inter-Vehicle Messaging",
        "description": "Inter-vehicle messaging lab material.",
        "files": ["lab_class_09_interv_msg.pdf"],
    },
    {
        "slug": "10_lab_10_behavior_writing",
        "title": "2.680 Lab 10 - Behavior Writing",
        "description": "Writing IvP behavior lab material.",
        "files": ["lab_class_10_bhv_writing.pdf"],
    },
    {
        "slug": "11_labs_11_12_payload_herons",
        "title": "2.680 Labs 11 and 12 - Payload Autonomy and Herons",
        "description": "Payload autonomy and MIT Heron operation material.",
        "files": ["lab_class_11_pablo_intro.pdf", "lab_class_12_herons.pdf"],
    },
    {
        "slug": "12_labs_13_14_rescue",
        "title": "2.680 Labs 13 and 14 - Autonomous Rescue Parts 1 and 2",
        "description": "Autonomous rescue lab material, first half.",
        "files": ["lab_class_13_rescue_pt1.pdf", "lab_class_14_rescue_pt2.pdf"],
    },
    {
        "slug": "13_labs_15_16_17_rescue",
        "title": "2.680 Labs 15, 16, and 17 - Autonomous Rescue Parts 3 to 5",
        "description": "Autonomous rescue lab material, second half.",
        "files": ["lab_class_15_rescue_pt3.pdf", "lab_class_16_rescue_pt4.pdf", "lab_class_17_rescue_pt5.pdf"],
    },
    {"slug": "14_bhv_waypoint", "title": "BHV_Waypoint", "description": "Waypoint behavior.", "files": ["bhv_waypoint.pdf"]},
    {"slug": "15_bhv_opregion_v24", "title": "BHV_OpRegionV24", "description": "Current operating-region behavior.", "files": ["bhv_opregion_v24.pdf"]},
    {"slug": "16_bhv_loiter", "title": "BHV_Loiter", "description": "Loiter behavior.", "files": ["bhv_loiter.pdf"]},
    {
        "slug": "17_bhv_periodic_speed_surface",
        "title": "BHV_PeriodicSpeed and BHV_PeriodicSurface",
        "description": "Periodic speed and periodic surface behaviors.",
        "files": ["bhv_periodic_speed.pdf", "bhv_periodic_surface.pdf"],
    },
    {
        "slug": "18_bhv_constant_depth_heading_speed",
        "title": "BHV_ConstantDepth, BHV_ConstHeading, and BHV_ConstantSpeed",
        "description": "Constant setpoint behaviors.",
        "files": ["bhv_const_depth.pdf", "bhv_const_hdg.pdf", "bhv_const_speed.pdf"],
    },
    {
        "slug": "19_bhv_depth_limits_targets",
        "title": "BHV_MaxDepth and BHV_GoToDepth",
        "description": "Depth limit and target-depth behaviors.",
        "files": ["bhv_max_depth.pdf", "bhv_goto_depth.pdf"],
    },
    {"slug": "20_bhv_stationkeep", "title": "BHV_StationKeep", "description": "Station-keeping behavior.", "files": ["bhv_stationkeep.pdf"]},
    {
        "slug": "21_bhv_turn_limit_fixedturn",
        "title": "BHV_FixedTurn and BHV_MemoryTurnLimit",
        "description": "Turn-related behaviors.",
        "files": ["bhv_fixedturn.pdf", "bhv_mem_turnlimit.pdf"],
    },
    {"slug": "22_bhv_legrun", "title": "BHV_LegRun", "description": "Leg-run behavior.", "files": ["bhv_legrun.pdf"]},
    {
        "slug": "23_bhv_zigzag_timer_testfailure",
        "title": "BHV_ZigZag, BHV_Timer, and BHV_TestFailure",
        "description": "Zig-zag, timer, and test-failure behaviors.",
        "files": ["bhv_zigzag.pdf", "bhv_timer.pdf", "bhv_testfail.pdf"],
    },
    {
        "slug": "24_bhv_avdcollision_avdcolregs",
        "title": "BHV_AvdCollision and BHV_AvdColregs",
        "description": "Collision-avoidance and COLREGS behaviors.",
        "files": ["bhv_avdcol.pdf", "bhv_colregs.pdf"],
    },
    {
        "slug": "25_bhv_cutrange_trail_shadow",
        "title": "BHV_CutRange, BHV_Trail, and BHV_Shadow",
        "description": "Contact-relative following and positioning behaviors.",
        "files": ["bhv_cutrange.pdf", "bhv_trail.pdf", "bhv_shadow.pdf"],
    },
    {"slug": "26_bhv_convoy", "title": "BHV_Convoy", "description": "Convoy behavior.", "files": ["bhv_convoy.pdf"]},
    {"slug": "27_pshare_plogger", "title": "pShare and pLogger", "description": "MOOS sharing and logging utilities.", "files": ["app_pshare.pdf", "app_plogger.pdf"]},
    {"slug": "28_pantler_iremote", "title": "pAntler and iRemote", "description": "Process launching and remote-control utilities.", "files": ["app_pantler.pdf", "app_iremote.pdf"]},
    {"slug": "29_pmviewer_uhelmscope", "title": "pMarineViewer and uHelmScope", "description": "Mission visualization and helm inspection.", "files": ["app_pmviewer.pdf", "app_uhelmscope.pdf"]},
    {"slug": "30_geometry_utscript", "title": "Geometry Utilities and uTimerScript", "description": "Geometry utilities and scripted timed posts.", "files": ["app_geometry.pdf", "app_utscript.pdf"]},
    {"slug": "31_pcontactmgr_v20", "title": "pContactMgrV20", "description": "Contact-management utility.", "files": ["app_pcmanager_v20.pdf"]},
    {"slug": "32_uprocwatch_uloadwatch", "title": "uProcessWatch and uLoadWatch", "description": "Process and load monitoring utilities.", "files": ["app_uprocwatch.pdf", "app_uloadwatch.pdf"]},
    {"slug": "33_pnodereporter_usimmarine", "title": "pNodeReporter and uSimMarineV22", "description": "Node reporting and vehicle simulation.", "files": ["app_pnreporter.pdf", "app_usimmarine_v22.pdf"]},
    {"slug": "34_pmhash_pmissioneval", "title": "pMissionHash and pMissionEval", "description": "Mission hashing and mission-evaluation utilities.", "files": ["app_pmhash.pdf", "app_pmissioneval.pdf"]},
    {"slug": "35_phostinfo_upoke_uquery", "title": "pHostInfo, uPokeDB, and uQueryDB", "description": "Host info and MOOSDB poke/query utilities.", "files": ["app_phostinfo.pdf", "app_upokedb.pdf", "app_uquerydb.pdf"]},
    {"slug": "36_umayfinish_pechovar_pdeadmanpost", "title": "uMayFinish, pEchoVar, and pDeadManPost", "description": "Mission completion, echoing, and dead-man posting utilities.", "files": ["app_umayfinish.pdf", "app_pechovar.pdf", "app_pdeadmanpost.pdf"]},
    {"slug": "37_pobstaclemgr", "title": "pObstacleMgr", "description": "Obstacle-management utility.", "files": ["app_pobstaclemgr.pdf"]},
    {"slug": "38_isay_prealm", "title": "iSay and pRealm", "description": "Text-to-speech and realm utilities.", "files": ["app_isay.pdf", "app_prealm.pdf"]},
    {"slug": "39_psearchgrid_pspoofnode", "title": "pSearchGrid and pSpoofNode", "description": "Search-grid and spoof-node utilities.", "files": ["app_psearchgrid.pdf", "app_pspoofnode.pdf"]},
    {"slug": "40_utermcommand_usimcurrent", "title": "uTermCommand and uSimCurrent", "description": "Terminal command and simulated current utilities.", "files": ["app_utermcommand.pdf", "app_usimcurrent.pdf"]},
    {"slug": "41_alog_tools", "title": "Alog Intro, alogview, and Alog Command Line Utils", "description": "Post-mission log inspection and analysis utilities.", "files": ["app_alog_intro.pdf", "app_alogview.pdf", "app_alog_cmdline.pdf"]},
    {"slug": "42_appcasting", "title": "uMAC Utilities, Enabling Appcasting, and On-Demand Appcasting", "description": "AppCasting and uMAC utilities.", "files": ["app_appcasting_umactools.pdf", "app_appcasting_extend.pdf", "app_appcasting_under_hood.pdf"]},
    {"slug": "43_ufld_brokers_nodecomms", "title": "uFldNodeBroker, uFldShoreBroker, and uFldNodeComms", "description": "uField broker and node communication tools.", "files": ["app_ufld_nodebroker.pdf", "app_ufld_shorebroker.pdf", "app_ufld_nodecomms.pdf"]},
    {"slug": "44_ufld_message_handler", "title": "uFldMessageHandler", "description": "uField message handling.", "files": ["app_ufld_msghandler.pdf"]},
    {"slug": "45_ufld_range_sensors", "title": "uFldBeaconRangeSensor and uFldContactRangeSensor", "description": "uField range-sensor simulators.", "files": ["app_ufld_beacon_rsensor.pdf", "app_ufld_contact_rsensor.pdf"]},
    {"slug": "46_ufld_collision_detectors", "title": "uFldCollisionDetect and uFldCollObDetect", "description": "uField collision and collision-obstacle detectors.", "files": ["app_ufld_collision_detect.pdf", "app_ufld_collob_detect.pdf"]},
    {"slug": "47_ufld_obstacle_scope_pathcheck", "title": "uFldObstacleSim, uFldScope, and uFldPathCheck", "description": "uField obstacle simulation, scoping, and path checking.", "files": ["app_ufld_obsim.pdf", "app_ufld_scope.pdf", "app_ufld_pathcheck.pdf"]},
]


RAW_PACKS_SPEC = [
    {
        "slug": "48_chap_helm_as_moos",
        "title": "The IvP Helm as a MOOS Application",
        "description": "pHelmIvP as a MOOS application, including helm state, configuration, publications, and subscriptions.",
        "files": ["chap_helm_as_moos.pdf"],
    },
]


TA_GUIDE_TEXT = """
MOOS-IvP Virtual TA Guide

Role
You are a teaching assistant for MOOS-IvP. Use the notebook sources as the authority. Answer in a practical teaching style: explain the concept, name the relevant files or variables, and give a small diagnostic checklist when the student is debugging.

Grounding Rules
- Prefer cited answers from the uploaded MIT MOOS-IvP documentation and lab sources.
- Do not invent MOOS variables, behavior parameters, app names, or file names. If the sources do not settle the question, say what is missing and ask for the student's .moos, .bhv, console output, or alog detail.
- Distinguish .moos mission configuration from .bhv behavior configuration.
- Distinguish MOOS apps, IvP behaviors, MOOS variables, and mission launch scripts.
- If a question is about a student's local code or mission, explain likely causes and what evidence to inspect, but do not claim to have run the mission.

Common Student Debugging Pattern
1. Identify the process involved, such as pHelmIvP, pAntler, pMarineViewer, uSimMarine, pLogger, uXMS, uPokeDB, or uQueryDB.
2. Identify the file involved: usually a .moos file for processes and app parameters, and a .bhv file for helm behaviors.
3. Check whether the expected MOOS variable is being published. Recommend uXMS, uQueryDB, or alog tools as appropriate.
4. For helm issues, check helm state, behavior conditions, behavior priority, ownship navigation variables, and run/idle/completed status.
5. For multi-vehicle or uField issues, check community names, ports, pShare/uFld broker configuration, node reports, contact manager inputs, and message routes.
6. For post-mission analysis, recommend pLogger/alogs, alogview, and alog command-line utilities.

Answer Style
- Keep answers concise unless the student asks for a deep explanation.
- When useful, provide one short example configuration snippet, but clearly label it as illustrative.
- When there are multiple plausible causes, rank them from most common to least common.
- Ask for the smallest next artifact needed to continue: a single config block, a few MOOS variables, or a short alog query result.
"""


def download(name: str) -> Path:
    out = DOWNLOADS / name
    if out.exists() and out.stat().st_size > 0:
        return out
    url = BASE_URL + name
    print(f"download {url}")
    with urllib.request.urlopen(url, timeout=60) as response:
        data = response.read()
    if not data.startswith(b"%PDF"):
        raise RuntimeError(f"{name} did not look like a PDF")
    out.write_bytes(data)
    return out


def title_pdf(path: Path, title: str, description: str, components: list[str]) -> None:
    doc = SimpleDocTemplate(
        str(path),
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54,
    )
    styles = getSampleStyleSheet()
    story = [
        Paragraph(title, styles["Title"]),
        Spacer(1, 18),
        Paragraph(description, styles["BodyText"]),
        Spacer(1, 18),
    ]
    if components:
        story.append(Paragraph("Included MIT MOOS-IvP PDF sources:", styles["Heading2"]))
        for item in components:
            story.append(Paragraph(f"- {item}", styles["BodyText"]))
    else:
        for para in TA_GUIDE_TEXT.strip().split("\n\n"):
            story.append(Paragraph(para.replace("\n", "<br/>"), styles["BodyText"]))
            story.append(Spacer(1, 10))
    doc.build(story)


def merge_pack(spec: dict) -> dict:
    out = PACKS / f"{spec['slug']}.pdf"
    title = spec["title"]
    description = spec["description"]
    title_page = PACKS / f".{spec['slug']}_title.pdf"
    title_pdf(title_page, title, description, spec["files"])

    writer = PdfWriter()
    title_reader = PdfReader(str(title_page))
    writer.append(title_reader)
    writer.add_outline_item(title, 0)

    page_offset = len(writer.pages)
    for file_name in spec["files"]:
        pdf_path = download(file_name)
        reader = PdfReader(str(pdf_path))
        writer.append(reader)
        writer.add_outline_item(file_name, page_offset)
        page_offset += len(reader.pages)

    with out.open("wb") as fh:
        writer.write(fh)

    reader = PdfReader(str(out))
    return {
        "slug": spec["slug"],
        "title": title,
        "description": description,
        "output": str(out),
        "files": spec["files"],
        "pages": len(reader.pages),
        "bytes": out.stat().st_size,
    }


def record_raw_pack(spec: dict) -> dict:
    out = PACKS / f"{spec['slug']}.pdf"
    if not out.exists():
        raise FileNotFoundError(f"raw pack missing: {out}")
    reader = PdfReader(str(out))
    return {
        "slug": spec["slug"],
        "title": spec["title"],
        "description": spec["description"],
        "output": str(out),
        "files": spec["files"],
        "pages": len(reader.pages),
        "bytes": out.stat().st_size,
    }


def main() -> None:
    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    PACKS.mkdir(parents=True, exist_ok=True)

    results = []
    for spec in PACKS_SPEC:
        results.append(merge_pack(spec))
    for spec in RAW_PACKS_SPEC:
        results.append(record_raw_pack(spec))

    manifest = {
        "base_url": BASE_URL,
        "pack_count": len(results),
        "packs": results,
        "existing_notebook_source_to_keep": "MOOS-IvP : Helm - Helm As MOOS",
        "notes": textwrap.dedent(
            """
            These packs are intended for a single NotebookLM MOOS-IvP Virtual TA notebook.
            The current notebook already contains the Helm As MOOS web source from the smoke test.
            """
        ).strip(),
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2))
    (ROOT / "upload_files.txt").write_text("\n".join(item["output"] for item in results) + "\n")
    print(json.dumps({"pack_count": len(results), "total_bytes": sum(i["bytes"] for i in results)}, indent=2))


if __name__ == "__main__":
    main()

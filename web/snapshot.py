#common

from enum import IntEnum

from browser import window, document
from config import API_URL, INTERPRETER_API_URL

last_submitted_code = ""
last_interpreter_payload = ""


class SnapshotStatus(IntEnum):
    SUCCESS = 1
    PARTIALSUCCESS = 2
    FAIL = 3
    ERROR = 4


def send_snapshot(code, result, details):
    global last_submitted_code

    if code == last_submitted_code:
        window.console.log("Codigo identico ao ultimo enviado, nao enviando snapshot")
        return

    if not hasattr(window, "jQuery"):
        window.console.log("jQuery not available for snapshot")
        return

    payload = {
        "code": code,
        "ide": "web",
        "status": str(result),
        "details": details or "",
    }
    window.jQuery.post(API_URL, payload)
    last_submitted_code = code


def send_interpreter_snapshot(result, details, code=""):
    global last_interpreter_payload

    if not hasattr(window, "jQuery"):
        window.console.log("jQuery not available for snapshot")
        return

    code = code.strip().rstrip('>\n ')
    code = document["code_header"].textContent + "\n" + code

    payload = {
        "code": code or "",
        "ide": "web",
        "status": str(result),
        "details": details or "",
    }
    payload_key = f"{payload['code']}|{payload['status']}|{payload['details']}"
    if payload_key == last_interpreter_payload:
        window.console.log("Snapshot do interpretador repetido, nao enviando")
        return

    window.jQuery.post(INTERPRETER_API_URL, payload)
    last_interpreter_payload = payload_key

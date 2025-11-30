from datetime import datetime

import pytest
from logger import logger

from test_api.tms_service import TmsService


@pytest.fixture
def tms_service():
    return TmsService()


@pytest.fixture
def token(tms_service):
    pytest.token = None
    response_json = tms_service.login("user@example.com", "Odmen123")
    assert response_json["access_token"]
    pytest.token = response_json["access_token"]
    return token


def test_create_second_admin(tms_service):
    pytest.token = None
    response_json = tms_service.register_admin("admin2", "Admin@example.com", "qwer111")
    assert response_json["detail"] == "Admin already exists. Registration is disabled."
    logger.info(response_json)


def test_create_board(token, tms_service):
    response_json = tms_service.create_board("string", "string", False)

    logger.info(response_json)
    assert response_json["id"]
    assert response_json["title"] == "string"
    assert response_json["description"] == "string"
    assert response_json["public"] is False
    assert response_json["created by"]
    assert response_json["archived"] is False

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created at"].startswith(current_date)


def test_create_task(token, tms_service):
    board_response = tms_service.create_board("string", "string", False)
    logger.info(board_response)
    board_id = board_response["id"]
    response_json = tms_service.create_task(
        board_id, "my second task", "description", "todo", "high"
    )
    assert response_json["id"]
    assert response_json["title"] == "my second task"
    assert response_json["description"] == "description"
    assert response_json["status"] == "todo"
    assert response_json["priority"] == "high"

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created at"].startswith(current_date)


def test_get_users_without_token(tms_service):
    pytest.token = None
    response_json = tms_service.get_users(skip=0, limit=100, code=403)

    logger.info(response_json)
    assert response_json["detail"] == "Not authenticated"


def test_get_board_members(token, tms_service):
    board_response = tms_service.create_board("Board", "abra", False)
    board_id = board_response["id"]
    response_json = tms_service.get_board_members(board_id)

    logger.info(response_json)
    assert len(response_json["members"]) >= 1
    assert response_json["members"][0]["id"]


def test_add_board_member(token, tms_service):
    board_response = tms_service.create_board("Board add", "abra", False)
    board_id = board_response["id"]
    user_response = tms_service.get_users(skip=0, limit=100)
    user = user_response[1] if len(user_response) > 1 else user_response[0]

    response_json = tms_service.add_board_member(board_id, user["id"])
    logger.info(response_json)

    assert response_json is not None

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_task_status(token, tms_service):
    board_response = tms_service.create_board("Board status change", "abra", False)
    board_id = board_response["id"]
    task_response = tms_service.create_task(
        board_id, "Task status change", "description", "todo", "high"
    )
    task_id = task_response["id"]

    response_json = tms_service.task_next_status(task_id)
    logger.info(response_json)
    assert response_json["id"] == task_id
    assert response_json["status"] != "todo"
    assert response_json["status"] == "in_progress"
    assert response_json["priority"] == "high"

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_bulk_update(token, tms_service):
    board_response = tms_service.create_board("Board bulk", "abra", False)
    board_id = board_response["id"]

    task1 = tms_service.create_task(board_id, "task1", "description", "todo", "high")
    task2 = tms_service.create_task(board_id, "task2", "description", "todo", "medium")

    task_ids = [task1["id"], task2["id"]]

    response_json = tms_service.update_task_status(board_id, task_ids, "in_progress")

    logger.info(response_json)
    assert response_json is not None

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_get_board_stats(token, tms_service):
    board_response = tms_service.create_board("Board stats", "abra", False)
    board_id = board_response["id"]

    tms_service.create_task(board_id, "task1", "description", "done", "high")
    tms_service.create_task(board_id, "task2", "description", "todo", "medium")

    response_json = tms_service.get_board_stats(board_id)

    logger.info(response_json)
    assert response_json is not None
    assert "total_tasks" in response_json
    assert "tasks_by_status" in response_json
    assert "task_by_priority" in response_json

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_search_tasks(token, tms_service):
    board_response = tms_service.create_board("Board search", "abra", False)
    board_id = board_response["id"]

    tms_service.create_task(board_id, "task123", "description", "done", "high")

    response_json = tms_service.search_tasks("task123")

    logger.info(response_json)
    assert "task123" in response_json

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_update_priority(token, tms_service):
    board_response = tms_service.create_board("Board update", "abra", False)
    board_id = board_response["id"]

    task = tms_service.create_task(board_id, "task123", "description", "todo", "medium")
    task_id = task["id"]

    new_priority = "high"
    response_json = tms_service.update_task_priority(task_id, new_priority)

    logger.info(response_json)
    assert response_json["id"] == task_id
    assert response_json["priority"] == new_priority
    assert response_json["priority"] != "medium"

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_get_my_tasks(token, tms_service):
    board_response = tms_service.create_board("Board get", "abra", False)
    board_id = board_response["id"]
    task1 = tms_service.create_task(board_id, "task1", "description", "done", "high")
    tms_service.create_task(board_id, "task2", "description", "todo", "medium")

    response_json = tms_service.get_my_tasks()

    logger.info(response_json)

    assert len(response_json["tasks"]) >= 2
    assert response_json["tasks"][0]["id"] == task1["id"]

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_archive(token, tms_service):
    board_response = tms_service.create_board("Board archive", "abra", False)
    board_id = board_response["id"]

    response_json = tms_service.archive_board(board_id)

    logger.info(response_json)
    assert response_json["id"] == board_id
    assert response_json["archived"] is True

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_move_task(token, tms_service):
    first_board = tms_service.create_board("First board", "abra", False)
    second_board = tms_service.create_board("Second board", "abra", False)

    first_board_id = first_board["id"]
    second_board_id = second_board["id"]

    task = tms_service.create_task(
        first_board_id, "task123", "description", "todo", "medium"
    )
    task_id = task["id"]

    response_json = tms_service.moving_tasks(task_id, second_board_id)

    logger.info(response_json)
    assert response_json["id"] == task_id
    assert response_json["board_id"] == second_board_id

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)
